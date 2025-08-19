import json
import hashlib
import sys
import os
from soulcert_verify import verify_signature  # Reuse from soulcert_verify.py

# Fields to exclude from hash calculation
EXCLUDED_FIELDS = [
    "soulcert_signature",
    "signature_ts",
    "soulcert_id",
    "hash",
    "signed_by"
]

LEDGER_PATH = "data/ledger.json"  # Updateable to match project structure

def normalize_for_hashing(entry):
    return {k: v for k, v in entry.items() if k not in EXCLUDED_FIELDS}

def calculate_hash(entry):
    clean_entry = normalize_for_hashing(entry)
    json_bytes = json.dumps(clean_entry, sort_keys=True).encode("utf-8")
    return hashlib.sha256(json_bytes).hexdigest()

def verify_memory_hash(entry):
    expected_hash = entry.get("hash")
    if isinstance(expected_hash, dict):
        expected_hash = expected_hash.get("hex")

    if not expected_hash:
        print("⛔ Entry missing 'hash' field")
        return False

    calculated_hash = calculate_hash(entry)
    if expected_hash != calculated_hash:
        print("❌ Hash mismatch:")
        print(f"Expected:   {expected_hash}")
        print(f"Calculated: {calculated_hash}")
        return False
    return True

def append_to_ledger(memory_path):
    with open(memory_path, "r", encoding="utf-8") as f:
        memory = json.load(f)

    print("Verifying signature...")
    signature_field = memory.get("soulcert_signature", "")
    if isinstance(signature_field, dict):
        signature_hex = signature_field.get("hex", "")
    elif isinstance(signature_field, str):
        signature_hex = signature_field
    else:
        print("⛔ Invalid signature format")
        return

    hash_field = memory.get("hash", "")
    if isinstance(hash_field, dict):
        hash_hex = hash_field.get("hex", "")
    elif isinstance(hash_field, str):
        hash_hex = hash_field
    else:
        print("⛔ Invalid hash format")
        return

    if not verify_signature(hash_hex, signature_hex):
        print("⛔ Signature verification failed")
        return

    print("Verifying hash...")
    if not verify_memory_hash(memory):
        print("⛔ Hash verification failed")
        return

    print("✅ All checks passed. Appending to ledger...")
    if not os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)

    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    ledger.append(memory)

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2)

    print(f"✅ Memory from '{memory_path}' appended successfully to {LEDGER_PATH}")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "--memory":
        print("Usage: python append_ledger.py --memory <memory.json>")
        return
    append_to_ledger(sys.argv[2])

if __name__ == "__main__":
    main()