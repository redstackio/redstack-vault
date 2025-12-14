---
tags:
  - wordpress
  - admin-access
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
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
updated_at: '2025-12-14T03:47:12.639Z'
sub_techniques: []
id: 148c1b8e-a064-4b10-b2f2-df357e831308
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-WordPress-Theme-Editor

## Summary

This procedure outlines logging into the WordPress admin dashboard and navigating to the theme editor to prepare for file modifications in an authenticated session.

## Description

In the context of exploiting the stored XSS vulnerability, authenticated users with sufficient privileges (e.g., administrator or editor roles) access the theme editor via the Appearance menu. This step requires valid credentials and direct access to the wp-admin interface. The goal is to reach the editable theme files without triggering any restrictions.

## Requirements

1. Valid WordPress user credentials with theme editor permissions
2. Web browser access to the WordPress site
3. No multi-factor authentication blocking admin login

## Defense

Defensive measures and detection strategies:

- Restrict theme editor access to trusted admins only via role-based permissions
- Enable WordPress security plugins like Wordfence to monitor admin logins

## Objectives

1. Establish authenticated session in the admin panel
2. Load the theme editor interface
3. Prepare for subsequent file editing steps

## Instructions

### Step 1: Log In to Admin Dashboard

**Context**: Authenticate to gain access to administrative functions.

No specific command; use the browser to navigate to /wp-admin and enter credentials.

> Upon successful login, the dashboard homepage appears.

### Step 2: Navigate to Theme Editor

**Context**: Access the file editing interface for themes.

In the left sidebar, go to Appearance > Theme Editor.

> The theme editor page loads, showing a list of PHP files from the active theme.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- wordpress
- admin-access
