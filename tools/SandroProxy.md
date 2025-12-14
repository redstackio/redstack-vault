---
id: sandroproxy-uuid
name: SandroProxy
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.813Z'
platforms:
  - Android
tags:
  - proxy
  - mitm
url: 'https://github.com/Sandrob/SandroProxy'
validated: true
submitted: true
---

# SandroProxy

**Status**: Unverified

## Overview

SandroProxy.apk is an Android-based HTTP/HTTPS proxy tool for intercepting, modifying, and replaying web requests, commonly used in mobile security testing to capture Phabricator traffic.

## Description

This tool acts as a man-in-the-middle proxy, allowing inspection of requests like Phabricator's email addition POST. It supports SSL decryption via CA installation and request editing. In attacks, it's pivotal for replaying modified sessions to exploit authentication flaws.

## Features

- Feature 1: Real-time request interception and modification
- Feature 2: HTTPS support with certificate pinning bypass
- Feature 3: Request replay functionality

## Installation

### Requirements

- Rooted Android device (preferred for full HTTPS)
- ~5MB storage

### Install Commands

```bash
# Sideload APK
adb install SandroProxy.apk
# Install CA cert: adb push proxy.crt /system/etc/security/cacerts/
```

## Basic Usage

```bash
# Launch app, set proxy port (e.g., 8080)
# Configure device WiFi to use proxy IP:8080
```

### Common Options

| Option | Description |
|--------|-------------|
| Capture All | Enable full traffic logging |
| Edit Request | Modify parameters before forwarding |
| Replay | Resend captured requests |

## Examples

### Example 1: Basic Usage

Start proxy, configure browser proxy, navigate to target site, intercept requests.

### Example 2: Advanced Usage

Intercept Phabricator POST, edit `email` param, replay to inject address.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of custom CA certificates on device
- Proxy-related traffic anomalies in network logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Lightning-Browser]]
- [[tools/Burp-Suite]]

## References

- GitHub documentation
- Mobile MITM proxy tutorials
