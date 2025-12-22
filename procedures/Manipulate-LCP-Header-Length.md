---
tags:
  - heap-manipulation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: eb01e05c-4adb-4700-863b-03d15d6b01bd
created_at: '2025-12-11T03:47:47.642Z'
updated_at: '2025-12-11T03:47:47.642Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Manipulate LCP Header Length

## Summary

This procedure manipulates the LCP header length to control malloc allocation sizes, enabling targeted heap overwrites in the PS4/PS5 kernel.

## Description

By setting ntohs(h->len), attackers influence buffer sizes, allowing copies from larger mbufs to smaller bufs, overwriting adjacent heap areas.

## Requirements

1. Active PPP session
2. Control over LCP packets
3. Vulnerable kernel version

## Defense

Defensive measures and detection strategies:

- Validate PPP header lengths in kernel
- Use intrusion detection for protocol anomalies

## Objectives

1. Control heap allocation
2. Overwrite heap structures
3. Escalate to RCE

## Instructions

### Step 1: Set Header Length

**Context**: Adjust ntohs(h->len) in LCP packets.

Modify and send LCP packets with custom len values.

### Step 2: Trigger Copy Operation

**Context**: Force the kernel to perform the vulnerable copy.

Send subsequent packets to invoke the allocation and copy.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #heap-manipulation
