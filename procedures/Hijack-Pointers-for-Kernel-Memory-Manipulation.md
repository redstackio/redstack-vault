---
tags:
  - pointer-hijack
  - kernel-rw
  - use-after-free
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - FreeBSD
  - PlayStation 4
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 106e1cfe-8ac4-40a2-9f6f-8c81f07af7a5
created_at: '2025-12-11T06:10:28.808Z'
updated_at: '2025-12-11T06:10:28.808Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Hijack Pointers for Kernel Memory Manipulation

## Summary

This procedure involves hijacking pointers in the freed ip6_pktopts structure, such as ip6po_pktinfo, to gain arbitrary kernel read/write primitives after triggering a use-after-free.

## Description

Following the UAF trigger, the freed memory is reallocated with attacker-controlled data, allowing pointer redirection for kernel memory access. This enables reading and writing arbitrary kernel addresses, crucial for escalation.

## Requirements

1. Successful UAF trigger from prior step
2. Ability to allocate memory in the freed slab
3. Knowledge of kernel memory layout

## Defense

Defensive measures and detection strategies:

- Kernel address space layout randomization (KASLR) to hinder pointer prediction
- System call auditing for anomalous memory operations

## Objectives

1. Reallocate freed memory with crafted pointers
2. Achieve kernel R/W access
3. Prepare for code execution

## Instructions

### Step 1: Reallocate Freed Memory

**Context**: Allocate new memory in the place of the freed struct ip6_pktopts.

In the PoC, use malloc or similar to occupy the freed slab with data that hijacks ip6po_pktinfo.

> Expected: Pointer now under attacker control.

### Step 2: Manipulate Kernel Memory

**Context**: Use the hijacked pointer to read/write kernel addresses.

Craft operations via setsockopt to leverage the pointer for arbitrary R/W.

> Expected: Successful kernel memory access verified.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[pointer-hijack]]
- [[kernel-rw]]
