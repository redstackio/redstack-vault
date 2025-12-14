---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - xss
  - execution
  - admin-compromise
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.118Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Admin-Ticket-List

## Summary

This procedure triggers the stored XSS payload by accessing the SupportFlow admin ticket list, where messages are rendered unescaped, leading to JavaScript execution in the admin's browser context.

## Description

The vulnerability stems from `class-supportflow-admin.php` line 1175, where ticket messages are output without `esc_html()` in the admin table at `/wp-admin/edit.php?post_type=sf_ticket`. As an admin or editor views the list, the payload executes, potentially enabling session hijacking or data exfiltration. This step requires admin access and assumes the payload is already stored. Impact includes arbitrary code execution with admin privileges (CVSS 4.8).

## Requirements

1. Admin or editor role on the WordPress site
2. Stored XSS payload in a ticket from prior steps
3. Browser session as the target admin

## Defense

Defensive measures and detection strategies:

- Apply output escaping like `esc_html()` in admin table rendering
- Patch the plugin to fix unescaped outputs
- Monitor admin access logs for anomalous JavaScript alerts or errors

## Objectives

1. Execute stored JavaScript in high-privilege context
2. Achieve arbitrary code execution for further compromise
3. Demonstrate impact on admin session security

## Instructions

### Step 1: Log In as Admin

**Context**: Gain access to the WordPress admin dashboard with appropriate roles.

Log in at `/wp-login.php` using admin credentials.

> Ensure the session is active and no CSP blocks JavaScript.

### Step 2: Navigate to Ticket List

**Context**: Access the vulnerable admin page to render the ticket table.

Go to `/wp-admin/edit.php?post_type=sf_ticket`.

> The table displays tickets, including unescaped messages from the database.

### Step 3: Observe Execution

**Context**: View the page to trigger the payload in the message column.

Locate the injected ticket; the payload should execute immediately upon rendering.

> Expect an alert('XSS') or custom effects; inspect console for errors if it fails.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- stored-xss
- admin-trigger
- javascript-execution
