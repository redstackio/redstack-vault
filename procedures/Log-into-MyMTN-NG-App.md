---
tags:
  - authentication
  - mobile-app
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Mobile (iOS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.195Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 33b02ccb-a547-47c4-abe8-981db12e9e70
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-into-MyMTN-NG-App

## Summary

This procedure authenticates a user into the MyMTN NG mobile app using a valid MTN phone number, establishing a session for subsequent API interactions and enabling traffic interception.

## Description

The MyMTN NG app requires login via MSISDN (phone number) and typically an OTP for verification. This step gains initial access to user features like transaction history, which triggers API calls vulnerable to interception. It assumes the attacker has a legitimate MTN SIM for testing, but in a real attack, a compromised or test account suffices. Expected outcomes include a valid session token for API requests.

## Requirements

1. iOS device with MyMTN NG app installed from App Store
2. Valid MTN phone number (MSISDN starting with 2347 or 2348)
3. Network connectivity (mobile data or Wi-Fi)

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) beyond OTP for app logins
- Monitor for unusual login patterns from new devices or locations
- Rate-limit login attempts to prevent brute-force

## Objectives

1. Establish authenticated session in the app
2. Access user-specific sections to trigger API endpoints
3. Prepare for traffic interception without session invalidation

## Instructions

### Step 1: Install and Launch App

**Context**: Download and open the app to begin the login process.

No specific command; perform via App Store.

> Install MyMTN NG, launch it, and select 'Login' or 'Register' if new.

### Step 2: Enter Phone Number and Verify

**Context**: Provide MSISDN and complete OTP verification to authenticate.

No command; app-native process.

> Enter phone number (e.g., 2347032233323), receive and input OTP sent via SMS. Successful login redirects to dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- authentication
- mobile-app
