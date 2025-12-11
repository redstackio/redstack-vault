---
url: null
tags:
  - debugging
  - network-inspection
type: tool
platforms:
  - Web
description: >-
  Built-in browser developer tools for inspecting network requests and debugging
  web applications.
id: 64d57ada-0467-4240-8c81-ea528cf29c3c
created_at: '2025-12-11T03:47:49.880Z'
updated_at: '2025-12-11T03:47:49.880Z'
verified: false
validated: true
submitted: true
---
# Browser DevTools

**Status**: Unverified

## Overview

Browser DevTools are integrated tools in modern browsers like Chrome and Firefox, used for inspecting elements, network traffic, and debugging JavaScript in security testing.

## Description

Primarily used to monitor failing script imports and network requests during XSS exploitation, helping identify paths for hosting malicious files.

## Features

- Network request inspection
- Console for JavaScript execution
- Element inspector for DOM manipulation

## Installation

### Requirements

- Modern web browser (Chrome, Firefox)

### Install Commands

No installation needed; access via F12 or right-click > Inspect.

## Basic Usage

```bash
# Open in browser: Press F12
```

### Common Options

| Option | Description |
|--------|-------------|
| Network tab | View requests |
| Console tab | Run JS |

## Examples

### Example 1: Basic Usage

Open DevTools and reload page to inspect failed loads.

### Example 2: Advanced Usage

Filter network requests for JS files.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[procedures/Trigger-and-Verify-XSS-Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser activity logs
- Anomalous debugging sessions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #burpsuite

## References

- Chrome DevTools documentation
