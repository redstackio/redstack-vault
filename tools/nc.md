---
url: ''
tags:
  - network
  - payload-sending
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: Netcat utility for reading and writing data across network connections.
id: 4fe9387d-d888-454f-a688-95d9851dca28
created_at: '2025-12-13T09:01:22.388Z'
updated_at: '2025-12-13T09:01:22.388Z'
verified: false
validated: true
submitted: true
---
# nc

**Status**: Unverified

## Overview

Netcat (nc) is a versatile networking tool used to send raw data over TCP/UDP, commonly employed in security testing to deliver crafted payloads like HTTP requests.

## Description

nc allows establishing connections and sending data, making it suitable for exploiting network vulnerabilities by sending custom payloads to servers.

## Features

- TCP/UDP connections
- Data piping
- Port scanning

## Installation

### Requirements

- Standard on most Unix-like systems

### Install Commands

```bash
# For Ubuntu: sudo apt install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
echo 'data' | nc 127.0.0.1 80
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic monitoring for raw connections
- Log unusual port access

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/socat]]

## References

- man nc
