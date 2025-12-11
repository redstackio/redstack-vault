---
url: >-
  https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/netstat
tags:
  - network
  - discovery
type: tool
platforms:
  - Windows
  - Linux
description: Command-line tool for displaying network connections and listening ports
id: 7d0a94b5-aa24-4bcf-bd6b-d1be153b2081
created_at: '2025-12-11T06:10:30.635Z'
updated_at: '2025-12-11T06:10:30.635Z'
verified: false
validated: true
submitted: true
---
# netstat

**Status**: Unverified

## Overview

Netstat displays active TCP connections, ports on which the computer is listening, Ethernet statistics, and more.

## Description

Essential for discovering local servers and ports, as used in identifying the PlayStation Now WebSocket server.

## Features
- Connection listing
- Process association with -b

## Installation

### Requirements
- Built-in on Windows and most Linux distros

### Install Commands

N/A (built-in)

## Basic Usage

```cmd
netstat -anb
```

### Common Options

| Option | Description |
|--------|-------------|
| `-a` | All connections |
| `-n` | Numerical addresses |
| `-b` | Executable names |

## Examples

### Example 1: Basic Usage

```cmd
netstat -anb
```

## MITRE ATT&CK Mapping

### Techniques
- [[Network Sniffing]]

### Tactics
- [[Discovery]]

## Detection

- Log command execution

## Related Procedures

## Related Tools
- [[tools/Process-Monitor]]

## References
- Microsoft documentation
