---
id: tool-chrome-devtools
url: 'https://developer.chrome.com/docs/devtools/'
tags:
  - browser
  - debugging
  - network-inspection
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.631Z'
validated: true
submitted: true
---
# Chrome-DevTools

**Status**: Unverified

## Overview

Chrome DevTools is a built-in suite in Google Chrome for debugging web pages, used here to inspect network requests and DOM changes demonstrating the XSS exploit impact.

## Description

DevTools provides tabs for Elements, Network, and Console to examine <base> tag insertions and cross-origin fetches, essential for verifying protocol-relative URL behavior in real-time.

## Features

- Feature 1: Network tab for request monitoring
- Feature 2: Elements inspector for DOM analysis
- Feature 3: Console for JS execution testing

## Installation

### Requirements

- Google Chrome browser

### Install Commands

No installation needed; press F12 or Ctrl+Shift+I in Chrome.

## Basic Usage

Open DevTools and select tabs as needed.

### Common Options

| Option | Description |
|--------|-------------|
| Network tab | Monitor HTTP requests |
| Elements tab | Inspect HTML/JS |

## Examples

### Example 1: Basic Usage

Load manipulated URL, open Network tab, reload to see requests to assessmentbase.

### Example 2: Advanced Usage

In Elements tab, search for 'base' tag to confirm href attribute.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser debugging sessions (minimal footprint)
- Console errors from failed requests

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: MDN Web Docs
