---
id: proc-grab-identify-deeplinks
tags:
  - deeplink
  - mobile
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:25:22.884Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-Grab-App-Deeplinks

## Summary

This procedure identifies vulnerable deeplinks in the Grab mobile app, specifically the 'HELPCENTER' scheme that allows loading arbitrary URLs in the ZendeskSupportActivity WebView without validation.

## Description

In the Grab app, deeplinks like grab://open?screenType=HELPCENTER&page=<URL> are used to direct users to support pages but fail to validate the 'page' parameter, enabling attackers to inject external URLs into an insecure WebView. This step involves static or dynamic analysis of the app to uncover these schemes, setting the stage for payload delivery via social engineering links.

## Requirements

1. Installed Grab app on Android or iOS device/emulator
2. ADB (Android Debug Bridge) for Android or similar debugging tools for iOS
3. Basic knowledge of URI schemes and app behavior

## Defense

Defensive measures and detection strategies:

- Implement strict URL whitelisting in deeplink handlers
- Monitor for anomalous WebView loads in app logs
- Use certificate pinning to prevent external domain access

## Objectives

1. Locate exploitable deeplink schemes
2. Verify lack of input validation
3. Prepare for payload hosting

## Instructions

### Step 1: Analyze App for Deeplink Schemes

**Context**: Use app introspection tools to find registered URI schemes.

For Android, use ADB to logcat and test potential schemes:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "grab://open?screenType=HELPCENTER&page=https://example.com" com.grab.pax
```

> This command launches the app with the deeplink; monitor logs for WebView activity. Expected output: App opens ZendeskSupportActivity loading the URL.

### Step 2: Test Deeplink Response

**Context**: Confirm the deeplink bypasses validation.

Trigger via browser or note app and observe if arbitrary URLs load.

**Expected Output**: WebView displays content from the specified URL without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- deeplink
- mobile
