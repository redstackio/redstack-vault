---
id: tool-ms-authenticator-001
url: 'https://www.microsoft.com/en-us/security/mobile-authenticator-app'
tags:
  - 2fa
  - totp
  - authentication
type: tool
verified: false
platforms:
  - iOS
  - Android
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.888Z'
validated: true
submitted: true
---
# Microsoft Authenticator

**Status**: Unverified

## Overview

Microsoft Authenticator is a mobile app for generating time-based one-time passwords (TOTP) and supporting multi-factor authentication for services like HackerOne, used in security testing to simulate or exploit 2FA mechanisms.

## Description

The app generates 6-digit OTPs every 30 seconds based on a shared secret key (from QR code scan), compliant with RFC 6238. In offensive security, it's used to demonstrate TOTP vulnerabilities like rolling windows or reuse. Features include QR scanning, cloud backup, and push notifications, but for testing, focus on TOTP generation.

## Features

- Feature 1: TOTP generation for multiple accounts with 30-second timers
- Feature 2: QR code scanning for easy setup
- Feature 3: Offline operation for code generation

## Installation

### Requirements

- iOS 15.0+ or Android 8.0+ device
- App Store or Google Play access

### Install Commands

No command-line install; download from app store.

## Basic Usage

Open app, add account via QR scan, view generated codes.

### Common Options

| Option | Description |
|--------|-------------|
| QR Scan | Add new account by scanning setup code |
| Refresh | Manually update timer if needed |

## Examples

### Example 1: Basic Usage

Scan QR from HackerOne 2FA setup; app displays rotating 6-digit code.

### Example 2: Advanced Usage

Use in conjunction with browser to test OTP entry during login flows.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- App installation on test devices
- Network traffic to Microsoft sync services (if backups enabled)

## Related Procedures

- [[procedures/Exploit-HackerOne-2FA-OTP-Reuse]]

## Related Tools

- [[Google Authenticator]]
- [[Authy]]

## References

- Official documentation: https://support.microsoft.com/authenticator-app
- RFC 6238: TOTP Standard
