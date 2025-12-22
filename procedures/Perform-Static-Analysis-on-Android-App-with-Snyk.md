---
tags:
  - static-analysis
  - android
  - snyk
type: procedure
tools:
  - '[[tools/Snyk]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/snyk-code-test]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:42.611Z'
sub_techniques: []
id: ed9be28c-4b37-48c5-a063-46cfdd38de69
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Perform-Static-Analysis-on-Android-App-with-Snyk

## Summary

This procedure uses Snyk for static application security testing to identify vulnerabilities in Android apps, specifically detecting missing permissions like broadcastPermission in registerReceiver calls, as seen in the Nextcloud Talk app.

## Description

Static analysis scans the app's Java code without execution to uncover security flaws. In this scenario, targeting the Nextcloud Talk Android app, it reveals that the registerReceiver method lacks the broadcastPermission argument, allowing any app on the device to send broadcasts to the receiver. This can lead to unauthorized interference. Prerequisites include having the APK file and Snyk CLI installed. Expected outcomes include a detailed report of vulnerabilities for further exploitation or reporting.

## Requirements

1. Snyk CLI installed and authenticated with an API token
2. Android APK file (e.g., Nextcloud Talk APK downloaded or extracted)
3. Java development environment for any decompilation if needed

## Defense

Defensive measures and detection strategies:

- Enforce permission checks in all broadcast receivers during app development
- Use mobile security scanners like MobSF alongside Snyk for comprehensive analysis
- Monitor for anomalous app behaviors indicating broadcast interference

## Objectives

1. Detect improper access control in Android broadcast receivers
2. Generate evidence for vulnerability reporting (e.g., HackerOne)
3. Assess potential impact on app functionality like calls and audio

## Instructions

### Step 1: Install and Authenticate Snyk

**Context**: Set up Snyk to enable scanning of Android code.

**Command** ([[commands/snyk-auth]]):
```bash
snyk auth
```

> This prompts for your Snyk API token and authenticates the CLI. Expected output: "Successfully authenticated."

### Step 2: Scan the APK for Vulnerabilities

**Context**: Run static analysis to identify the missing broadcastPermission.

**Command** ([[commands/snyk-code-test]]):
```bash
snyk code test --file=NextcloudTalk.apk
```

> This analyzes the APK's code for issues. Expected output: A report listing vulnerabilities, including details on the registerReceiver call without permission, e.g., path to the Java file and line number.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/snyk-auth]]
- [[commands/snyk-code-test]]

## Tools Used

- [[tools/Snyk]]

## Tags

- [[static-analysis]]
- [[android-security]]
