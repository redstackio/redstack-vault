---
id: tool-uuid-2
url: 'https://hackerone.com/reports/446662'
tags:
  - attack
  - dos
  - http2
type: tool
verified: false
platforms:
  - Node.js
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.636Z'
validated: true
submitted: true
---
# Custom-HTTP2-Attack-Script

**Status**: Unverified

## Overview

A Node.js-based script for opening connections and sending large HTTP/2 SETTINGS frames to exploit DoS in Node.js servers.

## Description

This offensive tool crafts and transmits oversized SETTINGS frames (14400 bytes) over multiple connections, exploiting the Node.js HTTP/2 module's lack of bounds checking. Ideal for penetration testing resource exhaustion vulnerabilities.

## Features

- Feature 1: Multi-connection establishment
- Feature 2: Custom frame crafting for SETTINGS
- Feature 3: Payload size configuration for evasion

## Installation

### Requirements

- Node.js 10.x or later
- http2 module (built-in)

### Install Commands

```bash
# Save as attack.js; no external deps
npm install  # If any optional modules
```

## Basic Usage

```bash
node attack.js --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--target` | Target host:port |
| `--connections` | Number of connections |
| `--payload-size` | Frame payload bytes |

## Examples

### Example 1: Basic Usage

```bash
node attack.js --target localhost:3000 --connections 100
```

### Example 2: Advanced Usage

```bash
node attack.js --target example.com:443 --send-settings --payload-size 14400
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[OS Exhaustion Flood]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Node.js processes with high outbound HTTP/2 traffic
- Anomalous SETTINGS frame sizes in protocol logs

## Related Procedures

- [[procedures/Establish-Multiple-HTTP2-Connections]]
- [[procedures/Send-Large-SETTINGS-Frames]]

## Related Tools

- [[tools/Custom-Node-js-Server-Script]]

## References

- HackerOne Report #446662
