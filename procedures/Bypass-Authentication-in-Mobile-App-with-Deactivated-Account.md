---
tags:
  - authentication-bypass
  - shopify
  - mobile-app
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:44.988Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1078.004]]'
id: b41f196e-eced-4154-a5db-ef021559ea79
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Authentication-in-Mobile-App-with-Deactivated-Account

## Summary

This procedure demonstrates authenticating into the Shopify mobile app using credentials from a deactivated staff account, exploiting a failure in status validation. It allows unauthorized access to the store despite web-based deactivation, highlighting a critical synchronization issue.

## Description

The Shopify mobile app's login mechanism does not query the current account status from the backend API, relying on outdated or cached validation. This procedure targets iOS or Android devices with the app installed and uses deactivated staff credentials. Prerequisites include a recently deactivated account via the web interface. Successful execution grants full staff access in the app, enabling further exploitation.

## Requirements

1. Shopify mobile app installed on a test device (iOS or Android)
2. Deactivated staff account credentials (email and password)
3. Internet connectivity for app authentication

## Defense

Defensive measures and detection strategies:

- Add API calls in the mobile app to verify account status on login
- Log all mobile authentications and alert on deactivated account usage
- Use token-based auth with short expiration and revocation checks

## Objectives

1. Attempt login with known deactivated credentials
2. Confirm bypass of deactivation enforcement
3. Gain access to store dashboard in mobile app

## Instructions

### Step 1: Launch Shopify Mobile App

**Context**: Open the app to initiate the login process on the device.

Install and launch the Shopify app from the App Store or Google Play if not already present. Ensure the app is updated to the latest version.

> The app opens to the login screen.

### Step 2: Enter Deactivated Staff Credentials

**Context**: Input the email and password of the staff account deactivated via web.

Tap the login fields, enter the deactivated staff's email and password, then tap "Log in".

> No error for deactivation; authentication proceeds.

### Step 3: Complete Login and Verify Access

**Context**: Confirm successful entry into the app despite deactivation.

If prompted, allow permissions or complete any additional steps. Navigate to the store dashboard.

> Dashboard loads, showing access to staff features like orders or settings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[T1078.004]]

## Commands Used


## Tools Used


## Tags

- [[authentication-bypass]]
- [[shopify]]
- [[mobile-app]]
