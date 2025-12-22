---
id: tool-live-http-headers-001
url: 'https://addons.mozilla.org/en-US/firefox/addon/live-http-headers/'
tags:
  - browser-extension
  - http-interception
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.700Z'
validated: true
submitted: true
---
# Live-HTTP-Headers

**Status**: Unverified

## Overview

Live HTTP Headers is a Firefox browser extension for real-time monitoring, logging, and modification of HTTP traffic. It's useful in security testing for capturing and editing form submissions, such as tampering with email parameters in web apps like Gratipay to test validation bypasses.

## Description

The extension displays incoming and outgoing headers live, allows pausing and resuming requests, and supports basic editing of request bodies. In offensive security, it's employed for quick interception without full proxy setups, ideal for modifying POST data like 'address' in email APIs. It logs sessions for review and integrates with Firefox's developer tools.

## Features

- Feature 1: Live header viewing and request/response logging.
- Feature 2: Pause/resume functionality for interception.
- Feature 3: Simple body editing for parameter changes.

## Installation

### Requirements

- Firefox browser version 50+.

### Install Commands

No CLI install; add via Firefox Add-ons store.

```bash
# Manual: Download XPI and load in about:debugging
```

## Basic Usage

Enable the extension, open the Headers tab, and start capturing during browsing.

### Common Options

| Option | Description |
|--------|-------------|
| Log All | Capture all traffic |
| Pause | Halt requests for editing |

## Examples

### Example 1: Basic Usage

Navigate to Gratipay settings, submit form; pause request in Headers tab, edit body, resume.

### Example 2: Advanced Usage

Filter by POST method, log to file for analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Firefox extension traffic patterns in browser logs.
- Delayed requests indicating manual pauses.
- Modified headers not matching standard browser signatures.

## Related Procedures


## Related Tools

- [[tools/Burp-Repeater]]
- [[tools/Tamper-Data]]

## References

- Official documentation: Mozilla Add-ons page
- Related resources: Firefox Developer Tools docs
