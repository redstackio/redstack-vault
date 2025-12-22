---
id: proc-capture-nc-001
tags:
  - capture
  - ssrf
  - verification
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/netcat-listen-port-443]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:32:28.676Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
---

# Capture-Exfiltrated-Request-with-Netcat

## Summary

This procedure uses netcat to listen on a local port and capture the SSRF-induced HTTP POST request from the exploited Shopify SDK, verifying the leakage of sensitive form data.

## Description

During SSRF exploitation, the SDK sends a POST to an attacker-controlled endpoint like localhost:443. Netcat in listen mode intercepts this, displaying the request headers and body containing client_id, client_secret, and code. This confirms successful exfiltration in a controlled test environment.

## Requirements

1. Netcat installed (nc command)
2. Local port 443 available (or adjust as needed)
3. Concurrent execution with SSRF exploit

## Defense

Defensive measures and detection strategies:

- Block unauthorized inbound connections on internal ports
- Log and alert on unexpected HTTP traffic to localhost or internal IPs
- Use WAF rules to inspect outbound requests for sensitive data

## Objectives

1. Intercept SSRF request
2. Verify credential leakage in POST data
3. Validate exploitation success

## Instructions

### Step 1: Start Netcat Listener

**Context**: Listen for incoming TCP connections on port 443.

**Command** ([[commands/netcat-listen-port-443]]):
```bash
nc -l -n -vv -p 443
```

> Listens verbosely without DNS; expected: Waiting for connection message, then captures POST on exploit trigger.

### Step 2: Trigger Exploit and Observe

**Context**: Run SSRF procedure in parallel; netcat will show request.

No command here; monitor output for POST /admin/oauth/access_token with form params.

> Expected: Full HTTP request with leaked data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used

- [[commands/netcat-listen-port-443]]

## Tools Used

- [[tools/netcat]]

## Tags

- capture
- ssrf
- verification

---
