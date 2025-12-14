---
tags:
  - admin-access
  - discourse
  - web
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
updated_at: '2025-12-14T17:30:18.623Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 53b06012-d1d2-4e18-8cc9-044c53119123
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Discourse-Admin-Interface

## Summary

This procedure outlines gaining admin access to a Discourse instance via the web interface, required for interacting with the backups feature.

## Description

In the context of exploiting the backup restore vulnerability, admin privileges are necessary to create, upload, and restore backups. This involves loading the site, logging in, and navigating to admin sections. The target is a public-facing Discourse forum, assuming valid credentials are available. Outcomes include access to /admin/backups/ for further exploitation steps.

## Requirements

1. Valid admin username and password for the Discourse instance
2. Web browser with internet access to the target site
3. No additional tools needed beyond standard browsing

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin accounts
- Monitor login attempts and admin panel access logs for anomalies
- Use role-based access control to limit backup feature to trusted admins

## Objectives

1. Authenticate as admin to unlock privileged features
2. Reach the backups management page
3. Prepare for backup manipulation without triggering alerts

## Instructions

### Step 1: Load the Target Site

**Context**: Establish connection to the Discourse instance.

No command required; use browser to visit the main URL (e.g., https://target.com).

> Expected: Site loads; proceed to login if prompted.

### Step 2: Login as Admin

**Context**: Authenticate to gain admin privileges.

Enter credentials in the login form and submit.

> Expected: Redirect to dashboard with admin menu visible.

### Step 3: Navigate to Backups

**Context**: Access the specific admin endpoint for backups.

Visit /admin/backups/ or click the backups link in the admin sidebar.

> Expected: Backups page loads with create/restore options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- admin-login
- discourse-admin
