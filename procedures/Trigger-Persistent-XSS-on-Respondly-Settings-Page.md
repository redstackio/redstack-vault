---
id: proc-trigger-xss-respondly-settings
tags:
  - xss
  - trigger
  - settings-page
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:36.190Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Persistent-XSS-on-Respondly-Settings-Page

## Summary

This procedure triggers the persistent XSS payload injected via the group name by accessing the account settings page, causing arbitrary JavaScript to execute in the viewer's browser context, potentially leading to session hijacking or data theft.

## Description

After injection, the unsanitized group name is rendered on the /settings/account page without HTML escaping, allowing the payload to execute. For example, the img tag's onerror event fires an alert, but in a real attack, this could be replaced with code to steal cookies or redirect users. The vulnerability also affects feedback emails sent to staff, broadening the attack surface.

## Requirements

1. Valid login credentials from the injected account
2. Web browser to access the application
3. Knowledge of the account ID (e.g., from URL after login)

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., via libraries like DOMPurify) when rendering user inputs
- Implement user input whitelisting for group names (alphanumeric only)
- Log and alert on JavaScript errors or unexpected script executions in the frontend

## Objectives

1. Execute the stored JavaScript payload in the browser
2. Verify XSS by observing alert or inspecting DOM
3. Highlight risks to other users, including admins viewing the page

## Instructions

### Step 1: Log In to the Account

**Context**: Authenticate to access protected pages where the payload is rendered.

Use the email and password from the injected account to log in at https://app.respond.ly.

### Step 2: Navigate to Settings Page

**Context**: Load the page that reflects the group name to trigger execution.

After login, go to https://app.respond.ly/[account-id]/settings/account (replace [account-id] with your actual ID, e.g., 6sjp).

> Upon page load, the payload executes, showing an alert(4). Inspect the element to confirm the unsanitized HTML: the group name appears as `<group>"><img src=x onerror=alert(4)></group>` or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
