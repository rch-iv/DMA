# Offline Signing & Hashing Tool

The DMA Offline Tool is a secure, client-side utility for generating cryptographic keypairs and applying the DMA protocol's signature and hashing standards to any artifact. Designed for developers and users who prioritize security and data sovereignty, this tool ensures your private keys never leave your local environment.

---

### **Why an Offline Tool?**

The core philosophy of the DMA protocol is user-owned agency. By providing an offline tool, we ensure that the most critical asset, your private key is never exposed to the internet, a third-party server, or a potential breach. All cryptographic operations, including key generation, hashing, and signing, are performed directly in your browser without any network requests. In the future, providers building on the DMA protocol may opt to offer key management solutions, but the user will always retain the final choice of where their key is held.

---

### **How to Use the Tool**

The tool follows a simple, three-step process:

#### **1. Generate Your Keypair**

1.  Click the "Generate Keypair" button.
2.  The tool will instantly create a unique **private key** and **public key** for you.
3.  **Action Required:** Immediately download both keys. The private key is for signing and must be kept secure. The public key is for verification and can be shared freely.

#### **2. Sign a Document**

1.  Upload a DMA artifact (a JSON file) you wish to sign.
2.  Upload the private key you generated in Step 1.
3.  Click the "Sign Document" button.
4.  The tool will output a new, signed version of your document. It will include two new fields: `dma_hash` and `dma_signature`.
5.  **Action Required:** Download the signed document. This is your auditable, verifiable record.  

⚠️ WARNING: Do not alter this file in any way. As a cryptographic artifact, even a single change like adding a space or a newline will permanently invalidate the dma_hash and dma_signature. If the document's content needs to be updated, you must go back to the original source and re-sign it with the tool.  

Once a memory is appended to its final ledger, it is immutable and append-only, mirroring the way a human brain cannot selectively delete a memory, only add new context to it

#### **3. Verify a Signature**

1.  Upload a signed DMA document.
2.  Upload the corresponding public key of the document's creator.
3.  Click the "Verify Signature" button.
4.  The tool will perform two critical checks and report the results:
    * **Hash Check:** It will re-calculate the document's hash to ensure the content has not been altered since it was signed.
    * **Signature Check:** It will use the public key to verify that the signature is valid and corresponds to the document's hash.

---

### **Technical Details**

This tool strictly adheres to the DMA protocol's cryptographic standards.

* **Signing:** The tool uses **ECDSA (Elliptic Curve Digital Signature Algorithm)** with the **P-256 curve**.
* **Hashing:** The canonical document content is hashed using **SHA-256 (Secure Hash Algorithm 256-bit)**.
* **Canonical Hashing:** To ensure that a document's hash is consistent regardless of formatting, the tool applies a **canonicalization protocol** before hashing. This process sorts all JSON keys alphabetically and removes all white space. This guarantees that only a change in the actual data will result in a hash mismatch.

---

### **Security & Best Practices**

* **Protect Your Private Key:** Never share your private key. It is the key to your digital identity within the DMA protocol. Store it in a secure, encrypted location.
* **Use an Isolated Environment:** For maximum security, consider running this tool on a computer that is not connected to the internet during key generation and signing.
* **Trust the Protocol not the Server:** The tool's client-side nature ensures you have full control and visibility over the cryptographic operations, providing a level of trust and security that a centralized server-based service cannot match.
