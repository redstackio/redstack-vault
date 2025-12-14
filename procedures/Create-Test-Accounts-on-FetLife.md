---
tags:
  - account-creation
  - testing
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
updated_at: '2025-12-14T17:30:27.156Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[T1133.001]]'
id: db9c29e4-e5fe-49a7-8ef4-29bea05d52a2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Test-Accounts-on-FetLife

## Summary

This procedure involves registering multiple test accounts on FetLife to simulate attacker and victim roles in vulnerability testing, such as privacy bypass scenarios.

## Description

FetLife allows free account creation via email and basic profile info. For testing information disclosure, one account creates the private event (victim), while another accesses it without permission (attacker). Use distinct emails to avoid conflicts. This setup is essential for reproducing the vulnerability without affecting real users.

## Requirements

1. Valid email addresses for registration
2. Access to fetlife.com signup page
3. Compliance with platform terms for testing accounts

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification to limit bulk account creation
- Rate-limit registrations and monitor for suspicious patterns
- Use device fingerprinting to detect multi-account usage from single IPs

## Objectives

1. Establish isolated personas for attack simulation
2. Ensure accounts have necessary permissions for event creation and viewing
3. Prepare for controlled testing of privacy features

## Instructions

### Step 1: Navigate to Signup

**Context**: Begin account creation process.

Visit https://fetlife.com/signup in browser.

> Fill in username, email, password, and birthday. Expected: Account created and login prompt.

### Step 2: Create Attacker Account

**Context**: Register the first account for unauthorized access.

Use details like username 'Ezzra1', a disposable email.

> Log in to verify. Expected: Dashboard access confirmed.

### Step 3: Create Victim Account

**Context**: Register second account for event hosting.

Repeat signup with 'Ezzra2' and another email.

> Log in and complete profile if needed. Expected: Ready for event creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques

- [[T1133.001]] Web Portal

## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[testing]]
