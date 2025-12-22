---
tags:
  - xss
  - injection
  - web
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
updated_at: '2025-12-14T03:16:37.468Z'
sub_techniques: []
id: 3b88c8b9-b50f-4d1b-85e7-a49a955c4ba1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Group-Name

## Summary

This procedure injects a malicious XSS payload into the group name field during project creation in Localize.io, exploiting insufficient input sanitization to store executable HTML/JavaScript.

## Description

The group creation feature fails to properly escape user-supplied names, allowing HTML tags and JavaScript to be injected. The payload uses an SVG object with a base64-encoded onload handler to execute JavaScript upon rendering. This targets the reflected/stored XSS in the rendering of group lists. Prerequisites include an authenticated session and access to the creation form. Outcomes include the payload being stored and ready for execution when the group is viewed.

## Requirements

1. Access to the project creation form
2. Knowledge of XSS payloads (e.g., SVG-based for bypassing filters)
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs, especially HTML contexts, using libraries like DOMPurify
- Validate input length and content (e.g., reject HTML tags in names)
- Implement output encoding when rendering user data

## Objectives

1. Submit payload without validation errors
2. Store the injectable content in the group name
3. Set up for JavaScript execution on render

## Instructions

### Step 1: Locate Group Name Field

**Context**: Identify the vulnerable input in the form.

In the project creation form, find the field labeled for group name or similar.

### Step 2: Enter and Submit Payload

**Context**: Craft and inject the malicious string.

Type or paste `<object data="data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoNCk+></object>` into the group name field. Fill any required fields and submit the form.

> Submission succeeds if no client-side validation blocks it. The group is created, storing the payload. Verify by checking the group list for the encoded name.

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
- [[web]]
