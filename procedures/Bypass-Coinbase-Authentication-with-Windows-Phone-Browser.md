---
tags:
  - authorization-bypass
  - windows-phone
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: low
impact_level: high
detection_risk: low
sub_techniques: []
id: 0323dbee-7a17-4ae5-9812-ab4cac0885f6
created_at: '2025-12-14T17:28:51.746Z'
updated_at: '2025-12-14T17:28:51.746Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Coinbase-Authentication-with-Windows-Phone-Browser

## Summary

This procedure exploits a flaw in Coinbase's authentication system that fails to enforce email verification when logging in via Windows Phone browsers, allowing direct access without standard PC-enforced checks.

## Description

The attack targets the login flow of Coinbase's web application. On PC browsers, an email authorization link is required post-credential entry. However, Windows Phone browsers (e.g., on Nokia Lumia) bypass this due to user-agent or device detection issues, granting immediate account access. This occurs in the authentication endpoint and leads to unauthorized session establishment.

## Requirements

1. Windows Phone device with default browser (e.g., Nokia Lumia running Windows Phone 8 or similar)
2. Internet access to reach https://www.coinbase.com/login
3. Valid Coinbase credentials (though verification is bypassed, initial entry may still be needed)

## Defense

Defensive measures and detection strategies:

- Enforce consistent multi-factor authentication across all user-agents and devices
- Implement device fingerprinting to detect and block anomalous mobile bypass attempts
- Monitor login logs for Windows Phone user-agents without corresponding email verifications

## Objectives

1. Establish an authenticated session without email verification
2. Gain initial access to the user's Coinbase account
3. Set up for further data disclosure or modification

## Instructions

### Step 1: Launch Windows Phone Browser

**Context**: Open the browser to simulate mobile access and trigger the bypass.

Navigate to https://www.coinbase.com/login using the Windows Phone browser.

> The user-agent string from Windows Phone (e.g., Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0)) fails to trigger the PC-specific auth flow.

### Step 2: Enter Credentials and Submit

**Context**: Provide login details to initiate the flawed flow.

Enter username/email and password, then submit the login form.

> No email authorization link is sent or required; the session is established directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authorization-bypass]]
- [[windows-phone]]
