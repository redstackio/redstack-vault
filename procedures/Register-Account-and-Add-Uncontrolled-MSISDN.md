---
id: proc-register-msisdn
tags:
  - account-setup
  - msisdn-addition
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.561Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-Account-and-Add-Uncontrolled-MSISDN

## Summary

This procedure outlines creating a new account on shop.mtn.ng and adding an uncontrolled Nigerian mobile number (MSISDN) to the profile, setting the stage for OTP bypass and account takeover.

## Description

The MTN Shop platform allows users to register or log in and manage account details, including mobile numbers. By adding a valid but uncontrolled MSISDN (e.g., a victim's number), the attacker triggers an OTP verification flow that can later be manipulated. This step requires no special tools, only browser access, and uses publicly available Nigerian numbers for testing.

## Requirements

1. Internet access to shop.mtn.ng
2. A valid Nigerian MSISDN (e.g., from numverify.com)
3. Basic browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account registrations and MSISDN additions
- Log and monitor unusual MSISDN inputs (e.g., non-owned numbers)
- Require initial verification for account creation

## Objectives

1. Establish attacker presence on the platform
2. Link a foreign MSISDN to enable takeover
3. Trigger OTP flow for subsequent bypass

## Instructions

### Step 1: Access Account Creation

**Context**: Navigate to the MTN Shop and initiate account setup.

Go to shop.mtn.ng, click the 'Account' icon, select 'Login/Signup', then 'Create an Account'.

> Expected: Registration form loads.

### Step 2: Fill Registration Details

**Context**: Input basic info and proceed to profile management.

Enter first name (e.g., Test), last name (e.g., User), email (e.g., test@example.com). Complete registration.

> Expected: Account created; redirect to dashboard.

### Step 3: Add Uncontrolled MSISDN

**Context**: Edit profile to insert the target MSISDN.

In 'Manage Account' > 'Edit', input MSISDN (e.g., +2348012345678) into 'Mobile Number' field and click 'Save'.

> Expected: Save triggers OTP prompt for the added number.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-setup
- msisdn-addition
