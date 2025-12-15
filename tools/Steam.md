---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567896
url: 'https://store.steampowered.com/about/'
tags:
  - gaming
  - remote-play
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:36.095Z'
validated: true
submitted: true
---
# Steam

**Status**: Unverified

## Overview

Steam is Valve's digital distribution platform for games, featuring Remote Play for streaming gameplay over LAN or internet, which is exploited here for privilege escalation via driver installation.

## Description

Steam handles game libraries, updates, and Remote Play sessions. In this attack, its SteamServices component installs kernel drivers without runtime verification, allowing malicious replacements.

## Features

- Feature 1: Remote Play for cross-device streaming
- Feature 2: Automatic driver installation for audio devices
- Feature 3: Integrity checks on startup but not during sessions

## Installation

### Requirements

- Windows 10 x64
- Internet connection

### Install Commands

Download from official site; no CLI install, use GUI installer.

```bash
# No bash equivalent; use Windows installer
```

## Basic Usage

Launch Steam.exe and log in.

### Common Options

| Option | Description |
|--------|-------------|
| N/A | GUI-based; use settings for Remote Play enablement |

## Examples

### Example 1: Basic Usage

Run Steam and enable Remote Play in settings.

### Example 2: Advanced Usage

Authorize incoming connections during session.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor processes: Steam.exe, SteamServices.exe
- Check for driver installs in Event Logs
- Network traffic on Steam ports (27000-27100 UDP)

## Related Procedures


## Related Tools

- [[tools/SteamLink]]

## References

- Official documentation: https://help.steampowered.com
- HackerOne Report: https://hackerone.com/reports/852091
