---
tags:
  - buffer-overflow
  - heap-overflow
  - exfat
  - usb
  - jailbreak
  - ps4
  - ps5
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - PS4
  - PS5
complexity: high
procedures:
  - '[[procedures/Craft-Malformed-exFAT-USB]]'
  - '[[procedures/Insert-Malformed-USB-into-Console]]'
  - '[[procedures/Exploit-Buffer-Overflow-for-Heap-Corruption]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Exploitation for Privilege Escalation]]'
description: >-
  Exploits a heap-based buffer overflow in Sony's exFAT filesystem to achieve
  memory corruption and potential kernel code execution on PS4/PS5 via a
  malformed USB drive.
skill_level: advanced
impact_level: high
id: 71f22082-3316-4d9d-9f23-c18cd5e9f6f0
created_at: '2025-12-11T03:47:39.386Z'
updated_at: '2025-12-11T03:47:39.386Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1203]]'
  - '[[T1068]]'
---
# Heap Buffer Overflow in exFAT for PS4/PS5 Jailbreak via Malformed USB

Multi-stage attack chain demonstrating a complete workflow to exploit a heap-based buffer overflow in the exFAT filesystem implementation on Sony PS4 and PS5 consoles, leading to memory corruption and potential jailbreak through kernel code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via USB] --> B[Trigger Filesystem Read]
    B --> C[Heap Corruption and Exploitation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specified; requires tools for creating exFAT images (e.g., disk imaging software)

### Target Environment

- PS4 or PS5 console
- USB port access
- No specific network requirements

### Initial Access Requirements

- Physical access to the console's USB port
- Ability to create and format USB drives

## Detailed Attack Procedures

### Step 1: Craft Malformed exFAT USB - [[procedures/Craft-Malformed-exFAT-USB]]

**Procedure**: [[procedures/Craft-Malformed-exFAT-USB]]

**Objective**: Create a USB flash drive with a malformed exFAT structure to trigger the vulnerability.

**Expected Output**: A USB drive that, when inserted, causes the console to attempt reading an oversized up-case table.

**Success Indicators**:
- USB drive successfully formatted with exFAT and modified up-case table entry.
- dataLength set to a large value like 0x100000200 and sectorSize to 0x200.

Craft a malformed exFAT USB flash drive with an oversized dataLength in the up-case table entry. Set dataLength to a large value like 0x100000200 and sectorSize to 0x200 to cause size calculation that truncates to 0x200 during allocation. Use disk imaging tools to modify the exFAT structure accordingly.

### Step 2: Insert Malformed USB into Console - [[procedures/Insert-Malformed-USB-into-Console]]

**Procedure**: [[procedures/Insert-Malformed-USB-into-Console]]

**Objective**: Introduce the malformed USB to the target console to initiate the filesystem mounting process.

**Expected Output**: The console attempts to mount the USB and read the up-case table, triggering the vulnerable function.

**Success Indicators**:
- USB is recognized by the console.
- Filesystem mounting process begins without immediate errors.

Plug the malformed USB into the PS4/PS5. The system attempts to read the up-case table, triggering the UVFAT_readupcasetable function.

### Step 3: Exploit Buffer Overflow for Heap Corruption - [[procedures/Exploit-Buffer-Overflow-for-Heap-Corruption]]

**Procedure**: [[procedures/Exploit-Buffer-Overflow-for-Heap-Corruption]]

**Objective**: Leverage the buffer overflow to corrupt heap objects and achieve code execution.

**Expected Output**: Heap corruption leading to potential control over kernel structures like usb_endpoint.

**Success Indicators**:
- Evidence of memory corruption, such as system crashes or unexpected behavior indicating overflow.
- Successful jailbreak if fully exploited.

Exploit the buffer overflow to corrupt heap objects. The under-allocated buffer overflows during repeated UVFAT_ReadDevice calls, allowing corruption of subsequent heap objects like usb_endpoint structures with pointers.

## Attack Chain Summary

### Key Achievements

1. Successful triggering of heap-based buffer overflow via USB.
2. Memory corruption enabling kernel-level access.
3. Potential for full jailbreak and code execution on PS4/PS5.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
