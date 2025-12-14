---
id: tool-chrome-devtools-001
url: 'https://developer.chrome.com/docs/devtools/'
tags:
  - debugging
  - inspection
  - web-security
type: tool
verified: false
platforms:
  - Web
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.965Z'
validated: true
submitted: true
---
# Chrome-Developer-Tools

**Status**: Unverified

## Overview

Chrome Developer Tools is a built-in suite in Google Chrome for inspecting, debugging, and modifying web pages, commonly used in security testing for cookie manipulation, network monitoring, and script execution observation.

## Description

DevTools provides tabs like Elements, Console, Sources, and Network for real-time analysis. In offensive security, it's essential for tampering with client-side storage (e.g., cookies, localStorage) and tracing payload reflections in responses. Features include breakpoint setting, DOM editing, and resource overriding.

## Features

- Feature 1: Cookie editing and URL decoding for injection testing
- Feature 2: Network tab for capturing API requests/responses
- Feature 3: Console for executing and debugging JavaScript payloads

## Installation

### Requirements

- Google Chrome browser installed

### Install Commands

No installation needed; access via F12 or right-click > Inspect.

## Basic Usage

```bash
# No CLI; browser-based
```

### Common Options

| Option | Description |
|--------|-------------|
| F12 | Open DevTools |
| Ctrl+Shift+I | Toggle inspector |
| Network tab | Monitor requests |

## Examples

### Example 1: Basic Usage

Open DevTools (F12), go to Application > Cookies, edit a cookie value.

### Example 2: Advanced Usage

In Console, paste and run: document.cookie = 'location=%7B%22city%22%3A%22%3Cscript%3Ealert(1)%3C/script%3E%22%7D';

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Gather Victim Host Information]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser process anomalies (e.g., high CPU during inspection)
- Network logs showing repeated requests from devtools

## Related Procedures


## Related Tools

- [[tools/Web-Browser-Chrome]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Related resources: MDN Web Docs on Cookies
