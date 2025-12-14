---
tags:
  - auth-bypass
  - mobile
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
updated_at: '2025-12-14T17:31:19.781Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6f5638c6-91ed-454b-836a-c4d5d30f3b93
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Shopify-Mobile-App

## Summary

This procedure involves opening the Shopify mobile application on a device with an active logged-in session, leveraging the existing authentication to gain initial access without re-verification.

## Description

In the context of the authentication bypass vulnerability, an attacker with physical access to a device can launch the Shopify app and immediately access store management features. The app does not enforce session timeout or re-authentication for basic entry, setting the stage for deeper navigation into sensitive areas. This exploits the trust in the device's local session state, differing from the web app's stricter controls.

## Requirements

1. Physical access to the target mobile device (iOS or Android)
2. Shopify mobile app installed and logged into a target store account
3. No additional credentials or network access needed

## Defense

Defensive measures and detection strategies:

- Enforce device PIN or biometric locks to prevent unauthorized physical access
- Implement app-level session timeouts and re-authentication for all actions
- Monitor for unusual device activity via mobile device management (MDM) tools

## Objectives

1. Establish initial foothold in the app using persistent session
2. Prepare for navigation to sensitive settings
3. Avoid triggering any login prompts

## Instructions

### Step 1: Unlock and Launch App

**Context**: Secure physical access to the device and open the app to load the active session.

No command required; manually unlock the device screen and tap the Shopify app icon.

> The app dashboard should load directly, displaying store overview without prompting for credentials.

### Step 2: Verify Session Activity

**Context**: Confirm the session is valid and store data is accessible.

Navigate to the main store page within the app.

> Expected: Full access to store metrics and management options, indicating successful session hijack via physical access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[auth-bypass]]
- [[mobile]]
- [[shopify]]
