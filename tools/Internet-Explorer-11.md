---
id: tool-uuid-1
url: 'https://www.microsoft.com/en-us/download/details.aspx?id=29041'
tags:
  - browser
  - testing
  - legacy
type: tool
verified: false
platforms:
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.784Z'
validated: true
submitted: true
---
# Internet-Explorer-11

**Status**: Unverified

## Overview

Internet Explorer 11 is a legacy web browser from Microsoft, used here to demonstrate and reproduce the XSS vulnerability due to its weaker Content Security Policy enforcement compared to modern browsers.

## Description

IE11, released in 2013, supports older web standards and lacks robust protections against certain XSS vectors like javascript: URLs. In offensive security, it's used for testing vulnerabilities in legacy contexts or where modern browsers block exploits. Primary use case: Reproducing self-XSS in environments without strict CSP.

## Features

- Feature 1: Basic JavaScript execution without CSP blocks
- Feature 2: Support for legacy URL schemes like javascript:
- Feature 3: Developer tools for inspecting page execution

## Installation

### Requirements

- Windows 7 or later
- Administrative privileges

### Install Commands

```bash
# Download and run installer from Microsoft
# No CLI install; use GUI
```

## Basic Usage

```bash
# Launch via start menu or iexplore.exe
iexplore.exe https://apps.twitter.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-private` | Open in private mode |
| `-k` | Kiosk mode |

## Examples

### Example 1: Basic Usage

Navigate to https://apps.twitter.com and perform login/app creation.

### Example 2: Advanced Usage

Use F12 developer tools to inspect JS execution after payload injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-Agent string containing 'MSIE 11' or 'Trident/7.0'
- Legacy TLS/SSL negotiation patterns

## Related Procedures


## Related Tools

- [[tools/Google-Chrome]]

## References

- Official documentation: Microsoft Docs
- Related resources: XSS testing guides
