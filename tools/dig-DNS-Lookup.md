---
url: 'https://linux.die.net/man/1/dig'
tags:
  - dns
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows (via Cygwin)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:39.366Z'
id: bd269fd5-a889-4af4-aaed-dddae967e644
validated: true
submitted: true
---
# dig-DNS-Lookup

**Status**: Unverified

## Overview

Dig is a command-line DNS lookup tool used for querying DNS servers for records like A, CNAME, MX, essential for reconnaissance in security testing, such as detecting subdomain takeovers.

## Description

Dig (Domain Information Groper) provides flexible DNS queries, displaying detailed responses including headers, questions, and answers. In offensive security, it's used to enumerate DNS configurations, identify misconfigurations like dangling CNAMEs pointing to services like SendGrid.

## Features

- Feature 1: Supports multiple query types (A, CNAME, TXT, etc.)
- Feature 2: Short and verbose output modes
- Feature 3: Custom DNS server specification

## Installation

### Requirements

- Unix-like system or Windows with BIND tools

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install dnsutils

# On macOS (via Homebrew)
brew install bind
```

## Basic Usage

```bash
dig --help
```

### Common Options

| Option | Description |
|--------|-------------|
| +short | Concise output |
| @server | Query specific DNS server |
| -t type | Specify record type (e.g., CNAME) |

## Examples

### Example 1: Basic Usage

```bash
dig example.com
```

### Example 2: Advanced Usage

```bash
dig +short email.smule.com CNAME
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: DNS

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing DNS queries from unusual sources
- High volume of recursive DNS lookups

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[nslookup]]
- [[host]]

## References

- Official documentation: https://linux.die.net/man/1/dig
- Related resources: ISC BIND tools
