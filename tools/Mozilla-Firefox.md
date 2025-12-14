---
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - testing
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.346Z'
id: e057681c-8136-4873-87c3-a5a5997bb5fc
validated: true
submitted: true
---
# Mozilla-Firefox

**Status**: Unverified

## Overview

Mozilla Firefox is an open-source web browser used for security assessments, particularly for verifying cross-browser compatibility of exploits like stored XSS.

## Description

Firefox includes robust developer tools for examining page source, injecting payloads, and monitoring JavaScript execution. It was employed here to reproduce the XSS vulnerability on informatica.csod.com independently of Chrome.

## Features

- Feature 1: Firebug-like DevTools for real-time DOM inspection.
- Feature 2: Support for about:config tweaks for security testing.
- Feature 3: Privacy-focused modes to isolate test sessions.

## Installation

### Requirements

- Internet connection
- Compatible OS

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install firefox
```

## Basic Usage

```bash
firefox --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-private-window` | Open private window |
| `--safe-mode` | Start without extensions |

## Examples

### Example 1: Basic Usage

```bash
firefox https://informatica.csod.com
```

### Example 2: Advanced Usage

```bash
firefox -private-window https://informatica.csod.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-agent strings in logs identifying Firefox during tests.
- Anomalous JS errors or alerts in browser console.

## Related Procedures


## Related Tools

- [[tools/Google-Chrome]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools
- Related resources: Firefox Developer Edition
