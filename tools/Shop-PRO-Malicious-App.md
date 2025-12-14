---
url: null
tags:
  - malicious-app
  - deep-link-interceptor
type: tool
platforms:
  - Android
  - iOS
description: >-
  Custom malicious Android app designed to register and intercept shopapp://
  deep links for OAuth code capture.
id: a3401d96-89c2-41d7-9ac0-c4cee09b1ab5
created_at: '2025-12-14T17:31:30.999Z'
updated_at: '2025-12-14T17:31:30.999Z'
verified: false
validated: true
submitted: true
---
# Shop-PRO-Malicious-App

**Status**: Unverified

## Overview

A proof-of-concept malicious app that demonstrates deep link hijacking in mobile OAuth flows, specifically targeting the Shopify Shop App's shopapp:// scheme to intercept authorization codes for Microsoft Outlook access.

## Description

This APK registers the custom URL scheme in its manifest, allowing it to capture deep links during OAuth redirects. Upon receiving the link, it parses the authorization code and can forward it to an attacker server or exchange it directly. Built for Android, with iOS equivalents possible via custom schemes.

## Features

- Feature 1: Automatic scheme registration for shopapp://
- Feature 2: URI parsing to extract OAuth code parameter
- Feature 3: Network capabilities to exchange code for tokens

## Installation

### Requirements

- Android device with developer options enabled
- ADB tools for sideloading
- No root required

### Install Commands

```bash
# Sideload via ADB
adb install shop_pro.apk
```

## Basic Usage

```bash
# No CLI; launch app after install and wait for deep link trigger
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | App-based; no CLI options |

## Examples

### Example 1: Basic Installation

Install APK and verify scheme:

```bash
adb install shop_pro.apk
adb shell am start -a android.intent.action.VIEW -d "shopapp://test"
```

### Example 2: In Attack Context

Install before official app, trigger OAuth, select in modal.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[T1417]] Hijack Execution Flow

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of app with suspicious scheme registration (check manifest)
- Network traffic from app to OAuth endpoints
- Anomalous app installations from unknown sources

## Related Procedures

- [[procedures/Install-Malicious-App-to-Hijack-Shopapp-Scheme]]
- [[procedures/Select-Malicious-App-for-Deep-Link-Handling]]
- [[procedures/Intercept-and-Exchange-Authorization-Code]]

## Related Tools

- [[Burp Suite]] (for API testing)

## References

- HackerOne Report #1700734
- Android Deep Link Documentation
