"""Read a compact index or selected terms from the single taxonomy source."""
import argparse
import json
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parent.parent
TAX_PATH = ROOT / 'references' / 'taxonomy.json'


def dimension_code(value):
    value = unicodedata.normalize('NFKC', value).lstrip('#')
    match = re.match(r'^([A-E][1-3])(?:[A-Za-z]+)?$', value, re.I)
    return match.group(1).upper() if match else value


def query_taxonomy(dimensions=None, query=None, ids=None, all_terms=False, offset=0, limit=50):
    tax = json.loads(TAX_PATH.read_text(encoding='utf-8'))
    terms = tax['terms']
    codes = {dimension_code(d): d for d in tax['top_dimensions']}
    selected_dims = {dimension_code(d) for d in dimensions or []}
    unknown = selected_dims - set(codes)
    if unknown:
        raise ValueError('Unknown dimensions: ' + ', '.join(sorted(unknown)))
    selected_ids = set(ids or [])
    unknown_ids = selected_ids - {t['id'] for t in terms}
    if unknown_ids:
        raise ValueError('Unknown IDs: ' + ', '.join(sorted(unknown_ids)))
    if offset < 0 or limit < 1:
        raise ValueError('offset must be nonnegative and limit must be positive')
    if query is not None and not query.strip():
        raise ValueError('query must contain text')
    if all_terms and (selected_dims or selected_ids or query is not None):
        raise ValueError('--all is used without filters')
    base = {'version': tax['version'], 'canonical_count': len(terms), 'ai_marker_tag': tax['ai_marker_tag']}
    if not (selected_dims or selected_ids or query is not None or all_terms):
        return {**base, 'mode': 'index', 'dimensions': [
            {'code': c, 'prefix': '#' + d, 'count': sum(t['tag'].startswith('#' + d + '/') for t in terms)}
            for c, d in codes.items()]}
    aliases = {}
    for old, new in tax.get('rename_map', {}).items():
        if old != new:
            aliases.setdefault(new, []).append(old)
    needle = query.casefold().strip() if query is not None else None
    results = []
    for t in terms:
        if selected_dims and dimension_code(t['tag'].split('/')[0]) not in selected_dims:
            continue
        if selected_ids and t['id'] not in selected_ids:
            continue
        search_text = ' '.join([t['tag'], t.get('definition', ''), *t.get('aliases', []), *aliases.get(t['tag'], [])])
        if needle and needle not in search_text.casefold():
            continue
        results.append(t)
    page = results[offset:offset + limit]
    return {**base, 'mode': 'terms', 'total_matches': len(results), 'offset': offset,
            'returned': len(page), 'next_offset': offset + len(page) if offset + len(page) < len(results) else None,
            'terms': page}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dimension', action='append', default=[], help='Dimension code, e.g. A1, C1, D2; repeatable')
    p.add_argument('--query', help='Search names, definitions, aliases and exact legacy names')
    p.add_argument('--id', action='append', default=[], dest='ids', help='Stable tag ID; repeatable')
    p.add_argument('--all', action='store_true', dest='all_terms', help='Explicit full vocabulary access')
    p.add_argument('--offset', type=int, default=0)
    p.add_argument('--limit', type=int, default=50)
    args = p.parse_args()
    try:
        result = query_taxonomy(args.dimension, args.query, args.ids, args.all_terms, args.offset, args.limit)
    except ValueError as exc:
        p.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
