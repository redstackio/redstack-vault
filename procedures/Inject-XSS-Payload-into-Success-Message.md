---
id: proc-uuid-3
tags:
  - xss
  - payload-injection
  - judge-me
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
updated_at: '2025-12-14T03:47:12.942Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Success-Message

## Summary

This procedure involves inserting a malicious JavaScript payload into the success message field of the Judge.me Widget Form, exploiting lack of sanitization to store XSS content.

## Description

The success message field in Judge.me's Widget Form settings allows arbitrary text input that is later rendered in HTML without proper escaping. By injecting a payload like `'><img src=x onerror=alert(document.domain)>`, the attacker closes any open tags and embeds a script that executes on render. This stored XSS persists in the app configuration and affects preview renders.

## Requirements

1. Access to Widget Form settings page
2. Knowledge of basic XSS payloads
3. Browser developer tools for testing (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in admin settings with HTML entity encoding
- Implement content security policy (CSP) to block inline scripts
- Scan app configurations for suspicious patterns like <script> or onerror

## Objectives

1. Enter the payload without triggering immediate validation
2. Ensure the payload breaks out of HTML context
3. Prepare for rendering to confirm injection

## Instructions

### Step 1: Locate Success Message Field

**Context**: Identify the target input for payload placement.

Scroll to or find the 'Success Message' text area on the Widget Form page.

> Expected: Editable text field appears, possibly with placeholder text.

### Step 2: Insert Payload

**Context**: Craft and input the XSS string to exploit rendering.

Clear or append to the field with: `'><img src=x onerror=alert(document.domain)>`

> Expected: Field accepts the input; no errors on typing. The payload will execute later on preview.

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
- [[judge-me]]
