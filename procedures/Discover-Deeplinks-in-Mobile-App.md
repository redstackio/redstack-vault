---
tags:
  - deeplink
  - mobile
  - recon
type: procedure
tools:
  - '[[tools/grep]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/grep-search-string]]'
platforms:
  - Android
  - iOS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 40a5b3f4-a695-448e-9f2d-ab1d20b16b4d
created_at: '2025-12-11T06:10:22.786Z'
updated_at: '2025-12-11T06:10:22.786Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Discover Deeplinks in Mobile App

## Summary

This procedure involves identifying deeplinks in mobile apps that can be exploited to load arbitrary content, such as URLs in a WebView, without proper validation.

## Description

By analyzing the app's structure, deeplinks like HELPCENTER are found, which route to activities like com.grab.pax.support.ZendeskSupportActivity and allow loading of external URLs. This is typically done through app decompilation or runtime analysis, targeting mobile apps on Android and iOS.

## Requirements

1. Access to the target mobile app (APK or IPA)
2. Decompilation tools (e.g., Jadx for Android)
3. Mobile device or emulator for testing

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in deeplink handlers
- Monitor app logs for unexpected URL loads

## Objectives

1. Identify deeplinks accepting arbitrary parameters
2. Confirm WebView usage for loaded content
3. Map to exploitable activities

## Instructions

### Step 1: Analyze App for Deeplinks

**Context**: Decompile the app and search for deeplink handlers.

Examine manifest or code for intents handling schemes like grab://open?screenType=HELPCENTER&page=.

> Expect to find unprotected URL loading in WebView.

### Step 2: Test Deeplink Behavior

**Context**: Trigger the deeplink with a test URL to observe behavior.

Use adb (for Android) or similar to invoke the deeplink and confirm arbitrary URL loading.

> Validation: WebView loads the specified page without restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[deeplink]]
- [[mobile]]
