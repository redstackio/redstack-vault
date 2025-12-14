---
tags:
  - account-creation
  - setup
  - evernote
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.167Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f4d47646-3386-4d0c-bc80-1df5ea16a01f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create Test Accounts on Evernote

## Summary

This procedure registers new user accounts on Evernote to simulate attacker and victim roles in a CSRF testing scenario, enabling safe replication of the vulnerability without affecting real users.

## Description

In the context of testing the CSRF vulnerability in Evernote's account deactivation endpoint, creating disposable test accounts is essential. The attacker uses one account to capture legitimate requests, while the victim account tests the exploit's impact. This step requires no special tools and can be done via the standard Evernote registration flow. Expected outcomes include active accounts ready for login and navigation to sensitive endpoints.

## Requirements

1. Internet access to evernote.com
2. Valid email addresses for registration (use temporary emails if needed)
3. No prior Evernote account on the emails used

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from suspicious IPs
- Implement CAPTCHA on registration to deter automation

## Objectives

1. Establish attacker account for request capture
2. Create victim account for exploit validation
3. Ensure accounts are authenticated for session-based testing

## Instructions

### Step 1: Register Attacker Account

**Context**: Create the primary account used to interact with the deactivation page and capture requests.

No specific command; use the web interface:

1. Navigate to https://www.evernote.com/Signup.action
2. Enter email, password, and complete registration
3. Verify email and log in

> Successful registration redirects to the dashboard; check email for verification link.

### Step 2: Register Victim Account

**Context**: Create a secondary account to simulate the target of the CSRF attack.

Repeat the registration process with a different email:

1. Use https://www.evernote.com/Signup.action again
2. Provide distinct credentials
3. Verify and log in separately

> Both accounts should be premium-free for accurate testing; note credentials securely.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- setup
- evernote
