---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
url: 'https://play.google.com/store/apps/details?id=com.grabtaxi.passenger'
tags:
  - target-app
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.902Z'
validated: true
submitted: true
---
# Grab-Android-App

**Status**: Unverified

## Overview

The official Grab ride-hailing app for Android, targeted for vulnerability testing in authentication flows.

## Description

Grab app handles logins, profile management, and 2FA via SMS. Vulnerable endpoint in profile edit allows this attack chain.

## Features

- Feature 1: Google OAuth login
- Feature 2: SMS OTP for sensitive changes
- Feature 3: Profile editing with API backend

## Installation

### Requirements

- Android 5.0+

### Install Commands

```bash
# Via adb or Play Store
adb install grab.apk
```

## Basic Usage

Launch app and login.

### Common Options

N/A (mobile app)

## Examples

### Example 1: Basic Usage

Open app, select Google login.

### Example 2: Advanced Usage

Edit profile to trigger OTP.

## MITRE ATT&CK Mapping

### Techniques

- [[T1417]] Mobile App (as target)

### Tactics

- [[Initial Access]] Initial Access

## Detection

- App version checks
- Unusual API calls

## Related Procedures


## Related Tools

- [[tools/Uber-Android-App]] (similar targets)

## References

- Play Store: https://play.google.com/store/apps/details?id=com.grabtaxi.passenger
