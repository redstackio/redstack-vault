---
id: proc-create-account-trust
tags:
  - account-creation
  - device-trust
  - 2fa-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.491Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Attacker-Account-with-Device-Trust

## Summary

This procedure sets up an attacker-controlled account on Drugs.com with device trust enabled, creating a persistent session that skips 2FA for one month and forms the foundation for subsequent impersonation attacks.

## Description

In the context of exploiting Drugs.com's authentication logic, this initial step involves registering a new account using the attacker's email, verifying via OTP, and selecting the 'Trust this device' option. This establishes a session cookie that persists across email modifications without invalidation, enabling later bypasses. The target environment is the web-based account registration system, requiring only internet access and a controlled email. Expected outcomes include a fully trusted session ready for email manipulation.

## Requirements

1. Controlled email address for registration
2. Web browser with cookie support
3. Access to Drugs.com registration endpoint

## Defense

Defensive measures and detection strategies:

- Enforce session termination on email changes
- Require 2FA re-verification for all account modifications
- Monitor for rapid email change cycles from the same IP

## Objectives

1. Gain initial authenticated access with persistent session
2. Enable device trust to avoid future 2FA prompts
3. Prepare for email hijacking without alerting the system

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the account creation page to begin setup.

Open a web browser and go to https://www.drugs.com/account/register/. Fill in the registration form with the attacker's details, including a controlled email address.

### Step 2: Complete OTP Verification

**Context**: Verify email ownership to activate the account.

Submit the form; an OTP will be sent to the attacker's email. Retrieve the OTP and enter it on the verification page.

### Step 3: Enable Device Trust

**Context**: Bypass future 2FA by trusting the current device.

After verification, check the 'Trust this device for 1 month' option during the login or setup prompt. This sets a persistent session cookie.

**Expected Output**: Redirect to account dashboard without further 2FA.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[device-trust]]
- [[2fa-bypass]]
