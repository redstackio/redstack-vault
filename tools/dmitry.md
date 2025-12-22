---
id: f3865ce7-d76e-440f-9f63-33ec928182aa
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - UNIX
tags:
  - reconnaissance
  - information-gathering
  - whois
  - subdomain-enumeration
  - email-enumeration
  - port-scanning
url: 'https://sourceforge.net/projects/dmitry/'
commands:
  - '[[commands/dmitry-whois-lookup]]'
  - '[[commands/dmitry-subdomain-search]]'
  - '[[commands/dmitry-email-search]]'
  - '[[commands/dmitry-tcp-port-scan]]'
validated: true
---

# dmitry

**Status**: Unverified

## Overview

DMitry (Deepmagic Information Gathering Tool) is a lightweight, command-line tool designed for passive and active reconnaissance of target hosts. It collects publicly available information such as whois data, subdomains, email addresses, and performs basic TCP port scanning, making it useful for initial phases of security assessments and OSINT operations.

## Description

Coded in C for efficiency on UNIX/Linux systems, DMitry is modular, allowing users to select specific information-gathering modules. It supports whois queries across various databases, subdomain brute-forcing, web-based email harvesting, uptime estimation via banner grabbing, and TCP port scanning with optional banner retrieval. The tool outputs results to stdout or files and is particularly suited for environments where stealthy, command-line-only reconnaissance is needed without relying on heavy frameworks.

## Features

- **Whois Lookups**: Queries domain, IP, and network handle whois servers for registration and ownership details.
- **Subdomain Enumeration**: Performs dictionary-based searches to discover hidden subdomains.
- **Email Harvesting**: Crawls target websites to extract email addresses from public pages.
- **TCP Port Scanning**: Scans common ports and optionally grabs service banners for version detection.
- **Uptime Information**: Infers system uptime through banner responses during scans.
- **Modular Execution**: Run individual modules or combine them for comprehensive scans.
- **Output Flexibility**: Direct to console or save to files for further analysis.

## Installation

### Requirements

- UNIX/Linux operating system (e.g., Ubuntu, Kali).
- Basic build tools (GCC, make) if compiling from source.
- Internet access for whois queries and web crawling.

### Install Commands

On Debian/Ubuntu-based systems (including Kali Linux, where it may be pre-installed):

```bash
sudo apt update
sudo apt install dmitry
```

If not available in repositories, compile from source:

```bash
# Download from SourceForge
wget https://sourceforge.net/projects/dmitry/files/latest/download -O dmitry.tar.gz
tar -xzf dmitry.tar.gz
cd dmitry-*
make
sudo make install
```

For other platforms, check the official SourceForge page for binaries or adapt the build process.

## Basic Usage

```bash
dmitry --help
```

Basic syntax: `dmitry [options] <target>` where options enable specific modules.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and usage |
| -o <file> | Output results to specified file |
| -s | Enable subdomain search |
| -e | Enable email address search |
| -p | Enable TCP port scan |
| -w | Enable world whois lookup |
| -i | Enable internet number whois |
| -n | Enable NIC handle whois |
| -b | Enable banner grabbing during port scan |
| -t <threads> | Set number of threads for port scanning |

## Examples

### Example 1: Basic Usage (Whois + Subdomains)

```bash
dmitry -winse example.com
```

This runs whois (-win), subdomain (-s), and email (-e) modules on the target.

### Example 2: Advanced Usage (Port Scan with Banners)

```bash
dmitry -p -b -t 50 192.168.1.1
```

Performs a TCP port scan with banner grabbing using 50 threads.

### Example 3: Full Modular Scan to File

```bash
dmitry -winsep example.com -o recon_results.txt
```

Executes all core modules and saves output to a file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Gather Victim Network Information]] Gather Victim Network Information
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound connections to whois servers (e.g., whois.iana.org, whois.arin.net).
- Unusual HTTP requests during email/subdomain crawling from reconnaissance IPs.
- TCP SYN scans on common ports from a single source.
- Presence of DMitry binary or its strings in process lists/memory dumps.
- Log entries for banner grabs on services like SSH/HTTP.

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
- [[tools/theHarvester]]

## References

- Official SourceForge project: https://sourceforge.net/projects/dmitry/
- DMitry documentation and source code.
