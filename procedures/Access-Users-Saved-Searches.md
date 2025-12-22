---
tags:
  - web
  - recon
  - idor
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.108Z'
sub_techniques: []
id: ed6991ef-5cca-4b34-b043-bf097942fc4b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Users-Saved-Searches

## Summary

This procedure involves logging into the DoD web application and navigating to the Saved Searches section to view personal items, setting the stage for capturing delete requests in an IDOR exploitation scenario.

## Description

In the context of exploiting an IDOR vulnerability in the DoD web app's delete functionality, this initial step ensures the attacker has an authenticated session and can interact with the saved searches interface. It reveals the structure of saved items without performing any destructive actions, allowing preparation for URL capture. Expected outcomes include visibility into the user's own saved searches, confirming the endpoint's accessibility.

## Requirements

1. Valid authenticated session in the DoD web application
2. Web browser with developer tools enabled
3. Network access to the application

## Defense

Defensive measures and detection strategies:

- Implement session timeout and multi-factor authentication to limit unauthorized access
- Log all navigations to sensitive sections like Saved Searches for anomaly detection

## Objectives

1. Establish authenticated access to the Saved Searches interface
2. Verify personal saved items are loaded
3. Prepare for subsequent request interception

## Instructions

### Step 1: Log In and Navigate

**Context**: Authenticate and reach the account menu to access saved items.

No specific command; use the web interface:

- Enter credentials at the login page.
- From the account menu, select 'Saved Searches'.

> This loads the personal saved searches list. Expected output: Display of user's saved items.

### Step 2: Inspect Interface

**Context**: Confirm the section is functional and ready for delete actions.

Use browser developer tools to inspect elements.

> Expected output: HTML structure showing saved search entries with delete options.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[recon]]
