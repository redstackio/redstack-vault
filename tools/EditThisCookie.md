---
url: >-
  https://chromewebstore.google.com/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg
tags:
  - browser-extension
  - cookie-management
type: tool
verified: false
platforms:
  - Web
  - Chrome
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.448Z'
id: 81ad0909-1329-4c93-940d-71ef14c09217
validated: true
submitted: true
---
# EditThisCookie

**Status**: Unverified

## Overview

EditThisCookie is a Chrome browser extension for viewing, editing, and exporting cookies from web sessions, ideal for security testing of session hijacking vulnerabilities.

## Description

This tool provides a user-friendly interface to manage site-specific cookies directly in the browser. In offensive security, it's used to extract, modify, or inject cookies during web app assessments, such as testing OAuth session persistence. No installation beyond the extension store is needed.

## Features

- Feature 1: Real-time cookie viewing and search by domain
- Feature 2: Export/import in JSON or Netscape format for easy sharing
- Feature 3: Bulk editing for simulating cookie theft and reinjection

## Installation

### Requirements

- Google Chrome browser version 88 or higher

### Install Commands

No CLI; install via Chrome Web Store.

## Basic Usage

Click the extension icon while on the target site to view cookies.

### Common Options

| Option | Description |
|--------|-------------|
| Export | Download cookies as file |
| Import | Upload cookie file |

## Examples

### Example 1: Basic Usage

On https://micropurchase.18f.gov/, open extension and copy session cookies.

### Example 2: Advanced Usage

Export cookies, clear session, then import to hijack.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Extension presence in browser profiles
- Detection method 2: Unusual cookie modifications in client-side logs

## Related Procedures


## Related Tools

- [[tools/Cookies-Manager-Plus]]
- [[tools/Burp-Suite]]

## References

- Official documentation: Chrome Web Store page
- Related resources: Browser extension security guides
