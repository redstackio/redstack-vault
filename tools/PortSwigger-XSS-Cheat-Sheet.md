---
url: 'https://portswigger.net/web-security/cross-site-scripting/cheat-sheet'
tags:
  - xss
  - payloads
  - bypass
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.429Z'
id: 2ffc93f5-49ad-45eb-afa2-08111ed8f077
validated: true
submitted: true
---
# PortSwigger-XSS-Cheat-Sheet

**Status**: Unverified

## Overview

The PortSwigger XSS Cheat Sheet is an online resource providing a comprehensive list of payloads and bypass techniques for cross-site scripting vulnerabilities, aiding in WAF evasion and payload crafting.

## Description

Maintained by PortSwigger (creators of Burp Suite), this cheat sheet covers encoding methods, context-specific payloads, and filters bypasses, crucial for escalating simple injections to full JS execution in scenarios like the Glassdoor vulnerability.

## Features

- Feature 1: Categorized payloads for different contexts (HTML, JS, etc.)
- Feature 2: Encoding guides for URL, HTML, and polyglots
- Feature 3: Examples for common WAFs and filters

## Installation

### Requirements

- Web browser access

### Install Commands

No installation needed; access via URL.

```bash
# Open in browser
firefox https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
```

## Basic Usage

Browse the page and search for relevant payloads.

### Common Options

N/A (web-based)

## Examples

### Example 1: Basic Usage

Visit the URL and find onerror payloads for img tags.

### Example 2: Advanced Usage

Search for "double encoding" to find bypasses like &amp;#x00028; for parentheses.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- N/A (reference material, not executable)

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
- Related resources: Burp Suite extensions
