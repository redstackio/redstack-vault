---
id: 123e4567-e89b-12d3-a456-426614174003
name: Inject-XSS-Payload-into-Name-and-Description
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:26.696Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - injection
  - payload
  - web
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-XSS-Payload-into-Name-and-Description

## Summary

This procedure injects a stored XSS payload into the Name and Description fields of the Veris add member form, exploiting lack of sanitization to store executable JavaScript in the backend.

## Description

The Veris Member Book form accepts user input in Name and Description without proper escaping, allowing HTML and JavaScript tags to be stored. The payload `<svg onload=alert(1)>` uses an SVG element with an onload handler to execute JavaScript upon rendering. Submission stores the payload, which executes when any user (including the attacker) views the members page or related features. This enables arbitrary code execution in the victim's browser context, potentially stealing cookies or session data.

## Requirements

1. Loaded add member form with accessible input fields
2. Authenticated session to submit the form
3. Knowledge of effective XSS payloads for the target

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs using libraries like DOMPurify or server-side HTML encoding
- Implement Content Security Policy (CSP) to restrict inline script execution
- Validate input lengths and content types on submission
- Monitor for suspicious payloads in logs

## Objectives

1. Bypass input validation to store malicious script
2. Persist the payload in the database or storage
3. Set up for execution on subsequent page views

## Instructions

### Step 1: Enter Payload in Fields

**Context**: Fill the vulnerable inputs with the XSS vector.

In the Name field, type: `<svg onload=alert(1)>`
In the Description field, type the same: `<svg onload=alert(1)>`

> Ensure no client-side validation blocks the input; if it does, try variations like URL encoding.

### Step 2: Submit the Form

**Context**: Persist the payload to the backend.

Click the 'Submit' or 'Add Member' button to save the new member.

> The form should submit successfully, adding the member to the list without errors. Inspect the response in browser dev tools for successful POST to the members endpoint.

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
- [[payload]]
- [[web]]
