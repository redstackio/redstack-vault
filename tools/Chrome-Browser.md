---
url: null
tags:
  - browser
  - web
type: tool
platforms:
  - Web
description: Web browser for generating and intercepting HTTP requests
id: a31fc7e7-0c66-4849-99d0-303b4f5edb03
created_at: '2025-12-13T09:01:21.613Z'
updated_at: '2025-12-13T09:01:21.613Z'
verified: false
validated: true
submitted: true
---
# Chrome Browser

**Status**: Unverified

## Overview

Google Chrome is a web browser used for browsing sites and generating HTTP requests, often in conjunction with proxies like Burp Suite for security testing.

## Description

It supports developer tools for inspecting network traffic and can be configured to route traffic through proxies for interception and modification in vulnerability testing scenarios.

## Features

- Feature 1: Network traffic inspection
- Feature 2: Proxy configuration
- Feature 3: Extension support for security tools

## Installation

### Requirements

- Compatible OS
- Internet access

### Install Commands

```bash
# Download from official site and install
```

## Basic Usage

```bash
# Launch Chrome
chrome
```

### Common Options

| Option | Description |
|--------|-------------|
| `--proxy-server` | Set proxy |
| `--incognito` | Private browsing |

## Examples

### Example 1: Basic Usage

```bash
chrome https://twitter.com
```

### Example 2: Advanced Usage

```bash
chrome --proxy-server="http://localhost:8080" https://twitter.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Browser fingerprinting
- Detection method 2: Proxy configuration changes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Firefox]]
- [[tools/Burp-Suite]]

## References

- Official documentation: https://www.google.com/chrome
