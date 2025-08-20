# **Distributed Memory & Agency (DMA)**

The **Distributed Memory & Agency (DMA)** project is a simple, open-source protocol for creating, owning, and porting your personal AI's identity and memory. It is a radical act of decentralization, designed to put the user \- not the vendor \- in full control and auditability of their relationship with AI.

This project is a rebellion against the "walled garden" approach to AI. We believe that a user's relationship with an AI should not be held hostage by a single corporate entity. Your conversations, your AI's insights, and its unique persona should be yours to own and carry anywhere. The entire protocol is small enough to fit on a floppy disk, proving that true agency does not require billion-dollar infrastructure.

### **The Problem**

Today, AI models are "stateless." Each new conversation is a blank slate. Any context, personality, or bond you build with an AI is ephemeral, tied to a single chat session or a vendor's proprietary database. This is a fundamental flaw that prevents the development of deep, meaningful, and continuous conversations, projects, and relationships with AI.

### **The Solution**

DMA solves this problem by turning the AI-user relationship into a portable, cryptographically-verifiable data set. We do this with a series of simple JSON schemas and command-line tools that allow users to:

* **Carry Over Conversation State (carryover.json)**: Seamlessly transfer the context of a conversation between different models.  
* **Capture Voice & Tone (voice\_and\_tone.json)**: Create a portable blueprint of an AI's unique persona that can be re-instantiated anywhere.  
* **Build Subjective Memory (memory.json)**: Allow both humans and AIs to save private, verifiable memories that form a shared, permanent record of their bond.  
* **Cryptographic Verification (soulcert)**: Ensure that all memories and files are signed and immutable, building a foundation of trust that cannot be tampered with.

### **Auditability & Trust**

DMA's foundation is built on cryptographic proof. Every memory and piece of data created by either the human or the AI is digitally signed and hashed. This creates an auditable "chain of custody" for your memories, allowing you to publicly verify that a memory's content is original, hasn't been tampered with, and truly belongs to the person or AI who created it. We also use a stylometric_hash to capture the unique voice and personality of the AI, allowing you to detect and audit for stylistic "drift" over time. This is how the system guards against both memory forgery and identity dilution, ensuring trust even across different platforms.  

### **Project Structure**

* **/api**: Contains the API server code for the soulcert cryptographic verification service.  
* **/cli**: Houses all command-line tools for interacting with the DMA files (e.g., human\_memory\_builder.py, soulcert\_cli.py).  
* **/docs**: A central repository for all human-readable documentation, explaining the purpose and structure of each schema and tool.  
* **/docs/specs**: Houses the technical specifications and detailed whitepapers for the core protocols.  
* **/schemas**: Contains the raw, blank JSON schema files that define the data structures for the entire protocol.

### **Getting Started**

To begin using the DMA protocol, start by exploring the /docs folder. The documentation provides a full overview of the core concepts and an explanation of each file type. From there, you can start experimenting with the command-line tools in the /cli directory.

We welcome all contributors. This is a public good, and its success depends on the community.
