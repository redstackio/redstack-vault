---
id: p-bypass-closed-app-cancel
tags:
  - bypass
  - deeplink
  - intent
  - android
  - cancel
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/adb-start-deeplink-admin]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[T1626]]'
updated_at: '2025-12-14T17:28:36.396Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[T1626]]'
---
# Bypass-Auth-on-Closed-App-via-Cancel

## Summary

This procedure triggers a deeplink intent on a closed Shopify Android app, using a cancel button interaction to skip biometrics and gain access to admin features, effective in newer app versions.

## Description

In updated versions (e.g., 8.25.0), closing the app still allows intent exploitation if a prompt appears with a cancel option that bypasses auth upon selection. Targets https://shopify.com/admin/ via DeepLinkActivity.

## Requirements

1. ADB setup on device
2. Shopify app closed
3. Device unlocked for interaction

## Defense

Defensive measures and detection strategies:

- Remove cancel options that skip auth
- Enforce full re-auth on app launch from intents
- Audit intent handling for bypass paths

## Objectives

1. Launch app from closed state via intent
2. Use cancel to evade biometrics
3. Access admin dashboard

## Instructions

### Step 1: Trigger Intent on Closed App

**Context**: Send deeplink to reopen app with bypass opportunity.

**Command** ([[commands/adb-start-deeplink-admin]]):
```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://shopify.com/admin/'
```

> Launches app; a prompt may appear. Expected: App starts.

### Step 2: Interact with Cancel

**Context**: Skip auth by canceling any dialog.

Manual: Tap 'Cancel' on the prompt.

> Expected: App proceeds to admin/ without biometrics.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[T1626]] Abuse Elevation Control Mechanism

### Sub-Techniques


## Commands Used

- [[commands/adb-start-deeplink-admin]]

## Tools Used

- [[tools/ADB]]

## Tags

- bypass
- cancel
