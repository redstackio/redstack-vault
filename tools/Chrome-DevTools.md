---
url: ''
tags:
  - debugging
  - web
type: tool
platforms:
  - Web
description: 'Built-in browser debugging tools for inspecting code, network, and runtime.'
id: e684d642-6d67-46c7-8959-5c4b02ab0fd3
created_at: '2025-12-11T06:10:17.572Z'
updated_at: '2025-12-11T06:10:17.572Z'
verified: false
validated: true
submitted: true
---
# Chrome DevTools

**Status**: Unverified

## Overview

Chrome DevTools is a set of web developer tools built into Google Chrome for debugging, profiling, and inspecting web applications.

## Description

Used for setting breakpoints, searching code, inspecting network traffic, and more in the context of finding XSS in React apps.

## Features

- Code search and pretty print
- Breakpoints and call stack navigation
- Network monitoring with filters

## Installation

### Requirements

- Google Chrome browser

### Install Commands

Built-in, no installation needed.

## Basic Usage

```bash
# Open in Chrome: F12 or Ctrl+Shift+I
```

### Common Options

| Option | Description |
|--------|-------------|
| Sources | Debug code |
| Network | Inspect traffic |

## Examples

### Example 1: Basic Usage

Open DevTools and search for 'dangerously'.

### Example 2: Advanced Usage

Set breakpoint on innerHTML and trace stack.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual browser debugging activity
- Network anomalies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/React-Developer-Tools]]

## References

- https://developer.chrome.com/docs/devtools/
