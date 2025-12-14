---
tags:
  - xss-injection
  - html-injection
  - payload-delivery
type: procedure
tools: []
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:32.012Z'
sub_techniques: []
id: 35cdb4fb-516d-4da4-935b-6d9840d2a3ea
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Payload-in-Display-Name

## Summary

This procedure delivers stored XSS or HTML injection payloads into the Display Name field during Pressable site creation, exploiting poor sanitization to enable persistent script execution or content manipulation.

## Description

Targeting the Display Name input on try.pressable.com, this step involves crafting and submitting payloads that bypass frontend checks. The root cause is absent output escaping, allowing JavaScript for cookie theft or HTML for phishing when reflected in site info pages. Prerequisites include reaching the form; outcomes confirm storage for later execution.

## Requirements

1. Access to the Display Name field from prior steps
2. Knowledge of XSS/HTML payloads
3. Web browser developer tools for testing (optional)

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and HTML entity encoding on all user inputs
- Use Content Security Policy (CSP) to block inline scripts
- Scan stored data for malicious patterns before rendering

## Objectives

1. Store executable payloads without rejection
2. Enable credential theft via XSS
3. Facilitate phishing via HTML forms

## Instructions

### Step 1: Enter XSS Payload

**Context**: Input a script-executing payload to test for stored XSS.

No command required; manual form entry.

In the Display Name field, type: `"><img src=x onerror=javascript:alert(document.cookie)>` then submit the form to complete site creation.

> Payload breaks out of attributes and executes on render. Expected output: Site creates successfully; no errors on submission.

### Step 2: Enter HTML Injection Payload

**Context**: Input HTML to render interactive elements like forms.

No command required; manual form entry.

In the Display Name field, type: `<form action="/action_page.php"><label for="fname">First name:</label><input type="text" id="fname" name="fname"><br><br><label for="lname">Last name:</label><input type="text" id="lname" name="lname"><br><br><input type="submit" value="Submit"></form>` then submit.

> This renders a functional form. Expected output: Site creates; payload stored for display.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
