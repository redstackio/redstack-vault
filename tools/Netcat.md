---
url: null
tags:
  - network
  - payload-delivery
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Networking utility for reading from and writing to network connections using
  TCP or UDP
id: 411322d4-09dd-402a-8c62-2f320cb55062
created_at: '2025-12-11T03:47:57.194Z'
updated_at: '2025-12-11T03:47:57.194Z'
verified: false
validated: true
submitted: true
---
# netcat

**Status**: Unverified

## Overview

Netcat (nc) is a versatile networking tool used for sending data over networks, commonly in security testing for payload delivery and port scanning.

## Description

Netcat can create connections to send or receive data, making it ideal for exploiting network-based vulnerabilities like the BD-J chain on PS4/PS5.

## Features

- Feature 1: TCP/UDP connections
- Feature 2: Data transfer
- Feature 3: Port listening/scanning

## Installation

### Requirements

- Standard on most Unix-like systems
- Install via package manager if needed

### Install Commands

```bash
sudo apt install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v` | Verbose output |
| `-l` | Listen mode |

## Examples

### Example 1: Basic Usage

```bash
nc target_ip 1337 < file.bin
```

### Example 2: Advanced Usage

```bash
nc -v target_ip 1337 < payload.bin
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]
- [[Exploitation for Privilege Escalation]]

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on unusual ports
- Anomalous data transfers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #socat
- [[tools/netcat]]

## References

- Man page: nc(1)
- Related resources
