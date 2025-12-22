---
type: tool
description: >-
  A framework for distributing Nmap scans across multiple clients to handle
  large-scale network reconnaissance efficiently.
url: 'https://github.com/krabelize/dnmap'
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - reconnaissance
  - scanning
  - distributed
validated: true
---

# dnmap-client

**Status**: Unverified

## Overview

dnmap is a Perl-based framework designed to distribute Nmap scanning tasks across multiple client machines, enabling efficient scanning of large networks or IP ranges. It uses a client-server architecture where the server coordinates tasks and clients execute individual Nmap scans. This tool is ideal for red team operations requiring broad reconnaissance without overwhelming a single machine's resources or bandwidth.

## Description

dnmap reads a pre-generated file containing Nmap commands (one per target or task) and distributes these to connected clients. The server handles logic, progress tracking, and statistics, while clients perform the actual scans and store partial outputs locally. Results are aggregated on the server. It's particularly useful when scanning extensive host lists across multiple internet connections or with collaborative setups.

## Features

- Feature 1: Distributed task allocation to balance load across clients
- Feature 2: Real-time progress monitoring and statistics on the server
- Feature 3: Support for custom Nmap commands in input files
- Feature 4: Output storage on both server and clients for redundancy
- Feature 5: Simple Perl scripting for easy extension

## Installation

### Requirements

- Perl 5 (with standard libraries)
- Nmap installed on all clients
- SSH/SCP access for result retrieval (optional but recommended)

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/krabelize/dnmap.git
cd dnmap

# No compilation needed; scripts are ready to run
chmod +x *.pl

# On Kali/Debian-based systems, ensure Nmap is installed
apt update && apt install nmap perl
```

For Windows or other platforms, use Cygwin or WSL with Perl and Nmap.

## Basic Usage

```bash
tool-name --help  # Shows: Usage: dnmap_server.pl [-f file] [-p port] [-h]
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Specify input file with Nmap commands |
| -p, --port | Server listening port (default 65000) |
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

First, create input file:

```bash
[[commands/dnmap-create-input-file]]

# Start server
[[commands/dnmap-start-server]]

# On clients, start client
[[commands/dnmap-start-client]]
```

### Example 2: Advanced Usage

Distribute a large scan across 5 clients:

```bash
# Server side
./dnmap_server.pl -f large_input.txt -p 66000 -v

# Client side (run on each)
./dnmap_client.pl -s 10.0.0.1 -p 66000

# Retrieve results post-scan
[[commands/dnmap-retrieve-results]]
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual Perl processes (dnmap_server.pl, dnmap_client.pl) on scanning machines
- Detection method 2: Multiple synchronized Nmap executions from different IPs targeting the same range
- Detection method 3: Network traffic on non-standard ports (e.g., 65000) between internal hosts
- Detection method 4: Log entries for distributed scan patterns in Nmap outputs or firewall rules

## Related Procedures

- No specific procedures linked yet; typically used in reconnaissance procedures like [[procedures/Distributed-Network-Enumeration]]

## Related Tools

- [[tools/Nmap]]
- [[tools/masscan]]

## References

- Official GitHub: https://github.com/krabelize/dnmap
- Nmap Documentation: https://nmap.org/book/
- Related: Distributed scanning techniques in red teaming guides
