---
id: proc-navigate-home-admin
tags:
  - privilege-escalation
  - path-traversal
  - saba-lms
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:00.483Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Navigate to Home Endpoint for Admin Privileges

## Summary

This procedure exploits improper path validation in Saba LMS by navigating from the error page to the /home endpoint, incorrectly assigning 'Samba administrator' privileges to a non-admin session, enabling unauthorized admin access.

## Description

After triggering the login error, the application's URL handling fails to normalize paths, allowing traversal to the /home endpoint. This grants elevated privileges without authentication, impacting web apps vulnerable to directory traversal. Outcomes include admin UI access, leading to exfiltration of sensitive data like system configs and credentials, and potential RCE or DoS.

## Requirements

1. Active session from non-admin login error page
2. Knowledge of the base URL (e.g., https://target.com)
3. Ability to manually edit browser URLs

## Defense

Defensive measures and detection strategies:

- Enforce path normalization and canonicalization in URL routing
- Implement role-based access control (RBAC) checks on all endpoints
- Monitor for direct jumps from error pages to sensitive paths like /home

## Objectives

1. Escalate privileges via path traversal
2. Verify admin status in the UI
3. Enable access to restricted administrative functions

## Instructions

### Step 1: Modify URL to Home Endpoint

**Context**: From the error page, alter the URL to traverse to the home path, bypassing privilege checks.

No command; in browser, change URL to https://target.com/home and press enter.

> The page reloads, and the account indicator shows 'Samba administrator' due to traversal flaw.

### Step 2: Confirm Privilege Escalation

**Context**: Inspect the loaded page for signs of elevated access.

Look for admin-specific elements, such as admin menus or data views not available to standard users.

> Success is indicated by the 'Samba administrator' label, confirming unauthorized elevation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-escalation]]
- [[path-traversal]]
