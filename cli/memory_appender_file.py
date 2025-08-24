# Copyright 2025 Rudolph C. Helm IV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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

