"""Validate and assemble Zotero V2.0 tags + ~ZTag-V2 marker against taxonomy.json."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAX_PATH = ROOT / "references" / "taxonomy.json"


def keep_specific_children(hash_tags: list[str]) -> list[str]:
    """Retain level-3 leaf tags and drop redundant level-2 parents when a child is present."""
    children_parents = {t.rsplit("/", 1)[0] for t in hash_tags if t.count("/") == 2}
    out = []
    for t in hash_tags:
        if t.count("/") == 1 and t in children_parents:
            continue
        if t not in out:
            out.append(t)
    return out


def validate_and_merge(new_tags: list[str], existing_tags: list[str], add_marker: bool = True) -> dict:
    tax = json.loads(TAX_PATH.read_text(encoding="utf-8"))
    canon_set = set(tax["canonical_tags"])
    status_order = {"/Done": 3, "/reading": 2, "/unread": 1}
    marker = tax.get("ai_marker_tag", "~ZTag-V2")

    errors = []
    hash_tags = []
    extra_user_tags = []
    preserved_status = None

    for t in existing_tags:
        if t in status_order:
            if preserved_status is None or status_order[t] > status_order[preserved_status]:
                preserved_status = t
        elif t == marker or t.startswith("#") or t.startswith("/"):
            continue
        elif t not in extra_user_tags:
            extra_user_tags.append(t)

    for t in new_tags:
        if t in status_order:
            if preserved_status is None or status_order[t] > status_order[preserved_status]:
                preserved_status = t
            continue
        if t == marker:
            continue
        if t not in canon_set:
            errors.append(f"Non-canonical tag: {t}")
            continue
        if any(ord(ch) < 32 or ord(ch) >= 0xE0000 for ch in t):
            errors.append(f"Invalid control char in: {repr(t)}")
            continue
        if t not in hash_tags:
            hash_tags.append(t)

    hash_tags = keep_specific_children(hash_tags)
    ptypes = [t for t in hash_tags if t.startswith("#\uff21\uff11Type/")]
    if len(ptypes) != 1:
        errors.append(f"Expected strictly 1 #Ａ１Type/* tag, got {len(ptypes)}: {ptypes}")

    if len(hash_tags) < 1:
        errors.append("No valid canonical # tags provided.")

    final = []
    if preserved_status:
        final.append(preserved_status)
    final.extend(sorted(hash_tags))
    final.extend(extra_user_tags)
    if add_marker:
        final.append(marker)

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "ai_marker_tag": marker if add_marker else None,
        "preserved_status_tag": preserved_status,
        "final_tags": final,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate V2.0 Zotero tags before write_tag.")
    parser.add_argument("--tags", nargs="+", required=True, help="Proposed V2.0 # tags")
    parser.add_argument("--existing", default="[]", help="JSON array of current tags on the Zotero item")
    parser.add_argument("--no-marker", action="store_true", help="Omit ~ZTag-V2 marker")
    args = parser.parse_args()

    existing_tags = json.loads(args.existing)
    res = validate_and_merge(args.tags, existing_tags, add_marker=not args.no_marker)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    if not res["valid"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
