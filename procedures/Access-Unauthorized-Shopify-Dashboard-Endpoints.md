---
id: proc-shopify-access-unauth-93680-2
tags:
  - authorization-bypass
  - endpoints
  - shopify
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-access-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.443Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Unauthorized-Shopify-Dashboard-Endpoints

## Summary

This procedure uses captured session cookies from a limited-privilege account to request restricted dashboard endpoints, exploiting the absence of separate authorization validations.

## Description

Shopify's dashboard endpoints for channel overviews and Home screen share cookie-based authentication but lack endpoint-specific permission checks. By sending requests to unauthorized sections (e.g., Home screen with channel-only perms), attackers bypass controls. This targets the web API layer and assumes a valid session. Outcomes include unauthorized data exposure without session invalidation.

## Requirements

1. Session cookies from a limited-privilege login
2. Knowledge of endpoint URLs (e.g., /store/home, /store/channel-overview)
3. HTTP client capable of cookie injection

## Defense

Defensive measures and detection strategies:

- Add granular permission checks on each endpoint using Shopify's API guards
- Log and alert on cross-section access attempts (e.g., channel user hitting Home)
- Use token scoping to limit session capabilities

## Objectives

1. Request restricted endpoints with limited session
2. Confirm bypass by receiving non-error responses
3. Identify exploitable data in responses

## Instructions

### Step 1: Prepare Session Cookies

**Context**: Load cookies into the HTTP client for authenticated requests.

No command; use -b flag in curl with cookies.txt from prior step.

> Expected: Cookies parsed successfully.

### Step 2: Request Unauthorized Endpoint

**Context**: Target a section outside the user's permissions.

**Command** ([[commands/curl-access-endpoint]]):
```bash
curl -b cookies.txt -H "User-Agent: Mozilla/5.0" https://admin.shopify.com/store/home
```

> Sends request to Home screen with channel perms. Expected output: HTML/JSON with dashboard data, no auth error.

### Step 3: Validate Response

**Context**: Check for sensitive content to confirm success.

Inspect the response body for store metrics or admin-only elements.

> Expected: Presence of restricted UI elements or data.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/curl-access-endpoint]]

## Tools Used

- [[tools/curl]]

## Tags

- [[authorization-bypass]]
- [[endpoints]]
- [[shopify]]
