---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - 2fa
  - authentication
  - bug
  - deprecated-api
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T17:24:47.971Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
---
# Verify-2FA-Activation-Failure

## Summary

This procedure demonstrates a functional bug in the 2FA activation process on app.pullrequest.com, where the deprecated Google Chart API fails to generate the required QR code, preventing users from securing their accounts with two-factor authentication.

## Description

The vulnerability arises during the 2FA setup in user settings, where the application relies on the now-deprecated Google Chart API to create a QR code for scanning into authenticator apps like Google Authenticator. When users attempt to enable 2FA, the QR code does not render, halting the process. This affects all users, leaving accounts reliant solely on password-based authentication and increasing susceptibility to credential stuffing or phishing attacks. The procedure involves manual steps in a web browser to replicate and verify the issue.

## Requirements

1. Valid login credentials for app.pullrequest.com
2. Web browser with JavaScript enabled
3. Network access to https://app.pullrequest.com/

## Defense

Defensive measures and detection strategies:

- Migrate to a supported QR code generation library (e.g., qrcode.js or a modern API)
- Implement fallback mechanisms for 2FA setup, such as manual secret key entry
- Monitor application logs for API errors related to chart generation
- Conduct regular audits of third-party dependencies for deprecation

## Objectives

1. Verify the failure of 2FA QR code generation
2. Document the impact on account security
3. Recommend remediation to restore 2FA functionality

## Instructions

### Step 1: Access the Login Page

**Context**: Begin by authenticating to the application to simulate a legitimate user attempting 2FA setup.

No specific command; use browser navigation to https://app.pullrequest.com/ and enter credentials.

> Upon successful login, the dashboard should appear, confirming access.

### Step 2: Navigate to Security Settings

**Context**: Locate the 2FA configuration to initiate the enablement process.

From the dashboard, click 'User Settings' > 'Security' > 'Two-Factor Authentication'.

> The 2FA page loads, displaying the enable option.

### Step 3: Attempt 2FA Enablement

**Context**: Trigger the QR code generation to observe the failure due to the deprecated API.

Click 'Enable Two-Factor Authentication'.

> The page attempts to load a QR code image via the Google Chart API (e.g., https://chart.googleapis.com/chart?chs=200x200&chld=M|0&cht=qr&chl=otpauth://totp/...), but it fails to render, resulting in a broken image or error.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- 2fa
- authentication
- vulnerability
- web

