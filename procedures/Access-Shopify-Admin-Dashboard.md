---
tags:
  - initial-access
  - shopify
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
updated_at: '2025-12-14T04:08:54.974Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ba2cb81a-ba6d-49a1-8313-afe653fbf629
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Admin-Dashboard

## Summary

This procedure authenticates a user to the Shopify admin dashboard, providing the necessary access to reach the Packing Slip Template editor for subsequent exploitation steps.

## Description

In the context of exploiting Shopify's HTML sanitization vulnerability, initial access requires logging into a valid merchant account. This step assumes possession of admin credentials and targets the web-based admin interface. Successful execution grants entry to administrative features, including the vulnerable template editor, without requiring advanced technical skills.

## Requirements

1. Valid Shopify admin email and password
2. Web browser with internet connectivity
3. Target store URL (e.g., mystore.myshopify.com)

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for admin logins
- Monitor login attempts from unusual IP addresses or locations
- Use session timeouts and IP whitelisting for admin access

## Objectives

1. Authenticate and access the Shopify admin dashboard
2. Verify admin privileges for template editing
3. Prepare for navigation to vulnerable features

## Instructions

### Step 1: Navigate to Login Page

**Context**: Direct the browser to the Shopify admin login to initiate authentication.

No command required; manually enter https://[store].myshopify.com/admin in the browser address bar.

> This loads the login form. Expected output: Login page with email and password fields.

### Step 2: Enter Credentials and Submit

**Context**: Provide valid admin credentials to gain authenticated access.

No command required; fill in the email and password fields, then click 'Log in'.

> Successful login redirects to the dashboard. Expected output: Admin homepage with navigation menu.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[shopify]]
- [[authentication]]
