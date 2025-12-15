---
id: auth-merchant-portal-001
name: Authenticate to RBKmoney Merchant Portal
tags:
  - authentication
  - web
  - rbkmoney
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-login-merchant]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:29.073Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate to RBKmoney Merchant Portal

## Summary

This procedure establishes an authenticated session to the RBKmoney merchant portal at merchant.rbmonkey.com, enabling access to shop management APIs as a prerequisite for exploiting vulnerabilities like IDOR.

## Description

The RBKmoney merchant portal requires user authentication to manage eShops. Attackers with valid credentials (e.g., from a compromised account or legitimate testing) can log in via the web interface or API to obtain a session token. This token is then used in subsequent requests. The procedure assumes possession of username and password; in a real attack, these may be obtained via phishing or credential stuffing.

## Requirements

1. Valid username and password for a merchant account
2. Network access to https://merchant.rbmonkey.com
3. curl or equivalent HTTP client

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized logins
- Monitor for unusual login attempts from new IPs or locations
- Use rate limiting on authentication endpoints

## Objectives

1. Obtain a valid authentication token or session
2. Verify access to personal shop management features
3. Prepare for API interactions requiring authorization

## Instructions

### Step 1: Send Login Request

**Context**: Submit credentials to the login endpoint to acquire an auth token.

**Command** ([[commands/curl-login-merchant]]):
```bash
curl -X POST 'https://merchant.rbmonkey.com/api/auth/login' \
  -H 'Content-Type: application/json' \
  -d '{"username": "testuser", "password": "testpass"}'
```

> This command sends a JSON payload with credentials to the login endpoint. Expected output is a JSON response containing the auth token, e.g., {"token": "eyJ..."}. Store the token for use in headers of subsequent requests.

### Step 2: Verify Authentication

**Context**: Use the token to access a protected endpoint, confirming session validity.

**Command** ([[commands/curl-verify-auth]]):
```bash
curl -X GET 'https://merchant.rbmonkey.com/api/shops' \
  -H 'Authorization: Bearer YOUR_AUTH_TOKEN'
```

> This fetches the user's own shops. Successful output lists shop data without errors, indicating valid authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-login-merchant]]
- [[commands/curl-verify-auth]]

## Tools Used


## Tags

- authentication
- web
- rbkmoney
