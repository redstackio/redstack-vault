---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
name: Inject-Blind-XSS-Payload-into-Review-Form
tags:
  - xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:55:38.079Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Inject-Blind-XSS-Payload-into-Review-Form

## Summary

This procedure involves submitting a crafted blind XSS payload into user-controllable form fields on a review ratings endpoint, which gets reflected unsanitized in an admin interface, enabling potential JavaScript execution upon admin viewing.

## Description

Blind XSS occurs when user input is reflected in a context not immediately visible to the attacker, such as an admin dashboard. Here, fields like Disliked_reviewers, Liked_reviewers, and Reasons in /reviews/ratings/{uuid} are targeted. The payload uses an image onerror handler with base64 encoding to evade detection and callback to an attacker server. This requires access to the public endpoint and a listening server for callbacks.

## Requirements

1. Access to the target endpoint (e.g., https://app.pullrequest.com/reviews/ratings/{uuid}/false)
2. Attacker-controlled domain for blind detection
3. Browser or automation tool for form submission

## Defense

Defensive measures and detection strategies:

- Encode all user input in admin views (e.g., HTML entity encoding)
- Implement Content Security Policy (CSP) to block inline scripts
- Log and monitor form submissions for suspicious payloads

## Objectives

1. Inject payload without immediate detection
2. Ensure reflection in privileged context
3. Prepare for execution trigger

## Instructions

### Step 1: Access Endpoint and Fill Form

**Context**: Navigate to the form and input the payload in vulnerable fields.

No command; manual or scripted form submission.

Payload example: `''"><img src=x id=alert(1) onerror=eval(atob(this.id))>'` (base64 'YWxlcnQoMSk=' for alert(1)).

> Submit the form; success if no validation errors occur.

### Step 2: Confirm Submission

**Context**: Verify the payload is stored server-side.

Refresh or check via another method if possible.

> Expected: No errors; payload persisted for admin view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
