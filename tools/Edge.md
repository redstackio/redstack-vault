---
url: 'https://www.microsoft.com/en-us/edge'
tags:
  - browser
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.299Z'
id: 8fe1407b-2efd-4c6c-8c1f-33653eda5265
validated: true
submitted: true
---
# Edge

**Status**: Unverified

## Overview

Microsoft Edge (legacy Blink-based) for web vuln testing.

## Description

Tests XSS in Chromium engine variant.

## Features

- Feature 1: DevTools
- Feature 2: F12 tools

## Installation

### Requirements

- Windows 10+

### Install Commands

```bash
# Pre-installed; update via Settings
```

## Basic Usage

```bash
start microsoft-edge:https://www.mapbox.com/authorize/?redirect_uri=https://attacker.com/malicious.json
```

### Common Options

| Option | Description |
|--------|-------------|
| `--inprivate` | Incognito mode |

## Examples

### Example 1: Basic Usage

Launch and load URL.

## MITRE ATT&CK Mapping

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

- Edge user-agent

## Related Procedures


## Related Tools

- [[tools/Chrome]]

## References

- https://docs.microsoft.com/en-us/microsoft-edge/
