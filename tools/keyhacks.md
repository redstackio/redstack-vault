---
id: uuid-for-keyhacks-tool
url: 'https://github.com/streaak/keyhacks'
tags:
  - validation
  - api-keys
  - credential
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.112Z'
validated: true
submitted: true
---
# keyhacks

**Status**: Unverified

## Overview

keyhacks is a Python-based toolkit for checking leaked API keys from services like Google Maps and MapBox, determining if they are active, associated with projects, and overly permissive for exploitation.

## Description

Designed for offensive security, it automates validation of credentials found in decompiled apps or leaks, querying provider APIs to reveal quotas, permissions, and usage limits without triggering alerts. Commonly used post-extraction to prioritize exploitable keys.

## Features

- Feature 1: Validates Google API keys (Maps, Cloud, etc.) for validity and scopes
- Feature 2: Checks MapBox tokens for access levels and billing info
- Feature 3: Supports batch validation of multiple keys from files

## Installation

### Requirements

- Python 3.6+
- pip for dependencies like requests

### Install Commands

```bash
# Clone the repository
git clone https://github.com/streaak/keyhacks.git
cd keyhacks
pip install -r requirements.txt
```

## Basic Usage

```bash
python keyhacks.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--google-maps` | Validate Google Maps key |
| `--verbose` | Detailed output on API responses |

## Examples

### Example 1: Basic Usage

```bash
python keyhacks.py --google-maps AIzaSyD...
```

### Example 2: Advanced Usage

```bash
python keyhacks.py --mapbox pk.eyJ1... --verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Google/MapBox validation endpoints from non-standard IPs
- Python processes with 'keyhacks' in command lines

## Related Procedures

- [[procedures/Search-for-Hardcoded-API-Keys-in-Decompiled-Files]]

## Related Tools

- [[tools/apktool]]

## References

- Official GitHub: https://github.com/streaak/keyhacks
- Google API Docs for key validation
