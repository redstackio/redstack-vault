---
id: 3d18bacb-0830-4412-bc24-c7ef69dfb6a2
type: tool
verified: true
created_at: '2019-08-28T21:17:24.707379Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - reconnaissance
  - enumeration
  - dns
  - subdomain-bruteforce
url: 'http://dnsmap.info/'
validated: true
---

# dnsmap

**Status**: Unverified

## Overview

Dnsmap is a fast, multi-threaded tool designed for brute-forcing DNS subdomains during the reconnaissance phase of penetration testing. It helps security professionals enumerate hidden or non-obvious subdomains that could expose additional attack surfaces, such as administrative interfaces or internal services. Originally released in 2006, it remains relevant for infrastructure security assessments where traditional methods like zone transfers fail.

## Description

Dnsmap was inspired by the fictional story “The Thief No One Saw” from the book “Stealing the Network – How to Own the Box” by Paul Craig. It is primarily used in the information gathering and enumeration stages of pentests. During enumeration, pentesters identify target IP netblocks, domain names, and other details. Subdomain brute-forcing with dnsmap is particularly effective when zone transfers are blocked, as it systematically tests wordlist entries against the target domain's DNS to discover valid subdomains, record types (A, CNAME, MX, etc.), and associated IPs.

The tool supports recursive discovery, allowing it to chain findings for deeper enumeration, and outputs in various formats for integration with other recon tools.

## Features

- **Brute-Force Enumeration**: Tests wordlists against target domains to find subdomains.
- **Recursive Mode**: Automatically enumerates subdomains of discovered subdomains for comprehensive coverage.
- **Multi-Threaded**: Speeds up queries with parallel processing.
- **Flexible Output**: Supports stdout, file output, and CSV format for easy parsing.
- **Record Type Support**: Discovers A, CNAME, MX, and other DNS records.
- **Wordlist Compatibility**: Works with custom or standard wordlists like those in /usr/share/wordlists.

## Installation

### Requirements

- Linux/Unix environment (Kali Linux recommended).
- GCC compiler for building from source.
- Wordlists for brute-forcing (e.g., dnsmap.txt).

### Install Commands

```bash
# On Kali Linux (pre-installed or via repo)
apt update && apt install dnsmap

# On Ubuntu/Debian
apt update && apt install dnsmap

# From source (if not in repos)
git clone https://github.com/makdotnet/dnsmap.git
cd dnsmap/src
make
sudo make install
```

For macOS, use Homebrew: `brew install dnsmap` (if available) or compile from source.

## Basic Usage

```bash
dnsmap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -w <file> | Specify wordlist file |
| -r | Enable recursive subdomain brute-forcing |
| -R <levels> | Limit recursion to specified levels (default unlimited) |
| -o <file> | Output results to file |
| -c | Output in CSV format |
| -t <threads> | Number of threads (default 100) |
| -d | Enable debug mode |

## Examples

### Example 1: Basic Usage

```bash
dnsmap -w /usr/share/wordlists/dnsmap.txt example.com
```

This runs a basic brute-force scan using the default wordlist.

### Example 2: Advanced Usage

```bash
dnsmap -r -w custom.txt -o results.txt -c -t 200 example.com
```

Performs recursive enumeration with CSV output to a file using 200 threads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Domain Properties]] Gather Victim Network Information: Domain Properties
- [[Gather Victim Host Information]] Gather Victim Identity Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of DNS queries from a single source targeting common subdomain permutations (e.g., admin, test, dev).
- Unusual patterns in DNS logs, such as rapid A/CNAME lookups for non-existent subdomains.
- Network traffic analysis showing threaded DNS requests to authoritative name servers.
- Endpoint logs if run on compromised hosts, looking for dnsmap binary or child processes.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dnsenum]]
- [[tools/Sublist3r]]
- [[tools/amass]]

## References

- Official website: http://dnsmap.info/
- GitHub repository: https://github.com/makdotnet/dnsmap
- Book: "Stealing the Network – How to Own the Box" by Paul Craig
- Related Commands: [[commands/dnsmap-basic-subdomain-brute-force]], [[commands/dnsmap-recursive-subdomain-discovery]], [[commands/dnsmap-output-to-csv-file]]
