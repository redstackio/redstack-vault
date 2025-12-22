---
id: 84376964-db60-4d55-a45b-552b5e0b9b7a
type: tool
verified: true
created_at: '2019-08-28T21:17:21.227582+00:00'
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

# dns2tcpc

**Status**: Unverified

## Overview

Dns2tcpc is a network tunneling tool that encapsulates and relays TCP connections over DNS traffic. It enables communication in restricted environments where direct TCP is blocked but DNS queries are permitted, commonly used for command and control (C2) channels or data exfiltration in penetration testing and red team operations.

## Description

Dns2tcpc operates without requiring special privileges or TUN/TAP drivers, making it lightweight and easy to deploy. It consists of a server component that listens for DNS queries and a client component that sends encoded TCP data via DNS. The server uses a configuration file to define 'resources'—TCP services to relay. Clients connect to these resources by crafting DNS queries that tunnel the traffic. This tool is particularly useful for evading network filters in defensive environments.

## Features

- Feature 1: TCP encapsulation over DNS without kernel modules or elevated privileges
- Feature 2: Configurable resources for multiple relayed services (e.g., SSH, HTTP)
- Feature 3: Support for both foreground and daemon modes on server and client
- Feature 4: Customizable domain and query encoding for stealth

## Installation

### Requirements

- Linux or Unix-like system (e.g., Kali, Ubuntu)
- GCC compiler for building from source
- libevent development libraries

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/alex-sector/dns2tcp.git dns2tcpc
cd dns2tcpc

# Build from source
make
sudo make install

# Alternative: On Kali/Debian (if packaged)
sudo apt update
sudo apt install dns2tcp
```

## Basic Usage

```bash
dns2tcpc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -F, --file | Specify configuration file |
| -f | Foreground mode |
| -d | Daemon mode |
| -R | Client resource selection |
| -S | Server IP for client |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Start server:
```bash
dns2tcpc -F /etc/dns2tcpc.cfg -f
```

Start client:
```bash
dns2tcpc -R ssh -r 192.168.1.100 -l 2222 -S 10.0.0.1 -d tunnel.example.com
```

### Example 2: Advanced Usage

Server in daemon mode with custom config:
```bash
dns2tcpc -F custom.cfg -d
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exfiltration Over Unencrypted Non-C2 Protocol]] Exfiltration Over Alternative Protocol: DNS Tunneling
- [[Protocol Tunneling]] Protocol Tunneling

### Tactics

- [[Command and Control]] Command And Control
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Anomalous DNS query volume or patterns (e.g., high TXT record queries to unusual domains)
- Detection method 2: DNS traffic analysis for base64-like encoded payloads in subdomains
- Detection method 3: Network logs showing TCP relay over UDP/53 without legitimate DNS resolution
- Detection method 4: Process monitoring for dns2tcpc binaries or unusual libevent usage

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
- [[tools/iodine]]

## References

- Official GitHub: https://github.com/alex-sector/dns2tcp
- Documentation: Included in source or man pages after installation

*Last updated: 2023-10-01*
