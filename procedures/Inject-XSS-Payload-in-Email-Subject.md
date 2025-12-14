---
id: proc-insightly-xss-inject-001
tags:
  - xss-injection
  - payload-delivery
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.892Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Email-Subject

## Summary

This procedure injects a malicious JavaScript payload into an Insightly email subject, leveraging the lack of sanitization to store executable code in notifications.

## Description

The email subject field in Insightly accepts user input without proper HTML/JS escaping. The payload uses an <img> tag with an onerror attribute to execute obfuscated JavaScript that captures and exfiltrates document.cookie when rendered.

## Requirements

1. Configured email service in Insightly
2. Access to email creation interface
3. Attacker-controlled endpoint for cookie exfiltration (e.g., a webhook URL)

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs in subjects with HTML entity encoding
- Implement Content Security Policy (CSP) to block inline scripts
- Scan stored content for common XSS patterns

## Objectives

1. Store malicious script in shared notifications
2. Ensure payload executes on render without errors
3. Enable cookie theft for session compromise

## Instructions

### Step 1: Create New Email

**Context**: Open the email composition interface.

In Insightly, navigate to Emails > New Email.

### Step 2: Enter Malicious Subject

**Context**: Inject the payload directly.

In the subject field, input: `<img src="X" onerror="top[8680439..toString(30)](1337+document.cookie)">`. This obfuscates the exfiltration (e.g., appends cookies to a URL).

### Step 3: Save and Send

**Context**: Persist the email to trigger storage.

Leave body empty if desired, then save or send to a test contact. The subject is now stored in notifications.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]

