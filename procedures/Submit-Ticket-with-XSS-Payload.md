---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - xss
  - payload-injection
  - stored-xss
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.121Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Ticket-with-XSS-Payload

## Summary

This procedure submits a ticket through the SupportFlow form with a JavaScript payload in the message field, exploiting inadequate output escaping to store malicious code for later execution.

## Description

Targeting the SupportFlow plugin's ticket submission, this step injects a stored XSS payload like `<script>alert('XSS');</script>` into the message textarea. Input is sanitized via `sanitize_ticket_reply()` but not sufficiently for HTML contexts, allowing script tags to persist. This requires a logged-in user account and access to the embedded form page. The payload is stored in the database associated with the `sf_ticket` post type, setting up execution when admins view the list. Expected outcome is successful storage without immediate triggering.

## Requirements

1. Access to the embedded ticket form page
2. Logged-in WordPress user account
3. Knowledge of effective XSS payloads for the target context

## Defense

Defensive measures and detection strategies:

- Enhance input sanitization to strip script tags in `sanitize_ticket_reply()`
- Log and review ticket submissions for anomalous content
- Use WAF rules to block common XSS patterns in form posts

## Objectives

1. Inject and store unescaped JavaScript in ticket data
2. Bypass input validation for HTML/script content
3. Prepare for admin-context execution

## Instructions

### Step 1: Access Form Page

**Context**: Navigate to the published page containing the SupportFlow form.

Visit the URL of the page with `[supportflow_submissionform]`, ensuring you are logged in.

> The form should display fields including a message textarea.

### Step 2: Fill Form Fields

**Context**: Enter legitimate data in required fields to avoid validation failures.

Provide a subject like "Test Ticket" and your name/email, then paste `<script>alert('XSS');</script>` into the message field.

> Test simpler payloads if needed, but script tags target the output vulnerability.

### Step 3: Submit Ticket

**Context**: Send the form to store the payload in the database.

Click submit and confirm the ticket is created (e.g., via success message).

> The payload is now stored in the `sf_ticket` post meta, ready for admin viewing.

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
- javascript
- ticket-submission
