---
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:46:31.573Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: ba9c1b85-3a17-48fa-8889-6d51b23c1172
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Admin-Email-Field

## Summary

This procedure demonstrates injecting a malicious JavaScript payload into the admin email field of Revive Adserver, exploiting lack of input sanitization to store XSS for later execution.

## Description

In Revive Adserver, the Preferences > Change E-mail section fails to sanitize user input in the Email field. By appending a script tag to a valid email, the payload is stored in the database and later rendered unsafely on the Inventory > Admin Access page. This enables persistent XSS attacks targeting other admins, such as stealing session cookies or logging keystrokes. Prerequisites include admin access and a web browser like Firefox.

## Requirements

1. Valid admin credentials for the attacker account
2. Access to Revive Adserver instance via web browser
3. Knowledge of basic JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization for all user inputs, especially in admin panels
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for unusual admin email changes or JavaScript in logs

## Objectives

1. Store arbitrary JavaScript in the application backend
2. Prepare for cross-admin execution without direct access
3. Enable persistent attacks like session hijacking

## Instructions

### Step 1: Access Email Change Form

**Context**: Log in and navigate to the vulnerable form to input the payload.

No specific command; use the web interface in [[tools/Firefox]] to log in as admin and go to Preferences > Change E-mail.

> Expected: Form loads with Email address field visible.

### Step 2: Submit Malicious Payload

**Context**: Enter and save the payload to store it unsanitized.

In the Email field, input: `admin1@example.com<script>alert('xss');</script>`. Enter current password and submit.

> Expected: Form saves without errors; payload is now stored.

### Step 3: Verify Storage (Optional)

**Context**: Log out to simulate separation between attacker and victim sessions.

Log out after submission.

> Expected: Clean logout; payload persists in backend.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[stored-xss]]
