---
id: 95bfb4ed-1477-4936-a534-10e0fdebbdca
name: dnsdict6
type: tool
verified: true
created_at: '2019-08-28T21:17:35.687802Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - dns
  - brute-force
  - reconnaissance
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# dnsdict6

**Status**: Unverified

## Overview

Dnsdict6 is a specialized tool from the THC-IPv6 toolkit designed for performing dictionary-based brute-force attacks against IPv6 DNS servers. It exploits potential weaknesses in IPv6 name resolution by systematically querying DNS for guessed hostnames, helping to enumerate hidden or undocumented IPv6 hosts in a network or domain.

## Description

Dnsdict6 sends AAAA (IPv6) DNS queries for each entry in a provided wordlist, appending it to the target domain. It is particularly useful in reconnaissance phases of security assessments targeting IPv6-enabled environments, where traditional IPv4 tools may miss dual-stack or IPv6-only infrastructure. The tool supports output redirection and verbose logging for detailed analysis of query responses.

## Features

- Feature 1: Dictionary-driven IPv6 hostname enumeration via DNS queries
- Feature 2: Support for custom wordlists tailored to common IPv6 naming conventions
- Feature 3: Verbose mode for debugging query timings and responses
- Feature 4: Output file support for logging discovered hosts

## Installation

### Requirements

- Linux environment with IPv6 support enabled
- Git and build essentials (gcc, make)
- THC-IPv6 toolkit dependencies

### Install Commands

```bash
# Clone the THC-IPv6 repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Configure and build
./configure
make
sudo make install
```

Dnsdict6 will be available in /usr/local/bin after installation.

## Basic Usage

```bash
dnsdict6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -d, --domain | Specify the target domain |
| -o, --output | Save results to a file |
| -v, --verbose | Enable detailed query logging |
| -h, --help | Show usage information |

## Examples

### Example 1: Basic Usage

```bash
dnsdict6 -d example.com /usr/share/wordlists/dnsmap.txt
```

This runs a basic dictionary attack using a standard wordlist.

### Example 2: Advanced Usage

```bash
dnsdict6 -d example.com -o discovered_hosts.txt -v /path/to/custom_ipv6_wordlist.txt
```

Performs a verbose attack and saves results to a file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software]] Gather Victim Host Information: DNS

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of AAAA DNS queries from a single source to a domain
- Detection method 2: DNS server logs showing patterned hostname queries matching wordlist patterns
- Detection method 3: Network monitoring for unusual IPv6 DNS traffic spikes

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/thc-ipv6-toolkit]]
- [[tools/DNSRecon]]

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in repository README
