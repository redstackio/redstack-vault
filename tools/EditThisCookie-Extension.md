---
url: >-
  https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg
tags:
  - cookies
  - browser
type: tool
verified: false
platforms:
  - Web
  - Browser
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.635Z'
id: 00922467-24f6-497a-998f-dcbb7fa8c4b3
validated: true
submitted: true
---
# EditThisCookie-Extension

**Status**: Unverified

## Overview

EditThisCookie is a Chrome browser extension for viewing, editing, exporting, and importing cookies on websites, commonly used in security testing to manipulate session cookies for vulnerability assessment like session hijacking.

## Description

This tool allows security researchers to inspect and modify cookies in real-time, facilitating tests for persistence, theft, and reuse in web applications. It's particularly useful for OWASP A2 Broken Authentication scenarios, enabling export/import without developer tools. No server-side access required; operates client-side.

## Features

- Feature 1: View all cookies for a domain with details (name, value, expiry)
- Feature 2: Edit, add, or delete individual cookies
- Feature 3: Export cookies as JSON/Netscape format for backup/sharing
- Feature 4: Import cookies from files to restore sessions

## Installation

### Requirements

- Google Chrome browser (or Chromium-based)
- Internet access for Chrome Web Store

### Install Commands

No CLI install; browser-based:

1. Go to Chrome Web Store
2. Search for "EditThisCookie"
3. Click 'Add to Chrome' and confirm

## Basic Usage

Click the extension icon in the toolbar while on a webpage to open the cookie manager.

### Common Options

| Option | Description |
|--------|-------------|
| Export | Save cookies to clipboard or file |
| Import | Load cookies from JSON/text |
| Delete All | Clear cookies for domain |

## Examples

### Example 1: Basic Usage

1. Navigate to target site (e.g., hackerone.com)
2. Click extension icon
3. View cookies list

### Example 2: Advanced Usage

1. Export: Select domain > Export as JSON > Copy to file
2. Later import: Open extension > Import > Paste JSON > Apply

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Browser extension logs or installed extensions inventory
- Anomalous cookie modifications in web app access logs
- Network traces showing repeated session initiations from same IP

## Related Procedures


## Related Tools

- [[Developer Tools (Browser)]
- [[Cookie-Editor-Extension]]

## References

- Official Chrome Web Store page
- OWASP Testing Guide for Session Management
