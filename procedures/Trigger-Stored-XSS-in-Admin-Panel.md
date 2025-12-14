---
id: proc-trigger-stored-xss-admin
tags:
  - xss
  - trigger
  - stored-xss
  - concrete-cms
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.883Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS in Admin Panel

## Summary

This procedure triggers the execution of the stored XSS payload by accessing the admin page that renders the unsanitized points action data in Concrete CMS.

## Description

Once stored, the payload in `upaHandle` or `upaName` is output without escaping on pages like `/index.php/dashboard/users/points/actions/action_saved`. Viewing this as an admin executes the JS (e.g., prompt(1)) in the browser, enabling theft of session data or further attacks. This relies on social engineering to lure the admin or direct access.

## Requirements

1. Stored payload from prior steps
2. Admin browser access to dashboard
3. No CSP blocking inline JS

## Defense

Defensive measures and detection strategies:

- Escape all outputs with context-aware sanitization
- Deploy CSP headers to prevent JS execution
- Monitor for unexpected JS alerts or DOM manipulations in admin sessions

## Objectives

1. Render the vulnerable page to execute payload
2. Confirm JS runs in admin context
3. Escalate to session hijacking if possible

## Instructions

### Step 1: Navigate to Render Page

**Context**: Access the page displaying stored actions.

Log in as admin and go to `/dashboard/users/points/actions` or the saved action view.

> Ensure the malicious action is listed.

### Step 2: Observe Execution

**Context**: Watch for payload trigger.

The onload attribute in `upaHandle` should fire JS like prompt(1) automatically.

> Check browser console for errors or alerts.

### Step 3: Validate Impact

**Context**: Test for broader exploitation.

Replace prompt(1) with payload to steal cookies (e.g., document.cookie) and exfil to attacker server.

> Success if alert appears or network request sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- Browser dev tools (for inspection)

## Tags

- xss
- trigger
- stored-xss
