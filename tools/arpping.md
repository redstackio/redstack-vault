---
url: 'https://www.npmjs.com/package/arpping'
tags:
  - network-discovery
  - vulnerable
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.906Z'
id: de68e486-a564-4855-a6e6-d7da8c06a91e
validated: true
submitted: true
---
# arpping

**Status**: Unverified

## Overview

arpping is a Node.js module for discovering internet-connected devices using ICMP ping and ARP requests, vulnerable to command injection in version 2.0.0.

## Description

The tool wraps OS 'ping' and 'arp' commands to scan networks but fails to sanitize inputs, allowing attackers to inject shell commands via the IP parameter in ping() and arp() functions. Commonly used in IoT or network scanning apps; exploitation leads to RCE on the host.

## Features

- Feature 1: Ping multiple IPs asynchronously
- Feature 2: ARP table querying for MAC-IP mapping
- Feature 3: Callback-based results for device discovery

## Installation

### Requirements

- Node.js 10+
- npm

### Install Commands

```bash
npm install arpping@2.0.0
```

## Basic Usage

```bash
node -e "require('arpping').ping(['8.8.8.8'], console.log);"
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Module functions: ping(ips, callback), arp(interface, callback) |

## Examples

### Example 1: Basic Usage

```javascript
const arpping = require('arpping');
arpping.ping(['127.0.0.1'], (err, data) => console.log(data));
```

### Example 2: Advanced Usage

```javascript
arpping.arp('eth0', (err, data) => console.log(data));
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor npm installs for arpping@2.0.0
- Log unexpected OS command invocations from Node.js processes
- Scan for anomalous file creations post-execution

## Related Procedures


## Related Tools

- [[tools/Node.js]]

## References

- https://www.npmjs.com/package/arpping
- HackerOne Report: https://hackerone.com/reports/972220
