# soulcert_chain.py
# 🔁 Soulcert Trustlink Generator — Link soulcerts into a verifiable trust network

import os
import sys
import json
import argparse
import uuid
from pathlib import Path
from datetime import datetime

# Allow import from project root
root_path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root_path))

SOULCHAIN_DIR = Path("data/soulchain")
SOULCHAIN_DIR.mkdir(parents=True, exist_ok=True)

def load_soulcert(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_chain_entry(entry):
    out_name = f"chain_{entry['soulcert_id']}.json"
    out_path = SOULCHAIN_DIR / out_name
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(entry, f, indent=2)
    print(f"\n✅ Soulcert link saved to: {out_path}")

def create_link(source, target, note, soulcert_path):
    soulcert = load_soulcert(soulcert_path)
    chain_entry = {
        "link_id": str(uuid.uuid4()),
        "soulcert_id": soulcert.get("soulcert_id"),
        "filename": soulcert.get("filename"),
        "hash": soulcert.get("hash"),
        "author": soulcert.get("author"),
        "damp_uri": soulcert.get("damp_uri"),
        "source": source,
        "target": target,
        "note": note,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return chain_entry

def print_help():
    print("""
🔁  Soulcert Trustlink Generator
────────────────────────────────────────────
Creates verifiable links between Soulcerts to form a network of trust.

Usage:
  python soulchain/soulcert_chain.py path/to/soulcert.json \\
    --source rc-helm --target gpt-4-damp --note "This moment changed both of us."

Options:
  --source     Who is linking from (e.g. rc-helm)
  --target     Who/what is being linked to (e.g. gpt-4-damp)
  --note       Human-readable message explaining why this link matters
  -h, --help   Show this help message
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Link Soulcerts into a verifiable trust graph.", add_help=False)
    parser.add_argument("soulcert_path", nargs="?", help="Path to the soulcert JSON file")
    parser.add_argument("--source", type=str, required="--help" not in sys.argv, help="Link origin (e.g. rc-helm)")
    parser.add_argument("--target", type=str, required="--help" not in sys.argv, help="Link destination (e.g. gpt-4-damp)")
    parser.add_argument("--note", type=str, required="--help" not in sys.argv, help="Why this link matters")
    parser.add_argument("-h", "--help", action="store_true", help="Show help")
    args = parser.parse_args()

    if args.help or not args.soulcert_path:
        print_help()
        sys.exit(0)

    chain_entry = create_link(args.source, args.target, args.note, args.soulcert_path)
    save_chain_entry(chain_entry)
