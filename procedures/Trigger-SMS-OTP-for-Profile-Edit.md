---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - 2fa
  - otp
  - android
type: procedure
tools:
  - '[[tools/Grab-Android-App]]'
  - '[[tools/Nox-App-Player]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.920Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Trigger-SMS-OTP-for-Profile-Edit

## Summary

This procedure initiates a profile edit in the Grab app to trigger the sending of a 4-digit SMS OTP, exposing the vulnerable confirmation endpoint.

## Description

After login, navigate to profile settings and attempt to change the name or phone number. Saving triggers an API request to send the OTP via SMS to the registered number. The app requires the code for confirmation, but the endpoint lacks protections, allowing later brute-force.

## Requirements

1. Active session from Google login
2. Access to phone receiving SMS
3. Emulator with app running

## Defense

Defensive measures and detection strategies:

- Implement OTP expiration after 5 minutes
- Rate limit OTP verification attempts per session

## Objectives

1. Send 4-digit OTP via SMS
2. Prepare for code brute-force
3. Identify vulnerable endpoint

## Instructions

### Step 1: Access Profile Settings

**Context**: Locate the edit option in the app.

Go to user profile and select edit name or phone.

### Step 2: Submit Edit to Trigger OTP

**Context**: Initiate the SMS send.

Enter changes and press Save; monitor for SMS arrival.

**Expected Output**: 4-digit code received via SMS.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Grab-Android-App]]
- [[tools/Nox-App-Player]]

## Tags

- 2fa
- otp
- android
