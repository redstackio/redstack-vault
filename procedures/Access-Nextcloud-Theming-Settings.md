---
tags:
  - nextcloud
  - admin-access
  - theming
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
updated_at: '2025-12-14T05:32:09.968Z'
sub_techniques: []
id: 2d71fefd-49df-4183-a95b-01bbc704dd56
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Nextcloud-Theming-Settings

## Summary

This procedure outlines logging into Nextcloud as an administrator and navigating to the theming settings to access the vulnerable file upload feature for logos and login backgrounds.

## Description

In a Nextcloud environment, administrators can customize the instance's appearance via theming settings. This procedure assumes valid admin credentials and focuses on reaching the upload interface, which lacks proper file validation, setting the stage for arbitrary file uploads. The target is a web-based PHP application like Nextcloud, and success enables subsequent exploitation steps. Expected outcome: Access to upload fields without errors.

## Requirements

1. Valid administrative username and password for Nextcloud
2. Web browser with network access to the Nextcloud instance
3. No additional tools; uses built-in web interface

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for admin accounts to prevent unauthorized access
- Monitor admin panel logins for anomalous IP addresses or times using Nextcloud's audit logs
- Restrict admin access to specific IP ranges via firewall rules

## Objectives

1. Authenticate as administrator and enter the settings panel
2. Locate and prepare the theming upload options
3. Confirm access to vulnerable upload endpoints

## Instructions

### Step 1: Log In to Nextcloud

**Context**: Authenticate to gain admin privileges, required for theming access.

Navigate to the Nextcloud login page (e.g., http://example.com/nextcloud) and enter admin credentials.

> Upon successful login, the dashboard appears, confirming admin role.

### Step 2: Navigate to Theming Settings

**Context**: Reach the specific upload interface within admin settings.

From the dashboard, click on your user icon > Settings > Administration settings > Theming. Locate the sections for "Logo" and "Login background image."

> The page loads with file upload buttons, indicating success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- admin-access
- theming
