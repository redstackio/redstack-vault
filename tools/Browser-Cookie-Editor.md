---
url: >-
  https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg
tags:
  - cookie-management
  - session-hijacking
type: tool
verified: false
platforms:
  - Web
  - Browser
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:47.924Z'
id: 8ec5b982-97fc-4843-bdf7-608d85b736eb
validated: true
submitted: true
---
# Browser-Cookie-Editor

**Status**: Unverified

## Overview

Browser Cookie Editor is a browser extension (e.g., EditThisCookie for Chrome/Firefox) used in security testing to view, edit, export, and import cookies, facilitating session hijacking and authentication bypass scenarios.

## Description

This tool allows manipulation of HTTP cookies in real-time, essential for extracting session tokens post-authentication or injecting stolen cookies. In offensive operations, it's used to replicate sessions across browsers, as in 2FA bypass attacks. Supports JSON export/import for portability.

## Features

- Feature 1: View all domain cookies with values and expiration
- Feature 2: Export/import cookies in JSON, Netscape, or raw format
- Feature 3: Edit cookie attributes like path, domain, and secure flags

## Installation

### Requirements

- Compatible browser (Chrome, Firefox, Edge)
- Extension store access

### Install Commands

No CLI install; use browser store:

```bash
# For automation, use Selenium or manual install
```

## Basic Usage

```bash
tool-name --help
```

Click extension icon on any page to access cookie list.

### Common Options

| Option | Description |
|--------|-------------|
| Export | Save cookies to file/clipboard |
| Import | Load from file/clipboard |
| Edit | Modify individual cookie values |

## Examples

### Example 1: Basic Usage

- On target site, click extension > Export All > Copy to clipboard.

### Example 2: Advanced Usage

- Import JSON: Click Import > Paste JSON > Apply to domain.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Browser extension logs showing cookie modifications
- Anomalous cookie patterns in traffic (e.g., mismatched user-agents)
- Extension installation traces in browser profiles

## Related Procedures


## Related Tools

- [[tools/Evilginx2]]

## References

- Official Chrome Web Store page
- Mozilla Add-ons for Firefox version
