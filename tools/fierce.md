---
id: f41e1c0b-dd97-43cf-bd76-7e94897e727f
type: tool
verified: true
created_at: '2019-08-28T21:17:38.993918+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - dns
  - subdomain-enumeration
url: 'https://github.com/mschwager/fierce'
commands:
  - '[[commands/fierce-scan-domain]]'
  - '[[commands/fierce-bruteforce-subdomains]]'
  - '[[commands/fierce-scan-with-wordlist]]'
validated: true
---

# fierce

**Status**: Unverified

## Overview

Fierce is a domain reconnaissance tool designed specifically for enumerating subdomains of a target domain through DNS queries. It is not an IP scanner or a tool for untargeted attacks but focuses on quickly identifying potential entry points within a corporate network by bruteforcing common subdomain names and patterns. Commonly used in penetration testing for mapping the attack surface during the reconnaissance phase.

## Description

Fierce is a PERL-based script that performs fast domain scans (typically completing in minutes) by generating likely subdomain permutations and validating them via DNS responses. It avoids exploitation and is purely for information gathering, listing only responsive targets unless configured otherwise. Key tactics include bruteforcing with built-in wordlists, custom wordlist support, and optional searches for existing subdomains. It supports specifying DNS servers and output formats for integration with other tools.

## Features

- Feature 1: Built-in subdomain wordlist for common names (e.g., www, mail, ftp)
- Feature 2: Custom wordlist support for organization-specific terms
- Feature 3: Bruteforce mode with numeric permutations (e.g., trailing numbers)
- Feature 4: Configurable DNS servers to bypass filtering
- Feature 5: Output to file for chaining with tools like httpx or subfinder

## Installation

### Requirements

- Perl 5 (with Net::DNS module)
- Access to DNS resolvers

### Install Commands

```bash
# On Kali Linux (pre-installed or via repo)
apt update && apt install fierce

# Manual install from GitHub
git clone https://github.com/mschwager/fierce.git
cd fierce
perl fierce.pl --help
```

## Basic Usage

```bash
fierce --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -d, --domain | Specify target domain |
| -w, --wordlist | Use custom wordlist |
| -s, --subdomain | Enable bruteforce mode |
| -D, --dns-servers | Specify DNS servers (comma-separated) |
| -o, --file-output | Output results to file |

## Examples

### Example 1: Basic Usage

```bash
fierce --domain example.com
```

### Example 2: Advanced Usage

```bash
fierce --domain example.com --wordlist /usr/share/wordlists/subdomains.txt --dns-servers 8.8.8.8,1.1.1.1 --file-output results.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain Profile
- [[Domain Properties]] Gather Victim Network Information: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of DNS queries from a single source targeting subdomain permutations
- Detection method 2: Unusual patterns in DNS logs for common words (e.g., admin, test) appended to the domain
- Detection method 3: Network monitoring for PERL process spawning with fierce.pl arguments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/subfinder]]
- [[tools/DNSRecon]]

## References

- Official GitHub Repository: https://github.com/mschwager/fierce
- Kali Tools Documentation: https://www.kali.org/tools/fierce/
