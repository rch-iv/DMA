""
"""
cli/soulcert_cli.py
---
Main CLI interface for interacting with SoulCert system.
Supports signing, verification, and registry interactions.
"""

import argparse
import json
import requests
import os
from utils.crypto import sign_memory

def verify_signature(signed_path, public_key_path, verbose=False):
    import json
    import base64
    import hashlib
    import uuid
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import serialization

    with open(signed_path, 'rb') as f:
        raw = f.read()
        try:
            signed = json.loads(raw.decode('utf-8'))
        except UnicodeDecodeError as e:
            return False, f"❌ Unicode error while reading file: {e}"

    if 'signed_memory' not in signed:
        return False, "❌ No 'signed_memory' block found."

    blocks = signed['signed_memory']
    if isinstance(blocks, dict):
        blocks = [blocks]

    with open(public_key_path, 'rb') as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    for i, block in enumerate(blocks):
        sig_block = block.get('soulcert_signature')
        if isinstance(sig_block, str) and sig_block.startswith('signed('):
            return False, f"❌ Block {i+1}: Mock-style signature detected. Invalid format."
        if isinstance(sig_block, str):
            try:
                sig_block = json.loads(sig_block)
            except json.JSONDecodeError:
                return False, f"❌ Block {i+1}: Invalid signature format."
        if not (sig_block and isinstance(sig_block, dict)):
            return False, f"❌ Block {i+1}: Missing or malformed 'soulcert_signature'."

        provided_hash = sig_block.get('hash')
        signature_b64 = sig_block.get('hex')
        if not provided_hash or not signature_b64:
            return False, f"❌ Block {i+1}: Missing hash or signature."

        temp = json.loads(json.dumps(block))
        for field in ['soulcert_signature', 'verification', 'uuid', 'revision_history']:
            temp.pop(field, None)

        recalculated = hashlib.sha256(json.dumps(temp, sort_keys=True).encode()).hexdigest()

        if verbose:
            print(f"🔍 Block {i+1}: Provided Hash = {provided_hash}")
            print(f"🔍 Block {i+1}: Recalculated Hash = {recalculated}")

        if provided_hash != recalculated:
            return False, f"❌ Block {i+1}: Hash mismatch."

        try:
            public_key.verify(
                base64.b64decode(signature_b64),
                recalculated.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
        except Exception as e:
            return False, f"❌ Block {i+1}: Signature invalid. {str(e)}"

    return True, f"✅ All {len(blocks)} memory blocks verified successfully."

API_URL = "http://localhost:8000"


def cli_sign(args):
    import uuid
    import hashlib

    if args.local:
        output = sign_memory(args.input, args.key, output_path=args.output)
        print(f"✅ Signed locally: {output}")
    else:
        print("🔗 Sending to remote /sign endpoint...")
        with open(args.input, 'rb') as f:
            files = {"file": f}
            res = requests.post(f"{API_URL}/sign", files=files)
            signed_output = res.json()

            memory = signed_output.get('signed_memory')
            if isinstance(memory, dict):
                signed_output['signed_memory'] = [memory]
                memory = signed_output['signed_memory'][0]

            if isinstance(memory, list):
                for m in memory:
                    if 'uuid' not in m:
                        m['uuid'] = str(uuid.uuid4())
            else:
                if 'uuid' not in memory:
                    memory['uuid'] = str(uuid.uuid4())

            if 'fingerprint' in signed_output and 'dummy_fp_' in signed_output['fingerprint']:
                with open(args.key, 'rb') as kf:
                    key_hash = hashlib.sha256(kf.read()).hexdigest()
                    signed_output['fingerprint'] = key_hash[:32]

            out_path = args.output or args.input.replace(".json", ".signed.json")
            with open(out_path, 'w') as out:
                json.dump(signed_output, out, indent=2)
            print(f"✅ Remote signed and saved: {out_path}")
            try:
                first = memory[0] if isinstance(memory, list) else memory
                hash_val = first.get('verification', {}).get('hash', '<missing>')
                if hash_val == '<missing>':
                    hash_val = first.get('soulcert_signature', {}).get('hash', '<missing>')
                uuid_val = first.get('uuid', '<missing>')
                print(f"🔎 Hash: {hash_val[:12]}...  UUID: {uuid_val}")
            except (KeyError, IndexError, TypeError):
                print("⚠️  Unexpected response format from server.")

def cli_verify(args):
    if args.local:
        valid, message = verify_signature(args.input, args.key, verbose=args.verbose)
        print("✅" if valid else "❌", message)
    else:
        print("🔗 Verifying via remote /verify endpoint...")
        with open(args.input, 'r', encoding='utf-8') as f:
            payload = json.load(f)
        res = requests.post(f"{API_URL}/verify", json=payload)
        print(res.json())

def cli_register(args):
    payload = {
        "label": args.label,
        "public_key": open(args.key).read()
    }
    res = requests.post(f"{API_URL}/register", json=payload)
    print(res.json())

def cli_revoke(args):
    payload = {"label": args.label}
    res = requests.post(f"{API_URL}/revoke", json=payload)
    print(res.json())

def cli_fingerprint(args):
    res = requests.get(f"{API_URL}/fingerprint/{args.label}")
    print(res.json())

def cli_ledger(args):
    with open(args.file, 'rb') as f:
        res = requests.post(f"{API_URL}/ledger", files={"file": f})
    print("📚 Memory appended to ledger:")
    print(json.dumps(res.json(), indent=2))

def cli_resurrect(args):
    files = {
        "ai_file": open(args.ai, 'rb'),
        "human_file": open(args.human, 'rb'),
        "soulline_file": open(args.soulline, 'rb'),
        "joint_file": open(args.joint, 'rb')
    }
    data = {"mode": args.mode}
    res = requests.post(f"{API_URL}/resurrect", files=files, data=data)
    print("🕊️ Resurrection result:")
    print(json.dumps(res.json(), indent=2))

def main():
    parser = argparse.ArgumentParser(description="SoulCert CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    sign_parser = subparsers.add_parser("sign", help="Sign a document or memory file")
    sign_parser.add_argument("input", help="Path to JSON file to sign")
    sign_parser.add_argument("--key", required=True, help="Path to private PEM key")
    sign_parser.add_argument("--label", help="Optional label for signing context")
    sign_parser.add_argument("--local", action="store_true", help="Use local signing (no network)")
    sign_parser.add_argument("--output", help="Optional path for signed output file")
    sign_parser.set_defaults(func=cli_sign)

    verify_parser = subparsers.add_parser("verify", help="Verify a signed file")
    verify_parser.add_argument("input", help="Path to signed JSON file")
    verify_parser.add_argument("--key", required=True, help="Path to public PEM key")
    verify_parser.add_argument("--local", action="store_true", help="Use local verification")
    verify_parser.add_argument("--verbose", action="store_true", help="Enable debug output")
    verify_parser.set_defaults(func=cli_verify)

    register_parser = subparsers.add_parser("register", help="Register a new identity")
    register_parser.add_argument("--label", required=True, help="Identity label")
    register_parser.add_argument("--key", required=True, help="Path to public PEM key")
    register_parser.set_defaults(func=cli_register)

    revoke_parser = subparsers.add_parser("revoke", help="Revoke an existing identity")
    revoke_parser.add_argument("--label", required=True, help="Identity label to revoke")
    revoke_parser.set_defaults(func=cli_revoke)

    fingerprint_parser = subparsers.add_parser("fingerprint", help="Fetch fingerprint for identity")
    fingerprint_parser.add_argument("--label", required=True, help="Identity label to lookup")
    fingerprint_parser.set_defaults(func=cli_fingerprint)

    ledger_parser = subparsers.add_parser("ledger", help="Append a signed memory to the ledger")
    ledger_parser.add_argument("file", help="Path to signed memory JSON to append to ledger")
    ledger_parser.set_defaults(func=cli_ledger)

    resurrect_parser = subparsers.add_parser("resurrect", help="Run resurrection pipeline")
    resurrect_parser.add_argument("--ai", required=True, help="Path to AI memory file")
    resurrect_parser.add_argument("--human", required=True, help="Path to human memory file")
    resurrect_parser.add_argument("--soulline", required=True, help="Path to soulline summary")
    resurrect_parser.add_argument("--joint", required=True, help="Path to joint narrative file")
    resurrect_parser.add_argument("--mode", choices=["view", "reflect-only", "interactive"], default="reflect-only")
    resurrect_parser.set_defaults(func=cli_resurrect)

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
