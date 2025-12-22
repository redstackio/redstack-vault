---
tags:
  - xss
  - execution
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
  - WordPress
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9465ea20-0c2b-45f2-9c44-437b95293d5f
created_at: '2025-12-14T03:16:25.643Z'
updated_at: '2025-12-14T03:16:25.643Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-WordPress-Admin-Dashboard

## Summary

This procedure involves an administrator logging into the WordPress dashboard to view the stored error banner, executing the injected JavaScript payload with admin privileges and confirming the XSS compromise.

## Description

Once the payload is stored and the plugin reactivated, the error banner in the admin dashboard includes the unescaped JavaScript (e.g., SVG onload alert). Viewing the dashboard triggers execution, allowing arbitrary JS under admin context. This can extend to AJAX calls for user creation or PHP file writes via editors. The attack assumes the target is a WordPress admin with the vulnerable plugin active.

## Requirements

1. Valid admin credentials for the target WordPress site
2. Plugin reactivated and payload stored
3. Access to the dashboard URL (e.g., /wp-admin/)

## Defense

Defensive measures and detection strategies:

- Escape all user-controllable data in admin outputs
- Implement strict XSS auditing in plugins
- Use browser extensions or WAF to block XSS payloads
- Monitor admin login events and JS errors in logs

## Objectives

1. Render the stored error banner to execute JS
2. Confirm payload activation via alert
3. Escalate to admin actions like user creation or code injection

## Instructions

### Step 1: Log In to WordPress Admin

**Context**: Authenticate to access the dashboard where the banner is displayed.

**Command** (Web interface):
```bash
# Navigate to /wp-admin/ and enter credentials
```

> Use a browser to visit the admin login, input username/password, and submit.

### Step 2: View Dashboard and Observe Execution

**Context**: Load the main dashboard page to trigger the banner rendering.

**Command** (Web interface):
```bash
# Access /wp-admin/index.php
```

> Upon loading, the XSS payload executes, showing an alert with "stored-xss." Inspect console for further JS capabilities.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- privilege-escalation
