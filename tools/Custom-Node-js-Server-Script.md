---
id: tool-uuid-1
url: 'https://hackerone.com/reports/446662'
tags:
  - server
  - http2
type: tool
verified: false
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.646Z'
validated: true
submitted: true
---
# Custom-Node-js-Server-Script

**Status**: Unverified

## Overview

A Node.js script to start an HTTP/2 server for replicating the vulnerable environment in the DoS exploit scenario.

## Description

This custom tool implements a basic HTTP/2 server using Node.js's built-in http2 module, without frame size limits, to test the SETTINGS frame vulnerability. It's used in offensive security to simulate targets.

## Features

- Feature 1: HTTP/2 server initialization with TLS support
- Feature 2: Handles incoming connections without restrictions
- Feature 3: Logs basic request handling for monitoring

## Installation

### Requirements

- Node.js 10.x or later

### Install Commands

```bash
# No installation needed; save as server.js
npm init -y  # If needed for project setup
```

## Basic Usage

```bash
node server.js
```

### Common Options

| Option | Description |
|--------|-------------|
| Port configuration in script | Change listening port |
| TLS certs | Provide for HTTPS/2

## Examples

### Example 1: Basic Usage

```bash
node server.js
```

### Example 2: Advanced Usage

```bash
node server.js --port 8443 --tls
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for node server.js
- Network logs showing HTTP/2 handshakes

## Related Procedures

- [[procedures/Start-Node-js-HTTP2-Server]]

## Related Tools

- [[tools/Custom-HTTP2-Attack-Script]]

## References

- HackerOne Report #446662
