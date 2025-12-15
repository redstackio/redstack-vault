---
id: proc-shopify-trigger-login-001
tags:
  - android
  - api-trigger
  - user-login
type: procedure
tools:
  - '[[tools/Custom-POC-APK-shopifyhack]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1475]]'
updated_at: '2025-12-14T17:32:11.005Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1475]]'
---
# Trigger-Shopify-API-Requests-via-User-Login

## Summary

This procedure simulates normal user behavior by opening the Shopify app and performing a login, which triggers API requests and subsequent unprotected broadcasts of response data to any listening receivers.

## Description

User interactions like login cause the Shopify app's NetworkService to send implicit broadcasts with full API response details in Intent extras. This step relies on the victim using the app naturally, making the attack stealthy as it requires no additional privileges.

## Requirements

1. Shopify app and POC APK installed on the device
2. Valid Shopify credentials for login
3. Device unlocked for app interaction

## Defense

Defensive measures and detection strategies:

- Educate users on app permissions and unusual behavior
- Implement broadcast protections like LocalBroadcastManager or permissions
- Monitor app logs for unexpected API calls

## Objectives

1. Initiate API requests to generate broadcasts
2. Leak sensitive data via unprotected Intents
3. Maintain user unawareness during the process

## Instructions

### Step 1: Launch Shopify App

**Context**: Open the app to prepare for login, ensuring the POC receiver is active.

No command; manually launch via device interface.

> The app starts normally; background receiver from POC remains active.

### Step 2: Perform Login

**Context**: Enter credentials to trigger authentication API calls.

Enter username/password or use OAuth; submit login form.

> This sends requests to Shopify API, resulting in broadcasts with responses including tokens and cookies.

### Step 3: Confirm Trigger

**Context**: Verify login success, indicating broadcasts were sent.

Observe app UI showing successful login.

> No visible errors; data is leaked silently to the POC.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1475]] Install Malicious Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-POC-APK-shopifyhack]]

## Tags

- android
- api-trigger
- user-login
