---
id: e134d976-6551-4fec-bd9f-08d28307391d
name: Manipulate-Email-Parameter-for-Account-Takeover
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.515Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - parameter-manipulation
  - bypass
  - account-takeover
  - web
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---

# Manipulate-Email-Parameter-for-Account-Takeover

## Summary

This procedure exploits the broken authentication by modifying the 'email' URL parameter to gain unauthorized access to another user's DoD account, leading to PII disclosure and potential takeover.

## Description

The vulnerability stems from the application's failure to validate session ownership or require credentials when the email parameter is altered to a valid existing email. In a DoD web app context, this allows attackers to impersonate users after initial login. Prerequisites include a captured URL from authentication. Outcomes: Direct access to target data without verification, exposing names, surnames, and SSNs.

## Requirements

1. Captured URL with email parameter from login
2. List of target DoD emails (e.g., from reconnaissance)
3. Web browser or [[tools/Burp-Suite]] for manipulation/fuzzing

## Defense

Defensive measures and detection strategies:

- Server-side authorization checks tying sessions to user IDs, not emails
- Parameter sanitization and validation on redirects
- Logging and alerting on URL parameter changes matching different emails

## Objectives

1. Bypass authentication for target account
2. Disclose sensitive PII
3. Achieve effective account takeover

## Instructions

### Step 1: Edit URL Parameter

**Context**: Change the email to a target user's valid email.

In the browser address bar, replace the email value (e.g., change 'your-email@domain.com' to 'ag3nt-z3@███'). Press Enter to reload.

> The page loads as the target user without prompts.

### Step 2: Fuzz for Valid Emails (Optional)

**Context**: Use Burp to identify valid emails if unknown.

Configure [[tools/Burp-Suite]] Intruder: Set the email parameter as payload position, load a wordlist of DoD emails, and attack the URL.

> Responses with 200 OK and user data indicate valid emails.

### Step 3: Access Disclosed Data

**Context**: View the unauthorized information.

Once loaded, inspect the profile or dashboard for PII like name, surname, and SSNs.

> Sensitive data is visible, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[parameter-manipulation]]
- [[bypass]]
- [[account-takeover]]
- [[web]]
