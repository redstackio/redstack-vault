---
tags:
  - buffer-overflow
  - udf
  - ps4
  - ps5
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 6839fb6d-45cd-4fa1-9882-e93b023d7947
created_at: '2025-12-11T03:47:57.313Z'
updated_at: '2025-12-11T03:47:57.313Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Trigger Buffer Overflow in UDF Driver

## Summary

This procedure triggers a buffer overflow in the UDF driver to cause kernel panics on PS4 and PS5.

## Description

Create a UDF file with inf_len > sector_size, leading to memcpy overflow in udf_read_internal.

## Requirements

1. Custom UDF file with oversized inf_len
2. Network access to send payload
3. Vulnerable UDF driver

## Defense

Defensive measures and detection strategies:

- Add bounds checks in udf_read_internal
- Monitor for kernel crashes from disc loads

## Objectives

1. Overflow buffer
2. Trigger kernel panic
3. Potential code execution

## Instructions

### Step 1: Create Oversized UDF File

**Context**: Set inf_len larger than sector_size.

Craft the UDF structure for overflow.

> This prepares the malicious file.

### Step 2: Send Payload via Netcat

**Context**: Transmit to trigger overflow.

Execute [[commands/nc-send-payload]]:

```bash
nc $PS4IP 1337 < payload.bin
```

> Expected: Kernel panic on target.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used

- [[commands/nc-send-payload]]

## Tools Used

- #netcat

## Tags

- #buffer-overflow
- #udf
