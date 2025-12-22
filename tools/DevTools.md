---
url: 'https://developer.chrome.com/docs/devtools/'
tags:
  - debugging
  - inspection
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.781Z'
id: 0b4ff261-4f64-4dd1-ba8b-60bffaa0da47
validated: true
submitted: true
---
# DevTools

**Status**: Unverified

## Overview

Browser Developer Tools (e.g., Chrome DevTools) for inspecting, debugging, and analyzing web applications, commonly used in security testing to monitor network requests, DOM changes, and console errors during XSS exploitation.

## Description

Built into modern browsers, DevTools provides tabs for Elements, Console, Sources, and Network to dissect page behavior. In offensive security, it's essential for validating injections, observing failed loads, and debugging payloads without external tools.

## Features

- Feature 1: Network tab for request/response inspection
- Feature 2: Console for JS execution and error logging
- Feature 3: Elements tab for DOM manipulation and tag verification

## Installation

### Requirements

- Modern browser (Chrome, Firefox, Edge)

### Install Commands

No installation; access via F12 or right-click > Inspect.

## Basic Usage

```bash
# No CLI; browser shortcut: F12
```

### Common Options

| Option | Description |
|--------|-------------|
| Network | Monitor HTTP requests |
| Console | Run/eval JS |

## Examples

### Example 1: Basic Usage

F12 > Network > Reload to see requests.

### Example 2: Advanced Usage

Elements > Search for '<base>' to confirm injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]
- [[JavaScript]]

### Tactics

- [[Discovery]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser extensions or dev mode enabled
- Unusual console logs in app monitoring

## Related Procedures

- [[procedures/Observe-Failed-Script-Loads-in-DevTools]]

## Related Tools

- [[tools/Web-Server]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools
