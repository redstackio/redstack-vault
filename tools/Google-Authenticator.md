---
id: t4d5e6f7-g8h9-0123-defg-456789012345
name: Google-Authenticator
type: tool
verified: false
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:42.471Z'
platforms:
  - Android
  - iOS
tags:
  - 2fa
  - auth
url: >-
  https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2
validated: true
submitted: true
---

# Google-Authenticator

**Status**: Unverified

## Overview

Google Authenticator is a mobile app for generating time-based one-time passwords (TOTP) for two-factor authentication, commonly used in security testing to simulate or bypass 2FA setups by generating codes independently of account linkage.

## Description

The app supports TOTP and HOTP algorithms, allowing manual entry of secret keys or QR code scanning. In offensive security, it's used to create unlinked 2FA sessions by generating codes without proper association, exploiting platforms that don't validate linkage during enablement. It's lightweight, offline-capable, and integrates with services like HackerOne for auth testing.

## Features

- Feature 1: Generates 6-digit TOTP codes every 30 seconds
- Feature 2: Supports manual secret key entry for unlinked setups
- Feature 3: No internet required for code generation post-setup

## Installation

### Requirements

- Android 5.0+ or iOS 14.0+
- Google Play Store or App Store access

### Install Commands

For Android via ADB (if emulating):

```bash
# Download and install APK
adb install google-authenticator.apk
```

Or directly from store.

## Basic Usage

```bash
# No CLI; app-based. Open app and add account manually.
```

### Common Options

| Option | Description |
|--------|-------------|
| Manual Entry | Add account by typing secret key |
| Time Sync | Sync device time for accurate codes |

## Examples

### Example 1: Basic Usage

Open app, tap '+', select 'Enter a setup key', input a generic secret (e.g., 'JBSWY3DPEHPK3PXP'), label as 'Test', and generate codes.

### Example 2: Advanced Usage

For unlinked bypass: Generate codes without any service QR, input sequentially into target platform's 2FA field during enablement.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Mobile app traffic to auth endpoints without QR scan logs
- Repeated code entries from independent TOTP sources
- Anomalous 2FA enablements without linkage validation

## Related Procedures


## Related Tools

- [[Authy]]
- [[Microsoft-Authenticator]]

## References

- Official documentation: https://support.google.com/accounts/answer/1066447
- Related resources: TOTP RFC 6238
