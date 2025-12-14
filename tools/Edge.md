---
id: tool-edge
url: 'https://www.microsoft.com/edge'
tags:
  - browser
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.160Z'
validated: true
submitted: true
---
# Edge

**Status**: Unverified

## Overview

Microsoft Edge (legacy Chromium-based) is a browser for reproducing XSS by loading URLs and checking JS execution, bridging modern and legacy testing.

## Description

Edge's DevTools mirror Chrome's, aiding in inspection of network fetches and script injections for web vuln validation.

## Features

- Feature 1: F12 tools
- Feature 2: Extensions
- Feature 3: IE mode for legacy

## Installation

### Requirements

- Windows 10+

### Install Commands

```bash
# Pre-installed or download from Microsoft
```

## Basic Usage

Launch Edge and load URL.

### Common Options

| Option | Description |
|--------|-------------|
| `--inprivate` | Incognito mode |

## Examples

### Example 1: Basic Usage

Navigate to malicious URL in Edge.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-agent: Edge/...

## Related Procedures


## Related Tools

- [[tools/Chrome]]

## References

- Official documentation: https://www.microsoft.com/edge
