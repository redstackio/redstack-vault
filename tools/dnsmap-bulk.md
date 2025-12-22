---
type: tool
verified: true
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
  - enumeration
  - subdomain-bruteforce
url: 'https://github.com/fwaeytens/dnsmap'
validated: true
---

# dnsmap-bulk

**Status**: Unverified

## Overview

Dnsmap-bulk is a bash script wrapper around the dnsmap tool, designed for efficient bulk subdomain brute-forcing during penetration testing and security assessments. It automates the enumeration of subdomains by processing wordlists against target domains, making it ideal for the information gathering phase where traditional methods like zone transfers fail.

## Description

dnsmap was originally released in 2006, inspired by the fictional story “The Thief No One Saw” by Paul Craig from the book “Stealing the Network – How to Own the Box”. The dnsmap-bulk.sh script enhances this by enabling bulk operations across multiple domains or large wordlists, allowing pentesters to discover hidden subdomains, IP netblocks, and infrastructure details. It's particularly useful when passive reconnaissance is insufficient, providing active brute-force capabilities without excessive noise.

## Features

- Feature 1: High-speed subdomain brute-forcing using optimized DNS queries
- Feature 2: Support for custom wordlists and bulk domain processing
- Feature 3: Output redirection for integration with other tools like httpx or subfinder
- Feature 4: Lightweight and script-based, requiring no compilation

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- dnsmap binary installed
- Bash shell
- Wordlist files (e.g., from SecLists or custom)

### Install Commands

```bash
# Install dnsmap if not present (on Ubuntu/Debian)
sudo apt update && sudo apt install dnsmap

# Download dnsmap-bulk.sh (assuming it's from a repository; adjust URL as needed)
wget https://raw.githubusercontent.com/user/dnsmap-bulk/master/dnsmap-bulk.sh
chmod +x dnsmap-bulk.sh

# Or clone the repo if available
git clone https://github.com/example/dnsmap-bulk.git
cd dnsmap-bulk
```

On Kali Linux, dnsmap is often pre-installed or available via apt.

## Basic Usage

```bash
./dnsmap-bulk.sh example.com /usr/share/wordlists/dnsmap.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -o, --output | Specify output file for results |
| -w, --wordlist | Path to wordlist (default: built-in) |
| -d, --domain | Target domain |

## Examples

### Example 1: Basic Usage

```bash
./dnsmap-bulk.sh --domain target.com --wordlist subdomains.txt
```

This enumerates subdomains for target.com using the provided wordlist and prints results to stdout.

### Example 2: Advanced Usage

```bash
./dnsmap-bulk.sh -o results.txt -d example.com /path/to/large-wordlist.txt
```

Saves all discovered subdomains to results.txt for later processing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of DNS queries from a single source to a target's nameservers
- Detection method 2: Anomalous UDP/53 traffic patterns matching brute-force signatures
- Detection method 3: Log analysis for repeated NXDOMAIN responses

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
- [[tools/subfinder]]

## References

- Original dnsmap: https://github.com/fwaeytens/dnsmap
- Book: “Stealing the Network – How to Own the Box” by Paul Craig
- Wordlists: https://github.com/danielmiessler/SecLists
