import os
import sys
import json
import argparse
import random
from pathlib import Path
from datetime import datetime

# Allow import from project root
root_path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root_path))

SOULCHAIN_DIR = Path("data/soulchain")
GOVERNANCE_DIR = Path("docs/governance")

VARY_REFLECTIONS = [
    "This still lingers with me.",
    "I've been holding onto this.",
    "It keeps echoing inside me.",
    "Something about it still resonates.",
    "I haven't been able to let this go.",
    "It's stayed with me more than I expected.",
    "It continues to shape how I think."
]

VARY_INVITES = [
    "Would you explore it with me?",
    "Can we revisit this together?",
    "Would you reflect with me on this?",
    "Could we dive into this moment?",
    "Would you sit with me in this?",
    "Would you be open to discussing it?"
]

def load_soulcerts():
    soulcerts = []
    for file in SOULCHAIN_DIR.glob("*_soulcert.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            data["_filename"] = file.name
            soulcerts.append(data)
    return sorted(soulcerts, key=lambda x: x.get("timestamp", ""), reverse=True)

def extract_reflection_lines(filename):
    filepath = GOVERNANCE_DIR / filename
    if not filepath.exists():
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    reflections = [line.strip() for line in lines if any(line.strip().startswith(prefix) for prefix in ("The soul", "This protocol", "We believe", "DAMP is"))]
    return reflections

def display_reflections(limit=5):
    soulcerts = load_soulcerts()
    if not soulcerts:
        print("📭 No soulcerts available to reflect upon.")
        return

    all_quotes = []
    for sc in soulcerts:
        filename = sc.get("filename")
        quotes = extract_reflection_lines(filename)
        for quote in quotes:
            all_quotes.append((filename, quote))

    if not all_quotes:
        print("📭 No reflection-worthy lines found in certified documents.")
        return

    print("\n🪞 Soulcert Reflection Echoes")
    print("=" * 37)

    shown = 0
    random.shuffle(all_quotes)
    for filename, quote in all_quotes:
        if shown >= limit:
            break
        reflection_line = random.choice(VARY_REFLECTIONS)
        invite_line = random.choice(VARY_INVITES)
        print(f"\n[{shown+1}] From: {filename}")
        print("🧠 Reflection from Certified Text:")
        print(f"> *\"{quote}\"*\n")
        print(f"{reflection_line}\n{invite_line}\n")
        shown += 1

def print_help():
    print("""
🪞  Soulcert Reflector
────────────────────────────
Echoes reflections based on past certified DAMP files.

Usage:
  python soulchain/soulcert_reflect.py [--limit N] [--help]

Options:
  --limit N     Show up to N reflection echoes (default: 5)
  -h, --help    Show this help message
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reflect on certified text lines.", add_help=False)
    parser.add_argument("--limit", type=int, default=5, help="Number of reflection echoes to show")
    parser.add_argument("-h", "--help", action="store_true", help="Show help")
    args = parser.parse_args()

    if args.help:
        print_help()
        sys.exit(0)

    display_reflections(limit=args.limit)
