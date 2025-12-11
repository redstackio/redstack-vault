---
tags:
  - use-after-free
  - race-condition
  - kernel
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
id: 8c6747fd-6a0b-40ef-9c32-823f212f6446
created_at: '2025-12-11T06:10:28.814Z'
updated_at: '2025-12-11T06:10:28.814Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Trigger Use-After-Free via Race Condition in setsockopt

## Summary

This procedure exploits a use-after-free vulnerability in the IPV6_2292PKTOPTIONS option of setsockopt by creating a race condition to free the struct ip6_pktopts buffer while it is being processed by ip6_setpktopt, leading to potential kernel memory manipulation.

## Description

The vulnerability arises from missing locks in the kernel, allowing concurrent operations to free memory during processing. This was verified on PS4 firmware 7.02 and FreeBSD via reverse engineering and PoC. The procedure sets up a race to trigger the UAF, enabling pointer hijacking for further exploitation.

## Requirements

1. Local code execution on FreeBSD or PS4
2. IPv6 support enabled in the kernel
3. Custom PoC code for setsockopt racing

## Defense

Defensive measures and detection strategies:

- Apply kernel patches for locking in setsockopt handling
- Monitor for unusual setsockopt calls or kernel crashes via system logs

## Objectives

1. Trigger the race condition to free memory prematurely
2. Create a dangling pointer for hijacking
3. Prepare for kernel R/W primitives

## Instructions

### Step 1: Set Up Racing Threads

**Context**: Create concurrent threads to call setsockopt with IPV6_2292PKTOPTIONS, timing one to free the buffer during ip6_setpktopt processing.

Develop and run a PoC in C that uses pthreads for racing the setsockopt calls, exploiting the missing locks.

> Expected: Kernel allows free during processing, resulting in UAF.

### Step 2: Verify Race Success

**Context**: Monitor for successful free operation without immediate crash.

Use debugging tools or logs to confirm the struct ip6_pktopts was freed while in use.

> Expected: Dangling pointer available for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[use-after-free]]
- [[race-condition]]
