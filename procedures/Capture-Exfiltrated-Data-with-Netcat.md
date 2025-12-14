---
id: proc-uuid-4
tags:
  - ssrf
  - exfiltration
  - capture
type: procedure
tools:
  - '[[tools/nc]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/netcat-listen-443]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
updated_at: '2025-12-14T04:39:18.768Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Alternative Protocol]]'
---
# Capture-Exfiltrated-Data-with-Netcat

## Summary

This procedure uses netcat to listen on localhost port 443 and capture the SSRF-induced HTTP POST request, revealing exfiltrated sensitive data from the Shopify SDK exploitation.

## Description

During SSRF exploitation, the SDK's Net::HTTP sends a request to the injected localhost endpoint. Netcat in listen mode captures the full request, including headers and form-encoded body with leaked client_secret, client_id, and OAuth code.

## Requirements

1. Netcat installed (common on Unix-like systems)
2. Port 443 available (may require sudo if privileged)
3. Exploitation triggered concurrently

## Defense

Defensive measures and detection strategies:

- Firewall rules blocking outbound to localhost/private ranges from app processes
- Log analysis for unexpected internal connections
- Network segmentation to isolate app traffic

## Objectives

1. Intercept SSRF traffic
2. Extract leaked credentials from request body
3. Validate exploitation success

## Instructions

### Step 1: Start Netcat Listener

**Context**: Listen for incoming TCP connections on port 443.

**Command** ([[commands/netcat-listen-443]]):
```bash
nc -l -n -vv -p 443
```

> Listens without DNS, verbose output. Expected output: Connection from 127.0.0.1, followed by POST request details.

### Step 2: Trigger Exploit and Observe

**Context**: Run the SSRF exploit in parallel (e.g., in pry) and monitor netcat output.

**Instructions**: After starting listener, execute the request_token command from the exploitation procedure.

**Expected Output**: Captured request like POST /?/admin/oauth/access_token with form data: client_id=..., client_secret=..., code=....

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exfiltration Over Alternative Protocol]]

### Sub-Techniques


## Commands Used

- [[commands/netcat-listen-443]]

## Tools Used

- [[tools/nc]]

## Tags

- ssrf
- exfiltration
- capture
