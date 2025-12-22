---
tags:
  - xss
  - payload
  - hackerone
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.949Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 2055b029-6ed7-4662-95a5-3578cdcddbea
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Malicious-Report-with-XSS-Payload

## Summary

This procedure involves submitting a bug report to a HackerOne program with an XSS payload embedded in the additional information field, storing the malicious JavaScript for later execution.

## Description

Targeting the custom fields feature, a hacker submits a report containing a payload like '"><img src=x onerror=alert(document.domain)>'. This payload is stored and can be triggered when an admin edits the associated custom field. The attack relies on the lack of sanitization in report data rendering, specific to IE11.

## Requirements

1. Valid hacker account on HackerOne
2. Access to submit reports to the target program
3. Knowledge of a simple XSS payload

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in report fields, especially HTML attributes
- Escape special characters in additional information sections
- Review submitted reports for suspicious scripts before processing

## Objectives

1. Persist the XSS payload in the program's report database
2. Associate the payload with the custom field for rendering
3. Avoid immediate detection during submission

## Instructions

### Step 1: Create a New Report

**Context**: Log in as a hacker and start a new bug report for the target program.

Navigate to the program's report submission page on hackerone.com.

### Step 2: Inject the Payload

**Context**: Embed the malicious payload in the additional information field.

In the "Additional information" field, insert the payload: `"><img src=x onerror=alert(document.domain)>`

Fill out other required fields with dummy vulnerability details and submit the report.

> The payload breaks out of any HTML context and executes on render, alerting the document domain upon trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload]]
