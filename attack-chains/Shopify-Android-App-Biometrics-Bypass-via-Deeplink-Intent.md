---
id: ac-shopify-biometrics-bypass
tags:
  - auth-bypass
  - biometrics
  - android
  - deeplink
  - intent
type: attack_chain
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Enable-Fingerprint-Biometrics-in-Shopify-App]]'
  - '[[procedures/Launch-Shopify-App-in-Background]]'
  - '[[procedures/Trigger-Deeplink-Intent-for-Auth-Bypass]]'
  - '[[procedures/Bypass-Auth-on-Closed-App-via-Cancel]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[T1626]]'
updated_at: '2025-12-14T17:28:36.405Z'
description: >-
  Multi-stage attack chain exploiting the Shopify Android app's failure to
  enforce biometrics re-authentication when handling deeplinks via
  DeepLinkActivity, allowing unauthorized access to admin features.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[T1626]]'
---
# Shopify Android App Biometrics Bypass via Deeplink Intent

Multi-stage attack chain demonstrating a complete attack workflow to bypass biometrics authentication in the Shopify Android app by exploiting deeplink handling in DeepLinkActivity.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable Biometrics] --> B[Launch App in Background]
    B --> C[Trigger Deeplink Intent]
    C --> D[Bypass on Closed App]
    D --> E[Access Admin Features]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ADB]]

### Target Environment

- Android device with Shopify app (com.shopify.mobile) installed, version vulnerable (e.g., prior to fixes)
- ADB enabled on device for debugging
- Fingerprint biometrics supported on device

### Initial Access Requirements

- Physical or ADB access to the Android device
- App installed but no credentials needed post-bypass
- No network position required beyond local device access

## Detailed Attack Procedures

### Step 1: Enable Fingerprint Biometrics

procedure: [[procedures/Enable-Fingerprint-Biometrics-in-Shopify-App]]

**Objective**: Activate biometrics in the app to set up the authentication mechanism that will later be bypassed.

**Instructions**: Navigate to the app settings manually on the device.

**Expected Output**: Biometrics option toggled on, app prompts for fingerprint on next login.

**Success Indicators**:
- Biometrics enabled in settings
- App requires fingerprint for authentication on launch

### Step 2: Launch App in Background

procedure: [[procedures/Launch-Shopify-App-in-Background]]

**Objective**: Keep the app running in the background to maintain an active session without locking the screen.

**Instructions**: Manually launch the Shopify app and minimize it without closing or locking.

**Expected Output**: App icon shows as recently used, session active.

**Success Indicators**:
- App remains open in background
- No authentication prompt on relaunch from recent apps

### Step 3: Trigger Deeplink Intent for Auth Bypass

procedure: [[procedures/Trigger-Deeplink-Intent-for-Auth-Bypass]]

**Objective**: Use ADB to send a deeplink intent to DeepLinkActivity, bypassing the biometrics prompt and accessing protected admin features.

**Instructions**: With the app in background, execute the following using [[commands/adb-start-deeplink-products]]:

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://www.shopify.com/admin/products'
```

This launches the activity with the admin products URL, skipping authentication.

**Expected Output**: App foregrounds to the admin products page without biometrics prompt.

**Success Indicators**:
- Direct access to /admin/products
- No credential or fingerprint required

### Step 4: Bypass Auth on Closed App via Cancel

procedure: [[procedures/Bypass-Auth-on-Closed-App-via-Cancel]]

**Objective**: For scenarios where the app is closed, trigger an intent that allows skipping auth via a cancel button.

**Instructions**: Ensure app is closed, then execute using [[commands/adb-start-deeplink-admin]]:

```bash
adb shell am start -n com.shopify.mobile/com.shopify.mobile.lib.app.DeepLinkActivity -d 'https://shopify.com/admin/'
```

Interact by clicking cancel on any prompt that appears.

**Expected Output**: App opens to admin dashboard after cancel, without biometrics.

**Success Indicators**:
- Access granted post-cancel
- Protected features visible without auth

## Attack Chain Summary

### Key Achievements

1. Enabled biometrics to simulate secure setup
2. Maintained background session for intent exploitation
3. Bypassed auth via deeplink to admin products
4. Extended bypass to closed app state using cancel mechanism

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[T1626]] Abuse Elevation Control Mechanism

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
