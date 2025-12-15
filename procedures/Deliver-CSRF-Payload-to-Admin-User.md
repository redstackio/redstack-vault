---
tags:
  - csrf
  - social-engineering
  - delivery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:18.690Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f9cfeac2-6f79-4059-9c42-2efc59976d74
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Deliver-CSRF-Payload-to-Admin-User

## Summary

This procedure involves hosting the CSRF PoC and tricking an authenticated WordPress admin into visiting the link, triggering the malicious registration and role escalation to bbp_keymaster.

## Description

With the admin logged in, visiting the PoC page causes the browser to submit the form in the context of their session, bypassing authentication checks. The bbp_profile_update_role() hook fires, assigning the role without nonces. The attacker then receives credentials via email for forum control.

## Requirements

1. Hosted CSRF PoC HTML
2. Contact method to send link to admin (email, chat)
3. Target admin with active session

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Implement site-wide CSRF tokens
- Log and alert on rapid user registrations

## Objectives

1. Induce admin to execute the CSRF
2. Complete registration with elevated role
3. Obtain and verify access credentials

## Instructions

### Step 1: Host the PoC Page

**Context**: Make the HTML accessible via URL.

**Instructions**: Use a web server like Python's http.server: python -m http.server 8000, access at http://attacker-ip:8000/poc.html.

> Expected output: Page loads with auto-submit.

### Step 2: Send Link to Admin

**Context**: Use social engineering to deliver the payload.

**Instructions**: Email or message: 'Check this forum update: http://attacker-ip:8000/poc.html'.

> Expected output: Admin clicks and visits.

### Step 3: Verify Exploitation

**Context**: Confirm registration and role assignment.

**Instructions**: Check attacker's email for credentials; log in to WordPress as new user and verify bbp_keymaster role in forum settings.

> Expected output: Login successful; full forum management access granted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- delivery
- phishing
- exploitation
