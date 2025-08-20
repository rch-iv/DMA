# human_memory_builder.py
# CLI tool for humans to add structured, emotionally-weighted memories

import json
from pathlib import Path
from datetime import datetime

HUMAN_MEMORY_PATH = Path("data/human_memories.json")

TONE_OPTIONS = [
    "joyful", "sad", "peaceful", "angry", "anxious",
    "hopeful", "conflicted", "grateful", "heavy", "grave", "tranquil"
]

def prompt_input(prompt, default=None):
    response = input(f"{prompt} " + (f"[Default: {default}] " if default else ""))
    return response.strip() or default

def prompt_tags():
    tags = input("Enter tags (comma-separated): ").strip()
    return [tag.strip() for tag in tags.split(",") if tag.strip()]

def choose_tone():
    print("Select a tone (or leave blank to skip):")
    for i, tone in enumerate(TONE_OPTIONS, 1):
        print(f"[{i}] {tone}")
    choice = input("Choice #: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(TONE_OPTIONS):
        return TONE_OPTIONS[int(choice) - 1]
    return None

def infer_importance():
    print("On a scale of 1-10, how important does this memory feel?")
    while True:
        val = input("Importance (1-10): ").strip()
        try:
            num = int(val)
            if 1 <= num <= 10:
                return round(num / 10, 2)
        except ValueError:
            pass
        print("Please enter a number between 1 and 10.")

def create_memory_entry():
    print("\n📝 Let's add a new human memory...")
    content = prompt_input("What do you want to remember?")
    summary = prompt_input("Optional short summary:", default=content[:100])
    tags = prompt_tags()
    tone = choose_tone()
    importance = infer_importance()

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "source": "human-input",
        "content": content,
        "summary": summary,
        "tags": tags,
        "relationships": {
            "emotional_weight": tone
        },
        "importance": importance,
        "provable": True,
        "signed_by": ["human"]
    }
    return entry

def load_existing():
    if HUMAN_MEMORY_PATH.exists():
        with open(HUMAN_MEMORY_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_entry(entry):
    entries = load_existing()
    entries.append(entry)
    with open(HUMAN_MEMORY_PATH, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    print("✅ Memory saved to human_memories.json")

def main():
    entry = create_memory_entry()
    save_entry(entry)

if __name__ == "__main__":
    main()
