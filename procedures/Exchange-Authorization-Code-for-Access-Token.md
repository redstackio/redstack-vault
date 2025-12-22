---
id: 123e4567-e89b-12d3-a456-426614174002
name: Exchange-Authorization-Code-for-Access-Token
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:10.917Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
sub_techniques: []
tags:
  - oauth2
  - token-exchange
commands:
  - '[[commands/exchange-oauth-code-for-token]]'
  - '[[commands/verify-access-token]]'
platforms:
  - Web
tools:
  - '[[tools/getAccessToken-sh]]'
  - '[[tools/me-sh]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---

# Exchange-Authorization-Code-for-Access-Token

## Summary

This procedure exchanges an OAuth2 authorization code for a bearer access token via Vimeo's token endpoint, followed by verification to ensure the token grants API access to the user's account.

## Description

Targeting the /oauth/access_token endpoint, this uses POST requests with client credentials and the code. The vulnerability allows this even post-revocation if codes aren't invalidated. Expected outcomes include token issuance and successful API calls like /me.

## Requirements

1. Valid authorization code from prior procedure
2. Client secret for the app
3. Access to [[tools/getAccessToken-sh]] and [[tools/me-sh]] scripts

## Defense

Defensive measures and detection strategies:

- Invalidate codes immediately upon exchange or revocation
- Log token exchanges and alert on codes used multiple times
- Enforce single-use enforcement with server-side checks

## Objectives

1. Obtain a functional access token
2. Verify token validity against user data endpoint
3. Demonstrate access to scoped resources (e.g., public/private)

## Instructions

### Step 1: Exchange Code

**Context**: Submit the code to the token endpoint to receive an access token.

**Command** ([[commands/exchange-oauth-code-for-token]]):

```bash
./getAccessToken.sh e1fa87cd449ae55b74445b31ac79450c14eeb657
```

> This script performs a POST to /oauth/access_token with grant_type=authorization_code, returning JSON with access_token (e.g., d3ac3bb53d1c4ebc3de7d28e4ed801c0) and scopes.

### Step 2: Verify Token

**Context**: Use the token to query the /me endpoint and confirm access.

**Command** ([[commands/verify-access-token]]):

```bash
./me.sh d3ac3bb53d1c4ebc3de7d28e4ed801c0
```

> Returns 200 OK with user URI (/users/39285903) and data if valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used

- [[commands/exchange-oauth-code-for-token]]
- [[commands/verify-access-token]]

## Tools Used

- [[tools/getAccessToken-sh]]
- [[tools/me-sh]]

## Tags

- [[oauth2]]
- [[token-exchange]]
