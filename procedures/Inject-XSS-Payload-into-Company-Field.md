---
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
updated_at: '2025-12-14T03:16:14.442Z'
sub_techniques: []
id: 6e071cea-327b-43e5-af05-b8aa3f776555
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Company-Field

## Summary

This procedure details the insertion of a JavaScript payload into the company field of the form to exploit the lack of input sanitization, preparing for reflection upon submission.

## Description

The vulnerability stems from improper sanitization in the company lookup field. By injecting an XSS payload like `<svg onload=confirm(document.domain)>xs`, the attacker tests for reflection. This step occurs client-side before submission and relies on the form accepting arbitrary input.

## Requirements

1. Access to the loaded form page
2. Knowledge of effective XSS payloads
3. Web browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Client-side input validation to reject suspicious characters
- Server-side encoding of reflected inputs
- Content Security Policy (CSP) to block inline scripts

## Objectives

1. Deliver unsanitized payload to the server
2. Bypass any client-side checks
3. Set up for JavaScript execution on reflection

## Instructions

### Step 1: Locate and Fill Company Field

**Context**: Identify the vulnerable field and insert the payload to simulate malicious input.

No command required; in the form, enter the payload `<svg onload=confirm(document.domain)>xs` into the company field. Fill other fields with benign data if needed to complete the form.

> The field should accept the input, including angle brackets and event handlers, without truncation or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- payload-injection
