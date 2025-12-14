---
id: proc-uuid-1
tags:
  - wordpress
  - authentication
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:05.171Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-WordPress-Admin-with-Reports-Privilege

## Summary

This procedure authenticates a user to the WordPress admin dashboard using credentials with 'view reports' privileges, enabling access to WooCommerce reporting features vulnerable to SQL injection.

## Description

In a WordPress environment with WooCommerce, users with roles like shop manager can access admin reports. This step establishes a valid session required for exploiting the SQL injection in the coupon usage report. The vulnerability requires authentication but no elevated privileges beyond viewing reports. Expected outcome is a logged-in session cookie for subsequent HTTP requests to the admin endpoints.

## Requirements

1. Valid WordPress username and password with 'view reports' privilege (e.g., shop manager role)
2. Network access to the WordPress site
3. Browser or HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and multi-factor authentication for admin accounts
- Monitor login attempts and failed authentications via WordPress logs or WAF
- Limit 'view reports' privileges to necessary users only

## Objectives

1. Obtain authenticated session to WooCommerce admin reports
2. Capture session cookie for request chaining
3. Prepare for vulnerability exploitation without alerting defenses

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the WordPress login endpoint to initiate authentication.

No specific command; use a browser to visit /wp-login.php and enter credentials.

> Successful login redirects to /wp-admin/, confirming access.

### Step 2: Verify Privileges

**Context**: Confirm the account can access WooCommerce reports.

Navigate to /wp-admin/admin.php?page=wc-reports after login.

> Page loads without permission errors, indicating sufficient privileges.

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
- wordpress
