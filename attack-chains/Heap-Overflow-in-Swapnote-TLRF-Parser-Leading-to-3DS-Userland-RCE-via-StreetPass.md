---
id: ac-nintendo-3ds-swapnote-heap-overflow-rce
tags:
  - heap-overflow
  - rce
  - streetpass
  - 3ds
  - embedded-exploit
  - reverse-engineering
type: attack_chain
tools:
  - '[[tools/Ghidra]]'
  - '[[tools/Hex-Editor]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Nintendo 3DS
submitted: true
complexity: high
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Reverse-Engineer-Swapnote-TLRF-Parser]]'
  - '[[procedures/Craft-Malicious-TLRF-Chunk-for-Heap-Overflow]]'
  - '[[procedures/Exploit-via-StreetPass-Message-Exchange]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:41.410Z'
description: >-
  Multi-stage exploit chain leveraging a heap overflow vulnerability in the
  Nintendo 3DS Swapnote application's TLRF chunk parser to achieve remote code
  execution in userland via StreetPass message exchange.
skill_level: advanced
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Exploit Public-Facing Application]]'
---
# Heap Overflow in Swapnote TLRF Parser Leading to 3DS Userland RCE via StreetPass

Multi-stage attack chain demonstrating a complete exploit workflow for a heap overflow vulnerability in the Nintendo 3DS Swapnote application, enabling remote code execution in userland through StreetPass message exchange.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~120 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reverse Engineering] --> B[Craft Malicious Payload]
    B --> C[Trigger via StreetPass]
    C --> D[Remote Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Ghidra]]
- [[tools/Hex-Editor]]

### Target Environment

- Target OS/Platform: Nintendo 3DS firmware with Swapnote application installed
- Required services/ports: StreetPass communication (local wireless, no specific ports exposed)
- Network access requirements: Physical proximity for StreetPass (within ~10 meters)

### Initial Access Requirements

- Credential requirements: None (exploits application parser)
- Network position: Attacker must be in StreetPass range of target
- Prior access needed: Swapnote app must be installed and StreetPass enabled on target

## Detailed Attack Procedures

### Step 1: Reverse Engineering
procedure: [[procedures/Reverse-Engineer-Swapnote-TLRF-Parser]]

**Objective**: Analyze the Swapnote application's TLRF chunk parser to identify vulnerable memcpy operations.

**Instructions**: Use [[tools/Ghidra]] to disassemble the Swapnote binary and locate the TLRF parsing routine. Focus on heap buffer allocations and memcpy calls that use user-controlled offsets and sizes from the TLRF buffer.

**Expected Output**: Identification of unsafe memcpy at specific offsets (e.g., 0x70C for size, 0x6DC for offset) copying into fixed-size heap buffers.

**Success Indicators**:
- Vulnerable code paths confirmed via disassembly
- Unsafe unlink techniques viable for heap manipulation

### Step 2: Payload Crafting
procedure: [[procedures/Craft-Malicious-TLRF-Chunk-for-Heap-Overflow]]

**Objective**: Create a malicious message file that overflows heap buffers using controlled data.

**Instructions**: Modify a valid Swapnote message file using [[tools/Hex-Editor]]. Set large size values at offsets 0x70C and 0x71C (e.g., 0x1000), and corresponding source offsets at 0x6DC and 0x6EC to copy attacker-controlled data beyond the heap_buffer_0 and heap_buffer_1 boundaries.

**Expected Output**: A crafted .plt message file ready for exchange, with embedded overflow payload targeting unsafe unlink for code execution.

**Success Indicators**:
- Payload file validates as a Swapnote message
- Simulated parsing shows buffer overflow

### Step 3: Exploitation
procedure: [[procedures/Exploit-via-StreetPass-Message-Exchange]]

**Objective**: Deliver the malicious message to trigger RCE on the target device.

**Instructions**: Enable StreetPass on the attacker's 3DS, load the crafted message into Swapnote, and exchange it with the target device in proximity. The target's Swapnote app will parse the TLRF chunk upon receipt, executing the heap overflow and achieving userland RCE.

**Expected Output**: Target device processes the message, leading to controlled heap manipulation and code execution (e.g., shellcode deployment).

**Success Indicators**:
- Message exchanged successfully via StreetPass
- Signs of RCE, such as custom code execution or app crash with manipulation

## Attack Chain Summary

### Key Achievements

1. Identified heap overflow in TLRF parser via reverse engineering
2. Crafted payload exploiting memcpy without bounds checks
3. Achieved remote userland RCE through StreetPass, bypassing typical 3DS security

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
