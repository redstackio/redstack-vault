---
id: tool-firefox
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - testing
  - web
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.807Z'
validated: true
submitted: true
---
# Firefox-Browser

**Status**: Unverified

## Overview

Firefox is an open-source web browser used for accessing web applications, testing vulnerabilities like SSRF by simulating victim interactions, and viewing local interfaces such as ngrok dashboards.

## Description

In security testing, Firefox (version 80.0.1 as used here) provides developer tools for inspecting network requests, but in this context, it's primarily for loading malicious URLs to trigger server-side exploits. It's cross-platform and supports extensions for proxying or tampering.

## Features

- Feature 1: Built-in developer tools for network inspection
- Feature 2: Privacy-focused with no telemetry by default
- Feature 3: Extension ecosystem for security testing (e.g., FoxyProxy)

## Installation

### Requirements

- Compatible OS (Linux, macOS, Windows)
- Internet for download

### Install Commands

```bash
# Linux (Ubuntu/Debian)
sudo apt update
sudo apt install firefox

# Or download from Mozilla
wget https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US

tar xjf firefox-*.tar.bz2
sudo mv firefox /opt/
```

## Basic Usage

```bash
firefox https://example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help (via firefox --help) |
| `-P` | Open profile manager |
| `-no-remote` | Allow multiple instances |

## Examples

### Example 1: Basic Usage

```bash
firefox http://127.0.0.1:4040
```

Opens ngrok interface locally.

### Example 2: Advanced Usage

```bash
firefox --new-instance https://malicious-url.com
```

Launches isolated instance for victim simulation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]
- [[T1566.001]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser process (firefox.exe) accessing suspicious URLs
- Network logs showing requests from known browser User-Agents
- Extension installations for proxy or dev tools

## Related Procedures

- [[procedures/Access-Malicious-URL-and-Capture-Victim-Request]]

## Related Tools

- [[Related Tool: Chrome]]
- [[Related Tool: Burp Suite Browser Extension]]

## References

- Official documentation: https://support.mozilla.org/en-US/products/firefox
- Related resources: Mozilla Developer Network (MDN) for web testing
