---
tags:
  - mfa
  - activation
  - security-settings
  - web
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.468Z'
sub_techniques: []
id: ff028498-bd4f-4a5f-9104-008524e2fa3c
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Activate-MFA-on-One-Device

## Summary

This procedure enables Multi-Factor Authentication (2FA) on the target account via the security settings, intended to enhance security but revealing a flaw in session management.

## Description

Targeting https://account.grammarly.com/security, this step involves navigating to the security page on device A, selecting the 2FA option, and completing setup (e.g., scanning a QR code with an authenticator app). The process should ideally invalidate all existing sessions, but in this vulnerability, it does not, allowing bypass. Prerequisites include an active session and no prior MFA.

## Requirements

1. Active session on device A.
2. Authenticator app installed (e.g., Google Authenticator).
3. Account with admin privileges for security changes.

## Defense

Defensive measures and detection strategies:

- Force session invalidation upon MFA enablement via server-side token revocation.
- Log and alert on MFA activation events, cross-referencing active sessions.

## Objectives

1. Enable 2FA to simulate a security hardening action.
2. Observe lack of session termination on other devices.
3. Confirm vulnerability in authentication process.

## Instructions

### Step 1: Navigate to Security Settings

**Context**: Access the page where MFA can be configured.

From the account dashboard on device A, click on the security or settings link to reach https://account.grammarly.com/security.

> The page loads with options for authentication methods.

### Step 2: Enable 2FA

**Context**: Complete the full activation process.

Select the 2FA option, follow prompts to generate and scan a QR code, enter a verification code from the app, and confirm setup.

> A success message appears, and future logins require 2FA codes, but existing sessions persist.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[mfa]]
- [[activation]]
- [[security-settings]]
- [[web]]
