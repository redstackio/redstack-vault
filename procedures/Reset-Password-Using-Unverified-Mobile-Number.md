---
tags:
  - broken-authentication
  - account-takeover
  - password-reset
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
updated_at: '2025-12-14T17:30:58.796Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4a7484b1-b971-4a39-afb6-14ffced17480
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Password-Using-Unverified-Mobile-Number

## Summary

This procedure leverages the unverified mobile number association to bypass standard verification and perform an unauthorized password reset, resulting in account takeover.

## Description

On Twitter's forgot password page, the system allows selection of the loosely associated unverified number for reset code delivery without confirming its verified status from the addition step. An attacker controlling the number receives the code, enters it, and sets a new password. This targets the web-based password reset flow, requiring prior unverified number addition and logout. Expected outcome is full control over the account via new credentials.

## Requirements

1. Unverified mobile number associated from previous steps
2. Control over the mobile number for SMS receipt
3. Access to Twitter's forgot password page

## Defense

Defensive measures and detection strategies:

- Require full verification of mobile numbers before enabling them for resets
- Add delays or CAPTCHAs on reset attempts with recently added numbers
- Alert on password resets using unverified contact methods

## Objectives

1. Initiate password reset using the unverified number
2. Receive and validate the reset code
3. Gain persistent access via new password

## Instructions

### Step 1: Access Forgot Password

**Context**: Navigate to the reset interface and identify the target account.

Go to Twitter's login page, click "Forgot password?", and enter the target account's username or email.

### Step 2: Select Mobile Reset Option

**Context**: Choose the mobile number option and input the unverified number.

Select "Reset via phone", enter the previously added unverified mobile number, and request the code. The system sends an SMS to the controlled number without additional checks.

> A message confirms code delivery; no prior verification is enforced.

### Step 3: Complete Reset

**Context**: Use the received code to set a new password.

Enter the SMS code, proceed to the new password form, input a strong new password, and confirm. Log in with the new credentials to verify takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-authentication]]
- [[account-takeover]]
- [[password-reset]]
