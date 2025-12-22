---
id: 6ea6d81e-4c32-49c9-9092-73e775846df6
name: Sublist3r
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - Enumeration
  - Network
  - OSINT
url: 'https://github.com/aboul3la/Sublist3r'
commands:
  - '[[commands/sublist3r-show-help]]'
  - '[[commands/sublist3r-enumerate-subdomains]]'
validated: true
---

# Sublist3r

**Status**: Unverified

## Overview

Sublist3r is a Python-based tool for enumerating subdomains of target websites using Open Source Intelligence (OSINT) techniques. It is commonly used by penetration testers and bug bounty hunters to identify subdomains associated with a target domain, expanding the attack surface for further reconnaissance.

## Description

Sublist3r leverages multiple search engines and services to discover subdomains, including Google, Yahoo, Bing, Baidu, Ask, Netcraft, VirusTotal, ThreatCrowd, DNSdumpster, and ReverseDNS. It supports subdomain brute-forcing and port scanning on discovered subdomains, making it a versatile reconnaissance tool in offensive security operations. The tool outputs results to the console or a file for further analysis.

## Features

- Feature 1: OSINT-based subdomain enumeration via multiple search engines
- Feature 2: Optional subdomain brute-force module for additional discovery
- Feature 3: Port scanning capabilities for live subdomains
- Feature 4: Verbose mode and multi-threading for efficient execution
- Feature 5: Output to file in various formats for integration with other tools

## Installation

### Requirements

- Python 3.6 or higher
- pip and git
- Internet access for search engine queries

### Install Commands

```bash
# On Kali/Ubuntu
sudo apt update
sudo apt install python3-pip git

git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip3 install -r requirements.txt
sudo python3 setup.py install
```

For macOS, use Homebrew to install dependencies: `brew install python git`, then follow the git clone steps.

## Basic Usage

```bash
sublist3r -d example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d, --domain` | Specify the target domain to enumerate |
| `-b, --bruteforce` | Enable the subdomain brute-force module |
| `-p, --ports` | Scan top ports on discovered subdomains |
| `-v, --verbose` | Enable verbose output mode |
| `-t, --threads` | Set number of threads (default: 10) |
| `-e, --engines` | Specify search engines to use |
| `-o, --output` | Save results to a file |
| `-n, --no-banner` | Suppress the startup banner |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

```bash
sublist3r -d example.com
```

This enumerates subdomains for example.com using default engines and displays them in the console.

### Example 2: Advanced Usage

```bash
sublist3r -d example.com -b -p 80,443 -o subdomains.txt -v
```

This enables brute-force, scans ports 80 and 443 on found subdomains, saves output to a file, and runs in verbose mode.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains and Subdomains
- [[Gather Victim Network Information]] Gather Victim Network Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic to search engines (Google, Bing, etc.) with subdomain query patterns from a single source IP
- Detection method 2: High volume of DNS queries for subdomains associated with the organization's domain
- Detection method 3: Presence of Sublist3r binaries or Python scripts in process lists or logs

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
- [[tools/amass]]

## References

- Official GitHub Repository: https://github.com/aboul3la/Sublist3r
- Python Documentation for Dependencies: https://pypi.org/
