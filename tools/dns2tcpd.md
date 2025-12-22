---
id: e5c70ceb-d4c4-4c3f-bc06-eb0a74239bf1
name: dns2tcpd
type: tool
verified: true
created_at: '2019-08-28T21:17:39.138902+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
tags:
  - dns-tunneling
  - c2
  - evasion
  - post-exploitation
url: 'https://github.com/alex-sector/dns2tcp'
validated: true
---

# dns2tcpd

**Status**: Unverified

## Overview

Dns2tcpd is a daemonized version of the dns2tcp tool, designed for relaying TCP connections over DNS traffic to create covert channels. It encapsulates TCP data within DNS queries and responses, allowing data exfiltration, command and control (C2), or access to internal services in firewall-restricted environments without needing special privileges or TUN/TAP drivers.

## Description

Dns2tcpd operates in client-server mode. The server listens for DNS queries and forwards them to configured local or remote TCP resources (e.g., SSH, HTTP). The client connects to a local port and tunnels traffic via DNS to the server. This is useful in red team operations for evading network monitoring, as DNS traffic often bypasses deep packet inspection. No root privileges are required for the client, making it stealthy for compromised hosts.

## Features

- TCP encapsulation over DNS (UDP-based)
- Configurable resources (services) on the server side
- Support for multiple concurrent tunnels
- Low-privilege operation (no TUN/TAP needed)
- Debug logging for troubleshooting
- Domain-based authentication for queries

## Installation

### Requirements

- Linux/Unix system with GCC and make
- libevent development libraries (for event handling)
- UDP port 53 access on server (or custom port)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/alex-sector/dns2tcp.git
cd dns2tcp

# Compile
make

# Install (optional, to /usr/local/bin)
make install
```

On Kali Linux, it may be available via apt: `apt install dns2tcp`, but verify the version matches dns2tcpd.

## Basic Usage

```bash
dns2tcpd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -F | Foreground mode (non-daemon) |
| -c | Configuration file path |
| -d | Debug level (0=silent, 3=verbose) |
| -z | DNS server for client |
| -l | Local listen port for client |

## Examples

### Example 1: Basic Usage

Start server:

```bash
dns2tcpd -F -c server.conf
```

Start client:

```bash
dns2tcpd -z server.example.com -d tunnel.example.com -l 8080 -R ssh
```

### Example 2: Advanced Usage

Server with debug:

```bash
dns2tcpd -c server.conf -d 2
```

Client with custom resolver port:

```bash
dns2tcpd -z 10.0.0.1 -r 5353 -d tunnel.example.com -l 4444 -R http
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Protocol Tunneling
- [[Communication Through Removable Media]] Communication Through Removable Media (adapted for DNS)

### Tactics

- [[Command and Control]] Command And Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual volume of DNS queries from a single host (e.g., high TXT/CNAME query rates)
- DNS responses larger than typical (due to encapsulated data)
- Network logs showing TCP-like patterns in DNS traffic
- Process monitoring for dns2tcpd binary or unusual libevent usage
- Anomaly detection in DNS resolver logs for non-standard domains

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/DNScat2]]
- [[tools/iodine]]

## References

- Official GitHub: https://github.com/alex-sector/dns2tcp
- Documentation: Included in repo README
- Blog on DNS Tunneling: Various SANS or security blogs
