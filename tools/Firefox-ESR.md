---
url: 'https://www.mozilla.org/en-US/firefox/enterprise/'
tags:
  - browser
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.206Z'
configuration: Version 52.7.3 (64-bit)
id: 0ad50d33-f05c-49f9-a93e-732a3134e500
validated: true
submitted: true
---
# Firefox-ESR

**Status**: Unverified

## Overview

Firefox Extended Support Release (ESR) is a stable browser version for enterprises, used here to access and demonstrate XSS execution in vulnerable web pages like the http-file-server listing.

## Description

Firefox ESR provides long-term support with security patches. In pentesting, it's used for manual verification of client-side vulnerabilities, offering developer tools for inspection.

## Features

- Feature 1: Developer tools for JS debugging
- Feature 2: Extensions for security testing
- Feature 3: Cross-platform support

## Installation

### Requirements

- Linux with package manager

### Install Commands

```bash
# Ubuntu
sudo apt update
sudo apt install firefox-esr
```

## Basic Usage

```bash
firefox-esr --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-P` | Profile manager |
| `--new-instance` | New instance |

## Examples

### Example 1: Basic Usage

```bash
firefox-esr http://localhost:8080/
```

### Example 2: Advanced Usage

```bash
firefox-esr --no-remote http://localhost:8080/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser process with firefox-esr
- Network requests to localhost
- JS alerts or console logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/nodejs]]

## References

- Official documentation: https://www.mozilla.org/en-US/firefox/enterprise/
