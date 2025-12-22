---
url: 'https://www.yubico.com/product/yubikey-5c/'
tags:
  - fido
  - u2f
  - hardware
type: tool
platforms:
  - iOS
  - Web
description: >-
  FIDO U2F hardware security key for authenticating registration prompts in
  browser exploits.
id: 62b12bd9-8b44-4f93-9cb6-4df29d8c8f9a
created_at: '2025-12-14T03:47:12.881Z'
updated_at: '2025-12-14T03:47:12.881Z'
verified: false
validated: true
submitted: true
---
# YubiKey-5Ci

**Status**: Unverified

## Overview

YubiKey 5Ci is a portable hardware authentication device supporting FIDO U2F and WebAuthn protocols, commonly used in security testing to interact with browser-based authentication flows, including exploit demonstrations like fake U2F registrations.

## Description

This USB-C/Lightning-compatible key provides secure key storage and touch-based confirmation for protocols like FIDO U2F. In offensive security, it's used to simulate legitimate user interactions in browser vulnerabilities, such as completing prompts in Brave iOS to trigger payload execution. Features include NFC, USB-C, and Lightning connectors for iOS compatibility, with no software installation needed for basic U2F use.

## Features

- Feature 1: FIDO U2F/WebAuthn support for passwordless auth simulation
- Feature 2: Touch-to-confirm for physical interaction in exploits
- Feature 3: Cross-platform compatibility, including iOS via Lightning

## Installation

### Requirements

- iOS device with Lightning port
- No software; plug-and-play for U2F

### Install Commands

```bash
# No installation; insert device directly
```

## Basic Usage

```bash
# Usage in browser: Insert and touch when prompted
```

### Common Options

| Option | Description |
|--------|-------------|
| Touch Sensor | Confirm actions physically |
| LED Indicator | Shows device status |

## Examples

### Example 1: Basic Usage

Insert YubiKey 5Ci into iOS device; touch during FIDO prompt in Brave.

### Example 2: Advanced Usage

Use in WebAuthn flow: Browser detects key, prompts touch for registration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor USB/Lightning device insertions in logs
- Detect FIDO touch events in browser audits

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://developers.yubico.com/
- Related resources: FIDO Alliance specs
