---
url: ''
tags:
  - dos
  - network
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.566Z'
id: b2c5a525-682a-4a91-aada-01d57ef87b54
validated: true
submitted: true
---
# TARPIT

**Status**: Unverified

## Overview

TARPIT is a technique or tool to hold open TCP connections indefinitely by sending minimal ACKs, simulating slow responses to exhaust attacker or target resources, used here for DoS by keeping ffmpeg waiting.

## Description

In the exploit, port 12346 is redirected to a tarpit, causing ffmpeg to hang while awaiting video data from the m3u8 playlist, leading to resource exhaustion on Imgur's side.

## Features

- Feature 1: Slow response simulation
- Feature 2: Connection holding without closure
- Feature 3: Resource denial via open sockets

## Installation

### Requirements

- iptables or custom script for tarpitting

### Install Commands

```bash
# Use iptables for basic tarpit
iptables -A INPUT -p tcp --dport 12346 -j DROP  # Simple drop, or use delay modules

# Or install honeypot tools like LaBrea
# Custom script example
```

## Basic Usage

No direct binary; configure via firewall or script.

### Common Options

N/A

## Examples

### Example 1: Basic Usage

Redirect traffic to tarpit script that ACKs slowly.

### Example 2: Advanced Usage

Use in conjunction with nc: pipe nc output to a delay script.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Long-lived half-open connections
- High number of SYN-ACK without data
- Firewall logs showing delayed responses

## Related Procedures

- [[procedures/Craft-DoS-Payload-to-Hang-FFmpeg]]

## Related Tools

- [[Related Tool: iptables]]
- [[Related Tool: tc (traffic control)]]

## References

- Related resources: Tarpit techniques in network security docs
