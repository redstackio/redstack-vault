---
id: tool-netcat
url: 'https://nc110.sourceforge.net/'
tags:
  - network
  - shell
  - listener
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:57.507Z'
validated: true
submitted: true
---
---
# netcat

**Status**: Unverified

## Overview

Netcat (nc) is a versatile networking utility for reading/writing data across TCP/UDP, commonly used in security testing for reverse shells and port scanning.

## Description

In offensive operations, netcat excels at creating listeners for reverse shells, transferring files, or simple port forwarding. Here, it's used to catch shells from RCE exploits in environments like LGTM sandboxes.

## Features

- Feature 1: TCP/UDP support for connections
- Feature 2: Shell execution over network (-e flag)
- Feature 3: Verbose logging and port binding

## Installation

### Requirements

- Standard Unix-like system

### Install Commands

```bash
# On Debian/Ubuntu
apt install netcat

# On Alpine
apk add netcat-openbsd
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | Listen mode |
| `-p` | Specify port |
| `-v` | Verbose |

## Examples

### Example 1: Basic Usage

```bash
nc -vlp 4444
```

### Example 2: Advanced Usage

```bash
nc -l -p 4444 -k  # Persistent listener
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Unix Shell
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing nc processes on high ports
- IDS signatures for netcat traffic patterns
- Process monitoring for nc binaries

## Related Procedures


## Related Tools

- [[tools/SSH]]
- [[tools/socat]]

## References

- Official documentation: https://nc110.sourceforge.net/
- Related resources: Man pages for nc

---
