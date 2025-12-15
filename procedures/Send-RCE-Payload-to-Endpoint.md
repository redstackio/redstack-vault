---
id: proc-send-rce-payload
tags:
  - rce
  - exploit
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-send-rce-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:27.722Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
# Send-RCE-Payload-to-Endpoint

## Summary

This procedure sends the generated Java deserialization payload to the vulnerable /monitor endpoint in Oracle PeopleSoft, triggering unsafe deserialization for RCE.

## Description

The endpoint at https://target/monitor/EXPROD_1 accepts POST data without validation, deserializing it via readObject() and allowing gadget chain execution. Curl is used with --data-binary to preserve the payload and -k to bypass SSL issues. This step assumes the payload file exists and the target is reachable.

## Requirements

1. Generated 'payload' file from ysoserial
2. Network access to the target HTTPS endpoint
3. Curl installed

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all deserialized inputs
- Deploy RASP to detect gadget chains
- Log and alert on large binary POSTs to admin endpoints

## Objectives

1. Deliver payload to trigger deserialization
2. Achieve RCE on the server
3. Observe indirect confirmation via DNS

## Instructions

### Step 1: POST Payload with Curl

**Context**: Transmit the binary payload to the endpoint, ignoring SSL validation.

**Command** ([[commands/curl-send-rce-payload]]):
```bash
curl https://█████████/monitor/EXPROD_1 --data-binary @payload -k
```

> Sends the payload; expected output is the server's HTTP response (e.g., 200 OK). Deserialization happens server-side.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-rce-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- rce
- exploit
- curl
