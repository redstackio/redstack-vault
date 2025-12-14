---
id: tool-netcat-001
url: 'https://nc110.sourceforge.net/'
tags:
  - network
  - utility
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.535Z'
validated: true
submitted: true
---
# netcat

**Status**: Unverified

## Overview

Netcat (nc) is a versatile networking utility for reading/writing data across TCP/UDP connections, commonly used in security testing to create listeners for verifying exploits like SSRF.

## Description

Netcat enables port scanning, file transfer, and simple servers/clients. In offensive security, it's ideal for setting up quick listeners to confirm server requests without complex setups. Supports IPv4/IPv6 and basic scripting.

## Features

- Feature 1: TCP/UDP listening and connecting
- Feature 2: Data piping for banners or payloads
- Feature 3: Port scanning capabilities

## Installation

### Requirements

- Standard Unix-like system or Windows with nc.exe

### Install Commands

```bash
# On Debian/Ubuntu
apt install netcat

# On macOS (built-in or brew install netcat)
brew install netcat
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
| `-v` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
nc -l 81
```
Listen on port 81 for connections.

### Example 2: Advanced Usage

```bash
nc -l -p 81 -v
```
Verbose listener on port 81.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Encrypted Channel]] Encrypted Channel

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing ephemeral port listening
- Unusual inbound connections on non-standard ports
- Process monitoring for nc.exe or nc binary

## Related Procedures

- [[procedures/Exploit-XXE-for-SSRF-via-External-Resource-Fetch]]

## Related Tools

- [[Related Tool 1|socat]]
- [[Related Tool 2|tcpdump]]

## References

- Official documentation: https://nc110.sourceforge.net/
- Related resources: man nc
