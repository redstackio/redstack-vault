---
id: uuid-1
tags:
  - account-setup
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile App
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.251Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate Initial QR Code and Password in BCM Messenger

## Summary

This procedure sets up a BCM Messenger account by registering or accessing it and generating the initial QR code (containing a private key) and password for authentication, establishing the baseline credentials needed for subsequent exploitation.

## Description

In BCM Messenger, authentication relies on a combination of a password and a QR code that embeds a private key. This step involves creating or logging into an account to obtain these credentials. The QR code is scanned during login to load the private key locally. This is a prerequisite for testing the vulnerability where old credentials persist after changes. The target environment is the BCM Messenger mobile app or web interface, requiring standard internet access and no prior privileges.

## Requirements

1. BCM Messenger app installed on mobile or access to web version
2. Valid email or phone for account registration
3. Device capable of scanning QR codes (for mobile)

## Defense

Defensive measures and detection strategies:

- Enforce strong password policies during registration
- Monitor for unusual account creation patterns
- Use device binding to prevent credential sharing

## Objectives

1. Obtain functional initial credentials for the account
2. Verify QR code authentication mechanism
3. Prepare for password change testing

## Instructions

### Step 1: Register or Access Account

**Context**: Create a new account or log in to an existing one to initiate the authentication flow.

Open the BCM Messenger app or web client and follow the registration prompts to provide an email/phone and set an initial password. If accessing an existing account, use known credentials.

> Upon successful registration or login initiation, the app prompts for QR code setup.

### Step 2: Generate and Scan QR Code

**Context**: Generate the QR code containing the private key and complete authentication.

The app displays a QR code during the login process. Scan it using the app's built-in scanner or a secondary device to load the private key locally. Enter the password to finalize authentication.

> Successful scan and password entry grants access to the account dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-setup]]
- [[authentication]]
