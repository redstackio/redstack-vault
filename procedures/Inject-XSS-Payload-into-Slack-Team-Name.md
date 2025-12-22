---
tags:
  - xss
  - payload-injection
  - slack
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
updated_at: '2025-12-14T03:16:14.717Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: cfea85dc-a4bb-4a99-8bac-2ec431a9a285
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Slack-Team-Name

## Summary

This procedure injects a stored XSS payload into the Slack team name field via the admin panel, exploiting lack of sanitization to store malicious JavaScript for later execution.

## Description

The team name field at /admin/name does not properly escape HTML or JavaScript, allowing injection of payloads that break out of attributes and execute on rendering. This targets web-based Slack workspaces; prerequisites include admin access from the prior procedure. Expected outcomes: payload storage without immediate execution, enabling persistence.

## Requirements

1. Access to the admin panel (from previous procedure)
2. Knowledge of XSS payloads
3. Web browser for form submission

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs, especially in admin fields
- Implement Content Security Policy (CSP) to block inline scripts
- Log and review team name changes for suspicious patterns

## Objectives

1. Store malicious JavaScript in the team name
2. Ensure payload survives storage
3. Set up for triggering on vulnerable pages

## Instructions

### Step 1: Enter Payload

**Context**: Input the XSS payload into the team name field to exploit attribute breakout.

In the team name input field, enter: `'><img src=x onerror=prompt(document.domain)>`

> This closes any HTML attribute (e.g., alt=""), injects an <img> tag, and uses onerror to execute prompt(document.domain), demonstrating domain access.

### Step 2: Submit and Verify

**Context**: Update the team name to store the payload.

Click the save or submit button.

> Expected: No errors; team name updates. Check the UI to see if the payload is reflected (may appear garbled but stored).

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
- [[payload-injection]]
- [[slack]]
