---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - injection
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.356Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-BIO-Field

## Summary

This procedure injects a JavaScript-based XSS payload into the BIO field of a Khan Academy user profile, exploiting insufficient input validation to store malicious code for later execution.

## Description

In the context of the Khan Academy web application, the user profile BIO field accepts unsanitized input, allowing storage of HTML/JavaScript payloads. This step focuses on entering the payload without triggering immediate execution, setting up for deferred activation during subsequent profile interactions. The target environment is the authenticated profile editing page, with expected outcomes including successful payload acceptance and persistence in the form state.

## Requirements

1. Authenticated session on Khan Academy
2. Access to the profile editing interface
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Implement client-side and server-side input sanitization for profile fields using libraries like DOMPurify
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript alerts or DOM manipulations in user sessions

## Objectives

1. Store malicious JavaScript in the BIO field
2. Avoid immediate detection or execution
3. Prepare for trigger via form resubmission

## Instructions

### Step 1: Access Profile Editing

**Context**: Navigate to the page where profile details can be edited to reach the BIO input.

Open Khan Academy in your browser, log in, and go to the user profile settings (typically under account or settings menu). Locate the BIO text input field.

### Step 2: Enter Malicious Payload

**Context**: Input the crafted payload to bypass basic filters and store executable code.

In the BIO field, enter: `"><svg/onload=alert(document.domain);>"` or `"><svg/onload=alert(document.cookie);>`. This SVG-based payload evades some sanitization by mimicking HTML attributes.

> The payload uses onload to execute JavaScript, targeting domain or cookie data, but may result in 'undefined' due to context issues.

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
- [[injection]]
