---
id: tool-chrome-dev-tools
url: 'https://developer.chrome.com/docs/devtools/'
tags:
  - dev-tools
  - network-analysis
type: tool
verified: false
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.787Z'
validated: true
submitted: true
---
# Google-Chrome-Developer-Tools

**Status**: Unverified

## Overview

Chrome Developer Tools (DevTools) is an integrated debugging suite for inspecting, monitoring, and manipulating web page resources, crucial for intercepting XHR/GraphQL requests and executing exploits in browser consoles.

## Description

DevTools enables security testers to filter network requests (e.g., ThemesProcessingLegacy), preview JSON responses for ID extraction, copy requests as fetch, and run JavaScript in the console. In this Shopify exploit, it's used to capture publish mutations and time race conditions by monitoring installation progress.

## Features

- Feature 1: Network tab for XHR/GraphQL filtering
- Feature 2: Console for fetch execution and logging
- Feature 3: Response preview for JSON parsing

## Installation

### Requirements

- Google Chrome browser installed

### Install Commands

```bash
# Built-in; access via F12 or right-click > Inspect
```

## Basic Usage

```bash
# In Chrome, press F12 to open DevTools
```

### Common Options

| Option | Description |
|--------|-------------|
| Network tab | Filter by name (e.g., GraphQL) |
| Console | Execute JS commands |

## Examples

### Example 1: Basic Usage

Open DevTools (F12), go to Network, perform action, filter for request.

### Example 2: Advanced Usage

In Console: Paste and run fetch code; in Network: Copy as fetch.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Defense Evasion]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual console logs or network filters in client-side scripts
- Frequent request copies in session

## Related Procedures


## Related Tools

- [[tools/Google-Chrome]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/
- Network guide: https://developer.chrome.com/docs/devtools/network/
