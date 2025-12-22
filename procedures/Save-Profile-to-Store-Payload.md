---
tags:
  - profile-save
  - payload-storage
  - stored-xss
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
updated_at: '2025-12-14T03:15:26.673Z'
sub_techniques: []
id: 0d6c1ff8-8be1-42f2-b700-26f8864deffb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Profile-to-Store-Payload

## Summary

This procedure submits the profile form to store the injected XSS payload server-side in the Uber Partners database.

## Description

Submitting the form persists the unsanitized VAT number input, making it a stored XSS. Upon profile view, the payload renders and executes in the browser. This is limited to self-exploitation. The technical approach relies on the lack of server-side validation. Prerequisites: Payload injected in the form.

## Requirements

1. Modified profile form with payload
2. Active session to submit changes
3. No form validation blocking submission

## Defense

Defensive measures and detection strategies:

- Server-side input validation and sanitization before storage
- Audit logs for profile updates containing suspicious strings (e.g., <script>)
- Escape outputs when rendering stored data in HTML

## Objectives

1. Persist the payload in the user's profile
2. Enable execution on profile view
3. Confirm storage without data loss

## Instructions

### Step 1: Review Form Changes

**Context**: Verify the payload is in place before submission.

No command required; inspect the VAT field to ensure the full payload is present.

> Look for the alert(0) script tag.

### Step 2: Submit the Form

**Context**: Save the changes to store the payload.

No command required; click the 'Save' or 'Update Profile' button at the bottom of the form.

> Success shows a confirmation; the payload is now stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- profile-save
- payload-storage
