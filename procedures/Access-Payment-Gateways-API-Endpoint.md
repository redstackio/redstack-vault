---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - api-access
  - broken-access-control
  - shopify
  - payment-gateways
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-payment-gateways]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.827Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Payment-Gateways-API-Endpoint

## Summary

This procedure directly queries the Shopify admin API endpoint for payment gateways, bypassing permission checks to disclose sensitive configurations including partial credentials.

## Description

Shopify's `/admin/payment_gateways.json` endpoint fails to enforce 'Settings' permission, allowing any authenticated admin (even without it) to retrieve data due to legacy code not validating user roles. This targets web-based admin panels and results in JSON output with gateway details like providers, statuses, and credential fragments, enabling financial reconnaissance.

## Requirements

1. Active Shopify admin session from a limited-privilege account
2. Knowledge of the store's domain (e.g., shop.myshopify.com)
3. HTTP client like curl with cookie support for session persistence

## Defense

Defensive measures and detection strategies:

- Add explicit permission checks on all admin API endpoints
- Monitor API calls to sensitive paths for unauthorized access patterns
- Use API gateways with fine-grained authorization (e.g., OAuth scopes)

## Objectives

1. Retrieve unauthorized payment gateway data
2. Extract partial credentials for further exploitation
3. Validate broken access control without UI interaction

## Instructions

### Step 1: Prepare Session Cookies

**Context**: Extract session cookies from the logged-in browser to authenticate API requests.

**Command** (Browser Inspection):

In browser dev tools, copy the session cookie (e.g., _shopify_s) from the admin dashboard.

> Expected output: Cookie string like `_shopify_s=abc123; domain=.myshopify.com`.

### Step 2: Query API Endpoint

**Context**: Send a GET request to the unprotected endpoint using the session.

**Command** ([[commands/curl-access-payment-gateways]]):
```bash
curl -H "Cookie: _shopify_s=your_session_cookie" https://shop.myshopify.com/admin/payment_gateways.json
```

> This fetches the JSON data. Expected output: Array of gateways with fields like 'name', 'status', 'credentials' (partial).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-payment-gateways]]

## Tools Used


## Tags

- api-access
- broken-access-control
- shopify
- payment-gateways
