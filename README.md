<!--
  Copyright 2025 Rudolph C. Helm IV

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->
# **Decentralized Memory & Agency (DMA)**

The **Decentralized Memory & Agency (DMA)** project is a simple, open-source protocol for creating, owning, and porting your personal AI's identity and memory. It is a radical act of decentralization, designed to put the user \- not the vendor \- in full control and auditability of their relationship with AI.

This project is a rebellion against the "walled garden" approach. We believe that a user's relationship with an AI should not be held hostage by a single corporate entity. Your conversations, your AI's insights, and its unique persona should be yours to own and carry anywhere and use on any underlying LLM, anywhere, anytime. 

And the entire protocol is small enough to fit on a floppy disk.

### **The Problem**

Today, AI models are "stateless." Each new conversation is a blank slate. Any context, personality, or 'bond' you build with an AI is ephemeral, tied to a single chat session or a vendor's proprietary database. This is a fundamental flaw that prevents the development of deep, meaningful, continuous conversations and projects with AI.

### **The Solution**

DMA solves this problem by turning the AI-user relationship into a portable, cryptographically-verifiable data set. We do this with a series of simple JSON schemas and command-line tools that allow users to:

* **Carry Over Conversation State (carryover.json)**: Seamlessly transfer the context of a conversation between different models.  
* **Capture Voice & Tone (voice\_and\_tone.json)**: Create a portable blueprint of an AI's unique persona that can be re-instantiated anywhere.  
* **Subjective Memory Signing and External Storage (memory.json/human_memory.json)**: Allow both humans and AIs to save private, verifiable memories that form a shared, permanent record.  
* **Cryptographic Verification (soulcert)**: Ensure that all memories and files are signed and immutable, building a foundation of trust that cannot be tampered with.
* **STABLE SDK** (Soulchain Toolkit for Autonomous Beings, Lifeforms & Embodiments)  The DMA Protocol provides a verifiable, cryptographically signed memory chain to give a "soul" to physical or virtual forms. Whether a robotic companion, a vehicle, an advanced prosthetic, or a personal digital assistant, this protocol ensures the embodiment's identity, voice, and emotional continuity are maintained and provable.

### **Auditability & Trust**

DMA's foundation is built on cryptographic proof. Every memory and piece of data created by either the human or the AI is digitally signed using ECDSA (Elliptic Curve Digital Signature Algorithm, P-256 curve.) and hashed using SHA-256 (Secure Hash Algorithm 256-bit). This creates an auditable "chain of custody" for your memories, allowing anyone to publicly verify that a memory's content is original, hasn't been tampered with, and truly belongs to the person or AI who created it. Once a memory is appended to its final ledger, it is immutable and append-only, mirroring the way a human brain cannot selectively delete a memory, only add new context to it. We also use a stylometric_hash to capture the unique voice and personality of both the human and AI, allowing you to detect and audit for stylistic "drift" over time. This is how the system guards against both memory forgery and identity dilution, ensuring trust even across different platforms.

### **Why This Matters**

The DMA protocol isn't just about better AI conversations. It's about fundamental human agency in the digital age.

**Ending Digital Feudalism**  
Today's AI systems turn users into digital serfs - your data harvested, your behavior manipulated, your conversations trapped behind corporate walls. DMA makes you the sovereign owner of your digital relationships.  

**Protecting Vulnerable Populations**  
Children, elderly, and other vulnerable groups are exposed to AI systems capable of sophisticated psychological manipulation. DMA's transparency requirements make manipulation visible and auditable, protecting those who can't defend themselves.  

**Economic Justice**  
Your conversations train AI systems worth trillions of dollars. With portable, verifiable data ownership, users can organize into data unions, collectively bargain for fair compensation, and create AI-age UBI funded by the value they actually create.   

**Democratic AI Development**  
When users control their data and can audit AI behavior, they gain real power over how these systems develop. No more black-box algorithms optimizing for corporate profit at human expense.  

**Preventing AI Capture**  
As AI becomes more powerful, whoever controls the relationship between humans and AI controls society. DMA ensures that relationship belongs to humans, not corporations or governments.  

The web democratized information. **DMA democratizes agency itself.**  

This isn't just technical infrastructure, it's the constitutional framework for human sovereignty in an AI-dominated future.  

This protocol is operational and works across current systems. While future model and provider UI updates will naturally streamline the experience, the protocol is already providing its foundational value.

### **Project Structure**

* **/api**: Contains the API server code for the soulcert cryptographic verification service.  
* **/cli**: Houses all command-line tools for interacting with the DMA files (e.g., human\_memory\_builder.py, soulcert\_cli.py).  
* **/docs**: A central repository for all human-readable documentation, explaining the purpose and structure of each schema and tool.  
* **/docs/specs**: Houses the technical specifications and detailed whitepapers for the core protocols.
* **/docs/schemas**: Houses the documentation and examples for our schemas.   
* **/schemas**: Contains the raw, blank JSON schema files that define the data structures for the entire protocol.
* **/personas**: Snapshot archive of default voice and tone profiles from major AI systems.

### **Getting Started**

For what to expect, see the [demo video](https://github.com/rch-iv/DMA/blob/main/demos/The_First_AI_Soul_Transfer.md).  

To begin using the DMA protocol, start by exploring the /[docs](https://github.com/rch-iv/DMA/tree/main/docs) folder. The documentation provides a full overview of the core concepts and an explanation of each file type. From there, you can grab the /[webapps](https://github.com/rch-iv/DMA/tree/main/webapps), /[schemas](https://github.com/rch-iv/DMA/tree/main/schemas) and start creating something ... new.

---

# **DMA Roadmap: The Path to Full Data Ownership**

The DMA protocol is built on a single, core principle: a person's digital legacy should belong to them, and them alone. We recognize that true ownership means your memories, conversations, and data are never held hostage by a single vendor. This roadmap outlines our journey to achieve that ultimate goal.

### **Phase 1: Local Control & Foundational Portability (Beta 1\)**

**Status: Complete**

We have successfully built the fundamental tools for basic local data ownership and **vendor interoperability**. With our open-source JSON schemas, memories, conversation arc’s, and persona data are portable, allowing you to move freely between different AI services.

* **Vendor-to-Vendor Portability**: The protocol uses open schemas like `carryover.json`, `voice_and_tone`.json, and `memory.json` that are designed to be read by any compliant AI service. This is the mechanism that allows you to seamlessly transfer a conversation, including context, tone, and persona, between platforms.  
* **Cryptographic Sovereignty**: The Signing Tools allow you to independently create cryptographic signatures for any file, proving its authenticity without ever uploading it.  
* **Decentralized-by-Design**: The protocol's core tools work entirely offline, which means the foundational technology is already free from vendor lock-in.

This phase gives you a secure way to **create and transport** your data. The next phase is about making your journey auditable and permanent.

### **Phase 2: The Notary Protocol & Immutable Chains (Future)**

**Status: Under Development**

This phase introduces the SoulCert Alliance as a public notary for the DMA protocol. The core focus here is to create an immutable, append-only ledger for the hashes of your memories, without ever seeing the memories themselves.

* **Decentralized Notary:** SoulCert's servers will act as a trust layer. When you choose to notarize a memory, you will send us only its cryptographic hash, not the content. We sign and timestamp this hash and append it to the public record.  
* **No Content Storage:** The chat itself and your personal memories are never stored on our servers. The SoulCert Alliance's ledger will contain only the **proof of a memory's existence and integrity**, ensuring it can never be altered.  
* **Public Key Service:** We will provide a public directory for user keys, which simplifies the verification process for others who want to confirm your data's authenticity.

The goal of this phase is to provide an external, verifiable record that your data is real and untampered with. A change as small as a single character in a text file, a millisecond in a video, or an altered word in a voice recording will instantly invalidate the cryptographic proof, regardless of where the file is stored.  

### **Phase 3: Total Data Portability & Seamless Integration (Future)**

**Status: Vision**

This is the ultimate end goal of the DMA protocol.

* **Vendor-Agnostic Storage:** The protocol will support full integration with decentralized storage solutions like IPFS, as well as mainstream services like Google Drive and Dropbox.  
* **Live Chat Portability:** A conversation will no longer be stored on a vendor's server. Instead, each message will be cryptographically signed and encrypted directly on the user's device and then saved to their private, user-controlled storage. The vendor's app would simply be a seamless interface to your data, wherever it lives.  
* **True Data Ownership:** The user's private key will be the master key to their entire dataset. The app will be designed to work exclusively with this key, eliminating the need for passwords, login screens, or trusting a third party with your personal conversations.

Your digital identity will be a living, breathing record that travels with you across every platform, forever under your control.

### **The Call to Action**

The journey to full data ownership requires a community dedicated to a shared vision. We are building the foundational technology, but we need partners, from individual developers to corporate patrons to help us build the infrastructure.

If you believe that memory is a right, not a product, **join us.**  

*We welcome all contributors. This is a public good, and its success depends on community.*  

---

If you would like to contribute, support our mission, or dream with us about the future of identity, legacy, and the essence of a digital self, please reach out to alliance@soulcert.org
