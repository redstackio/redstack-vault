---
id: proc-uuid-3
tags:
  - xss-execution
  - javascript
  - session-hijacking
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
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
updated_at: '2025-12-14T00:11:09.663Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-upon-Victim-Login

## Summary

This procedure details how the victim triggers the reflected XSS by visiting the malicious URL and logging in, causing the injected JavaScript to execute in their browser context for data theft or further exploitation.

## Description

When the victim accesses the URL in a browser like Firefox or Chrome and authenticates, the server reflects the unsanitized path payload back into the page HTML. The `<img src=xss onerror=prompt('XSS')>` triggers an error, executing the `onerror` handler. This runs arbitrary JS, such as stealing cookies or session tokens. High impact as it affects authenticated users without project-specific access. Prerequisites: Victim must visit and log in.

## Requirements

1. Malicious URL distributed to victim
2. Victim's browser (e.g., [[tools/Firefox]] or [[tools/Chrome]])
3. Valid login credentials for OWOX BI

## Defense

Defensive measures and detection strategies:

- Output encoding for all user inputs in HTML contexts
- Browser-based protections like XSS auditors
- Logging and alerting on JS errors or prompts in dashboards

## Objectives

1. Execute the payload in the victim's authenticated session
2. Collect sensitive data like cookies or tokens
3. Enable follow-on attacks such as account takeover

## Instructions

### Step 1: Victim Accesses URL

**Context**: Victim clicks the link and navigates to the dashboard page.

Use [[tools/Firefox]] or [[tools/Chrome]] to open the URL.

### Step 2: Authenticate

**Context**: Victim logs in with their credentials, loading the full page.

The path payload is reflected without escaping.

### Step 3: Payload Executes

**Context**: Page load triggers the img error, running `prompt('XSS')` or custom JS.

**Expected Output**: Alert dialog or JS actions (e.g., data exfiltration to attacker server).

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
- [[tools/Chrome]]

## Tags

- [[xss-execution]]
- [[JavaScript]]
