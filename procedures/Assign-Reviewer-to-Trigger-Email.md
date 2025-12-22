---
id: proc-assign-reviewer-trigger-email
tags:
  - email-trigger
  - reviewer
  - xss
type: procedure
tools:
  - '[[tools/GDK-GitLab-Development-Kit]]'
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
updated_at: '2025-12-13T23:52:20.772Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Assign-Reviewer-to-Trigger-Email

## Summary

This procedure assigns a reviewer to a merge request in GitLab, triggering an email notification that renders the unsanitized branch name, executing the XSS payload in the recipient's client.

## Description

GitLab sends HTML emails for MR notifications (via `notify/new_merge_request_email.html.haml`), inserting branch names without sanitization at line 6. Assigning a maintainer as reviewer sends the email. Applies to CE/EE; also affects push emails and approver additions. Outcome: Email delivered with executable JS.

## Requirements

1. Created merge request with malicious branch.
2. List of target repo maintainers.
3. Email notifications enabled in GitLab.

## Defense

Defensive measures and detection strategies:

- Sanitize all user-supplied data in email templates (e.g., use Rails html_escape).
- Monitor email logs for suspicious HTML in subjects/bodies.
- Educate users on phishing risks in GitLab emails.

## Objectives

1. Trigger notification email containing payload.
2. Execute JS in reviewer's email client.
3. Demonstrate persistence and branding spoofing.

## Instructions

### Step 1: Select and Assign Reviewer

**Context**: Choose a target user to receive the malicious email.

Use GitLab UI on MR page:

- In the merge request, select a maintainer from the original repo as reviewer.
- Submit the assignment.

> This queues the email to the reviewer.

**Expected Output**: Assignment confirmation; email sent.

### Step 2: Verify Trigger

**Context**: Confirm email generation (use Letter Opener in test env).

- Check email delivery status in GitLab admin or logs.

> Ensures payload is in the email body.

**Expected Output**: Notification email logged or sent.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDK-GitLab-Development-Kit]]

## Tags

- email-notification
- reviewer-assignment
- trigger
