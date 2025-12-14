---
tags:
  - authentication
  - shopify
  - admin-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:25:29.833Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: c81b28e0-7cb8-4887-8755-144d435e2bc1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Attacker-to-Shopify-Admin

## Summary

This procedure authenticates an attacker into the Shopify admin panel using valid credentials, establishing a session necessary for subsequent exploitation steps.

## Description

In the context of exploiting an IDOR vulnerability in Shopify's admin settings, initial authentication is required to access protected endpoints. The attacker uses their own legitimate credentials to log in, gaining a valid session cookie that allows interaction with admin features like account settings. This step assumes the attacker has obtained credentials through prior means, such as social engineering or purchase.

## Requirements

1. Valid Shopify admin credentials (email and password)
2. Web browser or HTTP client with proxy support (e.g., [[tools/Burp-Suite]] for interception)
3. Internet access to Shopify's admin domain (admin.shopify.com)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin logins to prevent credential-based access
- Monitor login attempts from unusual IP addresses or locations using Shopify's audit logs
- Use session monitoring tools to detect anomalous admin activity post-login

## Objectives

1. Establish authenticated session in Shopify admin
2. Obtain session cookies for request forwarding
3. Prepare for navigation to vulnerable endpoints

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Shopify admin login portal to begin authentication.

No specific command; use a browser to visit https://admin.shopify.com/auth/login.

> Enter attacker credentials and submit the form. Expected output: Redirect to dashboard if successful.

### Step 2: Verify Authentication

**Context**: Confirm the session is active by checking for dashboard elements.

No command; inspect browser developer tools for session cookies (e.g., _shopify_s).

> Successful login shows the admin dashboard with account overview.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication]]
- [[shopify]]
- [[admin-access]]
