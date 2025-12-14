---
tags:
  - navigation
  - setup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:25.343Z'
sub_techniques: []
id: e462206c-d262-4d85-ac4f-c0408ca2b52f
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Navigate-to-SMTP-Users-Settings

## Summary

This procedure guides an authenticated user through the SMTP2GO dashboard to the SMTP users management section, positioning the attacker to access the vulnerable user creation form.

## Description

Once logged in, the dashboard provides menu options for settings. Navigating to SMTP users exposes the add user functionality where input sanitization is lacking. This step is prerequisite for injection and assumes a standard web interface without additional auth layers.

## Requirements

1. Active authenticated session in SMTP2GO
2. Web browser capable of handling session cookies
3. No ad blockers interfering with dashboard loads

## Defense

Defensive measures and detection strategies:

- Role-based access control to restrict settings navigation
- Audit logs for access to admin-like sections by new accounts
- Session timeout enforcement to limit exposure windows

## Objectives

1. Locate the SMTP user management interface
2. Verify access to add user functionality
3. Confirm no intermediate protections like CSRF tokens

## Instructions

### Step 1: Access Dashboard Menu

**Context**: From the post-login dashboard, identify navigation elements.

Locate and click the "Settings" option in the main menu or sidebar.

### Step 2: Select SMTP Users

**Context**: Drill down to the specific vulnerable module.

In the settings submenu, click on "SMTP Users" to load the management page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[web]]

