---
tags:
  - xss
  - self-xss
  - web
  - uber
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.276Z'
sub_techniques: []
id: 71b997bf-2f50-4b39-9403-a8d4182ce262
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Script-as-New-Password

## Summary

This core procedure injects a JavaScript payload into Uber's new password field during recovery, exploiting poor sanitization to store executable code.

## Description

On the recovery page, input a script tag like `<script>alert(document.domain);</script>` as the password and submit. The app accepts it without escaping, storing the payload. This enables self-XSS when rendered. Requires prior link access. Outcome: Password set with embedded JS.

## Requirements

1. Access to password set form
2. Knowledge of XSS payloads
3. Valid recovery session

## Defense

Defensive measures and detection strategies:

- Client-side and server-side input validation for passwords (e.g., disallow < >)
- Content Security Policy (CSP) to block inline scripts

## Objectives

1. Bypass password validation for script injection
2. Store unsanitized payload
3. Set up for execution trigger

## Instructions

### Step 1: Enter Payload and Submit

**Context**: Use the form to input and save the malicious password.

No command; form input:

```plaintext
Set password: <script>alert(document.domain);</script>
Click Submit
```

> Submission succeeds; password is updated. No immediate execution.

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
- [[self-xss]]
- [[web]]
- [[uber]]
