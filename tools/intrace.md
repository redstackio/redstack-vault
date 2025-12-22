---
id: 7919d91f-65f2-4404-9636-727ae249ac32
name: intrace
type: tool
verified: true
created_at: '2019-08-28T21:17:41.611071+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - network
  - traceroute
url: 'https://github.com/jfoote/intrace'
commands:
  - '[[commands/intrace-basic-traceroute]]'
  - '[[commands/intrace-remote-connection-trace]]'
  - '[[commands/intrace-port-specific-trace]]'
validated: true
---

# intrace

**Status**: Unverified

## Overview

InTrace is a network reconnaissance tool that functions like traceroute but leverages existing TCP connections (local or remote) to enumerate IP hops between the source and target. It is particularly useful for mapping network paths in environments where traditional ICMP-based traceroute is blocked by firewalls, enabling stealthy reconnaissance and potential firewall evasion.

## Description

InTrace exploits established TCP sessions to send probe packets, revealing intermediate routers and hops without generating new traffic that might be filtered. It supports both local connections (e.g., to web servers) and remote pivots (using connections from compromised hosts). Common use cases include discovering internal network topology during penetration tests, identifying firewall rules, and bypassing restrictions on outbound ICMP.

## Features

- **TCP Connection Exploitation**: Uses existing sessions to avoid ICMP blocks.
- **Local and Remote Tracing**: Supports tracing from local system or via remote hosts.
- **Port-Specific Probing**: Targets specific TCP ports like 80/443 for reliable paths.
- **Stealthy Operation**: Minimal footprint as it piggybacks on legitimate traffic.
- **Cross-Platform Compilation**: Written in C, compilable on Unix-like systems.

## Installation

### Requirements

- GCC compiler (for building from source)
- libpcap development libraries (for packet capture)
- Linux kernel with raw socket support

### Install Commands

```bash
# Clone the repository
git clone https://github.com/jfoote/intrace.git
cd intrace

# Compile the tool
make

# Or manual compile
gcc -o intrace intrace.c -lpcap

# Install to /usr/local/bin (optional)
sudo cp intrace /usr/local/bin/
```

For Kali Linux, it may be available via custom repositories or build from source as above.

## Basic Usage

```bash
intrace --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -p PORT | Specify TCP port for probing (default: 80) |
| -s IP:PORT | Use remote source connection |
| -v | Verbose output for detailed hops |

## Examples

### Example 1: Basic Usage

```bash
intrace example.com
```

This performs a local trace to example.com using default port 80.

### Example 2: Advanced Usage

```bash
intrace -s 10.0.0.5:443 -p 80 -v internal.target.net
```

This uses a remote connection from 10.0.0.5:443 to trace internal.target.net on port 80 with verbose details.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual TCP probe packets piggybacking on existing sessions (monitor with Wireshark or tcpdump).
- Outbound connections to common ports (80/443) with traceroute-like TTL patterns.
- Process monitoring for 'intrace' binary execution on endpoints.
- Network logs showing fragmented or low-TTL packets from non-standard sources.

## Related Procedures

- [[procedures/Network-Hop-Enumeration]]
- [[procedures/Firewall-Bypass-Traceroute]]

## Related Tools

- [[tools/traceroute]]
- [[tools/Nmap]]

## References

- Official GitHub: https://github.com/jfoote/intrace
- Original paper/discussion: Search for "InTrace: Network Path Discovery Using Existing TCP Connections"
