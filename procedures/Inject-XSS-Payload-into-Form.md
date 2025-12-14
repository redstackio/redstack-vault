---
tags:
  - xss
  - payload
  - injection
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
updated_at: '2025-12-14T03:15:53.537Z'
sub_techniques: []
id: b1bf498e-d594-48a9-94d3-422c068de0ad
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Form

## Summary

This procedure details injecting a stored XSS payload into the q_13774 parameter of the DoD registration form's additional information section, bypassing any client-side checks.

## Description

The vulnerability stems from insufficient sanitization of user input in the form field. The payload uses URL encoding to evade basic filters and employs an SVG onload attribute to execute JavaScript upon rendering of stored data.

## Requirements

1. Access to the loaded form from the previous procedure.
2. Knowledge of the target parameter (q_13774).
3. Basic understanding of XSS payloads.

## Defense

Defensive measures and detection strategies:

- Apply client-side and server-side input validation to reject special characters like < > " '.
- Use Content Security Policy (CSP) to block inline JavaScript execution.

## Objectives

1. Enter the malicious payload without rejection.
2. Ensure the payload is positioned to break out of any context (e.g., quote escaping).
3. Test for immediate execution if possible, though stored XSS defers to viewing.

## Instructions

### Step 1: Locate and Fill Vulnerable Field

**Context**: Identify the additional information section and input the payload to store malicious script.

No command; manually type or paste the encoded payload `%22%27%3e%3csvg%2fonload%3dconfirm(666)%3e` into the q_13774 field.

> This decodes to "'><svg onload=confirm(666)>", closing any attributes and injecting an executable SVG element. Expected: Field accepts input without alerts or blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[payload]]
- [[injection]]
