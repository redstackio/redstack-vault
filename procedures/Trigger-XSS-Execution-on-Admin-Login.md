---
id: proc-trigger-xss-admin
tags:
  - xss
  - execution
  - privilege-escalation
type: procedure
tools: []
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
updated_at: '2025-12-14T17:28:58.966Z'
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
# Trigger-XSS-Execution-on-Admin-Login

## Summary

This procedure activates the stored XSS payload by logging into the WordPress admin dashboard, causing the plugin's error banner to render the injected JavaScript, which executes with administrator privileges to enable further compromise like user creation or PHP code injection.

## Description

After payload injection, the error banner persists in the admin dashboard. Upon administrator login, WordPress loads the dashboard, evaluates the unescaped HTML/JS in the banner, and executes the payload (e.g., <svg/onload=alert(...)>) in the admin context. This allows AJAX requests to WordPress APIs for malicious actions. Prerequisites: Payload already injected, admin credentials, plugin active. Expected outcome: JavaScript execution confirming compromise, with potential for RCE.

## Requirements

1. Stored XSS payload from prior injection
2. Valid administrator credentials for WordPress
3. Plugin not disabled post-injection
4. Browser access to admin panel

## Defense

Defensive measures and detection strategies:

- Escape HTML in all error messages and admin notices
- Use nonces and capability checks for AJAX endpoints
- Log and alert on suspicious admin dashboard JavaScript execution
- Regular plugin updates and vulnerability scanning

## Objectives

1. Render the stored error banner to execute injected JavaScript
2. Leverage admin privileges for server-side actions
3. Confirm compromise via alert or AJAX success

## Instructions

### Step 1: Reactivate Plugin if Needed

**Context**: Ensure the All In One Event Calendar plugin is enabled, as disabling might clear the error banner.

**Instructions**: Access WordPress admin > Plugins, and activate if inactive. No command; manual via UI.

> Expected: Plugin status shows active.

### Step 2: Admin Login and Dashboard Load

**Context**: Log in to trigger banner rendering and payload execution.

**Instructions**: Navigate to /wp-admin, enter admin credentials, and load the dashboard. Observe for immediate JS execution.

> Expected: Alert popup or console errors/network requests indicating payload run (e.g., alert('stored-xss')).

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
- execution
- privilege-escalation
