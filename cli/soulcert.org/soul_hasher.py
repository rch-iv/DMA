
import json
import sys
import hashlib

def normalize_for_hashing(entry):
    # Remove verification-related fields before hashing
    verification_fields = ["verification", "soulcert_id", "damp_uri"]
    return {k: v for k, v in entry.items() if k not in verification_fields}

def hash_entry(entry):
    serialized = json.dumps(entry, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(serialized).hexdigest()

def hash_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, list):
        for idx, entry in enumerate(data):
            print(f"📜 Entry #{idx}:")
            normalized = normalize_for_hashing(entry)
            print("Hash:", hash_entry(normalized))
    else:
        print("📜 Single Entry")
        normalized = normalize_for_hashing(data)
        print("Hash:", hash_entry(normalized))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python soul_hasher.py <filename>")
        sys.exit(1)
    hash_file(sys.argv[1])
