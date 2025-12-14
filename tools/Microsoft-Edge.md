---
url: null
tags:
  - browser
  - testing
  - xss
type: tool
platforms:
  - Windows
description: >-
  Web browser used for testing and exploiting DOM XSS vulnerabilities where URL
  encoding is not applied.
id: 1c390cb4-7c49-4886-a8fc-1c974d00d09f
created_at: '2025-12-13T23:56:20.483Z'
updated_at: '2025-12-13T23:56:20.483Z'
verified: false
validated: true
submitted: true
---
# Microsoft Edge

**Status**: Unverified

## Overview

Microsoft Edge is a web browser that, in legacy modes, can be used for security testing similar to IE, particularly for XSS exploits where URL encoding is absent.

## Description

Edge is employed to verify vulnerabilities in scenarios where modern encoding prevents exploits, allowing injection testing on Windows platforms.

## Features
- Compatibility with legacy behaviors
- Developer tools for DOM inspection
- Integration with Windows security features

## Installation

### Requirements
- Windows 10 or later

### Install Commands

Pre-installed on Windows; update via Settings.

## Basic Usage

```bash
# Launch via Windows Run: msedge https://target.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `--inprivate` | InPrivate browsing |
| `--headless` | Headless mode |

## Examples

### Example 1: Basic Usage

Open Edge and load the POC URL.

### Example 2: Advanced Usage

Use DevTools to monitor script execution.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques
- [[JavaScript]]

### Tactics
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:
- Track Edge launches with anomalous URLs
- Analyze browser logs for injection attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools
- [[tools/Internet-Explorer]]
- [[tools/Chrome]]

## References
- Microsoft Edge documentation
