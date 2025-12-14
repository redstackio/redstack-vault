---
tags:
  - deep-link-hijacking
  - malicious-app-install
type: procedure
tools:
  - '[[tools/Shop-PRO-Malicious-App]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Android
  - iOS
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 41714357-96e5-45d5-bd32-45c429f497dd
created_at: '2025-12-14T17:31:31.019Z'
updated_at: '2025-12-14T17:31:31.019Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Install-Malicious-App-to-Hijack-Shopapp-Scheme

## Summary

This procedure installs a custom malicious Android (or iOS) app that registers the shopapp:// URL scheme, enabling interception of deep links used in the Shopify Shop App's OAuth flow for Microsoft Outlook integration.

## Description

The attack relies on mobile OS behavior allowing multiple apps to register the same custom URL scheme. By installing the malicious app first or alongside the official one, it positions itself to capture sensitive deep links containing OAuth authorization codes. No PKCE is used, so intercepted codes are fully usable. This targets Android via APK sideloading or iOS via enterprise distribution.

## Requirements

1. Access to the victim's device for app installation (physical or via social engineering)
2. Malicious app APK built with shopapp:// intent filter in AndroidManifest.xml
3. Android device (API 21+) or jailbroken/rooted iOS for sideloading

## Defense

Defensive measures and detection strategies:

- Implement PKCE in OAuth flows to invalidate intercepted codes
- Use App Links (Android) or Universal Links (iOS) with domain validation instead of custom schemes
- Educate users on app installation risks and verify app sources
- Monitor for multiple apps registering the same scheme via device management tools

## Objectives

1. Register the malicious app to handle shopapp:// deep links
2. Prepare for OAuth code interception without alerting the user
3. Enable subsequent hijacking during legitimate app usage

## Instructions

### Step 1: Prepare Malicious App

**Context**: Build or obtain the malicious app that declares the shopapp:// scheme in its configuration.

For Android, ensure the AndroidManifest.xml includes:

```xml
<intent-filter>
    <data android:scheme="shopapp" />
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
</intent-filter>
```

**Expected Output**: APK file ready (e.g., shop_pro.apk).

### Step 2: Install on Device

**Context**: Sideload the APK on the target Android device or install via iOS method.

Enable unknown sources in settings, then install using ADB or file manager:

```bash
adb install shop_pro.apk
```

**Expected Output**: Installation complete, app listed in device apps.

### Step 3: Verify Scheme Registration

**Context**: Confirm the app can handle the scheme.

Test by opening a shopapp:// URL; the malicious app should launch.

**Expected Output**: App opens without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Shop-PRO-Malicious-App]]

## Tags

- [[deep-link-hijacking]]
- [[malicious-app-install]]
