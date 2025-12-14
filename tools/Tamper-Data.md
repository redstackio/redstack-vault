---
id: tool-tamper-data-001
url: 'https://addons.mozilla.org/en-US/firefox/addon/tamper-data/'
tags:
  - browser-extension
  - request-editing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.692Z'
validated: true
submitted: true
---
# Tamper-Data

**Status**: Unverified

## Overview

Tamper Data is a Firefox extension for intercepting and editing HTTP/HTTPS requests and responses. It's particularly effective for testing web form vulnerabilities by allowing on-the-fly changes to parameters, such as invalidating email inputs in applications like Gratipay.

## Description

Tamper Data starts a proxy on demand, captures requests, and opens an editor for headers and body before forwarding. In security assessments, it's used to simulate attacks like input manipulation without external tools. It supports URL encoding and basic authentication handling, making it suitable for quick exploits of validation weaknesses.

## Features

- Feature 1: Request interception with full body editing.
- Feature 2: Header modification and cookie handling.
- Feature 3: Export logs for further analysis.

## Installation

### Requirements

- Firefox browser.

### Install Commands

Install via Add-ons manager.

```bash
# No CLI; browser-based
```

## Basic Usage

Activate Tamper Data before browsing, submit form, edit in popup, send.

### Common Options

| Option | Description |
|--------|-------------|
| Start Tamper | Begin interception |
| Edit & Resend | Modify and forward |

## Examples

### Example 1: Basic Usage

Enable tamper, submit Gratipay email form, edit 'address' to invalid, resend.

### Example 2: Advanced Usage

Tamper multiple requests in sequence for chained tests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Proxy-like delays in request timing.
- Anomalous parameter values in logs.
- Firefox-specific extension artifacts.

## Related Procedures


## Related Tools

- [[tools/Burp-Repeater]]
- [[tools/Live-HTTP-Headers]]

## References

- Official documentation: Mozilla Add-ons
- Related resources: OWASP proxy tools guide
