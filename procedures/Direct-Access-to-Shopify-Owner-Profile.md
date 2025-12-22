---
tags:
  - broken-access-control
  - privilege-escalation
  - authorization-bypass
  - shopify
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-shopify-profile-access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.674Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 1e5e494e-72c1-41b5-ba26-1506982ff44a
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Direct Access to Shopify Owner Profile

## Summary

This procedure exploits a missing authorization check in Shopify's user profile endpoint, allowing a full-access administrator to directly access and view the account owner's sensitive profile information via a simple URL request, resulting in unauthorized data exposure and privilege escalation.

## Description

In Shopify's admin interface, user profiles are intended to be restricted such that only the account owner can view their own profile, while full-access administrators should be limited to viewing their assigned team members' profiles. However, due to a flaw in the authorization logic, directly requesting the account owner's profile URL (e.g., `/users/[owner-id]/profile`) as a full-access admin bypasses these checks. This leads to the disclosure of sensitive information such as the owner's contact details, which could facilitate further attacks like social engineering or account takeover. The procedure requires an authenticated admin session and knowledge of the owner's user ID, which may be discoverable through team management views. Expected outcomes include immediate access to restricted data without triggering errors.

## Requirements

1. Valid full-access administrator credentials for the Shopify store (not the account owner)
2. Authenticated session in the Shopify admin dashboard
3. Knowledge of the account owner's user ID (inferable from URLs or team listings)
4. Access to a web browser or HTTP client like curl for making requests

## Defense

Defensive measures and detection strategies:

- Implement server-side authorization checks to validate user roles against requested resources (e.g., ensure only owners access their own profiles)
- Log and monitor direct URL access to sensitive endpoints, alerting on non-owner admin requests
- Use rate limiting and anomaly detection on profile access patterns
- Enforce principle of least privilege by scoping admin roles strictly

## Objectives

1. Gain unauthorized read access to the account owner's user profile
2. Expose sensitive personal information for potential further exploitation
3. Demonstrate escalation from admin to owner-equivalent data access

## Instructions

### Step 1: Authenticate as Full-Access Admin

**Context**: Establish a valid session to mimic a legitimate admin user, setting the stage for the unauthorized request.

Log in to the Shopify admin dashboard at `https://admin.shopify.com/store/[store-name]` using full-access admin credentials. Verify access to team management or user listings to note the owner's user ID (typically numeric, e.g., from `/users` endpoint).

No command required for login; use the web interface.

### Step 2: Direct URL Request to Owner's Profile

**Context**: Exploit the missing check by requesting the profile endpoint directly, bypassing any UI restrictions.

**Command** ([[commands/curl-shopify-profile-access]]):
```bash
curl -v -H "Cookie: [extracted-admin-session-cookie]" "https://admin.shopify.com/store/[store-name]/users/[owner-user-id]/profile"
```

> This command sends an HTTP GET request to the profile URL with the admin's session cookie. Extract the cookie from your browser's developer tools (e.g., under Application > Cookies). Replace placeholders with actual values. The `-v` flag provides verbose output to inspect headers and response status. Expected output includes a 200 OK response with HTML/JSON containing the owner's profile data, such as name, email, and address. If successful, no 403 or redirect occurs.

### Step 3: Validate Access

**Context**: Confirm the data exposure by inspecting the response for sensitive owner-only information.

Review the response body for restricted fields. In a browser, simply navigate to the URL after login; the page should load fully without denial.

**Expected Output**: Profile details visible, indicating successful bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/curl-shopify-profile-access]]

## Tools Used


## Tags

- broken-access-control
- privilege-escalation
- authorization-bypass
- shopify
