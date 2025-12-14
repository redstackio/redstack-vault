---
tags:
  - xss
  - self-xss
  - uber
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.285Z'
sub_techniques: []
id: 0a8b3641-bee8-4bdd-b770-f4cff2da54ae
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Uber-Password-Field

## Summary

This procedure involves entering a crafted XSS payload into the new password field of Uber's reset form, exploiting the lack of sanitization to prepare for self-execution.

## Description

With the reset form loaded, this step focuses on inputting an XSS payload like ">'><img src=x onmouseover =prompt(document.domain)>" into the password field. The payload is designed to break out of the input context and inject HTML/JavaScript. Due to insufficient sanitization, it persists when the password is handled. This targets the web form at https://partners.uber.com/, with the outcome being the payload acceptance without validation errors, setting up the trigger in the next step.

## Requirements

1. Loaded password reset form
2. Knowledge of basic XSS payloads
3. Web browser developer tools (optional for testing)

## Defense

Defensive measures and detection strategies:

- Client-side input validation and sanitization
- Server-side password complexity checks rejecting special characters
- WAF rules to block common XSS patterns in forms

## Objectives

1. Successfully input the XSS payload
2. Ensure form accepts the input
3. Avoid immediate rejection or sanitization

## Instructions

### Step 1: Locate Password Field

**Context**: Identify the new password input.

Focus on the 'New Password' field in the form.

> Ensure the field is empty and ready for input.

### Step 2: Enter Payload

**Context**: Type the malicious string.

Input the following payload: ">'><img src=x onmouseover =prompt(document.domain)>"

> The field should accept the string; if masked, temporarily toggle 'show password' to verify.

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
- [[uber]]
- [[payload-injection]]
