---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567894
url: 'https://developer.chrome.com/docs/devtools/'
tags:
  - browser-devtools
  - debugging
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:43.942Z'
validated: true
submitted: true
---
# Google-Chrome-Developer-Tools

**Status**: Unverified

## Overview

Google Chrome Developer Tools is a built-in suite for debugging, inspecting, and modifying web pages, commonly used in security testing to simulate environments like mobile User-Agents and test vulnerabilities such as XSS.

## Description

DevTools provides tabs for Elements, Console, Sources, Network, and more, enabling real-time inspection of HTML, CSS, JS, and network requests. In offensive security, it's essential for payload crafting, User-Agent spoofing, and verifying exploit execution without external tools.

## Features

- Feature 1: Network throttling and User-Agent override for simulating devices.
- Feature 2: Console for executing JavaScript and testing payloads.
- Feature 3: Elements inspector to view reflected HTML injections.

## Installation

### Requirements

- Google Chrome browser installed.

### Install Commands

No separate installation; access via F12 or right-click > Inspect.

## Basic Usage

```bash
# Launch Chrome and open DevTools
chrome --remote-debugging-port=9222
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open DevTools |
| Ctrl+Shift+I | Alternative shortcut |

## Examples

### Example 1: Basic Usage

Press F12, go to Network > User agent > Custom, set mobile UA, reload page.

### Example 2: Advanced Usage

In Console tab: `document.domain` to test JS context.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser logs showing DevTools access.
- Anomalous User-Agent changes in server logs.

## Related Procedures


## Related Tools

- [[tools/Google-Chrome]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: Chrome DevTools security guides
