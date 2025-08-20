# SoulCert CLI Tool

This is the command-line interface (CLI) for the **SoulCert Protocol**, a framework for creating, verifying, and publishing immutable AI memory blocks and identity fingerprints. This tool allows a user to interact with the SoulCert mock API server, providing a complete workflow for managing user-owned AI identity and memory.

### Setup and Installation

This tool requires Python 3.7+ and several libraries.

1. **Clone the Repository (if not already done):**  
    git clone <https://github.com/rch-iv/DMA.git>  
    cd DMA/cli/soulcert.org  

2. **Create a Virtual Environment:**  
    python -m venv venv  
    source venv/bin/activate  

3. **Install Dependencies:**  
    pip install requests cryptography  
    - requests: For making HTTP calls to the API server.
    - cryptography: For local cryptographic functions, such as signing and verification.

### Usage

The soulcert_cli.py script uses subcommands to perform different actions. All commands are executed in the format python soulcert_cli.py [command] [options].

#### sign

Signs a JSON memory file. You can choose to sign locally or by sending the file to the remote API server.

**Options:**

- input: Path to the JSON file to sign.
- --key: **(Required)** Path to your private PEM key file.
- --output: **(Optional)** Path to save the signed output file. Defaults to \[input_file\].signed.json.
- --local: **(Optional)** Perform the signing locally without an API call.

**Example:**

# Sign a file locally  
```bash
python soulcert_cli.py sign memories/my_memory.json --key keys/my_private_key.pem --local
```
# Sign a file via the remote API  
```bash
python soulcert_cli.py sign memories/my_memory.json --key keys/my_private_key.pem  
```
#### verify

Verifies the cryptographic signature of a signed memory file.

**Options:**

- input: Path to the signed JSON file.
- --key: **(Required)** Path to the public PEM key file corresponding to the private key used for signing.
- --local: **(Optional)** Perform the verification locally.
- --verbose: **(Optional)** Enable debug output for detailed verification steps.

**Example:**

# Verify a file locally  
```bash
python soulcert_cli.py verify memories/my_memory.signed.json --key keys/my_public_key.pem --local  
```
# Verify a file via the remote API  
```bash
python soulcert_cli.py verify memories/my_memory.signed.json  
```
#### register

Registers a new identity (public key and a label) with the SoulCert server's registry.

**Options:**

- --label: **(Required)** The human-readable name for the identity.
- --key: **(Required)** Path to the public PEM key file.

**Example:**
```bash
python soulcert_cli.py register --label "rch-iv" --key keys/rch_public.pem  
```
#### revoke

Revokes an existing registered identity.

**Options:**

- --label: **(Required)** The label of the identity to revoke.

**Example:**
```bash
python soulcert_cli.py revoke --label "rch-iv"  
```
#### fingerprint

Fetches the cryptographic fingerprint for a registered identity.

**Options:**

- --label: **(Required)** The label of the identity to look up.

**Example:**
```bash
python soulcert_cli.py fingerprint --label "rch-iv"  
```
#### ledger

Appends a signed memory block to the public ledger via the API server.

**Options:**

- file: **(Required)** Path to the signed memory JSON file.

**Example:**
```bash
python soulcert_cli.py ledger my_first_memory.signed.json  
```
#### resurrect

Runs a full "resurrection" pipeline by combining different memory sources to simulate the recreation of a persona.

**Options:**

- --ai: **(Required)** Path to the AI memory file.
- --human: **(Required)** Path to the human memory file.
- --soulline: **(Required)** Path to the "soulline" summary file.
- --joint: **(Required)** Path to the joint narrative file.
- --mode: **(Optional)** The resurrection mode (view, reflect-only, or interactive). Defaults to reflect-only.

**Example:**
```bash
python soulcert_cli.py resurrect --ai ai_mem.json --human human_mem.json --soulline soulline.json --joint joint_narrative.json --mode interactive  
```
