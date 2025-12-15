---
id: tool-uuid-2
url: 'https://branch.io'
tags:
  - deeplinking
  - mobile
type: tool
verified: false
platforms:
  - Android
  - iOS
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.298Z'
validated: true
submitted: true
---
# Branch-io

**Status**: Unverified

## Overview

Branch.io is a deep linking platform for mobile apps, used by the Arrive app for magic link delivery. Misconfigurations, like empty assetlinks.json, allow interception.

## Description

Provides deeplinks for user attribution and login flows. In this vulnerability, the qvay.app.link domain lacks verification, enabling malicious apps to intercept links via Android intents.

## Features

- Feature 1: Universal deeplinks across platforms
- Feature 2: App Links and Universal Links support
- Feature 3: Parameter passing in links (e.g., tokens)

## Installation

### Requirements

- App integration via SDK

### Install Commands

```bash
# For Android, add to build.gradle
implementation 'io.branch.sdk.android:library:20.08.2022'
```

## Basic Usage

```bash
gradlew build  # After SDK integration
```

### Common Options

| Option | Description |
|--------|-------------|
| --link | Generate test deeplink |

## Examples

### Example 1: Basic Usage

Integrate SDK for handling deeplinks in app.

### Example 2: Advanced Usage

Configure dashboard for custom domains.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow (misuse)
- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Empty .well-known/assetlinks.json on domains
- Unverified deeplinks in app traffic
- Intent logs for branch domains

## Related Procedures

- [[procedures/Intercept-and-Extract-Token-from-Magic-Link]]

## Related Tools

- [[tools/Android-SDK]]

## References

- Official documentation: https://docs.branch.io
