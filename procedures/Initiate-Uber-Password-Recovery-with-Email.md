---
tags:
  - xss
  - web
  - uber
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:47.279Z'
sub_techniques: []
id: 84f2e5a2-0a94-4e66-a8d6-c8a2fa34b466
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Uber-Password-Recovery-with-Email

## Summary

This procedure submits a valid email to Uber's forgot password form, triggering a recovery link email and advancing the self-XSS exploitation chain.

## Description

Targeting Uber's web app, enter and submit an email linked to an account. This step relies on the recovery mechanism sending a link without validating user intent. Prerequisites include a registered Uber email. Outcome: Email delivery confirmation on the page.

## Requirements

1. Valid email address tied to an Uber account
2. Access to the forgot password page
3. Email client to receive the link

## Defense

Defensive measures and detection strategies:

- Email verification delays to slow automation
- Logging of recovery requests for anomaly detection

## Objectives

1. Request password reset for the target account
2. Receive the recovery email
3. Validate the flow proceeds to link opening

## Instructions

### Step 1: Submit Email Form

**Context**: Fill and submit the email field to initiate recovery.

No command; interact with the form:

```plaintext
Enter email: user@example.com
Click Submit
```

> Success shows a message like 'Check your email'. Monitor inbox.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[uber]]
