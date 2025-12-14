---
id: 80175d19-7f64-4311-ace5-671caac3e4ad
name: Login-to-Taken-Over-Uber-Account
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.408Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Valid Accounts]]'
tags:
  - account-takeover
  - login
  - uber
platforms:
  - Web
  - Mobile (iOS)
commands: []
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# Login-to-Taken-Over-Uber-Account

## Summary

This procedure authenticates into the victim's Uber account using the newly reset password, granting full unauthorized access to sensitive information and functionalities.

## Description

Following password modification via the vulnerable endpoint, this step completes the account takeover by logging in through the web portal or app. The attacker gains access to personal details, trip history, payment methods, and can perform actions like booking rides or changing account settings. This targets Uber's rider service, with high impact on user privacy and security.

## Requirements

1. Newly set password from previous exploitation
2. Target's phone number
3. Access to Uber web (riders.uber.com) or iOS app
4. Standard browser or app capabilities

## Defense

Defensive measures and detection strategies:

- Enable multi-factor authentication (MFA) for all accounts
- Alert on password reset events and unusual login locations
- Monitor for logins immediately after resets from unfamiliar IPs
- Use device fingerprinting to detect anomalous access

## Objectives

1. Gain persistent access to the compromised account
2. Exfiltrate or manipulate user data
3. Demonstrate full takeover impact

## Instructions

### Step 1: Initiate Login

**Context**: Use the web or app to start the authentication process with the target's phone number.

No command; navigate to http://riders.uber.com/ or open Uber app.

> Enter phone number and proceed to password entry.

### Step 2: Enter New Password

**Context**: Submit the attacker-controlled password to complete login.

No command; app/web UI driven.

> Expected: Successful authentication with dashboard access, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[login]]
- [[uber]]
