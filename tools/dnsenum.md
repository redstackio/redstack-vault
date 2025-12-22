---
type: tool
description: >-
  A multi-threaded Perl script for enumerating DNS information about domains and
  discovering non-contiguous IP blocks.
url: 'https://github.com/fwaeytens/dnsenum'
tags:
  - enumeration
  - dns
  - reconnaissance
platforms:
  - Linux
commands:
  - '[[commands/dnsenum-basic-enumeration]]'
verified: true
validated: true
---

# dnsenum

**Status**: Unverified

## Overview

Dnsenum is a multi-threaded Perl script designed for DNS enumeration. It gathers DNS information about a target domain, identifies non-contiguous IP blocks, and supports dictionary-based brute-force attacks to discover subdomains. It is commonly used in reconnaissance phases of security assessments to map out a target's DNS infrastructure.

## Description

Dnsenum performs comprehensive DNS enumeration by querying for host records (A, MX, TXT, etc.), name servers, and attempting zone transfers from authoritative servers. It can integrate wordlists for subdomain brute-forcing and handles permutations of common subdomain names. The tool is particularly useful for identifying hidden or misconfigured DNS entries that reveal internal network details.

## Features

- Feature 1: Enumerates standard DNS records including A, NS, MX, SOA, and TXT.
- Feature 2: Attempts zone transfers from name servers to extract full zone data.
- Feature 3: Supports subdomain brute-forcing with customizable wordlists and permutations.
- Feature 4: Discovers non-contiguous IP blocks associated with the domain.
- Feature 5: Multi-threaded for faster enumeration on large domains.

## Installation

### Requirements

- Perl (version 5.10 or higher)
- Required Perl modules: Net::DNS, Net::Netrc, XML::Writer, Getopt::Long, IO::Select, LWP::UserAgent

### Install Commands

```bash
# On Kali Linux (pre-installed)

# On Ubuntu/Debian
sudo apt update
sudo apt install dnsenum

# Manual installation from source
sudo apt install perl libnet-dns-perl libnet-netrc-perl libxml-writer-perl libgetopt-long-descriptive-perl libio-select-perl libwww-perl
wget https://github.com/fwaeytens/dnsenum/archive/master.zip
unzip master.zip
cd dnsenum-master
sudo make install
```

## Basic Usage

```bash
dnsenum --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose output for detailed logging |
| `-f file` | Specify a wordlist file for brute-forcing subdomains |
| `-t threads` | Set number of threads for multi-threaded operations |
| `-e` | Enable enumeration mode (default) |

## Examples

### Example 1: Basic Usage

```bash
dnsenum example.com
```

This runs basic enumeration on example.com, retrieving host addresses, name servers, and attempting zone transfers.

### Example 2: Advanced Usage

```bash
dnsenum -f /usr/share/wordlists/dnsmap.txt -t 10 example.com
```

This uses a wordlist for subdomain brute-forcing with 10 threads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] DNS
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of DNS queries from a single source to authoritative name servers.
- Detection method 2: Failed zone transfer attempts logged in DNS server logs (e.g., BIND query logs).
- Detection method 3: Unusual patterns of subdomain queries matching common wordlists.
- Detection method 4: Network traffic analysis showing Perl-based tool signatures or multi-threaded query bursts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[dig]]
- [[nslookup]]
- [[tools/fierce]]

## References

- Official GitHub Repository: https://github.com/fwaeytens/dnsenum
- DNS Enumeration Guide: https://www.offensive-security.com/metasploit-unleashed/dns/

*Last updated: 2023-05-29T16:48:53.029709+00:00*
