---
tags:
  - xss
  - stored-xss
  - javascript
  - weblate
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
updated_at: '2025-12-14T03:15:47.096Z'
sub_techniques: []
id: 36534ad0-9777-4ab8-8a6d-beed2433a71b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject JavaScript Payload in Editor Link

## Summary

This procedure details the injection of a JavaScript payload into Weblate's Editor Link field, exploiting the lack of validation to store a malicious javascript: URI for later self-XSS execution.

## Description

The Editor Link field in Weblate preferences accepts arbitrary input, including custom schemes like javascript:, which are persisted in the user's profile. This stored payload is retrieved and used when constructing links to source files on translation pages. The attack requires an authenticated session and results in the payload being saved without sanitization, leading to execution upon trigger.

## Requirements

1. Access to the preferences page with Editor Link field visible
2. Knowledge of a simple JavaScript payload (e.g., confirm dialog)
3. Ability to save profile changes

## Defense

Defensive measures and detection strategies:

- Enforce URL scheme whitelisting (e.g., only http/https allowed)
- Sanitize inputs with libraries like DOMPurify to strip script tags and schemes
- Monitor for unusual payloads in audit logs

## Objectives

1. Store unsanitized JavaScript URI in the backend
2. Confirm persistence without errors
3. Set up for self-XSS trigger in user context

## Instructions

### Step 1: Enter Payload

**Context**: Populate the field with a javascript: URI to test execution capabilities.

In the Editor Link input field, type `javascript:confirm(document.domain)`.

> This payload, when executed, will display a confirmation dialog with the current domain, verifying XSS.

### Step 2: Save Changes

**Context**: Persist the payload in the user's profile.

Click the save button on the preferences form.

> If successful, the page reloads without errors, and the payload remains in the field, indicating storage.

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
- stored-xss
- javascript
- injection
