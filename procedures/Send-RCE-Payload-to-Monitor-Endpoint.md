---
tags:
  - exploitation
  - rce
  - deserialization
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-rce-payload]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:27.259Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e9b27fd5-7731-4410-9115-3e58df16a2db
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Send-RCE-Payload-to-Monitor-Endpoint

## Summary

This procedure sends a binary Java deserialization payload to the vulnerable /monitor endpoint in Oracle PeopleSoft, triggering RCE via untrusted data processing.

## Description

The endpoint at https://███/psc/EXPROD/ (resolving to /monitor) deserializes POSTed data without validation, allowing gadget chains to execute. This step exploits the flaw for arbitrary code effects, confirmed via DNS in prior steps.

## Requirements

1. Generated payload file
2. Network access to target URL
3. SSL certificate tolerance (self-signed likely)

## Defense

Defensive measures and detection strategies:

- Disable or secure serialization endpoints
- Use WAF rules to block suspicious binary POSTs
- Enable Java serialization logging and auditing

## Objectives

1. Deliver payload to vulnerable service
2. Trigger deserialization process
3. Achieve code execution on server

## Instructions

### Step 1: POST Payload with Curl

**Context**: Transmit the binary payload, ignoring SSL verification due to potential cert issues.

**Command** ([[commands/curl-send-rce-payload]]):
```bash
curl https://█████/psc/EXPROD/ --data-binary @payload -k
```

> Sends raw binary via POST. Expected output: HTTP 200/OK or similar; no visible error if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-send-rce-payload]]

## Tools Used

- [[tools/Curl]]

## Tags

- exploitation
- rce
- deserialization
