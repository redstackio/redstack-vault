---
id: tool-firefox-001
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - testing
  - redirect
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:23.256Z'
validated: true
submitted: true
---
# Firefox-Browser-for-Redirect-Testing

**Status**: Unverified

## Overview

Firefox is a web browser essential for testing open redirects, as it follows 301 responses with scheme-relative // locations, unlike Chrome or Safari which block them, making it ideal for reproducing vulnerabilities like the fastify-static issue.

## Description

In security testing, Firefox's lenient handling of ambiguous redirect locations allows demonstration of exploits that may fail in stricter browsers. It's used here to trigger the double-slash path redirect to arbitrary sites, aiding in phishing or SSRF validation.

## Features

- Feature 1: Developer tools for inspecting HTTP responses and redirects
- Feature 2: Cross-platform support with consistent behavior for testing
- Feature 3: Extensions like tampermonkey for custom redirect simulations

## Installation

### Requirements

- Internet connection
- Compatible OS (Linux, Windows, macOS)

### Install Commands

```bash
# Linux (Ubuntu/Debian)
sudo apt update && sudo apt install firefox

# macOS (via Homebrew)
brew install --cask firefox

# Windows: Download from official site
```

## Basic Usage

```bash
firefox
```

### Common Options

| Option | Description |
|--------|-------------|
| `-P` | Open profile manager |
| `--new-instance` | Start new instance |
| `-private` | Open private window |

## Examples

### Example 1: Basic Usage

```bash
firefox http://localhost:3000//google.com/%2e%2e
```

### Example 2: Advanced Usage

Launch with dev tools open:
```bash
firefox --new-instance http://localhost:3000//google.com/%2e%2e
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Phishing]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to localhost:3000 from Firefox user agent
- Browser history or cache showing redirect patterns

## Related Procedures


## Related Tools

- [[tools/Chrome-Browser]]
- [[tools/Burp-Suite]]

## References

- Official documentation: https://www.mozilla.org/en-US/firefox/developer/
- Related resources: MDN Web Docs on HTTP redirects
