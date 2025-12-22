---
id: a23b35a7-99b9-45f7-a15b-d8c4c8ff8a7a
name: Bypass-Email-Verification-via-Back-Navigation
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:41.707Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - auth-bypass
  - mobile-security
  - email-verification
commands: []
platforms:
  - Android
  - iOS
  - Mobile
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Bypass-Email-Verification-via-Back-Navigation

## Summary

This procedure exploits a flaw in the Coinbase mobile app's signup flow on Android and iOS, allowing attackers to bypass email verification by using the back button to return to the login screen without completing the confirmation step, resulting in unverified account creation and access.

## Description

In the Coinbase app, the signup process requires email verification to confirm ownership, but the navigation logic fails to enforce this step. By initiating signup, reaching the verification prompt, and then backing out to login, an attacker can log in directly with the provided credentials. This violates secure design principles for authentication, enabling spoofed account creation for potential abuse like fraud or platform manipulation. The vulnerability affects both Android and iOS versions, discovered via manual testing of the app's UI flow.

## Requirements

1. Installed Coinbase mobile app (Android or iOS)
2. A test email address (for ethical testing; avoid production abuse)
3. Mobile device with internet access
4. No special permissions or root access needed

## Defense

Defensive measures and detection strategies:

- Enforce verification completion before allowing login or access to features
- Implement state management to block navigation away from incomplete flows
- Monitor for rapid account creations from the same IP or device
- Add client-side checks to prevent back navigation during sensitive steps

## Objectives

1. Create an account without verifying email ownership
2. Gain access to account features immediately
3. Demonstrate potential for account spoofing and abuse

## Instructions

### Step 1: Start Signup Process

**Context**: Initiate account creation to generate credentials and trigger the verification flow.

Open the Coinbase app, navigate to signup, and enter an email address and password.

> The app sends a confirmation email but displays a prompt to open it.

### Step 2: Reach Verification Prompt

**Context**: Arrive at the screen requiring email confirmation, which is the point of bypass.

The app shows a message indicating a verification email was sent and must be confirmed to proceed.

> Do not open the email; this sets up the navigation exploit.

### Step 3: Back Out to Login Screen

**Context**: Use device navigation to escape the verification enforcement.

Press the device's back button to return to the login screen.

> The app allows this without resetting or enforcing the pending verification.

### Step 4: Log In with New Credentials

**Context**: Access the account directly, confirming the bypass.

Enter the email and password from signup on the login form and submit.

> Successful login grants access without further prompts.

### Step 5: Verify Access

**Context**: Confirm unverified account functionality.

Navigate to account features; no verification should be requested.

> This indicates the bypass worked, allowing full use of the spoofed account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[mobile-security]]
- [[email-verification]]
