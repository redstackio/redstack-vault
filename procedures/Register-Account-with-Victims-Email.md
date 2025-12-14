---
tags:
  - broken-access-control
  - account-registration
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:44.456Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a0b5e213-6fd5-489c-851b-3949664b429c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Register-Account-with-Victims-Email

## Summary

This procedure exploits the lack of email validation during WakaTime account registration, allowing an attacker to create an account using a victim's email address without ownership verification.

## Description

In the WakaTime platform, the account creation endpoint permits registration with any email, even if it's already associated or in use, due to broken access control. This enables impersonation from the outset, setting the stage for API key generation and activity manipulation. The attack targets the web-based registration form, requiring only the victim's email and fabricated details. Expected outcomes include immediate dashboard access, highlighting the absence of email confirmation steps.

## Requirements

1. Victim's email address
2. Web browser with access to waketime.com
3. No authentication prerequisites

## Defense

Defensive measures and detection strategies:

- Implement email verification via one-time codes during registration
- Rate-limit registration attempts per email to prevent brute-forcing
- Log and alert on duplicate email registrations

## Objectives

1. Gain initial unauthorized access to a victim-associated account
2. Establish a foothold for API key issuance
3. Enable subsequent impersonation without victim awareness

## Instructions

### Step 1: Access Registration Endpoint

**Context**: Navigate to the public registration page to initiate the exploit.

No specific command required; use a web browser to visit https://waketime.com/signup and fill the form with the victim's email, a chosen username, and password.

> The form submission bypasses email uniqueness checks, creating the account instantly.

### Step 2: Confirm Account Creation

**Context**: Verify successful registration by attempting login.

Log in using the submitted credentials at https://waketime.com/signin.

> Successful login indicates the account is active, with no verification email sent or required.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-access-control]]
- [[account-takeover]]
