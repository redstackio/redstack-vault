---
id: proc-oauth-verify-revoke-001
tags:
  - token-verification
  - revocation-bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/get-api-me-verify-token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:38.816Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Tokens-and-Test-Revocation

## Summary

This procedure validates exploited tokens by querying protected APIs and tests revocation to show that only one token pair is invalidated, leaving others for bypass.

## Description

After race exploitation, each access token is tested against an endpoint like /api/me. Revocation is triggered via the provider's UI or /oauth/revoke, but due to flawed implementation, it targets only one token context. This is probabilistic and may require retries under load. Targets OAuth providers with incomplete revocation logic.

## Requirements

1. Multiple access tokens from race exploit.
2. Knowledge of a protected API endpoint (e.g., /api/me).
3. Access to revocation interface.

## Defense

Defensive measures and detection strategies:

- Revoke all tokens associated with an app/user pair.
- Audit logs for multiple active tokens post-revocation.
- Implement token blacklisting across all issuances.

## Objectives

1. Confirm token validity.
2. Demonstrate revocation ineffectiveness.
3. Maintain access via surviving tokens.

## Instructions

### Step 1: Verify Each Token

**Context**: Test tokens individually.

**Command** ([[commands/get-api-me-verify-token]]):
```bash
GET /api/me?access_token=ACCESS_TOKEN_VALUE HTTP/1.1
Host: OAUTH_PROVIDER_DOMAIN
```

> Use curl to send; replace ACCESS_TOKEN_VALUE. Expected: 200 OK with user data.

### Step 2: Perform Revocation

**Context**: Revoke via settings or endpoint.

No command; use web UI or POST to /oauth/revoke with one token.

> Retest all tokens; expect most to still work.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

- [[commands/get-api-me-verify-token]]

## Tools Used

- [[tools/curl]]

## Tags

- [[token-verification]]
- [[revocation-bypass]]
