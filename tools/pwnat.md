---
id: 4f89db53-0931-4b2e-bf6e-8b6326b14b54
name: pwnat
type: tool
verified: true
created_at: '2019-08-28T21:17:25.298718+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - network
  - nat-traversal
  - proxy
  - c2
url: 'http://samy.pl/pwnat/'
validated: true
---

# pwnat

**Status**: Unverified

## Overview

pwnat (pronounced "poe-nat") is a lightweight tool designed for NAT traversal, allowing clients and servers behind different NATs to establish direct connections without requiring port forwarding, DMZ configuration, or third-party services. It is commonly used in penetration testing for command-and-control (C2) communications, bypassing firewalls, and enabling peer-to-peer connections in restricted network environments.

## Description

pwnat works by exploiting properties of NAT and UDP hole punching techniques to create bidirectional communication channels. The server predicts incoming client connections and sends predictive packets to facilitate the traversal. This makes it ideal for scenarios where traditional port forwarding is not possible, such as in red team operations targeting internal networks or IoT devices behind NATs. It supports both TCP and UDP protocols and can handle multiple clients simultaneously.

## Features

- NAT traversal without port forwarding or UPnP
- Support for multiple clients connecting to a single server
- No third-party involvement or STUN/TURN servers required
- Lightweight C implementation, easy to compile and deploy
- Works with symmetric and full-cone NAT types
- Verbose logging for troubleshooting connections

## Installation

### Requirements

- GCC compiler (for building from source)
- Linux or macOS environment
- Root privileges not required

### Install Commands

```bash
# Download source from official site
git clone https://github.com/samyk/pwnat.git
cd pwnat

# Compile
make

# Install (optional, or just use ./pwnat)
sudo make install
```

On Kali Linux, it may be available via apt:

```bash
sudo apt update
sudo apt install pwnat
```

## Basic Usage

```bash
./pwnat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -s | Server mode |
| -c | Client mode |
| -v | Verbose output |
| -p | Specify port |
| -l | Local address binding |

## Examples

### Example 1: Basic Usage (Server Mode)

Start server listening on local port 4444, targeting external IP 203.0.113.1 on port 8080:

```bash
./pwnat -s 4444 203.0.113.1 8080
```

### Example 2: Advanced Usage (Client Mode)

Connect as client to server at 203.0.113.1 on port 8080:

```bash
./pwnat -c 203.0.113.1 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy (for NAT traversal in C2)
- [[Protocol Tunneling]] Protocol Tunneling (UDP-based hole punching)

### Tactics

- [[Command and Control]] Command and Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual UDP traffic patterns with predictive packet bursts
- Connections from internal hosts to external IPs without standard port forwarding
- Process monitoring for pwnat binary or compiled equivalents
- Network logs showing NAT hole punching attempts (e.g., multiple SYN packets)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ncat]]
- [[tools/socat]]

## References

- Official website: http://samy.pl/pwnat/
- GitHub repository: https://github.com/samyk/pwnat
- Related: UDP Hole Punching techniques in networking
