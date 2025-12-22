---
tags:
  - xss
  - trigger
  - javascript-execution
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:46:31.560Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 46c4936d-a263-4fda-856c-b760aa085a2c
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Admin-Access-Page

## Summary

This procedure triggers the execution of a stored XSS payload by loading the Admin Access page in Revive Adserver, causing JavaScript to run in the victim's browser context.

## Description

After payload injection, logging in as another admin and visiting Inventory > Admin Access renders the tainted email field, executing the script. This can lead to arbitrary code execution, such as alerts for testing or more sophisticated attacks like BeEF integration for hooking the browser. The attack is persistent and targets privileged users.

## Requirements

1. Payload already injected by another admin
2. Victim admin credentials
3. Web browser access to the application

## Defense

Defensive measures and detection strategies:

- Output encode all user data before rendering, e.g., using HTML entity encoding
- Audit admin pages for reflected/stored content
- Implement browser-based protections like XSS auditors

## Objectives

1. Execute stored JavaScript in victim browser
2. Collect data or hijack sessions via the payload
3. Demonstrate persistence over multiple sessions

## Instructions

### Step 1: Login as Victim

**Context**: Establish a new session to avoid contamination.

Use [[tools/Firefox]] to log in with victim admin credentials.

> Expected: Dashboard access granted.

### Step 2: Navigate to Vulnerable Page

**Context**: Load the page that displays the stored email.

Go to Inventory > Admin Access.

> Expected: Page loads, and payload executes (e.g., alert pops).

### Step 3: Observe Execution

**Context**: Confirm the XSS impact.

Check browser console or alert for script output.

> Expected: JavaScript runs, potentially stealing cookies or logging input.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[Execution]]
