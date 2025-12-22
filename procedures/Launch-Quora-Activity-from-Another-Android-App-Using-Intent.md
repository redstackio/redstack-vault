---
tags:
  - xss
  - android-intent
  - malicious-app
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Android
techniques:
  - '[[JavaScript]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 176cc8c8-891c-45f0-a4c7-408026420dde
created_at: '2025-12-13T23:52:44.057Z'
updated_at: '2025-12-13T23:52:44.057Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-Quora-Activity-from-Another-Android-App-Using-Intent

## Summary

This procedure simulates a malicious app exploiting the Quora vulnerability by creating and launching an Intent with malicious HTML, bypassing the need for ADB in real-world scenarios.

## Description

From a custom Android app, construct an Intent for ActionBarContentActivity, set 'url' and 'html' extras with XSS payload, and invoke startActivity. This allows sideloading or Play Store apps to trigger XSS. Requires Android development setup; outcomes mirror ADB exploitation but enable stealthier attacks.

## Requirements

1. Android development environment (e.g., Android Studio)
2. Target device with Quora app
3. Permissions for intent resolution (implicit)

## Defense

Defensive measures and detection strategies:

- Use android:exported="false" or intent filters with permissions
- Scan for malicious apps via Play Protect or antivirus
- Log intent receptions and validate extras in app code

## Objectives

1. Demonstrate app-to-app exploitation vector
2. Trigger XSS without external tools
3. Highlight supply chain risks from third-party apps

## Instructions

### Step 1: Create Malicious Intent in Custom App

**Context**: In your app's code, build the Intent targeting the vulnerable activity.

**Command** (Java/Kotlin snippet):
```java
Intent intent = new Intent();
intent.setComponent(new ComponentName("com.quora.android", "com.quora.android.ActionBarContentActivity"));
intent.putExtra("url", "http://test/test");
intent.putExtra("html", "XSS PoC <script>alert(123)</script>");
startActivity(intent);
```

> Expected output: Quora activity launches with alert.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android-intent
- malicious-app
