---
id: f534f6c5-5c6b-4c98-b77e-5d152b5a9f83
type: tool
verified: true
created_at: '2019-08-28T21:17:36.954532+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reconnaissance
  - distributed-scanning
  - nmap
url: 'https://github.com/krabelize/dnmap'
commands:
  - '[[commands/dnmap-start-server]]'
  - '[[commands/dnmap-connect-client]]'
  - '[[commands/dnmap-generate-input-file]]'
validated: true
---

# dnmap-server

**Status**: Unverified

## Overview

dnmap is a distributed nmap framework that allows users to parallelize large-scale network scans across multiple clients. It uses a client-server architecture where the server coordinates tasks and clients execute individual nmap scans, making it ideal for scanning extensive IP ranges with limited bandwidth or multiple collaborators.

## Description

dnmap reads a pre-prepared file containing nmap commands and distributes these tasks to connected clients. The server handles all logic, statistics, and aggregation of results, while output from scans is stored both on the server and individual clients. This tool is particularly useful for reconnaissance in large networks where a single machine would be too slow or bandwidth-constrained.

## Features

- Feature 1: Distributed task allocation to multiple clients over TCP.
- Feature 2: Centralized management of scan progress and statistics.
- Feature 3: Support for standard nmap syntax in input files for easy integration.
- Feature 4: Results aggregation and storage on server for post-scan analysis.

## Installation

### Requirements

- Perl 5 (with Socket and IO::Socket modules).
- nmap installed on all client machines.
- Network connectivity between server and clients.

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git perl -y
git clone https://github.com/krabelize/dnmap.git
cd dnmap

# Make scripts executable (if needed)
chmod +x dnmap_server.pl dnmap_client.pl
```

For Kali Linux, it may be available via apt:

```bash
sudo apt install dnmap
```

## Basic Usage

```bash
dnmap_server.pl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p, --port` | Specify listening port (default: 6699) |
| `-h, --help` | Show help message |
| `-v, --version` | Display version information |

## Examples

### Example 1: Basic Usage

Start the server:

```bash
perl dnmap_server.pl 6699
```

Generate an input file:

```bash
[[commands/dnmap-generate-input-file]]
```

Connect a client:

```bash
[[commands/dnmap-connect-client]]
```

### Example 2: Advanced Usage

For a large scan, prepare a file with multiple nmap lines (one per target or subnet) and distribute to several clients simultaneously.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual TCP connections on non-standard ports (e.g., 6699) between internal hosts.
- Detection method 2: High volume of outbound nmap traffic from multiple internal IPs.
- Detection method 3: Presence of dnmap_server.pl or dnmap_client.pl processes via process monitoring.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/masscan]]

## References

- Official GitHub: https://github.com/krabelize/dnmap
- Original documentation: Included in the repository README.
