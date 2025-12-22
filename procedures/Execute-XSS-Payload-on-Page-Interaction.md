---
id: proc-execute-xss-payload-interaction
tags:
  - xss
  - execution
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
updated_at: '2025-12-13T23:56:03.468Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute XSS Payload on Page Interaction

## Summary

This procedure triggers the reflected XSS payload by simulating or inducing user interaction with the vulnerable <a> tag on the Twitter Flight School page.

## Description

Once the malicious referer is reflected into an <a> tag, clicking elements like the 'X' button in the top left executes the javascript: payload. This runs arbitrary JS in the victim's browser, confirming control and allowing escalation. The attack relies on the lack of scheme validation, targeting web sessions.

## Requirements

1. Victim has loaded the crafted URL
2. Access to the page in a browser
3. Interaction capability (e.g., mouse click)

## Defense

Defensive measures and detection strategies:

- Avoid reflecting user input in executable contexts like href
- Implement clickjacking protection
- Log and alert on JS errors or unusual script executions

## Objectives

1. Trigger payload execution
2. Verify JS control via alert
3. Prepare for payload chaining

## Instructions

### Step 1: Load Vulnerable Page

**Context**: Navigate to the URL with injected referer.

No command; use browser to access https://www.twitterflightschool.com/student/award/[ID]?referer=javascript:alert(document.domain)

> Page loads with reflected payload. Expected: Inspect element shows <a href="javascript:alert(document.domain)">.

### Step 2: Interact to Execute

**Context**: Click the triggering element to run the JS.

Click the 'X' button in the top left.

> Alert pops up with "www.twitterflightschool.com". Success: JS executes without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- javascript
- click-trigger
