---
id: lightning-browser-uuid
name: Lightning-Browser
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.818Z'
platforms:
  - Android
  - Web
tags:
  - mobile-browser
url: 'https://github.com/anthonycr/Lightning-Browser'
validated: true
submitted: true
---

# Lightning-Browser

**Status**: Unverified

## Overview

Lightning.apk is an open-source mobile browser for Android, used here to access Phabricator's web interface and trigger requests for interception in security testing scenarios.

## Description

This lightweight Chromium-based browser supports proxy configuration and is ideal for mobile web app testing. In offensive operations, it's used to simulate victim interactions on Phabricator, allowing easy traffic capture via tools like SandroProxy. Features include ad-blocking and private mode, but for attacks, standard mode with proxy enabled is key.

## Features

- Feature 1: Fast rendering for web apps like Phabricator
- Feature 2: Easy proxy integration for request interception
- Feature 3: Support for cookies and session management

## Installation

### Requirements

- Android device (version 5.0+)
- ~10MB storage

### Install Commands

```bash
# Download APK from GitHub and sideload
adb install Lightning.apk
```

## Basic Usage

```bash
# Launch via ADB or directly on device
adb shell am start -n com.anthonycr.aria/.AriaActivity
```

### Common Options

| Option | Description |
|--------|-------------|
| Settings > Proxy | Configure HTTP proxy for interception |
| Incognito | Avoid local storage leaks |

## Examples

### Example 1: Basic Usage

Launch browser, navigate to `https://admin.phacility.com`, log in to Phabricator.

### Example 2: Advanced Usage

Set proxy to 127.0.0.1:8080, access email settings, submit form to trigger interceptable request.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual User-Agent strings in logs (e.g., Android Chrome variant)
- Traffic patterns from mobile IPs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/SandroProxy]]

## References

- Official GitHub repository
- Android proxy testing guides
