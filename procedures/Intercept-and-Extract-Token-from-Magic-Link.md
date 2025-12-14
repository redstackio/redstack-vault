---
id: proc-uuid-3
tags:
  - token-extraction
  - intercept
  - android
type: procedure
tools:
  - '[[tools/Android-SDK]]'
tactics:
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:33:12.314Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Hijack Execution Flow]]'
---
# Intercept-and-Extract-Token-from-Magic-Link

## Summary

This procedure intercepts the magic link deeplink when opened from email on an Android device and extracts the login token from URL parameters, exploiting the lack of App Links verification.

## Description

Once the verification email is opened, Android dispatches an intent to the malicious app due to the configured filter. The app receives the Intent with the deeplink URI (e.g., https://qvay.app.link/...?token=...&secret=...), which is parsed to obtain the token. This token is short-lived and enables session verification without further auth.

## Requirements

1. Installed malicious app with intent-filter
2. Magic link email opened on device
3. Android code to handle onNewIntent or onCreate

## Defense

Defensive measures and detection strategies:

- Verify deeplinks server-side with device fingerprints
- Use secure token binding to app package
- Log and alert on unexpected intent handling

## Objectives

1. Capture the deeplink intent
2. Parse and extract token parameter
3. Prepare token for verification

## Instructions

### Step 1: Handle Intent in App Code

**Context**: Override onNewIntent to receive and log the URI.

In MainActivity.java or Kotlin:
```java
@Override
protected void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    Uri data = intent.getData();
    if (data != null) {
        String token = data.getQueryParameter("token");
        Log.d("Intercepted", "Token: " + token);
    }
}
```

> When the link is opened (e.g., via email client), the app launches and extracts the token like FdPxCtPAaPUJ7hhLg75QeHFCRCk3ATxcvrim74QJiz87kzXBQecLYtjo2p4wgHRa.

### Step 2: Validate Extraction

**Context**: Confirm token is present and valid format.

Store or forward the token for next steps.

**Expected Output**: Token string extracted successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Android-SDK]]

## Tags

- intercept
- token
