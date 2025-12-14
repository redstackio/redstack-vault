---
id: proc-send-dos-payload
tags:
  - dos
  - exploit
  - curl
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-send-dos-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:23:27.701Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Send-DoS-Payload-to-Endpoint

## Summary

This procedure transmits the DoS deserialization payload to the Oracle PeopleSoft monitor endpoint, causing Java heap exhaustion and service denial.

## Description

Similar to the RCE step, curl POSTs the binary payload_dos to /monitor/EXPROD_1. Upon deserialization, it triggers infinite recursion, leading to OutOfMemoryError. Not executed in the original PoC to prevent disruption, but demonstrates potential impact. Requires the decoded payload file.

## Requirements

1. Generated 'payload_dos' file
2. Network access to target endpoint
3. Curl tool

## Defense

Defensive measures and detection strategies:

- Enforce request size limits on endpoints
- Monitor for JVM crashes or OOM errors
- Isolate deserialization in sandboxed threads

## Objectives

1. Deliver DoS payload
2. Exhaust server resources
3. Disrupt service availability

## Instructions

### Step 1: POST DoS Payload with Curl

**Context**: Send the binary to trigger memory exhaustion, bypassing SSL.

**Command** ([[commands/curl-send-dos-payload]]):
```bash
curl https://███████/monitor/EXPROD_1 --data-binary @payload_dos -k
```

> Transmits payload; expected output is initial HTTP response, followed by server-side crash logged as 'java.lang.OutOfMemoryError: Java heap space'.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/curl-send-dos-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- dos
- exploit
- curl
