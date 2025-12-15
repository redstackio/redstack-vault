---
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.102Z'
id: 039a5b20-385c-48dd-9461-bea7b4a77b35
validated: true
submitted: true
---
# Browser-Firefox

**Status**: Unverified

## Overview

Firefox is a web browser used for security testing, including inspecting network requests, executing JavaScript, and simulating cross-origin attacks like CORS exploitation.

## Description

In offensive security, Firefox's developer tools (Network tab, Console) allow sending custom requests, viewing headers, and running scripts to test web vulnerabilities. It's commonly used for CORS testing due to its robust dev tools and extensions like Firebug or built-in inspector.

## Features

- Feature 1: Network inspector for header analysis
- Feature 2: JavaScript console for executing exploits
- Feature 3: Support for custom User-Agent and request simulation

## Installation

### Requirements

- Compatible OS (Linux, Windows, macOS)

### Install Commands

```bash
# Download from official site or use package manager
sudo apt install firefox  # On Debian/Ubuntu
```

## Basic Usage

```bash
firefox https://nordvpn.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `--devtools` | Open developer tools on startup |
| `-P` | Manage profiles for testing |

## Examples

### Example 1: Basic Usage

```bash
firefox --new-window https://nordvpn.com/wp-json/
```
Open Network tab, send request with custom Origin.

### Example 2: Advanced Usage

```javascript
// In console: Test CORS
fetch('https://nordvpn.com/wp-json/wp/v2/users/1', {credentials: 'include'}).then(r => r.text()).then(alert);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Active Scanning]]

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual browser traffic patterns in logs
- JavaScript execution anomalies on client-side

## Related Procedures

- [[procedures/Test-CORS-Policy-with-Custom-Origin]]
- [[procedures/Exploit-CORS-to-Fetch-User-Data]]

## Related Tools

- [[Burp Suite]]
- [[Chrome Developer Tools]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools
- Related resources: Mozilla Security Blog
