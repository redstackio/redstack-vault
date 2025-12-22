---
tags:
  - kernel-rw
  - pointer-hijack
  - ipv6
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - FreeBSD
  - PlayStation
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 1cd736ec-bc77-43fb-8bc7-f33b781dc8b9
created_at: '2025-12-11T03:47:39.581Z'
updated_at: '2025-12-11T03:47:39.581Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Achieve Arbitrary Kernel Read/Write Primitives

## Summary

This procedure hijacks pointers in the freed ip6_pktopts structure, such as ip6po_pktinfo, to establish arbitrary read and write access in kernel memory.

## Description

Building on the use-after-free, the attacker reallocates the freed memory and overwrites pointers to control kernel data structures. This primitive allows reading and writing arbitrary kernel addresses, setting the stage for code execution.

## Requirements

1. Successful exploitation of the prior race condition
2. Knowledge of kernel memory layout
3. Custom PoC for pointer manipulation

## Defense

Defensive measures and detection strategies:

- Kernel address space layout randomization (KASLR) if available
- Monitor for anomalous kernel memory operations

## Objectives

1. Hijack specific pointers like ip6po_pktinfo
2. Gain read/write access to kernel memory
3. Avoid kernel crashes during manipulation

## Instructions

### Step 1: Reallocate Freed Memory

**Context**: After freeing the buffer, reallocate the memory slot with controlled data.

> Use socket operations to allocate new structures in the freed slot.

### Step 2: Overwrite Pointers

**Context**: Modify pointers in the structure to point to desired kernel addresses.

> Craft payload to hijack ip6po_pktinfo for R/W control.

### Step 3: Test Primitives

**Context**: Verify ability to read/write arbitrary kernel locations without crashing.

> Perform safe test reads/writes on known addresses.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #kernel-rw
- #pointer-hijack
