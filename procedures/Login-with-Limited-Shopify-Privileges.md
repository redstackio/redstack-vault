---
id: proc-shopify-login-limited-93680-1
tags:
  - shopify
  - authentication
  - session
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.459Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-with-Limited-Shopify-Privileges

## Summary

This procedure establishes a session in the Shopify dashboard using a user account with restricted permissions, such as access only to channel overviews, to prepare for authorization bypass attacks.

## Description

In the Shopify environment, user roles define access levels. By logging in with a limited-privilege account, attackers can obtain valid session cookies that authenticate requests. The vulnerability arises because subsequent endpoint requests do not re-validate permissions separately, allowing escalation. This step targets the web-based dashboard and requires a pre-configured low-privilege account. Expected outcomes include a valid session for further exploitation without triggering admin alerts.

## Requirements

1. Valid Shopify account credentials with limited privileges (e.g., channel overview access only, no Home screen)
2. Web browser or HTTP client like curl for session capture
3. Network access to Shopify's admin domain (admin.shopify.com)

## Defense

Defensive measures and detection strategies:

- Implement role-based access control (RBAC) with per-endpoint permission checks
- Monitor login events for unusual privilege patterns using Shopify's audit logs
- Enforce multi-factor authentication (MFA) for all accounts

## Objectives

1. Obtain authenticated session cookies from a restricted user
2. Verify limited access to confirm setup for bypass
3. Prepare cookies for reuse in unauthorized requests

## Instructions

### Step 1: Create or Select Limited-Privilege Account

**Context**: Ensure the account has specific restrictions to mimic real-world testing scenarios.

No command needed; configure via Shopify admin settings to grant only channel overview permissions.

> Expected: Account ready with limited role assigned.

### Step 2: Log In and Capture Session Cookies

**Context**: Authenticate to generate session tokens for later use.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -c cookies.txt -d "email=limited@example.com&password=yourpassword" https://accounts.shopify.com/login
```

> This logs in and saves cookies to cookies.txt. Inspect the file for session_id or similar tokens. Expected output: 302 redirect to dashboard upon success.

### Step 3: Verify Limited Access

**Context**: Confirm the session respects restrictions initially.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -b cookies.txt https://admin.shopify.com/store/home
```

> Attempt access to restricted Home screen; expect 403 error. This validates the limited session before bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

-

## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[shopify]]
- [[authentication]]
- [[session-management]]
