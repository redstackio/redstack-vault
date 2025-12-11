---
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - testing
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Web browser used for testing and reproducing web vulnerabilities like XSS.
id: 63d5c617-38a8-45ad-af29-0fd459d822d3
created_at: '2025-12-11T06:10:28.629Z'
updated_at: '2025-12-11T06:10:28.629Z'
verified: false
validated: true
submitted: true
---
# Firefox

**Status**: Unverified

## Overview

Firefox is a free and open-source web browser developed by Mozilla, commonly used in security testing for reproducing vulnerabilities such as cross-site scripting (XSS) by accessing malicious URLs and observing JavaScript execution.

## Description

Firefox provides developer tools for inspecting network requests, debugging JavaScript, and testing web application security. In offensive security, it's used to trigger client-side vulnerabilities without interference from extensions or security features in other browsers.

## Features

- Built-in developer console for JavaScript debugging
- Support for inspecting and modifying HTTP requests
- Customizable with add-ons for security testing

## Installation

### Requirements

- Compatible OS (Linux, Windows, macOS)
- Internet connection for download

### Install Commands

```bash
# Download from official site or use package manager
e.g., sudo apt install firefox (on Debian-based systems)
```

## Basic Usage

```bash
firefox --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--new-window URL` | Open URL in new window |
| `--private-window` | Open in private browsing mode |

## Examples

### Example 1: Basic Usage

```bash
firefox https://example.com
```

### Example 2: Advanced Usage

```bash
firefox --new-window https://www.glassdoor.com/employers/sem-dual-lp/?utm_source=malicious
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor browser traffic for suspicious URLs
- Log access to known vulnerable endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Chrome]]
- [[Burp Suite]]

## References

- https://www.mozilla.org/en-US/firefox/new/
- Mozilla Developer Network
