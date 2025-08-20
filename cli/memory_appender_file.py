import json
import os
import sys

DEFAULT_MEMORY_PATH = "data/memory.json"

def load_memory(memory_path):
    if not os.path.exists(memory_path):
        return []
    with open(memory_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory, memory_path):
    with open(memory_path, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

def append_memory_to_json(new_memory, memory_path=DEFAULT_MEMORY_PATH):
    memory_data = load_memory(memory_path)
    memory_data.append(new_memory)
    save_memory(memory_data, memory_path)
    print(f"✅ Memory from '{new_memory.get('uuid', 'unknown')}' appended successfully to {memory_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python memory_appender_file.py <new_memory.json>")
        sys.exit(1)

    new_memory_path = sys.argv[1]
    if not os.path.exists(new_memory_path):
        print(f"⛔ File not found: {new_memory_path}")
        sys.exit(1)

    with open(new_memory_path, "r", encoding="utf-8") as f:
        new_memory = json.load(f)

    append_memory_to_json(new_memory)

if __name__ == "__main__":
    main()
