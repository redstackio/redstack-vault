---
id: proc-block-registration
tags:
  - account-squatting
  - denial-of-service
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.481Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Block-Victim-Email-Registration

## Summary

This procedure demonstrates the side effect of the bypass by squatting the victim's email, preventing them from registering a legitimate account as the system flags it as already in use.

## Description

After email hijacking, the victim's attempt to sign up fails because the email is now tied to the attacker's session. This improper authentication lacks checks for dormant or hijacked emails, leading to denial of service and loss of trust. The scenario targets the registration endpoint in a web context, with outcomes including blocked access for the victim.

## Requirements

1. Victim's email already changed to in the attacker's account
2. Victim's perspective: Attempt normal signup
3. Access to https://www.drugs.com/account/register/

## Defense

Defensive measures and detection strategies:

- Implement email recovery flows with proof of ownership
- Allow email unclaiming after inactivity or via support
- Verify email availability beyond simple database checks

## Objectives

1. Deny legitimate account creation for the victim
2. Highlight squatting risks from the bypass
3. Amplify impact through DoS

## Instructions

### Step 1: Simulate Victim Signup

**Context**: Test from victim's viewpoint to confirm block.

Have the victim (or simulate) navigate to https://www.drugs.com/account/register/ and enter their email in the form.

### Step 2: Submit and Observe Error

**Context**: Trigger the registration check.

Submit the form; no OTP is sent as the email appears registered.

**Expected Output**: Error message: "This email is already in use. Please log in or use a different email."

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-squatting]]
- [[denial-of-service]]
- [[impersonation]]
