---
id: proc-trigger-xss-admin
tags:
  - xss-trigger
  - admin-exploitation
  - javascript-execution
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
updated_at: '2025-12-13T23:52:20.817Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-as-Admin

## Summary

This procedure triggers the stored XSS by having an admin user access the author edit page, causing the injected JavaScript to execute in the admin's browser context.

## Description

After payload injection, the edit page at /bridge/author/edit/{id} renders the unescaped author name, executing the script. This impacts privileged users, potentially allowing session hijacking or keylogging. CSP may block full execution, resulting in console warnings, but demonstrates the vulnerability's severity in unaudited CMS setups.

## Requirements

1. Created author with malicious payload
2. Admin or captain user credentials
3. Edit link for the vulnerable author

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers to prevent script execution
- Audit user-generated content rendering in templates
- Monitor browser console for CSP violations and alert on them

## Objectives

1. Execute payload in high-privilege context
2. Observe impact like alerts or data exfil potential
3. Validate mitigation effectiveness (e.g., CSP)

## Instructions

### Step 1: Obtain and Share Edit Link

**Context**: Generate the URL pointing to the vulnerable author edit page.

After creation, note the ID (e.g., 3) and form http://localhost:8080/bridge/author/edit/3; share with admin.

> Expected: Link ready for access.

### Step 2: Access as Admin User

**Context**: Load the page to trigger rendering and execution.

Login as admin and open the link in browser.

> Expected: Script executes (alert(1)) or CSP blocks with console error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- admin-exploitation
- javascript-execution
