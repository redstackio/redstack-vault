---
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - web-testing
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Web browser used for testing and demonstrating web vulnerabilities like XSS.
id: 2eb334a6-3f36-4877-b524-2ea58d8b3a23
created_at: '2025-12-13T09:01:26.566Z'
updated_at: '2025-12-13T09:01:26.566Z'
verified: false
validated: true
submitted: true
---
# Firefox Browser

**Status**: Unverified

## Overview

Firefox is a free and open-source web browser developed by Mozilla, commonly used in security testing for loading URLs, inspecting elements, and demonstrating client-side vulnerabilities such as XSS.

## Description

Firefox provides developer tools for network monitoring, element inspection, and JavaScript debugging, making it ideal for offensive security operations involving web exploits. In this context, it was used to load crafted URLs and trigger XSS payloads.

## Features

- Built-in developer tools for inspecting HTML and JavaScript
- Support for extensions like privacy and security add-ons
- Cross-platform compatibility

## Installation

### Requirements

- Compatible operating system (Linux, Windows, macOS)
- Internet connection for download

### Install Commands

Download from official site or use package managers:

```bash
# On Ubuntu
sudo apt install firefox
```

## Basic Usage

```bash
firefox --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--new-window URL` | Open URL in new window |

## Examples

### Example 1: Basic Usage

```bash
firefox https://example.com
```

### Example 2: Advanced Usage

```bash
firefox --private-window https://auth2.zomato.com/oauth2/fallbacks/error?error=xss&error_description=xsssy&error_hint=%3Cmarquee%20loop%3d1%20width%3d0%20onfinish%3dco%5Cu006efirm(document.cookie)%3EXSS%3C%2fmarquee%3E
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser user-agent strings in web logs
- Anomalous URL accesses with encoded payloads

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Chrome Browser]]
- [[Burp Suite]]

## References

- Official Mozilla Firefox documentation
- Security testing guides using Firefox
