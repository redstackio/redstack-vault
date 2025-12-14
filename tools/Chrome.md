---
url: 'https://www.google.com/chrome/'
tags:
  - browser
  - testing
  - xss-repro
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.305Z'
id: 3533ba39-7dbe-4d37-9e78-403c8ee0b77b
validated: true
submitted: true
---
# Chrome

**Status**: Unverified

## Overview

Google Chrome is a widely-used web browser for security testing, particularly effective in reproducing XSS vulnerabilities due to its robust JavaScript engine (V8) and dev tools.

## Description

Chrome renders GitLab's Markdown without blocking onload in image tags, allowing XSS payloads to execute. It's preferred for cross-browser verification alongside Firefox, providing console for error inspection.

## Features

- Feature 1: Chrome DevTools for network monitoring and script debugging
- Feature 2: Fast JavaScript execution for reliable payload testing
- Feature 3: Incognito mode for isolated sessions during exploits

## Installation

### Requirements

- Compatible OS
- Internet for download

### Install Commands

```bash
# Linux (Ubuntu)
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
sudo apt update && sudo apt install google-chrome-stable
```

## Basic Usage

```bash
google-chrome https://gitlab.example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `--incognito` | Open in private mode |
| `--disable-web-security` | Disable CORS for testing (use cautiously) |
| `--remote-debugging-port=9222` | Enable remote debugging |

## Examples

### Example 1: Basic Usage

```bash
google-chrome
```
Navigate to target manually.

### Example 2: Advanced Usage

```bash
google-chrome --incognito https://gitlab.example.com/issues
```
Test in isolated session.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-agent logs showing Chrome
- DevTools usage via performance metrics

## Related Procedures


## Related Tools

- [[tools/Firefox]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: Chromium Security
