---
id: tool-uuid-1
url: 'https://addons.mozilla.org/en-US/firefox/addon/eval-villain/'
tags:
  - browser-extension
  - xss-detection
  - logging
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:15.764Z'
validated: true
submitted: true
---
# Eval-Villain

**Status**: Unverified

## Overview

Eval Villain is a Firefox extension designed for security researchers to detect and analyze eval-based vulnerabilities by capturing strings passed to dangerous JavaScript functions like document.write, eval, and document.domain.

## Description

The tool intercepts and logs arguments to risky APIs, helping identify injection points in dynamic scripts such as ads. It's commonly used in web pentesting to uncover DOM XSS or other client-side issues, providing detailed traces for reproduction and reporting.

## Features

- Feature 1: Real-time logging of strings to eval, document.write, etc.
- Feature 2: Exportable logs for analysis (e.g., TXT files).
- Feature 3: Browser-specific interception without server-side changes.

## Installation

### Requirements

- Firefox browser (version 50+).
- No additional dependencies.

### Install Commands

No CLI install; use Firefox Add-ons:

1. Visit https://addons.mozilla.org/en-US/firefox/addon/eval-villain/.
2. Click 'Add to Firefox'.

## Basic Usage

Enable via extensions menu; it runs passively on page loads.

### Common Options

| Option | Description |
|--------|-------------|
| Enable/Disable | Toggle logging in extension popup |
| Clear Logs | Reset captured data |

## Examples

### Example 1: Basic Usage

Load a page with dynamic scripts; check popup for logs.

### Example 2: Advanced Usage

On a vulnerable site, export logs after triggering injections.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Active Scanning]]

### Tactics

- [[Discovery]]
- [[Resource Development]]

## Detection

Indicators and methods for detecting this tool's usage:

- Firefox extension list includes 'Eval Villain'.
- Network traces show no extra requests, but console logs may appear.

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[DOM Invader]]

## References

- Official documentation: Firefox Add-ons page
- Related resources: OWASP DOM-based XSS Prevention Cheat Sheet
