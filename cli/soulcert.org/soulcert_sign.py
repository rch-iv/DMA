import json
import hashlib
import base64
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def load_private_key():
    with open("soulcert_config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    key_path = config.get("private_key_path", "keys/soul_ai_private.pem")
    with open(key_path, "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

def normalize_for_hashing(entry):
    excluded_fields = ["verification", "soulcert_id", "damp_uri", "uuid", "soulcert_signature"]
    return {k: v for k, v in entry.items() if k not in excluded_fields}

def sign_memory(memory_entry):
    normalized = normalize_for_hashing(memory_entry)
    memory_str = json.dumps(normalized, sort_keys=True, separators=(",", ":"))
    hash_obj = hashlib.sha256(memory_str.encode("utf-8"))
    hash_hex = hash_obj.hexdigest()

    private_key = load_private_key()
    signature = private_key.sign(
        hash_obj.digest(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    signature_b64 = base64.b64encode(signature).decode("utf-8")

    memory_entry["soulcert_signature"] = {
        "hex": signature_b64,
        "algorithm": "RSA-SHA256",
        "signed_by": "soul:0xF3A1DEADBEEF"
    }

    return memory_entry, hash_hex, signature_b64

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python soulcert_sign.py <input_memory.json> --output <signed_output.json>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        memory_data = json.load(f)

    signed_data, _, _ = sign_memory(memory_data)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(signed_data, f, indent=2)

    print(f"✅ Memory signed and saved to {output_path}")
