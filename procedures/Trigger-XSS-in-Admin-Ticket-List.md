---
tags:
  - xss
  - trigger
  - admin-exploit
  - wordpress
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:51.819Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: 8a77179b-815c-49d6-8612-1ffdc737b6b3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Admin-Ticket-List

## Summary

This procedure triggers the stored XSS payload by viewing the admin tickets table, executing JavaScript in the privileged admin browser context for potential session hijacking or data exfiltration.

## Description

Once the payload is stored, accessing the admin tickets list at `/wp-admin/edit.php?post_type=sf_ticket` causes the plugin's `class-supportflow-admin.php` (line 1175) to output the message without escaping, rendering the `<script>` tag and executing it. This occurs in the Same-Origin Policy context of the admin area, allowing access to admin cookies, DOM manipulation, or redirects to phishing sites.

## Requirements

1. Admin access to the WordPress dashboard
2. Previously injected ticket with XSS payload
3. Vulnerable SupportFlow version without patches

## Defense

Defensive measures and detection strategies:

- Patch the plugin or apply custom escaping to table outputs
- Implement XSS auditors or browser extensions for admins
- Monitor admin access logs for anomalous JS execution

## Objectives

1. Execute the stored payload in admin browser
2. Achieve code execution for theft or escalation
3. Validate vulnerability exploitation

## Instructions

### Step 1: Log In as Admin

**Context**: Ensure privileged access to the dashboard.

Navigate to `/wp-login.php` and authenticate with admin credentials.

### Step 2: Access Tickets List

**Context**: Load the page where the unescaped output occurs.

Go to `/wp-admin/edit.php?post_type=sf_ticket` to view the table of tickets.

### Step 3: Observe Execution

**Context**: Confirm the payload triggers without user interaction beyond page load.

The message column renders the script, popping an alert or sending data to an attacker server. Check browser console for execution confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- trigger
- admin-exploit
- wordpress
