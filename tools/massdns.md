---
id: facec6bd-4a3b-46c1-b55f-ea5b018edbd0
name: massdns
type: tool
verified: true
created_at: '2020-06-30T04:48:39.331827+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - dns
  - reconnaissance
url: 'https://github.com/blechschmidt/massdns'
validated: true
---

# massdns

**Status**: ✓ Verified

## Overview

MassDNS is a high-performance DNS stub resolver designed for resolving massive numbers of domain names, in the order of millions or billions. It is particularly useful in offensive security for rapid DNS enumeration during reconnaissance, capable of resolving over 350,000 names per second with default public resolvers. Common use cases include subdomain enumeration follow-up, IP mapping, and large-scale OSINT gathering.

## Description

MassDNS operates by sending asynchronous DNS queries to a list of upstream resolvers, handling responses efficiently without relying on system resolvers. It supports various query types (A, AAAA, MX, etc.) and output formats, making it ideal for tools like subfinder or amass integrations. The tool is lightweight, written in C, and focuses on speed over features like recursive resolution.

## Features

- Feature 1: Asynchronous multi-threaded queries for high throughput
- Feature 2: Support for multiple DNS record types and output formats (simple, full, CSV)
- Feature 3: Configurable resolver lists and retry mechanisms
- Feature 4: Binary output mode for piping to other tools

## Installation

### Requirements

- GCC compiler and make
- Linux environment (Kali preferred)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/blechschmidt/massdns.git

# Build the tool
cd massdns
make

# Optional: Install to /usr/local/bin
sudo cp bin/massdns /usr/local/bin/
```

For Kali Linux: Not pre-installed; follow the above steps.

For Ubuntu: Install dependencies with `sudo apt install build-essential git`, then build as above.

## Basic Usage

```bash
./massdns --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -r, --resolvers | File containing resolver IPs (one per line) |
| -t, --type | DNS query type (A, AAAA, etc.) |
| -o, --output | Output format (S=simple, F=full, C=csv) |
| -w, --outfile | Output file path |
| -T, --timeout | Query timeout in seconds |
| -R, --retry | Number of retries per query |

## Examples

### Example 1: Basic Usage

Resolve A records from a domains file:

```bash
massdns -r resolvers.txt -t A -o S -w output.txt domains.txt
```

### Example 2: Advanced Usage

Resolve multiple types with retries:

```bash
massdns -r resolvers.txt -t A,AAAA -o S -w results.txt -R 3 -T 2 domains.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of UDP/53 traffic from a single host to multiple public DNS resolvers
- Detection method 2: Unusual patterns in DNS query logs (e.g., bursts of queries for many domains)
- Detection method 3: Presence of massdns binary or compilation artifacts on compromised systems

## Related Procedures

- [[procedures/Bulk-DNS-Resolution-for-Reconnaissance]]
- [[procedures/Subdomain-Enumeration-Workflow]]

## Related Tools

- [[tools/subfinder]]
- [[tools/DNSRecon]]

## References

- Official GitHub: https://github.com/blechschmidt/massdns
- Usage guide: https://github.com/blechschmidt/massdns/blob/master/README.md
