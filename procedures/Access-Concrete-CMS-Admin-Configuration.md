---
tags:
  - admin-access
  - concrete-cms
  - configuration
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
updated_at: '2025-12-14T03:15:35.393Z'
sub_techniques: []
id: 5b205bf1-2a6f-4a92-b649-acbe4359d477
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Concrete-CMS-Admin-Configuration

## Summary

This procedure outlines how to log in and navigate to the admin configuration for the 'Message to Display When No Pages Listed' feature in Concrete CMS, setting the stage for XSS injection.

## Description

In Concrete CMS, administrative settings for site-wide messages, including the no-pages display message, are accessible via the dashboard. This procedure assumes authenticated access and targets the sitemap or theme settings where user input is accepted without sanitization. The goal is to reach the editable field that renders HTML in no-pages scenarios, enabling stored XSS attacks that affect all users viewing such pages.

## Requirements

1. Valid admin credentials for the Concrete CMS instance
2. Web browser with access to the target site
3. Knowledge of the admin URL (typically /index.php/dashboard/)

## Defense

Defensive measures and detection strategies:

- Implement role-based access control to restrict configuration changes to trusted admins
- Enable logging of admin actions to monitor unauthorized changes to site messages
- Use web application firewalls (WAF) to scan for suspicious admin inputs

## Objectives

1. Gain access to the vulnerable configuration field
2. Prepare for payload injection without triggering alerts
3. Ensure the setup allows persistence of changes

## Instructions

### Step 1: Log In to Admin Panel

**Context**: Authenticate to the CMS to access privileged settings.

Log in using admin credentials at the dashboard URL.

> Upon successful login, the admin menu appears, confirming access.

### Step 2: Navigate to Sitemap Settings

**Context**: Locate the specific configuration for no-pages messages.

Go to Dashboard > Sitewide Settings > Sitemap or Pages & Themes section, and find the 'Message to Display When No Pages Listed' input field.

> The form loads with the editable text area for the message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[admin-access]]
- [[concrete-cms]]
