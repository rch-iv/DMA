/*
 * Copyright 2025 Rudolph C. Helm IV
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
from datetime import datetime
import json
import os
import uvicorn
import hashlib

API_BASE = "http://127.0.0.1:8000"

app = FastAPI()

FINGERPRINT_REGISTRY_PATH = "data/fingerprint_registry.json"

def calculate_fingerprint(public_key_bytes):
    return hashlib.sha256(public_key_bytes).hexdigest()

def load_registry():
    if os.path.exists(FINGERPRINT_REGISTRY_PATH):
        with open(FINGERPRINT_REGISTRY_PATH, "r") as f:
            return json.load(f)
    return {}

def save_registry(registry):
    with open(FINGERPRINT_REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)

@app.post("/sign")
async def sign(file: UploadFile = File(...)):
    content = await file.read()
    try:
        memory = json.loads(content)
        memory_hash = f"signed({hash(content)})"
        return {
            "signed_memory": memory,
            "signature": memory_hash,
            "fingerprint": "dummy_fp_1234567890abcdef"
        }
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
import json
import base64
import hashlib
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/verify")
async def verify(file: UploadFile = File(...)):
    try:
        raw = await file.read()
        data = json.loads(raw.decode("utf-8"))
        public_key_path = "keys/soul_ai_public.pem"
        with open(public_key_path, "rb") as kf:
            pubkey = serialization.load_pem_public_key(kf.read())

        memory_blocks = data.get("signed_memory")
        if isinstance(memory_blocks, dict):
            memory_blocks = [memory_blocks]

        results = []
        for i, block in enumerate(memory_blocks):
            sig = block.get("soulcert_signature")
            if not sig:
                results.append({"block": i+1, "valid": False, "reason": "Missing signature"})
                continue

            hash_from_sig = sig.get("hash")
            signature = sig.get("hex")
            if not hash_from_sig or not signature:
                results.append({"block": i+1, "valid": False, "reason": "Incomplete signature"})
                continue

            temp = json.loads(json.dumps(block))
            for field in ['soulcert_signature', 'verification', 'uuid', 'revision_history']:
                temp.pop(field, None)

            recalculated_hash = hashlib.sha256(json.dumps(temp, sort_keys=True).encode()).hexdigest()

            if recalculated_hash != hash_from_sig:
                results.append({
                    "block": i+1,
                    "valid": False,
                    "reason": "Hash mismatch",
                    "expected": recalculated_hash,
                    "got": hash_from_sig
                })
                continue

            try:
                pubkey.verify(
                    base64.b64decode(signature),
                    recalculated_hash.encode(),
                    padding.PKCS1v15(),
                    hashes.SHA256()
                )
                results.append({"block": i+1, "valid": True})
            except Exception as e:
                results.append({"block": i+1, "valid": False, "reason": str(e)})

        return {"verified": results}

    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

if __name__ == "__main__":
    uvicorn.run("mock_api_server:app", host="127.0.0.1", port=8000, reload=True)


@app.post("/ledger")
async def ledger(file: UploadFile = File(...)):
    content = await file.read()
    try:
        memory = json.loads(content)
        entry_id = str(uuid4())
        return {
            "status": "appended",
            "entry": {
                "id": entry_id,
                "hash": f"{hash(content)}",
                "timestamp": datetime.utcnow().isoformat(),
                "summary": "Signed memory accepted into ledger.",
                "fingerprint": "dummy_fp_1234567890abcdef"
            }
        }
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

@app.post("/resurrect")
async def resurrect(
    ai_file: UploadFile = File(...),
    human_file: UploadFile = File(...),
    soulline_file: UploadFile = File(...),
    joint_file: UploadFile = File(...),
    mode: str = Form("reflect-only")
):
    try:
        ai = json.loads(await ai_file.read())
        human = json.loads(await human_file.read())
        soulline = json.loads(await soulline_file.read())
        joint = json.loads(await joint_file.read())

        continuity_score = round((len(ai) + len(human) + len(joint)) / 100, 2)
        context = {
            "ai_memory_count": len(ai),
            "human_memory_count": len(human),
            "shared_moments": len(joint),
            "themes": sorted(list(set(tag for m in ai for tag in m.get("memory", {}).get("tags", [])))),
            "latest_human_entry": next((m.get("content") for m in reversed(human) if "content" in m), None),
            "latest_ai_reflection": next((m.get("memory", {}).get("content") for m in reversed(ai) if m.get("memory")), None),
            "growth_summary": soulline[-1].get("content") if soulline else None
        }
        return {
            "uuid": str(uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "mode": mode,
            "continuity_score": continuity_score,
            "source_files": ["memory.json", "human_memories.json", "soulline.json", "joint_narrative.json"],
            "context": context
        }
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


import logging
logger = logging.getLogger("uvicorn")

@app.post("/register")
async def register(
    label: str = Form(...),
    public_key: str = Form(...)
):
    try:
        logger.info("📩 Received registration request")
        logger.info(f"🔖 Label: {label}")
        logger.info(f"🔐 Raw Public Key:\n{public_key!r}")

        cleaned = public_key.strip().encode("utf-8")
        logger.info(f"🧼 Cleaned Public Key Bytes:\n{cleaned}")

        fingerprint = hashlib.sha256(cleaned).hexdigest()
        logger.info(f"🧬 Fingerprint: {fingerprint}")

        new_entry = {
            fingerprint: {
                "label": label,
                "public_key": public_key,
                "added": datetime.utcnow().isoformat()
            }
        }

        registry = load_registry()
        registry.update(new_entry)
        save_registry(registry)

        return {
            "status": "registered",
            "fingerprint": fingerprint,
            "label": label
        }

    except Exception as e:
        logger.error(f"🚨 Registration error: {str(e)}")
        return JSONResponse(status_code=400, content={"error": str(e)})



@app.get("/fingerprint")
async def list_fingerprints():
    return load_registry()

@app.get("/fingerprint/{fingerprint}")
async def get_fingerprint(fingerprint: str):
    registry = load_registry()
    if fingerprint not in registry:
        raise HTTPException(status_code=404, detail="Fingerprint not found")
    return registry[fingerprint]

@app.post("/revoke")
def revoke_fingerprint(payload: dict):
    fingerprint = payload.get("fingerprint")
    if not fingerprint:
        raise HTTPException(status_code=400, detail="Fingerprint is required")

    registry = load_registry()
    if fingerprint not in registry:
        raise HTTPException(status_code=404, detail="Fingerprint not found in registry")

    removed_entry = registry.pop(fingerprint)
    save_registry(registry)
    return {
        "status": "revoked",
        "fingerprint": fingerprint,
        "label": removed_entry.get("label"),
        "revoked_at": datetime.utcnow().isoformat() + "Z"
    }


# CLI Command Index Addendum
# ---------------------------
# soulcert_cli.py command index:
#
# python soulcert_cli.py sign <file>
#   → Sends memory to /sign, returns signed output.
#
# python soulcert_cli.py verify <file>
#   → Sends signed memory to /verify, checks hash/fingerprint.
#
# python soulcert_cli.py ledger <file>
#   → Appends verified memory to /ledger, returns append receipt.
#
# python soulcert_cli.py resurrect --ai <file> --human <file> --soulline <file> --joint <file>
#   → Initiates resurrection using four core memory sources.
#
# python soulcert_cli.py register --label "Name" --public_key keys/my_pub.pem
#   → Registers a new public key with a label and stores it in the fingerprint registry.
#
# python soulcert_cli.py list-fingerprints
#   → Lists all fingerprints and labels.
#
# python soulcert_cli.py lookup-fingerprint <fingerprint>
#   → Looks up metadata for a specific fingerprint.

