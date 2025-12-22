---
tags:
  - account-takeover
  - session-hijacking
  - authentication-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-reuse-session-cookie]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:34.557Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Local Accounts]]'
id: dd854370-1798-4333-a36a-4f2456e50a22
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Steal Web Session Cookie]]'
---
# Reuse-Session-Cookie-for-Authentication

## Summary

This procedure demonstrates reusing a stolen session cookie to authenticate as the victim user on a web platform, bypassing normal login mechanisms and gaining full account access.

## Description

Session cookies on platforms like HackerOne authenticate requests without IP or device checks, allowing attackers to inject the cookie into a new session via browser extensions, proxies, or HTTP clients. This leads to complete account takeover, enabling navigation to protected areas. The attack exploits unprotected credentials and assumes the cookie remains valid until revoked.

## Requirements

1. Extracted session cookie value from a leak source
2. HTTP client like cURL or browser with cookie import capability
3. Target domain access (e.g., hackerone.com)

## Defense

Defensive measures and detection strategies:

- Bind sessions to IP addresses, user agents, or devices
- Implement short cookie expiration times and rotation
- Use HttpOnly and Secure flags on cookies
- Log and alert on session reuse from new IPs

## Objectives

1. Establish authenticated session using leaked cookie
2. Verify access to user-specific dashboard
3. Maintain session for further actions

## Instructions

### Step 1: Set Cookie in HTTP Client

**Context**: Prepare the client to include the leaked cookie in requests.

**Command** ([[commands/curl-reuse-session-cookie]]):
```bash
curl -H "Cookie: __session=leaked_cookie_value_here" -v https://hackerone.com/
```

> The -v flag shows headers; look for 200 OK and authenticated redirects. Expected output: Successful homepage load with user menu.

### Step 2: Access Protected Endpoint

**Context**: Test deeper access to confirm takeover.

**Command** ([[commands/curl-reuse-session-cookie]]):
```bash
curl -H "Cookie: __session=leaked_cookie_value_here" https://hackerone.com/dashboard
```

> Expected output: JSON or HTML with account data, no 401/403 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques

- [[Local Accounts]] Local Accounts

## Commands Used

- [[commands/curl-reuse-session-cookie]]

## Tools Used


## Tags

- [[account-takeover]]
- [[session-hijacking]]
