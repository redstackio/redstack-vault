---
id: t-chrome-browser
url: 'https://www.google.com/chrome/'
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
updated_at: '2025-12-14T03:47:12.964Z'
validated: true
submitted: true
---
# Chrome Browser

**Status**: Unverified

## Overview

Google Chrome is a widely used web browser for testing web vulnerabilities like XSS, providing developer tools for inspection and payload execution.

## Description

Chrome's capabilities include a robust DevTools suite for debugging HTML/JS, network monitoring, and console for script testing. In offensive security, it's used to reproduce exploits, inspect reflections, and verify payload impacts on public sites.

## Features

- Feature 1: Developer Tools (Elements, Console, Network tabs)
- Feature 2: Built-in JS debugger
- Feature 3: Support for extensions like tamper-proof for manipulation

## Installation

### Requirements

- Compatible OS (Windows, macOS, Linux)
- Internet connection

### Install Commands

```bash
# Download from official site or use package manager
# On Ubuntu: sudo apt update && sudo apt install google-chrome-stable
# On macOS: brew install --cask google-chrome
```

## Basic Usage

```bash
# Launch Chrome
google-chrome
```

### Common Options

| Option | Description |
|--------|-------------|
| `--disable-web-security` | Disable CORS for testing (use cautiously) |
| `--user-data-dir=/tmp/chrome` | Use temporary profile |

## Examples

### Example 1: Basic Usage

Launch and navigate to URL:

```bash
google-chrome https://www.glassdoor.co.in/Job/test
```

### Example 2: Advanced Usage

With dev tools open (F12) to inspect XSS:

```bash
google-chrome --auto-open-devtools-for-tabs https://target.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser user-agent strings in logs
- DevTools network requests

## Related Procedures


## Related Tools

- [[tools/Firefox-Browser]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: OWASP Testing Guide
