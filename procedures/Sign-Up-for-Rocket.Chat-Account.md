---
tags:
  - account-creation
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 14034966-1ed4-40a8-a8df-a7a1d900fcfc
created_at: '2025-12-14T17:24:47.913Z'
updated_at: '2025-12-14T17:24:47.913Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Sign-Up-for-Rocket.Chat-Account

## Summary

This procedure creates a new user account on a Rocket.Chat instance, establishing the foundation for testing authentication vulnerabilities like 2FA bypass.

## Description

In the context of exploiting Rocket.Chat's email verification flaw, signing up simulates the victim's account setup. The process involves providing an email address and basic details on the public-facing signup page (e.g., open.rocket.chat). No special privileges are required, but access to the email is needed for verification. Expected outcome: A functional account ready for 2FA enablement.

## Requirements

1. Web browser with internet access
2. Valid email address under attacker control
3. Target Rocket.Chat instance accessible

## Defense

Defensive measures and detection strategies:

- Enforce CAPTCHA on signup to prevent automated account creation
- Monitor for unusual signup patterns from suspicious IPs
- Require admin approval for new accounts in self-hosted instances

## Objectives

1. Gain initial account presence on the target platform
2. Prepare for subsequent authentication testing
3. Validate email delivery for verification flows

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Access the public registration endpoint to begin account creation.

No command required; use browser to visit https://open.rocket.chat/signup or equivalent.

> Fill in username, password, and email fields. Submit the form.

### Step 2: Verify Email if Prompted

**Context**: Complete any initial email verification to activate the account.

Click the verification link sent to the provided email.

> Expected output: Account activation confirmation and redirect to login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[rocket-chat]]
