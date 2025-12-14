---
url: 'https://brave.com/'
tags:
  - browser
  - testing
type: tool
verified: false
platforms:
  - Windows
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.649Z'
id: 7d3eae1d-bf2c-4c36-bc8f-2f081c2b2896
validated: true
submitted: true
---
# Brave-Browser

**Status**: Unverified

## Overview

Brave is a privacy-focused browser based on Chromium, used for testing web vulnerabilities with built-in ad and tracker blocking.

## Description

The VDP team tested Brave for reproducing the DoD auth bypass but initially failed, likely due to stricter privacy settings affecting certificate handling; it shares core features with Chrome for web testing.

## Features

- Feature 1: Enhanced privacy with automatic blocking
- Feature 2: Sync across devices
- Feature 3: Chromium compatibility for extensions and tools

## Installation

### Requirements

- Standard OS setup

### Install Commands

```bash
# On Linux
sudo apt install brave-browser
```

## Basic Usage

```bash
brave-browser
```

### Common Options

| Option | Description |
|--------|-------------|
| `--incognito` | Private window |
| `--disable-brave-shields` | Temporarily disable protections for testing |

## Examples

### Example 1: Basic Usage

```bash
brave-browser https://████/
```

### Example 2: Advanced Usage

```bash
brave-browser --incognito --disable-brave-shields https://████/
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

- Logs showing Brave user-agent in access attempts

## Related Procedures


## Related Tools

- [[tools/Google-Chrome]]
- [[tools/Microsoft-Edge]]

## References

- Official documentation: https://brave.com/
- Related resources: Chromium base docs
