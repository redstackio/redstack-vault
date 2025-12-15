---
url: 'https://support.google.com/chrome/answer/95464'
tags:
  - privacy
  - testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.171Z'
id: 6bfc3308-89df-493c-82e3-e726da654b89
validated: true
submitted: true
---
# Incognito-Mode-Browser

**Status**: Unverified

## Overview

Incognito (or private browsing) mode in browsers like Chrome or Firefox, used to simulate unauthenticated sessions by isolating cookies, cache, and history, ideal for testing public access to web applications without prior login state.

## Description

This mode prevents persistence of session data, allowing clean tests of authentication bypasses or public endpoints. In security testing, it's crucial for verifying if resources like profiles are accessible without credentials, as in GraphQL disclosure scenarios.

## Features

- Feature 1: No cookie/storage persistence between sessions
- Feature 2: Blocks site tracking via history
- Feature 3: Allows extension use if enabled

## Installation

### Requirements

- Web browser supporting private mode

### Install Commands

No installation; Ctrl+Shift+N in Chrome/Firefox.

## Basic Usage

```bash
# Browser shortcut: Ctrl+Shift+N
```

### Common Options

| Option | Description |
|--------|-------------|
| Ctrl+Shift+N | Open incognito window |
| --incognito | Launch browser in incognito (CLI) |

## Examples

### Example 1: Basic Usage

Open incognito, navigate to https://hackerone.com/brdoors3?type=user.

### Example 2: Advanced Usage

Combine with DevTools to capture unauthenticated requests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Requests lacking session cookies
- IP patterns from testing environments

## Related Procedures

- [[procedures/Disable-Feedback-Visibility-and-Query-GraphQL-for-Disclosure]]

## Related Tools

- [[tools/Browser-Developer-Tools]]

## References

- Official documentation: https://support.google.com/chrome/answer/95464
