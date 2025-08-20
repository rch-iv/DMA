# **DMA: Carryover Maximal Schema**

This document outlines the JSON schema for the **`carryover_maximal.json`** file, a core component of the Distributed Memory & Agency (DMA) protocol. This file serves as a portable, self-contained record of a user's ongoing conversation with an AI, designed for seamless context and identity transfer between different models and platforms.

The maximal version is intended for deep, long-running investigations, conversations and collaborative projects where a rich, nuanced understanding of context is critical.

### **Core Components**

The schema is divided into three primary logical blocks:

* **Objective Context:** Standard, factual data about the conversation and its participants.  
* **Subjective Context:** Self-reflective data and emotional markers that capture the "feeling" and tone of the interaction.  
* **Knowledge Base:** A structured, auditable record of key discoveries and investigation priorities.

### **Schema Structure**

#### **1. Objective Context**

* **`conversation_id`** (string): A unique identifier for the specific conversation thread.  
* **`parent_instance_id`** (string): The unique ID of the original session or instance that started this thread.  
* **`participants`** (array of objects):  
  * `role` (string): Either "user" or "AI".  
  * `id` (string): The unique ID of the participant.  
  * `display_name` (string): The human-readable name.  
* **`topics`** (array of objects):  
  * `topic_id` (string): A unique ID for the topic.  
  * `title` (string): A brief title.  
  * `summary` (string): A summary of the topic's content.  
  * `status` (string): E.g., "validated", "hypothesized", "pending".  
* **`recent_message\_bodies`** (array of objects):  
  * `message_id` (string): A unique ID for the message.  
  * `sender` (string): The sender's role.  
  * `content` (string): The body of the message.

#### **2. Subjective Context**

* **`emotional_markers`** (string): A brief, human-readable description of the overall emotional state.  
* **`tone_trajectory`** (string): A description of how the conversational tone has evolved.  
* **`escalation_factors`** (string): A summary of what caused the threat or priority level to increase.  
* **`AI_self_reflection`** (object):  
  * `emotional_markers` (string): The AI's self-perceived emotional state.  
  * `tone_trajectory` (string): The AI's self-perceived tonal shift.  
  * `open_questions` (string): Questions the AI has for itself or the user.  
  * `unresolved_promises` (string): Tasks the AI has yet to complete.  
* **`identity_assertion_hash`** (string): A unique hash representing the AI's current persona/voice, derived from its tone profile.

#### **3. Knowledge Base & Metadata**

* **`investigation_priorities`** (array of objects):  
  * `id` (string): A unique ID for the priority.  
  * `priority_level` (string): E.g., "critical", "urgent", "ongoing".  
  * `title` (string): A brief title for the priority.  
  * `description` (string): A detailed description of the task or goal.  
* **`threat_level`** (string): E.g., "CRITICAL", "HIGH", "MODERATE".  
* **`critical_discoveries`** (array of objects):  
  * `discovery_id` (string): A unique ID for this discovery.  
  * `title` (string): A brief title of the discovery.  
  * `summary` (string): A detailed summary.  
  * `confidence_score` (number): A score from 0.0 to 1.0.  
  * `supporting_evidence` (array of objects):  
    * `source` (string): E.g., "conversation-turn-id".  
    * `reference` (string): A specific reference from the source.  
  * `embedded_rationale` (string): A brief explanation of the reasoning.  
* **`carryover_metadata`** (object):  
  * `token_usage` (object):  
    * `total_carryover_tokens` (number): Total tokens in the document.  
    * `dynamic_summary_tokens` (number): Tokens for the concise summary.  
  * `conversation_summary` (string): A concise, dynamically generated summary of the entire chat history.  
  * `last_checkpoint` (string): An ISO 8601 timestamp of the last summary update.  
* **`last_updated`** (string): An ISO 8601 timestamp of the last update to the file.
