---
tags:
  - integer-underflow
  - data-leak
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 581253c3-d5ee-4b05-afe2-b3e3d773429b
created_at: '2025-12-11T03:47:47.638Z'
updated_at: '2025-12-11T03:47:47.638Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Send Crafted PAP REQ Packets

## Summary

This procedure sends crafted PAP_REQ packets to trigger integer underflow and heap-buffer overread, leaking kernel data in PS4/PS5.

## Description

Setting len to 0-5 causes underflow, bypassing checks and enabling OOB memcmp for pointer leaks to defeat KASLR.

## Requirements

1. PPP session in PAP phase
2. Packet crafting tools
3. Target authentication via PAP

## Defense

Defensive measures and detection strategies:

- Enforce strict length checks in PAP processing
- Monitor for underflow attempts in logs

## Objectives

1. Bypass length validation
2. Leak kernel pointers
3. Defeat KASLR

## Instructions

### Step 1: Craft PAP_REQ with Low Len

**Context**: Set ntohs(h->len) to 0-5 for underflow.

Create PAP_REQ packets with small len and large name/passwd lengths.

### Step 2: Send and Analyze Oracle Responses

**Context**: Use responses as oracle for leaked data.

Transmit packets and observe memcmp results for OOB reads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #integer-underflow
- #data-leak
