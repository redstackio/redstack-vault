---
url: 'https://chromedevtools.github.io/devtools-protocol/'
tags:
  - debugging
  - ssrf-target
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.993Z'
id: 1722ffa6-3024-4973-8d53-cc27fab8f3e6
validated: true
submitted: true
---
# chrome-devtools-protocol

**Status**: Unverified

## Overview

The Chrome DevTools Protocol (CDP) enables remote debugging and automation of Chrome/Chromium instances, including headless mode, often exposed insecurely on port 9222 for SSRF exploitation to inspect tabs and execute commands.

## Description

When launched with --remote-debugging-port=9222, CDP exposes JSON endpoints like /json/list for tab enumeration. In headless Chrome used for PDF conversion, SSRF via iframe allows attackers to list open tabs, leaking internal URLs without authentication.

## Features

- Feature 1: Tab and frame inspection
- Feature 2: DOM manipulation and JS execution
- Feature 3: Network request interception

## Installation

### Requirements

- Chromium/Chrome binary

### Install Commands

```bash
# Launch headless with debugging
google-chrome --headless --remote-debugging-port=9222 --dump-dom https://example.com
```

## Basic Usage

```bash
curl http://localhost:9222/json/list
```

### Common Options

| Option | Description |
|--------|-------------|
| --remote-debugging-port | Port for CDP (default 9222) |
| --headless | Run without UI |

## Examples

### Example 1: Basic Usage

```bash
curl http://localhost:9222/json/version
```

### Example 2: Advanced Usage

Connect via WebSocket: ws://localhost:9222/devtools/browser/...

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell? No, [[Bypass User Account Control]] Bypass UAC? For web: [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Open port 9222 on internal services
- Unauthorized /json requests in Chrome logs

## Related Procedures


## Related Tools

- [[tools/puppeteer]]
- [[tools/selenium]]

## References

- Official documentation: https://chromedevtools.github.io/devtools-protocol/
