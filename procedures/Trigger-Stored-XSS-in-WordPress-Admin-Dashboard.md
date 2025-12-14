---
tags:
  - xss
  - execution
  - admin-dashboard
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
updated_at: '2025-12-14T00:11:09.218Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4adb20be-7d65-41aa-be90-aa0c68333d82
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-WordPress-Admin-Dashboard

## Summary

This procedure triggers the execution of the stored JavaScript payload in the Stream plugin's activity log by accessing the admin dashboard, resulting in arbitrary code execution with administrator privileges.

## Description

After injection, the unsanitized log entry containing the JavaScript payload is displayed in the Stream tab of the WordPress admin panel without HTML escaping. When an administrator views this tab, the payload renders and executes in the browser context, potentially allowing theft of session cookies, site modifications, or further exploits like PHP file uploads via the plugin editor.

## Requirements

1. Administrative credentials to access the WordPress dashboard
2. Injected payload already stored from prior procedure
3. Modern web browser for viewing the dashboard

## Defense

Defensive measures and detection strategies:

- Enable output escaping and HTML sanitization in plugin templates (e.g., using esc_html() in WordPress)
- Use browser extensions or WAF rules to block XSS payloads in admin views
- Audit plugin logs for suspicious entries and restrict dashboard access

## Objectives

1. Execute injected JavaScript in admin context
2. Gain control over site content and potentially server-side resources
3. Demonstrate full compromise potential

## Instructions

### Step 1: Access Admin Dashboard

**Context**: Log in as an administrator and navigate to the Stream plugin's main tab to display the activity log containing the payload.

**Command** (No command; manual browser action):

> Open the WordPress admin URL (e.g., https://newsroom.uber.com/wp-admin), authenticate, and click on the Stream tab. The log entry will render the <script>alert('stored xss');</script> payload, triggering the alert.

### Step 2: Verify Execution

**Context**: Confirm JS execution via browser console or visible effects.

> Inspect the page source or developer tools to see the unsanitized HTML; expected outcome is immediate JS alert or console errors indicating execution.

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
- admin-dashboard
