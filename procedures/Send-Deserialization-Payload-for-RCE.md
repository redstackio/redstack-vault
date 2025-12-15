---
id: proc-uuid-003
tags:
  - exploit
  - deserialization
  - rce
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-rce-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:20.524Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Deserialization-Payload-for-RCE

## Summary

This procedure sends a malicious serialized Java payload to the /monitor endpoint of Oracle PeopleSoft, exploiting the deserialization flaw to achieve RCE, demonstrated by a DNS lookup.

## Description

The attack targets the unvalidated readObject() method in the monitor service (CVE-2017-10366), allowing arbitrary gadget chains. The endpoint accepts HTTP POST with binary data, ignoring SSL validation in this PoC. Requires network access to the target.

## Requirements

1. Generated 'payload' file from ysoserial
2. Network reachability to https://████/monitor/
3. Curl installed

## Defense

Defensive measures and detection strategies:

- Validate and sanitize input before deserialization
- Use HTTPS with strict certificate validation
- WAF rules to block suspicious binary POSTs to admin endpoints

## Objectives

1. Trigger deserialization on the target server
2. Execute gadget chain for RCE
3. Confirm via external indicators like DNS

## Instructions

### Step 1: POST Payload to Endpoint

**Context**: Transmit the binary payload to initiate deserialization.

**Command** ([[commands/curl-send-rce-payload]]):
```bash
curl https://████/monitor/ --data-binary @payload -k
```

> Sends raw binary data via POST, skipping SSL checks. Expected output: Server HTTP response (e.g., 200 OK); deserialization happens server-side.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-send-rce-payload]]

## Tools Used

- [[tools/curl]]

## Tags

- [[exploit]]
- [[deserialization]]
- [[rce]]
