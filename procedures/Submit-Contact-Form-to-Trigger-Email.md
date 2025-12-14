---
id: uuid-3
tags:
  - form-submit
  - email-trigger
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
updated_at: '2025-12-14T17:27:50.055Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Contact-Form-to-Trigger-Email

## Summary

This procedure submits the tainted contact form, causing the server to process the input and send a confirmation email with the reflected XSS payload.

## Description

Upon submission, the server includes the unsanitized user inputs directly in the email HTML body, creating a vector for XSS when the recipient views the source.

## Requirements

1. Completed form with payload
2. Server-side form handler active
3. Email delivery service operational

## Defense

Defensive measures and detection strategies:

- Escape HTML in email templates
- Use Content Security Policy (CSP) if emails are rendered in browsers
- Rate-limit form submissions

## Objectives

1. Trigger email generation with payload
2. Ensure delivery to controlled inbox
3. Confirm reflection without alteration

## Instructions

### Step 1: Initiate Submission

**Context**: Click the submit button to send data to the server.

No command; manual action.

> Locate and click the "Submit" or "Send" button on the form. Watch for any success message.

### Step 2: Monitor for Confirmation

**Context**: Verify submission was accepted.

Check page response.

> The page may display a thank-you message; if errors occur, adjust payload and retry.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[submission]]
- [[email]]
