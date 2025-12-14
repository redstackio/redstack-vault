---
id: proc-coinbase-ios-login-001
tags:
  - authentication-bypass
  - web
  - ios
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:52.123Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Login-to-Coinbase-via-iOS-Browser-Without-Verification

## Summary

This procedure exploits an improper authentication vulnerability in Coinbase's web application when accessed through an iOS device browser, allowing login with just credentials without the required email authorization link, unlike desktop flows.

## Description

The attack targets the login flow discrepancy between desktop and iOS browsers. On iOS, the system bypasses email verification checks after entering credentials, granting direct access to the account dashboard. This enables unauthorized entry into victim accounts if credentials are known, leading to potential information disclosure and further exploitation. The vulnerability stems from platform-specific handling in the web app, discovered by comparing login behaviors across devices.

## Requirements

1. iOS device with a web browser (e.g., Safari)
2. Valid Coinbase account credentials (username and password)
3. Internet access to reach www.coinbase.com

## Defense

Defensive measures and detection strategies:

- Implement consistent multi-factor authentication (MFA) across all platforms and devices
- Monitor login attempts from mobile browsers and flag iOS-specific anomalies
- Enforce email verification or CAPTCHA on all login flows regardless of user agent

## Objectives

1. Achieve unauthorized login without secondary verification
2. Gain initial access to the account dashboard
3. Set stage for information disclosure and account manipulation

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the Coinbase sign-in page using the iOS browser to initiate the flawed authentication flow.

No command required; manually enter https://www.coinbase.com/signin in the browser address bar.

> The page loads the standard login form without device-specific prompts.

### Step 2: Submit Credentials

**Context**: Enter valid credentials to trigger the bypass, observing the absence of email verification.

No command required; input username and password in the form fields and submit.

> Successful submission redirects to the dashboard without prompting for email link confirmation, confirming the bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- authentication-bypass
- web
- ios
