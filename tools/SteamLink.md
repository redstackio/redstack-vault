---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567897
url: >-
  https://play.google.com/store/apps/details?id=com.valvesoftware.steamlink&hl=vi
tags:
  - gaming
  - remote-play
type: tool
verified: false
platforms:
  - Android
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:36.092Z'
validated: true
submitted: true
---
# SteamLink

**Status**: Unverified

## Overview

Steam Link is a mobile app by Valve for streaming Steam games from a PC to Android devices over LAN, used here to trigger the vulnerable Remote Play driver installation on the host.

## Description

The app connects to a host PC running Steam, initiating sessions that cause driver loading. It exploits the feature by sending connection requests that prompt unverified installations.

## Features

- Feature 1: LAN-based game streaming
- Feature 2: Device discovery and pairing
- Feature 3: Low-latency Remote Play initiation

## Installation

### Requirements

- Android device (API 16+)
- Google Play Store

### Install Commands

Install via Play Store; no CLI.

```bash
# App store installation only
```

## Basic Usage

```bash
# Launch app and connect
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Touch-based UI for connections |

## Examples

### Example 1: Basic Usage

Open app, scan, and connect to PC.

### Example 2: Advanced Usage

Pair with PIN for secure LAN streaming.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- App installation on mobile devices
- Traffic to Steam host on local network
- Logs of Remote Play sessions

## Related Procedures


## Related Tools

- [[tools/Steam]]

## References

- Play Store: https://play.google.com/store/apps/details?id=com.valvesoftware.steamlink
- Related resources: Steam Remote Play docs
