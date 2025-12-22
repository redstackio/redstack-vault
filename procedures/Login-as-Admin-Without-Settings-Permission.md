---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - authentication
  - shopify
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:51.828Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-as-Admin-Without-Settings-Permission

## Summary

This procedure authenticates to the Shopify admin panel using a valid administrator account that lacks the 'Settings' permission, establishing a session for subsequent unauthorized access to restricted resources.

## Description

In the context of Shopify's permission-based admin access, users with roles like 'Orders' can log in normally but are UI-restricted from settings. This procedure leverages valid credentials to gain initial foothold, exploiting the fact that downstream endpoints may not re-validate permissions. Expected outcomes include a session cookie enabling API and page requests without immediate denial.

## Requirements

1. Valid Shopify administrator email and password (with permissions excluding 'Settings', e.g., 'Orders' only)
2. Access to the Shopify store's admin URL (e.g., https://shop.myshopify.com/admin)
3. Web browser or HTTP client capable of handling session cookies

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) consistently across UI and API
- Log all admin logins with permission details for anomaly detection
- Implement session-based permission caching with re-validation on sensitive endpoints

## Objectives

1. Obtain a valid admin session token
2. Confirm limited UI access to avoid alerting
3. Prepare for authorization bypass in subsequent steps

## Instructions

### Step 1: Navigate to Admin Login

**Context**: Access the Shopify admin login page to initiate authentication.

**Command** (Browser Navigation):

Open a web browser and go to `https://shop.myshopify.com/admin/auth/login` (replace 'shop' with the target store name).

> This loads the login form. Expected output: Login page displays without errors.

### Step 2: Submit Credentials

**Context**: Enter and submit the limited-privilege admin credentials to authenticate.

**Command** (Form Submission):

Enter the email and password, then click 'Log in' or submit the form.

> Expected output: Redirect to `/admin` dashboard. Verify permissions in user menu to confirm no 'Settings' access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- shopify
- admin-access
