---
id: tool-universal_xss.html
url: null
tags:
  - poc
  - xss
  - clickjacking
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.159Z'
validated: true
submitted: true
---
# universal_xss.html

**Status**: Unverified

## Overview

universal_xss.html is a proof-of-concept HTML file that sends unvalidated postMessage to the Kaspersky URL Advisor frame and implements clickjacking to exploit universal XSS.

## Description

This file contains JavaScript to postMessage malicious data (e.g., javascript: URL) to the URL Advisor balloon frame without origin checks, then overlays for clickjacking to trigger execution in any domain's context. Used in testing the vulnerability where the frame assigns unsanitized data to link targets.

## Features

- Feature 1: postMessage injection targeting URL Advisor
- Feature 2: Clickjacking overlay for user interaction
- Feature 3: Alert for JS execution verification

## Installation

### Requirements

- Local HTTP server to host
- Browser with Kaspersky KIS

### Install Commands

```bash
# Download PoC file
curl -o universal_xss.html https://example-poc/universal_xss.html
```

## Basic Usage

```bash
# Serve via server and navigate to it
# Content includes: window.frames['url_advisor'].postMessage({data: 'javascript:alert(...)'}, '*');
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Static HTML; edit JS for custom payloads |

## Examples

### Example 1: Basic Usage

```html
<!-- Simplified: sends postMessage and clickjack -->
<iframe src="/ua/url_advisor_balloon.html"></iframe>
<script>/* postMessage code */</script>
```

### Example 2: Advanced Usage

```html
<!-- Customize alert for exfiltration: fetch('/exfil?data=' + document.cookie) -->
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

- Suspicious postMessage in browser console
- Clickjacking frames in dev tools
- Anomalous alerts on domains

## Related Procedures

- [[procedures/Load-Universal-XSS-POC-in-Microsoft-Edge]]

## Related Tools

- [[tools/server.py]]

## References

- HackerOne report: https://hackerone.com/reports/463915
