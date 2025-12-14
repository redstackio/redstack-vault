---
id: proc-view-email-letter-opener
tags:
  - xss-verification
  - email
  - letter-opener
type: procedure
tools:
  - '[[tools/Letter-Opener]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Email
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.768Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# View-Email-with-Letter-Opener-to-Verify-XSS

## Summary

This procedure uses the Letter Opener gem to intercept and view GitLab's generated emails in the browser, verifying the XSS execution from the malicious branch name.

## Description

In a development environment like GDK, Letter Opener prevents actual email sending and displays them via a web endpoint. Access the path `/rails/letter_opener/` after triggering the notification to see the HTML email with unsanitized branch name, confirming JS alert pops up. Ideal for safe testing without real recipients.

## Requirements

1. GitLab instance with Letter Opener gem installed (default in GDK).
2. Triggered email from previous steps.
3. Browser access to the instance.

## Defense

Defensive measures and detection strategies:

- N/A (testing tool); in prod, disable dev gems and monitor for email interception attempts.
- Validate email content before rendering in clients.

## Objectives

1. Inspect email HTML for unsanitized payload.
2. Confirm XSS execution (alert popup).
3. Validate vulnerability without real impact.

## Instructions

### Step 1: Access Letter Opener Endpoint

**Context**: View intercepted emails after MR submission.

Use browser:

- Navigate to `http://yourserver:3000/your-namespace/html5-boilerplate/rails/letter_opener/`.

> Lists recent emails, including the MR notification.

**Expected Output**: Email list; click the relevant one.

### Step 2: Inspect and Execute

**Context**: Open the email to trigger XSS.

- Click the MR email in the list.

> Renders HTML; `<script>alert(1)</script>` from branch name executes.

**Expected Output**: Alert dialog '1' appears in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Letter-Opener]]

## Tags

- verification
- email-inspection
- xss-test
