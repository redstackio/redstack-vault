---
tags:
  - xss
  - trigger
  - admin
  - execution
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
updated_at: '2025-12-13T23:52:34.326Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d6d79ec2-ab3c-44fa-b94d-57c7a781d6e8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload-in-Admin-Context

## Summary

This procedure triggers the persistent XSS payload by having an administrator view the injected customer profile in the WordPress admin panel, resulting in JavaScript execution within the admin's high-privilege browser session.

## Description

After payload injection into the county field, the vulnerability manifests when an admin accesses the user's profile via wp-admin/users.php or directly via wp-admin/user-edit.php?user_id=<ID>. The county value is output without HTML/JS encoding (e.g., via echo without esc_html), allowing the script to execute. This grants the attacker control over the admin's session for actions like data theft, forging requests, or even editing plugin files to achieve RCE.

## Requirements

1. Administrative access to the WordPress backend.
2. Knowledge of the target customer user ID (e.g., 4).
3. Payload already injected in the customer's address.

## Defense

Defensive measures and detection strategies:

- Encode all user data outputs in admin templates (e.g., use esc_attr() for attributes).
- Implement Content Security Policy (CSP) to block inline scripts.
- Log admin views of user profiles and monitor for XSS indicators like unexpected alerts.

## Objectives

1. Execute the payload in the admin browser context.
2. Demonstrate impact such as alert popping or console access.
3. Enable follow-on attacks like session hijacking.

## Instructions

### Step 1: Access Admin Users Page

**Context**: Navigate to the user management section.

Login as admin and go to http://192.168.0.101/wordpress/wp-admin/users.php.

> Locate the target customer in the list.

### Step 2: View Customer Profile

**Context**: Load the edit page to trigger the unencoded echo.

Click on the customer or directly visit http://192.168.0.101/wordpress/wp-admin/user-edit.php?user_id=4.

> Expected: Payload executes immediately, e.g., alert(1) dialog appears, confirming XSS in admin context.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[admin]]
