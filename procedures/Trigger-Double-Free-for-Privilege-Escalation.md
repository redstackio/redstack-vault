---
tags:
  - double-free
  - memory-corruption
  - privilege-escalation
type: procedure
tools:
  - '[[tools/poc.c]]'
  - '[[tools/ps4.c]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - PS4
  - FreeBSD
techniques:
  - '[[procedures/Trigger-Double-Free-for-Privilege-Escalation]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 533714b8-9cf1-4060-a797-4e70fe088f18
created_at: '2025-12-11T03:47:39.440Z'
updated_at: '2025-12-11T03:47:39.440Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Trigger Double Free for Privilege Escalation

## Summary

This procedure exploits the double free vulnerability to cause memory corruption and achieve kernel privilege escalation.

## Description

The double free in IP6_EXTHDR_CHECK leads to use-after-free behavior when new mbufs are allocated, enabling reliable escalation on FreeBSD (~80%) and PS4 (~20%).

## Requirements

1. Successful packet sending from previous steps
2. Vulnerable kernel version
3. Monitoring for crash or escalation

## Defense

Defensive measures and detection strategies:

- Update kernel to patch double free in IPv6 handling
- Use kernel exploit detection tools

## Objectives

1. Induce memory corruption
2. Escalate to kernel privileges
3. Enable data theft or unauthorized code execution

## Instructions

### Step 1: Execute Trigger

**Context**: Run the PoC to trigger the double free.

Continue from packet sending; the macro will free the mbuf twice due to unupdated pointers.

> Expected: Memory corruption occurs.

### Step 2: Exploit Corruption

**Context**: Leverage use-after-free for escalation.

Allocate new mbufs in the freed space to gain control and escalate privileges.

> Expected: Root shell or kernel access achieved.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[procedures/Trigger-Double-Free-for-Privilege-Escalation]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/poc.c]]
- [[tools/ps4.c]]

## Tags

- #double-free
- #memory-corruption
