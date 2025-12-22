---
id: tool-authy-16696
url: 'https://authy.com/'
tags:
  - 2fa
  - authentication
type: tool
verified: false
platforms:
  - Web
  - iOS
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:45.387Z'
validated: true
submitted: true
---
# Authy

**Status**: Unverified

## Overview

Authy is a two-factor authentication (2FA) application that generates time-based one-time passwords (TOTP) for securing online accounts, commonly used for services like cryptocurrency exchanges.

## Description

Authy provides cloud-synced 2FA across devices, allowing backup and recovery of tokens. In offensive security, it can be exploited by re-syncing on a compromised device to invalidate legitimate tokens and hijack authentication. Features include multi-device support and encrypted backups, but vulnerabilities arise from email-linked recovery.

## Features

- Feature 1: Cloud backup for seamless device transfers
- Feature 2: Multi-factor support beyond SMS, including push notifications
- Feature 3: Account recovery via email verification

## Installation

### Requirements

- Mobile device (iOS/Android) or desktop app
- Internet connection for sync

### Install Commands

```bash
# For Android/iOS: Download from app store
# For desktop: pip install authy or use web extension
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

Scan QR code from service (e.g., Coinbase) to add account and generate codes.

### Example 2: Advanced Usage

Re-sync existing account using backup password to transfer tokens to new device.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Reversible Encryption]] Multi-Factor Authentication Instrument

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual device sync logs in Authy account
- Multiple active sessions or token invalidations
- Email alerts for backup access

## Related Procedures


## Related Tools

- [[Google Authenticator]]
- [[Microsoft Authenticator]]

## References

- Official documentation: https://authy.com/docs
- Related resources: 2FA best practices from NIST
