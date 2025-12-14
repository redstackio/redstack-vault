---
url: 'https://ftp.mozilla.org/pub/firefox/releases/69.0/'
tags:
  - browser
  - vulnerable
  - testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:24.163Z'
id: d1e16971-b0ac-4f79-8bda-9071a81528f1
validated: true
submitted: true
---
---

# Firefox-69

**Status**: Unverified

## Overview

Firefox 69 is an older browser version vulnerable to a CSP bypass allowing javascript: URLs in <object> tags, used here to demonstrate XSS execution in the Tumblr attack.

## Description

This release of Firefox (September 2019) lacks patches for certain CSP enforcement issues, enabling drive-by JS execution despite restrictive policies. It's ideal for reproducing legacy browser vulnerabilities in web security testing.

## Features

- Feature 1: Standard browsing with dev tools
- Feature 2: Vulnerable CSP handling for <object> elements
- Feature 3: Session cookie management for testing theft

## Installation

### Requirements

- Compatible OS (Windows, macOS, Linux)
- ~200MB disk space

### Install Commands

```bash
# Download and extract for Linux
wget https://ftp.mozilla.org/pub/firefox/releases/69.0/linux-x86_64/en-US/firefox-69.0.tar.bz2
 tar -xjf firefox-69.0.tar.bz2
 ./firefox/firefox
```

## Basic Usage

```bash
firefox
```

### Common Options

| Option | Description |
|--------|-------------|
| `-P` | Create profile |
| `--no-remote` | Open new instance |

## Examples

### Example 1: Basic Usage

```bash
firefox https://www.tumblr.com/abuse/start?prefill=<payload>
```

### Example 2: Advanced Usage

```bash
firefox -P "TestProfile" --no-remote
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of outdated Firefox binaries
- Traffic to vulnerability demo sites
- Alert on legacy browser user agents

## Related Procedures


## Related Tools

- [[Modern Browsers for Comparison]]

## References

- Official download: https://ftp.mozilla.org/pub/firefox/releases/69.0/
- CSP bypass details: Mozilla bug trackers

