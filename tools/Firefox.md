---
id: tool-firefox
type: tool
name: Firefox
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.087Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - browser
  - web-access
url: 'https://www.mozilla.org/en-US/firefox/new/'
validated: true
submitted: true
---

# Firefox

**Status**: Unverified

## Overview

Firefox is an open-source web browser used for accessing and interacting with web applications during security testing, often configured with proxies like Burp Suite for traffic manipulation.

## Description

As a standard browser, Firefox supports extensions for developer tools and proxy configuration, making it ideal for navigating to vulnerable endpoints like forgot password pages and submitting forms while routing traffic through interception tools.

## Features

- Feature 1: Built-in developer tools for inspecting requests
- Feature 2: Easy proxy configuration via network settings
- Feature 3: Extension support for security testing (e.g., FoxyProxy)

## Installation

### Requirements

- Modern OS with graphical interface

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install firefox

# Or download from official site
```

## Basic Usage

```bash
firefox https://target.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `--proxy-server=host:port` | Set proxy for traffic routing |
| `-private` | Open private window |

## Examples

### Example 1: Basic Usage

Launch and visit target:

```bash
firefox http://██████/█████
```

### Example 2: Advanced Usage

With proxy for Burp:

```bash
firefox --proxy-server=127.0.0.1:8080 http://target.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-Agent: Mozilla/5.0 (compatible with Firefox)
- Proxy-related network anomalies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Chrome]]
- [[tools/Safari]]

## References

- Official documentation: https://support.mozilla.org/en-US/products/firefox
- Related resources: Mozilla Developer Network
