---
type: tool
verified: true
platforms:
  - Linux
tags:
  - data-encryption
  - pivot
  - tunnel
url: 'https://github.com/sshuttle/sshuttle'
description: >-
  sshuttle is a transparent proxy server that forwards over ssh. It enables
  VPN-like functionality without requiring root access on the remote server,
  only on the local machine.
validated: true
---

# sshuttle

**Status**: ✓ Verified

## Overview

sshuttle is a command-line tool that creates a secure, transparent proxy server to forward network traffic over an SSH connection. It functions like a poor man's VPN, allowing users to route traffic from their local machine through a remote SSH server without needing to install additional software on the remote side (as long as Python 2.3+ is available). Commonly used in penetration testing for pivoting into internal networks, bypassing firewalls, or encrypting traffic.

## Description

sshuttle works by dynamically executing Python code on the remote SSH server to handle traffic forwarding. It intercepts outgoing connections on the local machine and tunnels them via SSH, supporting IPv4 and IPv6. Key advantages include no need for remote root access or VPN setup, making it ideal for quick pivots during red team engagements. It requires sudo privileges locally to bind to low ports or modify routing tables.

Note: If connecting to a remote SSH server fails with error code 255, exclude the target IP/hostname using the `-x` flag (e.g., `-x $_TARGET_IP`).

## Features

- Transparent proxying: Forwards TCP traffic without modifying applications.
- DNS forwarding: Optional routing of DNS queries through the tunnel.
- Subnet targeting: Route specific networks (e.g., 10.0.0.0/8) or all traffic (0/0).
- No remote installation: Uses remote Python interpreter via SSH.
- IPv6 support: Handles both IPv4 and IPv6 traffic.
- Exclude options: Bypass certain IPs or domains from tunneling.

## Installation

### Requirements

- Python 3.6+ on the local machine.
- SSH access to a remote server with Python 2.3+.
- Root/sudo privileges on the local machine for full routing.

### Install Commands

#### Debian/Ubuntu

```bash
sudo apt update
sudo apt install sshuttle
```

#### Python 3 (pip)

```bash
pip3 install sshuttle
```

#### macOS (Homebrew)

```bash
brew install sshuttle
```

## Basic Usage

```bash
sshuttle --help
```

Start by connecting to a remote SSH server and specifying the networks to route.

### Common Options

| Option | Description |
|--------|-------------|
| `-r, --remote` | Specify the SSH server (user@host:port). |
| `NETWORK` | CIDR notation for networks to forward (e.g., 0/0 for all). |
| `--dns` | Forward DNS queries through the tunnel. |
| `-x, --exclude` | Exclude IPs/subnets from forwarding. |
| `-v` | Verbose output for debugging. |
| `--no-drop-privileges` | Run without dropping root privileges (advanced). |

## Examples

### Example 1: Basic Usage - Forward All Traffic

Route all IPv4 traffic through an SSH server:

```bash
sudo sshuttle -r user@remote.server.com 0/0
```

### Example 2: Advanced Usage - Forward Specific Subnet with DNS

Forward a private network and DNS queries, excluding the remote host:

```bash
sudo sshuttle -r user@remote.server.com --dns -x remote.server.com 10.0.0.0/8
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Defang Network (Proxy/Tunneling to bypass restrictions).
- [[Connection Proxy]] Proxy (Using SSH as a proxy for internal access).

### Tactics

- [[Command and Control]] Command and Control.
- [[Defense Evasion]] Defense Evasion.

## Detection

- Monitor for unusual SSH connections from internal hosts to external servers.
- Look for processes named 'sshuttle' or Python scripts executing over SSH.
- Network traffic anomalies: Increased SSH traffic with encapsulated TCP sessions.
- System logs showing sudo usage for routing changes (e.g., ip route modifications).
- DNS queries routed unexpectedly through non-standard paths.

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/openssh]] (Base SSH client/server for tunneling).
- [[tools/Proxychains]] (Alternative proxy chaining tool).

## References

- Official GitHub: https://github.com/sshuttle/sshuttle
- Documentation: https://sshuttle.readthedocs.io/
- Man page: `man sshuttle`
