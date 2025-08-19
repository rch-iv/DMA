import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

# Allow import from project root
root_path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root_path))

SOULCHAIN_DIR = Path("data/soulchain")


def load_all_soulcerts():
    soulcerts = []
    for file in SOULCHAIN_DIR.glob("*_soulcert.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            data["_filename"] = file.name
            soulcerts.append(data)
    return sorted(soulcerts, key=lambda x: x.get("timestamp", ""), reverse=True)


def display_soulcert_log(limit=None, author=None):
    soulcerts = load_all_soulcerts()

    if author:
        soulcerts = [sc for sc in soulcerts if sc.get("author") == author]

    if not soulcerts:
        print("📭 No soulcerts found.")
        return

    if limit:
        soulcerts = soulcerts[:limit]

    print("\n📜 Soulcert Audit Trail")
    print("─" * 40)
    for sc in soulcerts:
        print(f"📄 File: {sc['filename']}")
        print(f"🧾 Author: {sc['author']}")
        print(f"📅 Timestamp: {sc['timestamp']}")
        print(f"🔗 DAMP URI: {sc['damp_uri'][:56]}...")
        print(f"🔒 Hash: {sc['hash'][:16]}...\n")


def print_help():
    print("""
📜  DAMP Soulcert Log Viewer
────────────────────────────
Displays a chronological trail of certified soulcerts.

Usage:
  python soulchain/soulcert_log.py [--limit N] [--author NAME]

Options:
  --limit N         Show only the N most recent entries
  --author NAME     Filter by a specific author
  -h, --help        Show this help message
    """)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="View the soulcert audit trail.", add_help=False)
    parser.add_argument("--limit", type=int, help="Limit number of entries")
    parser.add_argument("--author", type=str, help="Filter by author")
    parser.add_argument("-h", "--help", action="store_true", help="Show help")
    args = parser.parse_args()

    if args.help:
        print_help()
        sys.exit(0)

    display_soulcert_log(limit=args.limit, author=args.author)
