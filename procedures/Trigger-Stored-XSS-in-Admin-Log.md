---
id: proc-trigger-xss-log
tags:
  - xss
  - execution
  - admin
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
updated_at: '2025-12-14T17:29:28.925Z'
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
# Trigger-Stored-XSS-in-Admin-Log

## Summary

This procedure triggers the execution of the stored XSS payload by viewing the tainted log entry in the WordPress admin dashboard's Stream tab, causing JavaScript to run with administrator privileges.

## Description

After injection, the unsanitized log entry in the Stream plugin's database table (handled via connectors/installer.php) displays raw HTML/JS when an admin accesses the dashboard. Navigation to the Stream log renders the payload, executing it in the browser context. This can lead to session hijacking, content manipulation, or further exploits like PHP file uploads. Requires admin access to the dashboard; attacker relies on social engineering or phishing to induce viewing.

## Requirements

1. Administrator credentials or access to the WordPress dashboard
2. The injected payload must already be in the log (from prior procedure)
3. Modern browser for JS execution

## Defense

Defensive measures and detection strategies:

- Apply output escaping (e.g., esc_html()) when rendering log entries in admin panels
- Use browser extensions or WAF to block XSS payloads in admin sessions
- Log and alert on unexpected JS execution in admin dashboards via SIEM

## Objectives

1. Execute injected JavaScript in admin browser context
2. Escalate to site control via admin privileges
3. Enable secondary attacks like file modification

## Instructions

### Step 1: Access Admin Dashboard

**Context**: Log in as an administrator to the WordPress site and navigate to the plugins section.

No command required; manually go to /wp-admin and select the Stream tab.

> Upon viewing the log, the payload executes automatically if present. Expected output: JS alert or console log; inspect page source to confirm unsanitized HTML.

### Step 2: Validate Execution

**Context**: Confirm payload trigger by observing effects like alerts or DOM changes.

Use browser dev tools (F12) to monitor console for errors or executed scripts.

> Successful execution shows the alert('stored xss') or custom payload actions; no server response needed.

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
- admin
