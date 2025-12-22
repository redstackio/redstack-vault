---
tags:
  - xss
  - profile-update
  - storage
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-05T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.106Z'
sub_techniques: []
id: 4186580b-d6eb-40ed-bcec-9af93c12f5f5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Malicious-Profile-Changes

## Summary

This procedure submits the form with the injected XSS payload, storing it unsanitized on the Bridge CMS server for subsequent rendering and execution.

## Description

Upon submission, the PHP backend processes the display name input without adequate validation, persisting it to the database. The Twig template later outputs it in a way that allows script execution in vulnerable contexts like IE11. This step completes the storage phase of the stored XSS attack, relying on the root cause of improper sanitization.

## Requirements

1. Payload already entered in the display name field
2. Form submission capability (no CAPTCHA or rate limits)
3. Server acceptance of the input

## Defense

Defensive measures and detection strategies:

- Validate input length and content server-side before storage
- Use prepared statements or ORM for database inserts to prevent injection
- Audit Twig templates for safe rendering practices (avoid |raw)

## Objectives

1. Persist the malicious payload in the user profile
2. Confirm successful storage without errors
3. Enable rendering in views for execution

## Instructions

### Step 1: Submit the Form

**Context**: Trigger the update to save changes to the server.

Click the 'Update' or 'Save' button on the account form.

> The server responds with a success message; payload is now stored.

### Step 2: Verify Storage

**Context**: Reload the page to check if the display name reflects the payload.

Refresh https://bridge.cspr.ng/my/account.

> The custom display name appears altered, confirming storage.

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
- save
- persistence
