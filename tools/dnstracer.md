---
id: 4170df85-2e57-4bde-bdf8-d218e2ee7432
type: tool
verified: true
created_at: '2019-08-28T21:17:42.630629+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Unix
tags:
  - dns
  - reconnaissance
  - network
url: 'https://linux.die.net/man/1/dnstracer'
validated: true
---

# dnstracer

**Status**: Unverified

## Overview

dnstracer is a command-line tool for DNS path tracing. It determines the chain of DNS servers a given resolver uses to obtain information for a hostname, following delegations back to the authoritative name server. Commonly used in reconnaissance to map DNS infrastructure, identify hidden resolvers, or debug DNS resolution paths during security assessments.

## Description

The tool sends iterative DNS queries starting from a specified or default resolver, displaying each delegation step, server responses, and final authoritative answer. It supports both UDP and TCP queries, query types like A, NS, and more, making it valuable for understanding DNS topologies in offensive security operations such as identifying internal DNS servers or spotting misconfigurations.

## Features

- Feature 1: Iterative tracing of DNS delegation chains from resolver to authoritative server
- Feature 2: Support for UDP (default) and TCP (-t) transport protocols
- Feature 3: Customizable query types (e.g., -q=A for A records, -q=NS for NS records)
- Feature 4: Verbose output showing query status, server addresses, and response details
- Feature 5: Handles timeouts and retries for unreliable networks

## Installation

### Requirements

- Linux/Unix environment with standard C libraries
- Internet access for package managers or source compilation

### Install Commands

```bash
# On Kali Linux (pre-installed or via apt)
apt update && apt install dnstracer

# On Ubuntu/Debian
apt update && apt install dnstracer

# From source (if not in repos)
git clone https://github.com/dnstracer/dnstracer.git  # Note: Actual source may vary; check official repo
cd dnstracer
make
make install
```

## Basic Usage

```bash
dnstracer --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -t | Use TCP instead of UDP for queries |
| -q=TYPE | Specify query type (e.g., A, NS, MX) |
| -T SECONDS | Set timeout for responses |
| -r RETRIES | Number of retries on failure |

## Examples

### Example 1: Basic Usage

```bash
dnstracer example.com
```

### Example 2: Advanced Usage

```bash
dnstracer -t -q=NS example.com 8.8.8.8
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Determine Physical Locations]] Gather Victim Host Information: Identify Infrastructure
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network logs showing iterative DNS queries from a single source to multiple authoritative servers
- Detection method 2: DNS server logs with unusual query patterns for internal domains
- Detection method 3: Process monitoring for 'dnstracer' binary execution on assessment machines

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[dig]]
- [[nslookup]]
- [[tools/host]]

## References

- Official man page: https://linux.die.net/man/1/dnstracer
- Source code and documentation: https://sourceforge.net/projects/dnstracer/

Related Commands:
- [[commands/dnstracer-basic-trace]]
- [[commands/dnstracer-tcp-trace]]
