---
id: proc-setup-accounts-001
tags:
  - account-creation
  - setup
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:33:06.658Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Setup-Attacker-and-Victim-Accounts

## Summary

This procedure establishes the necessary accounts for testing and exploiting the IDOR vulnerability by registering an attacker account and a victim account on the target web application.

## Description

In the context of an ASP.NET Core web app with user registration, create two distinct accounts to simulate attacker and victim roles. This allows the attacker to authenticate and perform profile updates while targeting the victim's profile. No special privileges are needed, but valid email addresses are required for registration.

## Requirements

1. Access to the target application's registration page (e.g., https://target.com/register)
2. Valid, unique email addresses for attacker and victim
3. Browser for manual registration

## Defense

Defensive measures and detection strategies:

- Rate-limit registration attempts to prevent abuse
- Monitor for multiple registrations from the same IP
- Require email verification during signup

## Objectives

1. Create authenticated attacker account for request interception
2. Establish victim account with known email for targeting
3. Verify login functionality for both accounts

## Instructions

### Step 1: Register Attacker Account

**Context**: Navigate to the registration page and create the attacker's account using a controlled email.

No command required; use the web form to register with Email=attacker@gmail.com, choose a strong password, and complete any CAPTCHA or verification.

> Successful registration redirects to login or dashboard.

### Step 2: Register Victim Account

**Context**: Repeat registration for the victim using a different email to simulate a target user.

Use the web form with Email=victim@gmail.com and a known password for later testing.

> Registration success confirms victim account creation.

### Step 3: Verify Logins

**Context**: Test authentication for both accounts to ensure they are active.

Login separately with each set of credentials.

> Dashboard access indicates successful setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- setup
