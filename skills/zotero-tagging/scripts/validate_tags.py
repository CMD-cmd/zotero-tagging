"""Validate controlled tags and preserve user metadata when assembling a write."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAX_PATH = ROOT / 'references' / 'taxonomy.json'


def validate_and_merge(new_tags, existing_tags, add_marker=True, mode='add', status=None):
    tax = json.loads(TAX_PATH.read_text(encoding='utf-8'))
    canon = set(tax['canonical_tags'])
    rename = tax.get('rename_map', {})
    owned = canon | set(rename)
    marker = tax['ai_marker_tag']
    states = set(tax['workflow_status_tags'])
    errors, warnings = [], []
    if mode not in ('add', 'replace-managed', 'rename-only'):
        errors.append(f'Unknown mode: {mode}')
    if not isinstance(new_tags, list) or not isinstance(existing_tags, list):
        return {'valid': False, 'errors': ['Tags must be arrays of strings'], 'final_tags': [], 'diff': {}}
    if any(not isinstance(t, str) for t in new_tags + existing_tags):
        return {'valid': False, 'errors': ['Tags must be strings'], 'final_tags': [], 'diff': {}}
    if status is not None and status not in states:
        errors.append(f'Unknown reading status: {status}')
    if mode == 'rename-only' and (new_tags or status is not None):
        errors.append('rename-only accepts existing tags only')

    def normalize(t):
        return rename.get(t, t)

    final = []
    for t in existing_tags:
        if mode == 'replace-managed' and t in owned:
            continue
        if status is not None and t in states:
            continue
        target = normalize(t) if t in owned else t
        if target not in final:
            final.append(target)
    for t in new_tags:
        target = normalize(t)
        if target not in canon and target not in states and target != marker:
            errors.append(f'Non-canonical proposed tag: {t}')
            continue
        if any(ord(c) < 32 or ord(c) >= 0xE0000 for c in target):
            errors.append(f'Invalid control character: {t!r}')
            continue
        if target not in final:
            final.append(target)
    if status is not None and status not in final:
        final.append(status)
    # rename-only keeps the exact membership of non-taxonomy tags and markers.
    if add_marker and mode != 'rename-only' and marker not in final:
        final.append(marker)

    controlled = [t for t in final if t in canon]
    types = [t for t in controlled if t.startswith('#Ａ１Type/')]
    if len(types) != 1:
        errors.append(f'Expected one controlled Type, found {len(types)}')
    before_states = {t for t in existing_tags if t in states}
    after_states = {t for t in final if t in states}
    if len(after_states) > 1:
        if after_states == before_states:
            warnings.append('Existing multiple reading states preserved')
        else:
            errors.append('Reading state conflict; use --status for an explicit transition')
    parents = [t for t in controlled if any(c.startswith(t + '/') for c in controlled if c != t)]
    if parents:
        if mode == 'rename-only':
            warnings.append('Parent and child tags coexist; review specificity: ' + ', '.join(parents))
        else:
            errors.append('Parent and child tags cannot coexist (keep specific child only): ' + ', '.join(parents))
    if len(controlled) > 9:
        warnings.append(f'{len(controlled)} controlled tags; count is informational')
    return {'valid': not errors, 'errors': errors, 'warnings': warnings,
            'taxonomy_version': tax['version'], 'mode': mode,
            'ai_marker_tag': marker if marker in final else None,
            'preserved_status_tags': [t for t in final if t in states],
            'final_tags': final,
            'diff': {'added': [t for t in final if t not in existing_tags],
                     'removed': [t for t in existing_tags if t not in final]}}


def main():
    parser = argparse.ArgumentParser(description='Validate Zotero controlled tags and show a precise diff.')
    parser.add_argument('--tags', nargs='*', default=[])
    parser.add_argument('--existing', default='[]', help='JSON array of current tag names')
    parser.add_argument('--mode', choices=['add', 'replace-managed', 'rename-only'], default='add')
    parser.add_argument('--status', choices=['/unread', '/reading', '/Done'])
    parser.add_argument('--no-marker', action='store_true', help='Preserve existing markers without adding one')
    args = parser.parse_args()
    result = validate_and_merge(args.tags, json.loads(args.existing), not args.no_marker, args.mode, args.status)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result['valid']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
