---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567897
url: 'https://developer.chrome.com/docs/devtools/network/'
tags:
  - devtools
  - request-capture
type: tool
verified: false
platforms:
  - Web
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:31.163Z'
validated: true
submitted: true
---
# Browser-Network-Inspector

**Status**: Unverified

## Overview

The Browser Network Inspector (e.g., Chrome DevTools Network panel) is a built-in feature for monitoring, capturing, and analyzing HTTP requests/responses during web interactions, ideal for security testing to intercept and replicate traffic.

## Description

Part of modern browser developer tools, it logs all network activity, allowing export as curl or HAR files. In offensive ops, it's used to capture authenticated requests for modification, bypassing client-side restrictions.

## Features

- Feature 1: Real-time request/response viewing with headers and payloads
- Feature 2: Copy as curl, cURL, or HAR for replay
- Feature 3: Filtering by type (XHR, POST) and preservation of logs

## Installation

### Requirements

- Modern browser like Chrome, Firefox, or Edge

### Install Commands

No installation needed; access via F12 or right-click 'Inspect'.

## Basic Usage

```bash
# No CLI; browser-based
```

### Common Options

| Option | Description |
|--------|-------------|
| Network Tab | Monitor all requests |
| Preserve Log | Keep logs across navigations |
| Copy > Copy as cURL | Export request |

## Examples

### Example 1: Basic Usage

Open DevTools (F12), go to Network, reload page to see requests.

### Example 2: Advanced Usage

Filter for POST, click a request, copy as cURL for modification.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Client-side; hard to detect remotely, but monitor for unusual request patterns
- Browser extensions or proxy traffic anomalies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[Wireshark]]

## References

- Official documentation: https://developer.chrome.com/docs/devtools/network/
- Related resources: MDN Web Docs
