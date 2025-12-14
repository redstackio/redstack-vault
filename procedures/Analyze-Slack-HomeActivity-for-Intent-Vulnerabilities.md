---
id: proc-slack-homeactivity-analysis
tags:
  - android
  - decompilation
  - intent-analysis
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/analyze-homeactivity-code]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:44.621Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze-Slack-HomeActivity-for-Intent-Vulnerabilities

## Summary

This procedure involves decompiling the Slack Android app to analyze the exported HomeActivity, identifying how it processes embedded intents without validation, enabling subsequent exploitation of protected components.

## Description

In the attack scenario, a malicious app exploits the Slack app's HomeActivity which is exported and handles intent extras in onResume by calling handleIntentExtras. This extracts 'extra_deep_link_intent' and starts it via startActivity without checks, allowing access to non-exported activities. Prerequisites include an Android decompiler like Jadx or APKTool. Expected outcomes: confirmation of vulnerability for crafting exploits.

## Requirements

1. Slack APK file for decompilation
2. Android development tools (e.g., Android Studio)
3. Knowledge of Java and Android intents

## Defense

Defensive measures and detection strategies:

- Restrict activity exports in AndroidManifest.xml
- Validate and sanitize intent extras in onResume
- Monitor for anomalous intent launches via app logs or device monitoring tools

## Objectives

1. Identify vulnerable code paths in HomeActivity
2. Confirm lack of validation on deeplinkIntent
3. Prepare for intent crafting based on analysis

## Instructions

### Step 1: Decompile Slack APK

**Context**: Obtain and decompile the app to access source code.

**Command** ([[commands/analyze-homeactivity-code]]):
```java
protected void onResume() { // ... handleIntentExtras(getIntent()); // attacker can pass anything to getIntent() } private void handleIntentExtras(Intent intent) { // ... Intent deeplinkIntent = (Intent) intent.getParcelableExtra("extra_deep_link_intent"); // ... if (!(deeplinkIntent == null || this.consumedDeeplinkIntent)) { // ... startActivity(deeplinkIntent); // danger! starting an intent provided by an attacker // ... } // ... }
```

> This code snippet reveals the vulnerability: getIntent() retrieves attacker-controlled data, extracts deeplinkIntent without validation, and starts it, allowing arbitrary activity access. Expected output: Vulnerable methods identified in decompiled code.

### Step 2: Examine Key Methods

**Context**: Focus on onResume and handleIntentExtras for intent processing flaws.

No specific command; manually review the decompiled code for extras handling and startActivity calls.

> Look for getParcelableExtra("extra_deep_link_intent") and absence of permission checks. Expected output: Confirmation of unvalidated intent starting.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/analyze-homeactivity-code]]

## Tools Used


## Tags

- [[android]]
- [[decompilation]]
- [[intent-analysis]]
