---
tags:
  - idor
  - web
  - account-setup
type: procedure
tools:
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1c00e8ae-d1dc-4fea-a76b-dbde6e3a24e1
created_at: '2025-12-14T17:25:47.566Z'
updated_at: '2025-12-14T17:25:47.566Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Accounts-for-IDOR-Testing

## Summary

This procedure sets up test attacker and victim accounts in the MTN Group application to prepare for IDOR exploitation testing, ensuring isolated environments for demonstration without affecting real users.

## Description

In the context of testing the IDOR vulnerability in the user profile update functionality, creating separate test accounts allows simulation of an authenticated attacker targeting a victim. The application is accessed via https://mtnmobad.mtnbusiness.com.ng, and accounts are created through the registration flow. This step establishes the baseline for capturing requests and verifying modifications, with expected outcomes including successful logins and profile access.

## Requirements

1. Access to the MTN Group app login/registration page
2. Valid email addresses for test accounts (e.g., using temporary services like wearehackerone.com)
3. [[tools/Mozilla-Firefox]] browser for the initial session

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation to prevent abuse
- Monitor for unusual login patterns from test-like emails
- Use CAPTCHA on registration to deter automated account creation

## Objectives

1. Establish authenticated sessions for attacker and victim
2. Prepare for request interception without real user impact
3. Validate application access for subsequent steps

## Instructions

### Step 1: Access Registration and Create Accounts

**Context**: Navigate to the login/registration page to create test accounts.

No specific command; use browser UI.

> In [[tools/Mozilla-Firefox]], go to https://mtnmobad.mtnbusiness.com.ng/#/login1, select registration if available, or use existing test credentials. Create 'attacker' account first, then 'victim' account. Expected output: Confirmation emails or successful account setup.

### Step 2: Login to Attacker Account

**Context**: Authenticate as the attacker to confirm access.

No specific command; use browser UI.

> Enter attacker credentials at the login page. Expected output: Redirect to dashboard or profile page, confirming authenticated session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Mozilla-Firefox]]

## Tags

- [[idor]]
- [[web]]
- [[account-setup]]
