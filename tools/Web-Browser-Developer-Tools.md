---
id: tool-uuid-003
url: ''
tags:
  - devtools
  - inspection
  - debug
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.251Z'
validated: true
submitted: true
---
# Web-Browser-Developer-Tools

**Status**: Unverified

## Overview

Built-in developer tools in web browsers (e.g., Chrome DevTools, Firefox Inspector) for examining HTML, CSS, JS, and network requests during security testing.

## Description

These tools allow inspection of page source, DOM elements, and resources like image URLs. Essential for extracting backend endpoints from client-side code in web vulns like this S3 disclosure.

## Features

- Feature 1: Element inspector for HTML
- Feature 2: Network tab for requests
- Feature 3: Console for JS execution

## Installation

### Requirements

- Compatible web browser

### Install Commands

Built-in; access via F12 or right-click > Inspect.

## Basic Usage

F12 to open, select Elements tab.

### Common Options

| Option | Description |
|--------|-------------|
| Elements | Inspect DOM |
| Network | View requests |

## Examples

### Example 1: Basic Usage

Right-click image > Inspect to view src.

### Example 2: Advanced Usage

Search for "s3" in Elements to find URLs.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1057.001]] Browser Information Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- JS hooks to detect dev tools open
- Anomalous inspection patterns

## Related Procedures


## Related Tools

- [[tools/Web-Browser]]

## References

- MDN Web Docs: https://developer.mozilla.org/en-US/docs/Tools
