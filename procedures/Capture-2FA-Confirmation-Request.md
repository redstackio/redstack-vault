---
tags:
  - capture
  - request
  - intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-capture-2fa]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.359Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: 9c6c5072-4bd8-439a-bbef-d09156453d19
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-2FA-Confirmation-Request

## Summary

This procedure intercepts the POST request to the /login/confirm endpoint during 2FA submission, allowing analysis of the steamid cookie and request structure.

## Description

Targeting web applications like CS Money that use SteamID cookies, this step uses a proxy to capture the HTTP POST with body {"token":"<token>","code":"<code>"}. It reveals the insecure cookie dependency, enabling downstream manipulation for IDOR exploitation.

## Requirements

1. Proxy tool configured (e.g., Burp Suite) between browser and target
2. Active 2FA session from prior login
3. HTTPS interception enabled (may require CA certificate installation)

## Defense

Defensive measures and detection strategies:

- Enforce HSTS and certificate pinning to hinder interception
- Log all 2FA requests for anomaly detection
- Use request signing to validate integrity

## Objectives

1. Isolate the 2FA confirmation request
2. Extract steamid cookie and token
3. Verify endpoint behavior

## Instructions

### Step 1: Configure Proxy and Submit 2FA

**Context**: Set up interception and trigger the request by entering a 2FA code.

Execute [[commands/curl-capture-2fa]] to simulate or use browser form:

```bash
curl -X POST https://target.com/login/confirm -H "Cookie: steamid=your_steamid" -d '{"token":"session_token","code":"123456"}'
```

> Proxy captures the full request; drop and inspect in Burp.

### Step 2: Analyze Captured Elements

**Context**: Review headers, body, and cookies for vulnerabilities.

Inspect steamid cookie value and ensure token is session-bound.

> Expected: Unvalidated steamid allowing substitution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-capture-2fa]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[capture]]
- [[request]]
- [[intercept]]
