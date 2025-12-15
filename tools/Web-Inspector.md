---
url: 'https://developer.chrome.com/docs/devtools/'
tags:
  - browser-devtools
  - inspection
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.831Z'
id: 53f3d2c8-837a-406b-8617-ddaaeaaee8c0
validated: true
submitted: true
---
# Web-Inspector

**Status**: Unverified

## Overview

Web Inspector (or Browser DevTools) is a built-in browser toolset for inspecting, debugging, and modifying web applications, used in security testing to analyze network requests and execute JavaScript for PoC exploits.

## Description

In Rocket.Chat exploitation, it monitors /api/v1/login requests, allowing inspection of unsanitized loginToken parameters and execution of fetch for injection payloads. Available in Chrome, Firefox, Safari for web-based offensive operations.

## Features

- Feature 1: Network tab for capturing HTTP requests
- Feature 2: Console for JavaScript execution (e.g., fetch API)
- Feature 3: Storage inspection for tokens

## Installation

### Requirements

- Modern web browser

### Install Commands

```bash
# No installation needed; access via F12 or right-click Inspect
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| Network Tab | Monitor requests |
| Console | Execute JS |

## Examples

### Example 1: Basic Usage

Open DevTools (F12) and go to Network tab.

### Example 2: Advanced Usage

In Console: fetch('/api/login', {method:'POST', body: JSON.stringify({loginToken: {$exists:false}})})

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser logs or CSP violations from console access
- Extended dev tools sessions on sensitive pages

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/curl]]
- [[tools/fetch]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools
