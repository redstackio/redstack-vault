---
url: 'https://addons.mozilla.org/en-US/firefox/addon/tamper-data/'
tags:
  - proxy
  - tamper
  - http
type: tool
platforms:
  - Web
  - Firefox
description: >-
  Firefox extension for intercepting and modifying HTTP requests, particularly
  useful for bypassing client-side validations in web uploads.
id: 8e295be3-01d2-4aab-85bf-ad8ac7218d9d
created_at: '2025-12-13T23:56:03.266Z'
updated_at: '2025-12-13T23:56:03.266Z'
verified: false
validated: true
submitted: true
---
# TamperData

**Status**: Unverified

## Overview

TamperData is a Firefox proxy tool for viewing, inspecting, and modifying HTTP/HTTPS communications. In security testing, it's used to bypass client-side restrictions like file upload validations by altering POST data on-the-fly.

## Description

It acts as a man-in-the-middle for browser requests, allowing edits to headers, bodies, and parameters. Common in web app pentesting for simulating attacks like parameter pollution or content injection. For WordPress exploits, it enables Unicode filename insertion and script bypassing.

## Features

- Feature 1: Real-time request interception and editing
- Feature 2: Support for POST, GET, and multipart/form-data
- Feature 3: Logging of all tampered sessions for review

## Installation

### Requirements

- Firefox browser version 50+

### Install Commands

No CLI install; use Firefox Add-ons:

1. Visit the Mozilla Add-ons page.
2. Search for "Tamper Data" and install.
3. Restart Firefox.

## Basic Usage

```bash
# No CLI; browser-based
```

Open Tools > Tamper Data > Start Tamper.

### Common Options

| Option | Description |
|--------|-------------|
| Start Tamper | Begin intercepting requests |
| Stop Tamper | End interception |
| Tamper | Edit selected request |

## Examples

### Example 1: Basic Usage

Start TamperData, perform an upload; edit filename in the popup to add Unicode.

### Example 2: Advanced Usage

Intercept POST to `/async-upload.php`, modify `name` field to '±file.png' and content-type.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual browser proxy settings or extension logs
- Server logs showing malformed or tampered requests
- Network traffic anomalies from Firefox user-agent

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Fiddler]]

## References

- Official documentation: https://add0n.com/tamper-data.html
- Related resources: OWASP Testing Guide on request tampering
