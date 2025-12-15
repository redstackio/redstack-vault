---
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:11.337Z'
id: 313c7eb0-d8bd-479d-aaa2-d75aa75b3f24
validated: true
submitted: true
---
# Mozilla-Firefox

**Status**: Unverified

## Overview

Mozilla Firefox is a free, open-source web browser used for accessing web applications and simulating user sessions in security testing, particularly for multi-browser vulnerability assessments like session management flaws.

## Description

Firefox provides robust developer tools for inspecting network requests, cookies, and sessions, making it ideal for testing authentication persistence across instances. In this context, it's used as Browser A to maintain a lingering session during password changes.

## Features

- Feature 1: Built-in Developer Tools for cookie and session inspection
- Feature 2: Profile isolation for multiple independent sessions
- Feature 3: Cross-platform support (Windows, macOS, Linux)

## Installation

### Requirements

- Internet connection
- Compatible OS (Windows 7+, macOS 10.10+, Linux)

### Install Commands

```bash
# Download and install via package manager (Linux example)
sudo apt update && sudo apt install firefox
```

For Windows/macOS, download from official site.

## Basic Usage

```bash
tool-name --help
```

Launch via GUI or command line: `firefox https://bridge.cspr.ng/`

### Common Options

| Option | Description |
|--------|-------------|
| `-P` | Open Profile Manager for isolated sessions |
| `--new-instance` | Launch new instance |

## Examples

### Example 1: Basic Usage

Launch and navigate:

Open Firefox and go to `https://bridge.cspr.ng/`.

### Example 2: Advanced Usage

```bash
firefox -P "SessionTest" https://bridge.cspr.ng/
```

Creates isolated profile for testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing Firefox User-Agent strings
- Multiple sessions from same IP with Firefox fingerprints

## Related Procedures


## Related Tools

- [[tools/Google-Chrome]]

## References

- Official documentation: https://www.mozilla.org/en-US/firefox/developer/
