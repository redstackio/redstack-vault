---
id: proc-ato-login-001
tags:
  - account-takeover
  - login
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.646Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform-Account-Takeover-via-Login

## Summary

This final procedure demonstrates account takeover by logging into the victim's account using the attacker's email (now assigned to victim) and the attacker's password, gaining full unauthorized access.

## Description

After the IDOR exploit changes the victim's email to the attacker's, the login system authenticates based on email-password pairs. Using the attacker's credentials on the victim's original email effectively grants access to the victim's session and data.

## Requirements

1. Updated victim email (attacker's)
2. Attacker's password
3. Access to login page

## Defense

Defensive measures and detection strategies:

- Email change notifications to original owner
- Multi-factor authentication for logins
- Session binding to prevent takeover

## Objectives

1. Authenticate to victim's account post-exploit
2. Access victim-specific data
3. Confirm full control without victim interaction

## Instructions

### Step 1: Attempt Login with Hijacked Credentials

**Context**: Use the login form with victim's email but attacker's password.

Enter Email=victim@gmail.com (now redirected internally) and attacker's password.

> No command; web form submission.

### Step 2: Access Victim Dashboard

**Context**: Upon success, navigate to sensitive areas.

Explore My Account or other victim-only sections.

> Full access to victim's profile, history, and actions.

### Step 3: Validate Takeover

**Context**: Check for victim-specific indicators like unique data.

View profile to confirm email change and access.

> Success if no errors and data visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-takeover
- login
