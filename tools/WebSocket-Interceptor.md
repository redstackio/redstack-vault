---
id: tool-uuid-001
url: 'https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API'
tags:
  - interception
  - websocket
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.596Z'
validated: true
submitted: true
---
# WebSocket-Interceptor

**Status**: Unverified

## Overview

Tool for intercepting and modifying WebSocket messages, commonly using browser dev tools or proxies like Burp Suite, to test for vulnerabilities in real-time bidirectional communication.

## Description

In security testing, WebSocket interceptors allow pausing, editing, and replaying frames to inject payloads or observe protocols. For this attack, it's used to tamper with set_watch responses in Quantopian's debugger.

## Features

- Feature 1: Real-time message capture and modification
- Feature 2: JSON parsing and editing for structured payloads
- Feature 3: Integration with browser or standalone proxies

## Installation

### Requirements

- Modern browser (Chrome/Firefox) or proxy software

### Install Commands

```bash
# For Burp Suite (example proxy with WS support)
# Download from portswigger.net/burp
```

## Basic Usage

```bash
# In browser dev tools: Open Network tab, filter WS, enable preservation
```

### Common Options

| Option | Description |
|--------|-------------|
| Break on WS | Pause incoming/outgoing frames |
| Edit JSON | Modify payload before forwarding |

## Examples

### Example 1: Basic Usage

In dev tools, reload page with debugger to capture set_watch.

### Example 2: Advanced Usage

Use Burp: Configure proxy, intercept WS response, append payload, drop/forward.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous delays in WS traffic
- Mismatched request/response payloads

## Related Procedures

- [[procedures/Intercept-Modify-WebSocket-for-XSS-Test]]

## Related Tools

- [[tools/Proxy-Tool]]

## References

- MDN WebSocket API
- Burp Suite Documentation
