---
tags:
  - graphql
  - id-extraction
  - proxy-intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.180Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f59b3c13-1a01-469a-a751-d93d0a57db84
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-LLM-Conversation-and-Extract-ID

## Summary

This procedure creates a new LLM conversation in the revealed Copilot GUI and intercepts the GraphQL response to extract the conversation ID, which is a base64-encoded incrementing integer usable for IDOR exploitation.

## Description

After revealing the UI, interact with it to start a new conversation, triggering a 'NewConversation' GraphQL mutation. Use a proxy to capture the response containing the llm_conversation.id. IDs are predictable, aiding IDOR attacks. This targets the victim account and requires proxy setup for traffic interception.

## Requirements

1. Revealed Copilot GUI from prior procedure
2. Proxy tool configured to intercept HTTPS traffic (e.g., Burp Suite with certificate installed)
3. Valid session on victim account

## Defense

Defensive measures and detection strategies:

- Implement ID randomization or UUIDs instead of sequential base64
- Rate-limit GraphQL mutations and log anomalous ID accesses
- Require authentication tokens tied to user context in all mutations

## Objectives

1. Generate a target conversation for deletion
2. Obtain exploitable ID from network traffic
3. Prepare for cross-account exploitation

## Instructions

### Step 1: Initiate Conversation

**Context**: Use the GUI to create a new LLM conversation, triggering the GraphQL request.

No command; click 'New Conversation' or equivalent in the UI.

> This sends a POST to the GraphQL endpoint. Monitor proxy for the request.

### Step 2: Intercept and Extract ID

**Context**: Capture the response and parse for the conversation ID.

Use Burp Suite proxy history to find the 'NewConversation' operationName response.

> Extract data.newConversation.llm_conversation.id, e.g., "bGxtX2NvbnZlcnNhdGlvbjoxMjM0". Copy for use in deletion.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- id-extraction
