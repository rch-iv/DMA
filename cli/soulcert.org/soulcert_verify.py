import json
import hashlib
import base64
import uuid
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def load_public_key():
    with open("soulcert_config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    key_path = config.get("public_key_path", "keys/soul_ai_public.pem")
    with open(key_path, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read(), backend=default_backend())

def normalize_for_hashing(entry):
    excluded_fields = ["verification", "soulcert_id", "damp_uri", "uuid", "soulcert_signature"]
    return {k: v for k, v in entry.items() if k not in excluded_fields}

def calculate_hash(memory_entry):
    normalized = normalize_for_hashing(memory_entry)
    memory_str = json.dumps(normalized, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(memory_str.encode("utf-8")).hexdigest()

def verify_signature(hash_hex, signature_b64, public_key):
    try:
        signature_bytes = base64.b64decode(signature_b64)
        hash_bytes = bytes.fromhex(hash_hex)
        public_key.verify(
            signature_bytes,
            hash_bytes,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"❌ Signature verification failed: {e}")
        return False

def verify_hash(memory_entry, expected_hash):
    calculated_hash = calculate_hash(memory_entry)
    return calculated_hash == expected_hash

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python soulcert_verify.py <signed_memory.json>")
        sys.exit(1)

    input_path = sys.argv[1]

    with open(input_path, "r", encoding="utf-8") as f:
        memory = json.load(f)

    signature_obj = memory.get("soulcert_signature", {})
    signature_b64 = signature_obj.get("hex", "")

    if not signature_b64:
        print("❌ Missing signature field")
        sys.exit(1)

    public_key = load_public_key()
    hash_hex = calculate_hash(memory)

    if verify_signature(hash_hex, signature_b64, public_key):
        print(f"✅ {input_path}: Memory verified")
    else:
        print(f"❌ {input_path}: Memory failed verification")
