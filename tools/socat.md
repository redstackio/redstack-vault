---
url: 'http://www.dest-unreach.org/socat/'
tags:
  - networking
  - relay
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.633Z'
id: 54731ffc-8484-4f75-bb34-6357a2264e98
validated: true
submitted: true
---
# socat

**Status**: Unverified

## Overview

Socat is a multipurpose relay tool for Linux/Unix systems, used here to create a simple TCP server simulating a malicious MQTT endpoint for vulnerability testing.

## Description

Socat (SOcket CAT) establishes bidirectional data streams between endpoints like files, TCP sockets, and more. In offensive security, it's commonly used for port forwarding, protocol simulation, and crafting network interactions to exploit client-side flaws like the curl MQTT DoS.

## Features

- Feature 1: Supports unidirectional (-u) and bidirectional data relay
- Feature 2: Address types for files, TCP/UDP, pipes, and more
- Feature 3: Forking for concurrent connections and address reuse

## Installation

### Requirements

- Linux/Unix system
- Standard package manager

### Install Commands

```bash
# On Debian/Ubuntu
apt install socat

# On Red Hat/CentOS
yum install socat
```

## Basic Usage

```bash
socat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u` | Unidirectional data transfer |
| `-d -d` | Increase debug verbosity |
| `fork` | Handle multiple connections |

## Examples

### Example 1: Basic Usage

```bash
socat TCP-LISTEN:8080 TCP:remote:80
```

### Example 2: Advanced Usage

```bash
socat -u FILE:input.txt TCP-LISTEN:12345,reuseaddr,fork
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing socat processes binding unusual ports
- Process lists with socat forking on high ports

## Related Procedures

- [[procedures/Set-Up-Malicious-MQTT-Server-with-socat]]

## Related Tools

- [[tools/nc-netcat]]
- [[tools/curl]]

## References

- Official documentation: http://www.dest-unreach.org/socat/doc/socat.html
