---
id: tool-uuid-002
url: 'https://firefox-source-docs.mozilla.org/devtools-user/'
tags:
  - devtools
  - debugging
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.443Z'
validated: true
submitted: true
---
# Firefox-DevTools

**Status**: Unverified

## Overview

Firefox DevTools is the integrated debugging suite in Firefox, used to inspect, capture, and replay HTTP requests in web security assessments.

## Description

DevTools enables copying requests as fetch snippets, viewing cookies, and executing JavaScript directly in the console, crucial for API exploitation like request replay in auth bypass attacks. It's lightweight, requiring no installation beyond the browser, and supports real-time modification of network traffic.

## Features

- Feature 1: Network tab for request interception and export
- Feature 2: Console for JavaScript execution
- Feature 3: Storage tab for cookie inspection

## Installation

### Requirements

- Firefox browser

### Install Commands

No separate install; enable via F12 in Firefox.

## Basic Usage

```bash
# In Firefox, press F12 to open DevTools
firefox --devtools
```

### Common Options

| Option | Description |
|--------|-------------|
| Network tab | Monitor requests |
| Console | Execute JS |

## Examples

### Example 1: Basic Usage

Press F12, go to Network, reload page to see requests.

### Example 2: Advanced Usage

Right-click request in Network tab > Copy > Copy as Fetch, then paste in Console.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous fetch executions in console logs
- Modified requests with DevTools fingerprints

## Related Procedures

- [[procedures/Replay-Modified-Request-to-Create-GovSlack-Workspace]]

## Related Tools

- [[tools/Firefox]]

## References

- Official documentation: https://developer.mozilla.org/en-US/docs/Tools
