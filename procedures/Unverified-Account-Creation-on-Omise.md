---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Unverified-Account-Creation-on-Omise
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.094Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Create Account]]'
sub_techniques: []
tags:
  - broken-access-control
  - account-creation
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Create Account]]'
---

# Unverified-Account-Creation-on-Omise

## Summary

This procedure exploits the absence of email verification in the Omise dashboard signup process to create an account using any email address, including a victim's, allowing immediate login and control without ownership confirmation.

## Description

In the context of the Omise payment platform's web dashboard at https://dashboard.omise.co/, the registration flow permits users to sign up with arbitrary email addresses. No verification email is sent or required, enabling attackers to associate fraudulent accounts with legitimate user emails. This sets the stage for further account manipulation, such as enabling 2FA, leading to denial of service for the real owner. The procedure requires only a web browser and knowledge of the target email; it targets web-based broken access control vulnerabilities.

## Requirements

1. Web browser with internet access
2. Knowledge of the victim's email address
3. No prior authentication or special permissions needed

## Defense

Defensive measures and detection strategies:

- Implement mandatory email verification during signup with time-bound tokens
- Require proof of email ownership (e.g., OTP) before enabling security features like 2FA
- Monitor for multiple signup attempts with the same email and flag suspicious activity

## Objectives

1. Gain initial access to an account tied to the victim's email
2. Establish a foothold for subsequent persistence mechanisms
3. Disrupt legitimate user access by pre-empting account creation

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Access the Omise dashboard registration endpoint to begin the unverified signup process.

Open a web browser and go to https://dashboard.omise.co/. Click on the signup or register button to load the account creation form.

### Step 2: Submit Signup Form

**Context**: Enter the victim's details to create the account without triggering verification.

Fill in the form with the victim's email address, a fabricated username, and a strong password. Submit the form. The account is created instantly, allowing immediate login.

> No command is executed; this is a manual web form submission. Expected output: Redirect to login or dashboard with success message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Create Account]] Create Account

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-access-control]]
- [[account-creation]]
