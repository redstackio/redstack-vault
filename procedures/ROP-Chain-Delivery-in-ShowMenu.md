---
id: proc-rop-delivery-001
tags:
  - rop
  - chain-delivery
type: procedure
tools:
  - '[[tools/CSGO-Malicious-Server-Simulator]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:42.206Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# ROP-Chain-Delivery-in-ShowMenu

## Summary

Delivers a Return-Oriented Programming (ROP) chain to the Source Engine client via CCSUsrMsg_ShowMenu, storing it in a global buffer using addresses derived from the leaked base for subsequent execution hijack.

## Description

After ASLR bypass, the ROP chain (gadgets for shellcode execution, e.g., to launch calc.exe) is embedded in a user message and stored in client_panorama.dll's buffer. The message type allows arbitrary data placement. Requires prior pointer leakage and reconnection.

## Requirements

1. Leaked base address from prior leakage.
2. Crafted ROP gadgets compatible with client binary.
3. Server to send user messages.

## Defense

Defensive measures and detection strategies:

- Validate user message contents and lengths.
- DEP/NX bits to prevent ROP execution.
- Monitor buffer overflows in UI messages.

## Objectives

1. Store ROP chain in accessible buffer.
2. Address gadgets relative to leaked base.
3. Prepare for vtable redirection.

## Instructions

### Step 1: Queue Reconnect

**Context**: Ensure session continuity post-leak.

Send retry:

```protobuf
Server sends connection retry command
```

> Client reconnects without dropping.

### Step 2: Send ShowMenu with ROP

**Context**: Embed chain in menu message.

In script:

```python
msg = CCSUsrMsg_ShowMenu()
msg.menu_string = rop_chain_data  # Addressed with base
send_to_client(msg)
```

> Stores chain in global buffer; calc.exe VirtualAlloc + CreateProcess gadgets.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (via ROP)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/CSGO-Malicious-Server-Simulator]]

## Tags

- [[rop]]
- [[chain-delivery]]
