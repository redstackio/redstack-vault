---
id: proc-uuid-2
name: Inspect-CSRF-Token-Persistence
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:29.830Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - token-inspection
  - web-vulnerability
commands:
  - '[[commands/curl-inspect-token]]'
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Inspect-CSRF-Token-Persistence

## Summary

This procedure examines CSRF tokens in web requests and responses across sessions to detect if they remain static, indicating a reuse vulnerability.

## Description

Targeting applications like Liberapay, this involves capturing and comparing CSRF token values after multiple auth cycles. The technical approach uses network inspection to extract tokens from forms or headers. In a real attack scenario, a stolen token could be reused for CSRF attacks. Prerequisites: Active session from prior procedure and inspection tools.

## Requirements

1. Access to browser dev tools or curl with verbose output
2. Knowledge of token location (e.g., in HTML forms or X-CSRF-Token header)
3. Captured session cookies from authentication

## Defense

Defensive measures and detection strategies:

- Regenerate CSRF tokens per session or request
- Log token usage and detect reuse attempts
- Enforce token binding to user sessions

## Objectives

1. Extract and compare CSRF token values
2. Confirm persistence across login/logout
3. Assess risk of token reuse for unauthorized actions

## Instructions

### Step 1: Capture Initial Token

**Context**: During login, inspect the response for the CSRF token.

Use curl to login and dump headers:

Execute [[commands/curl-inspect-token]] to capture:

```bash
curl -X POST https://liberapay.com/login -d "username=user&password=pass" -c cookies.txt -D headers1.txt -v
```

> Verbose output shows headers; grep for CSRF token in response body or Set-Cookie. Expected output: Token value like a UUID or random string.

### Step 2: Capture Token After Cycle

**Context**: After logout and relogin, inspect again.

Repeat login and dump to new file:

```bash
curl -X POST https://liberapay.com/login -d "username=user&password=pass" -b cookies.txt -c cookies.txt -D headers2.txt -v
```

> Compare headers1.txt and headers2.txt for token values.

### Step 3: Compare Tokens

**Context**: Verify if tokens match.

Manually or script compare extracted tokens.

**Expected Output**: Identical token strings, confirming persistence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-token]]

## Tools Used


## Tags

- [[csrf]]
- [[token-inspection]]
- [[web-vulnerability]]
