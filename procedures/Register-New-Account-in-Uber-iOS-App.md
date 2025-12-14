---
id: proc-uuid-1
tags:
  - account-creation
  - initial-access
  - mobile
  - uber
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:24:42.839Z'
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
# Register New Account in Uber iOS App

## Summary

This procedure outlines the creation of a new user account in the Uber iOS app, which serves as the initial access point for exploiting the promo code redemption vulnerability by providing a clean slate for testing without account history restrictions.

## Description

In the context of the Uber promo code enumeration attack, registering a new account is essential to immediately access the redemption feature post-signup. The app's registration process involves providing basic user details and verification, after which the vulnerable endpoint becomes accessible. This step ensures no prior rate limiting or usage patterns interfere with brute force attempts. Expected outcomes include a fully functional account ready for the next stages, with no technical barriers encountered.

## Requirements

1. Uber iOS app installed on an iPhone or simulator (version compatible with the vulnerability, e.g., pre-2016 patches)
2. Valid email address and phone number for verification
3. Internet connectivity for API calls during registration

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification delays on new registrations to slow automated account creation
- Monitor for unusual signup patterns from single IP addresses
- Rate limit registration attempts per device or IP

## Objectives

1. Gain initial access to Uber app services as a legitimate user
2. Enable access to promo code functionality without prerequisites
3. Prepare for subsequent brute force testing

## Instructions

### Step 1: Launch App and Start Registration

**Context**: Open the app to initiate the signup process, ensuring no existing account interferes.

No specific command; interact via UI:

- Tap "Sign Up" on the welcome screen.
- Enter email, phone, and password.

> The app submits details to the backend API. Expected output: Verification code sent via email/SMS.

### Step 2: Verify and Complete Signup

**Context**: Confirm identity to finalize account creation.

No specific command; interact via UI:

- Enter the received verification code.
- Provide additional details if prompted (e.g., name, location).
- Agree to terms and complete.

> Successful completion loads the dashboard. Expected output: Welcome message and account overview.

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
- initial-access
- mobile
