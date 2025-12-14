---
id: proc-uuid-2
tags:
  - access-control
  - admin-bypass
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.737Z'
skill_level: beginner
impact_level: informational
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access-Admin-Panel-Endpoints

## Summary

This procedure exploits missing authorization checks on admin endpoints of app.lemlist.com, allowing any authenticated user to view the administrative interface.

## Description

After authentication, the attacker navigates directly to hardcoded admin URLs discovered via JavaScript file analysis. These endpoints lack proper role verification, exposing admin views like dashboards and configurations. No modifications are possible, limiting impact to information disclosure. The vulnerability stems from frontend JavaScript revealing unprotected paths, and exploitation requires only browser navigation in an active session.

## Requirements

1. Active authenticated session from standard user login
2. Web browser to navigate URLs
3. Knowledge of exposed admin paths (e.g., from JS source inspection)

## Defense

Defensive measures and detection strategies:

- Enforce server-side authorization checks on all admin routes
- Obfuscate or remove admin URLs from client-side JavaScript
- Log and alert on access to admin endpoints from non-admin sessions
- Implement role-based access control (RBAC) with strict enforcement

## Objectives

1. Gain view access to admin interfaces
2. Identify exposed administrative data or configurations
3. Demonstrate the access control flaw without altering data

## Instructions

### Step 1: Inspect for Admin URLs

**Context**: Optionally, review JavaScript files on the site to identify unprotected admin paths, though direct navigation works post-login.

In the browser developer tools, search for strings like '/admin' in loaded JS files.

> This reveals URLs such as https://app.lemlist.com/admin without needing tools.

### Step 2: Navigate to Admin Endpoint

**Context**: Use the active session to directly access an admin URL, bypassing authorization.

Enter one of the following in the browser address bar: https://app.lemlist.com/admin, https://app.lemlist.com/admin/i18n, or https://app.lemlist.com/admin/mailboxes/123.

> The page loads the admin interface if successful, showing elements like admin menus or data views. No errors occur due to missing checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[access-bypass]]
- [[admin-panel]]
