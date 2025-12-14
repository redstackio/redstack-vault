---
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
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:37.090Z'
sub_techniques: []
id: 749b1d19-fd16-43c8-9b78-4b48bc440376
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate to WordPress Admin Panel

## Summary

This procedure outlines logging into the WordPress admin dashboard using valid admin or editor credentials, enabling access to features like unfiltered HTML post creation.

## Description

In WordPress environments, users with admin or editor roles can access the backend to manage content. This step is prerequisite for injecting payloads in post fields. It assumes credentials are available and targets versions like 5.3 where role-based permissions allow unfiltered HTML. Expected outcome is dashboard access for subsequent exploitation steps.

## Requirements

1. Valid admin or editor username and password
2. Web browser with cookies enabled
3. Access to the site's /wp-admin/ endpoint over HTTP/HTTPS

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies and multi-factor authentication (MFA) for admin accounts
- Monitor login attempts for brute-force or unusual IP origins using plugins like Wordfence

## Objectives

1. Gain authenticated access to the admin interface
2. Verify user privileges for unfiltered content posting
3. Prepare for content injection without restrictions

## Instructions

### Step 1: Navigate to Login Page

**Context**: Access the authentication endpoint to begin login.

Open a web browser and go to `https://target.com/wp-login.php` or `/wp-admin/`.

> The login form should load, prompting for username/email and password.

### Step 2: Submit Credentials

**Context**: Authenticate using privileged account details.

Enter the admin username and password, then click 'Log In'.

> Upon success, redirect to the dashboard at `/wp-admin/`. Failure shows an error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[wordpress]]
- [[authentication]]
