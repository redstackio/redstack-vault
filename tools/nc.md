---
id: tool-uuid-2
url: 'https://nc110.sourceforge.net/'
tags:
  - network
  - capture
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.703Z'
validated: true
submitted: true
---
# nc

**Status**: Unverified

## Overview

Netcat (nc) is a versatile networking utility for reading/writing data across TCP/UDP, commonly used in security testing to create listeners for capturing SSRF requests or port scanning.

## Description

Nc supports listening, connecting, and data transfer over networks. In SSRF scenarios, it's used to bind to localhost ports and log incoming requests from exploited applications, revealing leaked data.

## Features

- Feature 1: TCP/UDP support
- Feature 2: Port scanning capabilities
- Feature 3: File transfer and banner grabbing

## Installation

### Requirements

- Unix-like OS (pre-installed on most)

### Install Commands

```bash
# On Debian/Ubuntu
apt install netcat
# On macOS (built-in)
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -l | Listen mode |
| -p | Specify port |
| -v | Verbose |

## Examples

### Example 1: Basic Usage

```bash
nc -l -p 8080
```

### Example 2: Advanced Usage

```bash
nc -l -n -vv -p 443  # Verbose listen on 443
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: nc or netcat running in listen mode
- Network: Bindings to unusual ports like localhost:443

## Related Procedures

- [[procedures/Capture-Exfiltrated-Data-with-Netcat]]

## Related Tools

- [[tools/socat]]

## References

- Official documentation: https://nc110.sourceforge.net/
