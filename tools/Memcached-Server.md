---
id: tool-uuid-6789
url: 'https://memcached.org/'
tags:
  - memcached
  - cache
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.090Z'
validated: true
submitted: true
---
# Memcached-Server

**Status**: Unverified

## Overview

Memcached is an in-memory key-value store used for caching, commonly exploited in SSRF chains to deliver payloads like serialized gadgets for deserialization attacks.

## Description

In offensive security, attackers deploy their own memcached instance to host untrusted data fetched via SSRF. It lacks authentication by default, making it ideal for blind data injection in chains leading to RCE. Used here to store deserialization payloads for SVNBridge exploitation.

## Features

- Feature 1: High-speed key-value storage/retrieval
- Feature 2: Binary protocol support for serialized data
- Feature 3: No built-in auth, easy for unauthenticated access

## Installation

### Requirements

- Linux/Unix system
- Build tools (gcc, make)

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install memcached

# Or from source
wget http://memcached.org/latest
tar -xzvf memcached-*.tar.gz
cd memcached-*
./configure && make && make install
```

## Basic Usage

```bash
memcached -d -m 64 -p 11211 -u nobody
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Daemon mode |
| `-p 11211` | Port to listen on |
| `-m 64` | Memory limit in MB |

## Examples

### Example 1: Basic Usage

```bash
memcached -d -p 11211
# Then set via telnet: telnet localhost 11211
# set key 0 0 10
# value
# STORED
```

### Example 2: Advanced Usage

```bash
memcached -d -p 11211 -U 11211  # UDP too
# Use for SSRF: echo 'set payload ...' | nc localhost 11211
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation of Remote Services]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on port 11211 from unexpected sources
- Log anomalous 'get/set' commands in memcached logs
- Monitor for SSRF patterns leading to memcached fetches

## Related Procedures

- [[procedures/Exploiting-SSRF-to-Control-Memcached-Data]]

## Related Tools

- [[Netcat]]

## References

- Official documentation: https://memcached.org/documentation
- Related resources: OWASP SSRF Cheat Sheet
