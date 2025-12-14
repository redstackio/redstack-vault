---
id: proc-uuid-4
tags:
  - access
  - admin-panel
  - data-modification
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
updated_at: '2025-12-14T17:30:18.036Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Reset-Password-and-Admin-Panel

## Summary

This procedure exploits the bypassed checks to load the password reset page and navigate to admin sections, enabling unauthorized viewing and editing of user data and reports.

## Description

Post-manipulation, the Angular app renders /resetPassword without server validation, and from there, links to 'user' and 'report' management are accessible. This grants full control over sensitive data in the UPS support site.

## Requirements

1. Successful response modification from prior step
2. Active browser session
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Server-side auth checks on all admin routes
- Audit logs for unauthorized admin access attempts

## Objectives

1. Load restricted UI components
2. Manipulate user reports and data
3. Confirm full unauthorized access

## Instructions

### Step 1: Navigate to Reset Page

**Context**: The client-side redirect or manual navigation to /resetPassword now succeeds.

Manually enter or click to https://█████████/resetPassword

> Page loads fully, showing reset form.

### Step 2: Access Admin Sections

**Context**: From reset page, explore linked sections for user and report management.

Click on 'user' or 'report' tabs/links.

> Admin interfaces load, allowing CRUD operations on data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access]]
- [[admin-panel]]
- [[data-modification]]
