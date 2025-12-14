---
id: proc-uuid-004
tags:
  - unauthorized-access
  - basic-auth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:44.655Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Domain Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-In-to-Discovered-Subdomain-Using-Hardcoded-Credentials

## Summary

This procedure authenticates to a web endpoint using discovered hardcoded HTTP basic credentials, gaining unauthorized access to restricted areas like admin panels.

## Description

HTTP basic auth is a simple challenge-response mechanism, but hardcoded creds bypass it entirely. Here, applying app-extracted username:password to a bruteforced subdomain (e.g., dev-admin.zomato.com) exposed a clone of the main admin panel in the development environment. Success leads to data access until detection and shutdown.

## Requirements

1. Valid subdomain URL
2. Decoded credentials (username:password)
3. HTTP client like curl or browser
4. No additional auth layers

## Defense

Defensive measures and detection strategies:

- Replace basic auth with token-based (OAuth/JWT) or multi-factor
- Rotate credentials frequently and avoid hardcoding
- Log and alert on unusual logins from dev environments
- Use WAF to block credential stuffing

## Objectives

1. Bypass authentication using embedded secrets
2. Access sensitive admin functionality
3. Explore and extract development data

## Instructions

### Step 1: Test Credentials with Curl

**Context**: Verify auth on the subdomain.

Send a request with basic auth header.

**Command** (curl-basic-auth):
```bash
curl -u username:password -v http://subdomain.zomato.com/
```

> The -v flag shows headers; expect 200 OK and dashboard HTML if successful.

### Step 2: Browse Admin Panel

**Context**: Interact with the accessed interface.

If curl succeeds, open in a browser with creds or use --ntlm if needed, but basic auth is direct.

**Command** (browser-equivalent-curl):
```bash
curl -u username:password http://subdomain.zomato.com/admin
```

> Expected output: Admin panel content, confirming clone of main interface.

### Step 3: Validate Access

**Context**: Confirm unauthorized entry.

Check for dev-specific features or data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Domain Accounts]] Domain Accounts

## Commands Used

- None specific

## Tools Used

- None

## Tags

- [[unauthorized-access]]
- [[basic-auth]]
