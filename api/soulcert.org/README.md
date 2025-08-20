# SoulCert Mock API Server

This FastAPI application serves as a mock backend for the **SoulCert Protocol**, a framework for creating, verifying, and publishing immutable AI memory blocks and identity fingerprints. The protocol aims to establish a user-owned, auditable record of an AI's memory and persona, providing a foundation for data unions, universal basic income (UBI) models, and portable AI identity.

The server simulates the key operations of the protocol, including signing, verifying, and logging memory blocks to a ledger.

### Core Concepts

- **Memory Block:** A JSON object representing a specific moment or state of an AI's memory and identity (e.g., a carryover file).
- **Signature:** A cryptographic signature that proves the integrity of a memory block.
- **Fingerprint:** A unique hash of a public key, used to identify a specific signing entity (e.g., a human user or a trusted AI).
- **Ledger:** An immutable, public record of signed memory blocks.

### Setup and Installation

This server requires Python 3.7+ and several libraries.

1. **Clone the Repository (if not already done):**  
    git clone <https://github.com/rch-iv/DMA.git>  
    cd DMA/api/soulcert.org  

2. **Create a Virtual Environment:**  
    python -m venv venv  
    source venv/bin/activate  

3. **Install Dependencies:**  
    pip install "uvicorn\[standard\]" "fastapi\[all\]" cryptography  
    - uvicorn: The ASGI server to run the application.
    - fastapi: The web framework for the API endpoints.
    - cryptography: For cryptographic operations like signature verification.
4. Create the data Directory and Public Key:  
    The server expects a data directory for its registry and a keys directory containing a public key for verification.  
    mkdir data  
    mkdir keys  
    \# Create or place a public key file named soul_ai_public.pem inside the keys directory.  
    \# The server's /verify endpoint will look for this file.  

5. **Run the Server:**  
    uvicorn mock_api_server:app --reload  
    <br/>The --reload flag will automatically restart the server on code changes, which is useful for development. The server will run on <http://127.0.0.1:8000>.

### API Endpoints

The server provides a set of endpoints that correspond to the core functions of the SoulCert Protocol.

#### 1\. POST /sign

- **Description:** Simulates the signing of a memory block. It accepts a JSON file, hashes its content, and returns a dummy signature and fingerprint.
- **Method:** POST
- **Request Body:** multipart/form-data with a single file field named file.
**Example Response:**
  
```json
    {  
    "signed_memory": { ... },  
    "signature": "signed(hash_of_file)",  
    "fingerprint": "dummy_fp_1234567890abcdef"  
    }  
```

#### 2\. POST /verify

- **Description:** Verifies the integrity and authenticity of one or more signed memory blocks. It checks the content hash against the signature and validates the signature using a pre-configured public key (keys/soul_ai_public.pem).
- **Method:** POST
- **Request Body:** multipart/form-data with a single file field named file. The file should contain a JSON object with one or more signed memory blocks.
**Example Response:**

  ```json 
    {  
    "verified":[  
    {  
    "block": 1,  
    "valid": true  
    },  
    {  
    "block": 2,  
    "valid": false,  
    "reason": "Hash mismatch"  
    }  
    ]  
    }
  ```

#### 3\. POST /ledger

- **Description:** Appends a verified memory block to a conceptual ledger. This endpoint simulates the public publication of the block.
- **Method:** POST
- **Request Body:** multipart/form-data with a single file field named file.
**Example Response:**

```json
    {  
    "status": "appended",  
    "entry": {  
    "id": "uuid4_string",  
    "hash": "hash_of_content",  
    "timestamp": "ISO 8601 string",  
    "summary": "Signed memory accepted into ledger.",  
    "fingerprint": "dummy_fp_1234567890abcdef"  
    }  
    }  
```

#### 4\. POST /resurrect

- **Description:** Simulates the process of "resurrecting" an AI's identity by combining its memory blocks with human and joint narratives. It calculates a "continuity score" and provides a context summary.
- **Method:** POST
- **Request Body:** multipart/form-data with four file fields: ai_file, human_file, soulline_file, and joint_file. It also accepts an optional mode form field.
**Example Response:**

```json 
    {  
    "uuid": "uuid4_string",  
    "timestamp": "ISO 8601 string",  
    "mode": "reflect-only",  
    "continuity_score": 2.5,  
    "source_files": [ ... ],  
    "context": { ... }  
    }  
```

#### 5\. POST /register

- **Description:** Registers a new public key with an associated label. This is used to build the fingerprint registry.
- **Method:** POST
- **Request Body:** multipart/form-data with two form fields: label and public_key.
**Example Response:**

```json 
    {  
    "status": "registered",  
    "fingerprint": "sha256_hash_of_public_key",  
    "label": "Name"  
    }  
```

#### 6\. GET /fingerprint

- **Description:** Returns a list of all registered fingerprints and their associated metadata.
- **Method:** GET

#### 7\. GET /fingerprint/{fingerprint}

- **Description:** Returns the metadata for a single, specific fingerprint.
- **Method:** GET
- **Path Parameter:** fingerprint (a string).

#### 8\. POST /revoke

- **Description:** Revokes a registered fingerprint, effectively de-authorizing it.
- **Method:** POST
- **Request Body:** application/json with a single field "fingerprint".

