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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.836Z'
sub_techniques: []
id: 5977af73-1f30-4c4f-b0dc-6a58ff35684b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Recommendation-Description

## Summary

This procedure involves filling the recommendation form on Judge.me and inserting a malicious HTML payload into the product description field, exploiting poor sanitization to store executable JavaScript.

## Description

The attack targets the recommendation creation form in the user profile, where the description field allows HTML input without proper escaping. By using an <a> tag with a base64-encoded data URI, the procedure bypasses basic filters. Prerequisites include authenticated access. Outcomes: The payload is stored and rendered on the public profile, ready for execution on victim interaction.

## Requirements

1. Authenticated session in the user profile
2. Knowledge of base64 encoding for payload obfuscation
3. Web browser to input and preview the form

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding or allowlisting
- Use Content Security Policy (CSP) to block inline scripts and data URIs
- Log and scan form submissions for suspicious patterns like base64 strings

## Objectives

1. Insert unsanitized HTML into the description field
2. Ensure the payload renders as a clickable link
3. Prepare for persistence without form rejection

## Instructions

### Step 1: Open Recommendation Form

**Context**: Initiate the form to access input fields.

Click "Add Recommendation" in the profile section.

> The form loads with fields for product details and description.

### Step 2: Enter Payload

**Context**: Inject the malicious HTML in the description.

Fill product name, image, etc., then in description, enter: `<a href="data:text/html;charset=utf-7;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=">Click Here</a>`.

> The link appears clickable; base64 decodes to <script>alert('XSS')</script> on execution.

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
