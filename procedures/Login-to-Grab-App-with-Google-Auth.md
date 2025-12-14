---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - authentication
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
updated_at: '2025-12-14T17:31:42.923Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Grab-App-with-Google-Auth

## Summary

This procedure establishes an authenticated session in the Grab Android app using Google authentication, which correctly implements 2FA but exposes a vulnerable flow for subsequent profile changes.

## Description

In the context of testing the Grab app's profile editing vulnerability, log in using Google OAuth with a valid phone number. This step creates a session token that can be used for authenticated API calls, setting up the attack without triggering the full 2FA during login but allowing OTP for profile edits. The target environment is an Android emulator for controlled testing.

## Requirements

1. Nox App Player installed and running
2. Valid Google account with phone number
3. Grab app downloaded from Play Store

## Defense

Defensive measures and detection strategies:

- Monitor for unusual login patterns from emulators
- Enforce device fingerprinting to detect proxy usage

## Objectives

1. Gain initial authenticated access to the app
2. Obtain session for profile edit flow
3. Set up for OTP trigger

## Instructions

### Step 1: Launch App in Emulator

**Context**: Start the Grab app in a controlled Android environment.

Install and open the Grab app via [[tools/Nox-App-Player]].

### Step 2: Perform Google Login

**Context**: Use Google auth to bypass direct 2FA during login.

Select Google login option and authenticate with a phone-linked account.

**Expected Output**: Dashboard access with session established.

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

- authentication
- android
