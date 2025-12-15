---
id: tool-tarpit-001
url: ''
tags:
  - dos
  - network
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.476Z'
validated: true
submitted: true
---
# TARPIT

**Status**: Unverified

## Overview

TARPIT is a technique or tool to create TCP tarpits, slowing or hanging connections by sending minimal ACKs, used here to keep ffmpeg processes open for DoS.

## Description

In the Imgur attack, redirecting the SSRF port to a TARPIT causes ffmpeg to wait indefinitely for video data, exhausting resources as processes and sockets remain open.

## Features

- Feature 1: Slow response to tie up connections
- Feature 2: Minimal bandwidth usage while hanging
- Feature 3: Configurable delay per connection

## Installation

### Requirements

- Linux kernel with tarpit module or tool like honeyd

### Install Commands

```bash
# Using iptables for simple tarpit
apt install iptables

# Or use specialized tool like tarpitd (if available)
```

## Basic Usage

```bash
# Example with iptables
iptables -A INPUT -p tcp --dport 12346 -j DROP  # Simple drop, or use tarpit module
```

### Common Options

| Option | Description |
|--------|-------------|
| Delay | Time to hold connection | Varies |
| Port | Target port for tarpit | 12346 |

## Examples

### Example 1: Basic Usage

Configure server to tarpit port 12346, e.g., via script sending slow ACKs.

### Example 2: Advanced Usage

```bash
# Pseudo-script for tarpit
while true; do nc -l 12346 | sleep 10; done  # Basic slow response
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Long-lived half-open TCP connections
- Low-bandwidth inbound traffic to high ports
- Server resource spikes without data transfer

## Related Procedures

- [[procedures/Execute-DoS-via-Hanging-m3u8-Playlists]]

## Related Tools

- [[tools/nc]]

## References

- Related resources: https://en.wikipedia.org/wiki/TCP_honeypot
