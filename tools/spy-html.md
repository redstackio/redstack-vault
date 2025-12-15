---
url: null
tags:
  - html
  - poc
  - client
type: tool
verified: false
platforms:
  - Web
  - Desktop
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.366Z'
id: 01ca3a84-99df-4f61-a7d9-8271e94657aa
validated: true
submitted: true
---
# spy-html

**Status**: Unverified

## Overview

spy.html is a custom HTML file for generating multiple concurrent fetch requests to a PoC server, building up connections to trigger bursts and observe effects in proxied tools like Burp.

## Description

Placed in the server directory, it uses JavaScript to spawn threads (configurable var) of async requests to /memspy, with a console kill-switch. Purpose: Client-side repro of races by simulating load; includes display of results for analysis.

## Features

- Feature 1: Configurable thread count via JS var
- Feature 2: Console controls (killall=true)
- Feature 3: Displays fetched content post-burst

## Installation

### Requirements

- Modern browser
- Local file access

### Install Commands

```bash
# No install; save as spy.html in server dir
# Content: <script> let threads=4; for(let i=0;i<threads;i++) fetch('/memspy'); </script>
```

## Basic Usage

```bash
# Open http://127.0.0.1:8000/spy.html in proxied browser
```

### Common Options

| Option | Description |
|--------|-------------|
| `threads` | JS var for request count | Config in code |

## Examples

### Example 1: Basic Usage

```bash
# Browser: Load /spy.html; sets threads=4, initiates requests
```

### Example 2: Advanced Usage

```bash
# Console: threads=20; // Increase for larger bursts
killall=true; // Abort requests
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Multiple concurrent fetches to local endpoints
- Console vars like 'threads' in dev tools

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Custom PoC; no external docs
