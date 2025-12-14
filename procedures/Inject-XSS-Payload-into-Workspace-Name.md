---
id: 123e4567-e89b-12d3-a456-426614174002
tags:
  - xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.137Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Workspace-Name

## Summary

This procedure injects a JavaScript payload into the workspace name input field of the Mattermost Create New Workspace screen, exploiting the lack of input sanitization.

## Description

The workspace name field does not properly escape HTML or JavaScript, allowing tags like <img> with onerror handlers to be inserted. The payload used is '/><img src=x onerror=alert(document.cookie)>', which breaks out of any surrounding context and triggers an alert with cookies upon rendering. This is a classic reflected self-XSS, executing only in the injector's browser.

## Requirements

1. Access to the Create New Workspace form
2. Knowledge of basic XSS payloads
3. Web browser for manual input

## Defense

Defensive measures and detection strategies:

- Implement server-side and client-side input sanitization (e.g., HTML entity encoding)
- Use Content Security Policy (CSP) to restrict inline scripts
- Validate input against expected patterns (e.g., alphanumeric for names)

## Objectives

1. Insert executable JavaScript without rejection
2. Prepare payload for form submission
3. Demonstrate lack of escaping

## Instructions

### Step 1: Enter Payload in Input Field

**Context**: Focus on the vulnerable workspace name field and input the malicious string.

No command required; type or paste the following into the workspace name field: `/><img src=x onerror=alert(document.cookie)>`

> The field should accept the input fully, including angle brackets and script attributes, without auto-escaping or errors.

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
