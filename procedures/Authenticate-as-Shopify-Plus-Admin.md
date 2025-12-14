---
id: proc-authenticate-shopify-plus-admin
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
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:53.587Z'
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
# Authenticate-as-Shopify-Plus-Admin

## Summary

This procedure establishes an authenticated session as a Shopify Plus admin, providing the necessary privileges to access the admin interface and trigger API requests for further exploitation.

## Description

In the context of exploiting Shopify's GraphQL API vulnerability, authentication as a Plus admin is the entry point. This allows navigation to sensitive sections like users, where API calls can be intercepted. The procedure assumes valid credentials and focuses on session establishment without additional tools beyond a browser or proxy.

## Requirements

1. Valid Shopify Plus admin credentials (email and password)
2. Network access to the target Shopify organization domain
3. Configured proxy like Burp Suite for traffic monitoring (optional but recommended)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin accounts
- Monitor login attempts and unusual admin activity via Shopify audit logs
- Use IP whitelisting for admin access

## Objectives

1. Establish a valid admin session
2. Access the users section to prepare for API interception
3. Ensure session persistence for subsequent steps

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Shopify admin login to initiate authentication.

No command required; use a web browser to visit https://{organization}.myshopify.com/admin/login.

> Enter admin credentials and submit the login form. Expected output: Redirect to the admin dashboard upon success.

### Step 2: Verify Admin Privileges

**Context**: Confirm Plus organization access and navigate to users section.

No command required; in the dashboard, go to Settings > Users and permissions.

> Successful navigation indicates admin privileges. Look for Plus-specific features like organization management.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- shopify
- admin-access
