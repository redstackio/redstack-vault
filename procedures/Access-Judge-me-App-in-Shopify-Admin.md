---
id: proc-uuid-1
tags:
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:47:12.947Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Judge-me-App-in-Shopify-Admin

## Summary

This procedure outlines logging into a Shopify admin account and accessing the Judge.me app to initiate vulnerability exploitation in app settings.

## Description

In the context of exploiting web application vulnerabilities like stored XSS, initial access to the admin interface is crucial. This step assumes possession of valid Shopify admin credentials and focuses on navigating to the Judge.me app, a third-party review widget integrated into Shopify stores. Successful access positions the attacker to modify app configurations unsafely.

## Requirements

1. Valid Shopify admin account credentials
2. Internet browser with cookies enabled
3. Judge.me app pre-installed in the target Shopify store

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for Shopify admin logins
- Monitor admin login logs for unusual IP addresses or failed attempts
- Use role-based access control to limit app access to necessary personnel

## Objectives

1. Establish authenticated session in Shopify admin
2. Load the Judge.me app interface
3. Prepare for subsequent configuration changes

## Instructions

### Step 1: Log In to Shopify Admin

**Context**: Authenticate to gain admin privileges required for app management.

Navigate to the Shopify admin login page (admin.shopify.com) and enter credentials. Upon successful login, the dashboard will appear.

> Expected: Redirect to the main admin dashboard with personalized store overview.

### Step 2: Select Judge.me App

**Context**: Transition from the general dashboard to the specific app interface.

In the left sidebar, click 'Apps' and select 'Judge.me' from the list of installed applications.

> Expected: Judge.me dashboard loads, displaying review management options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[admin-access]]
