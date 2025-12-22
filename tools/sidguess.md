---
id: 14e1a2c3-6c6c-4f55-83aa-75d54a9b1aaa
name: sidguess
type: tool
verified: true
created_at: '2019-08-28T21:17:19.698634+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - oracle
  - database
  - reconnaissance
  - sid-guessing
url: 'https://www.dbnetworks.com/tools/sidguess'
validated: true
---

# sidguess

**Status**: Unverified

## Overview

sidguess is a specialized tool for enumerating Oracle database SIDs (System Identifiers) and instances through brute-force guessing using a dictionary-based approach. It is commonly used in penetration testing and reconnaissance phases to identify valid database identifiers on Oracle servers without prior knowledge of the SID. The tool operates slowly at 80-100 guesses per second but is effective for targeted enumeration in environments where speed is not critical.

## Description

sidguess connects to an Oracle database listener on TCP port 1521 (default) and systematically tests potential SID names from a provided dictionary file. It sends service requests to the listener and analyzes responses to determine if a SID is valid. This tool is particularly useful in scenarios involving legacy Oracle deployments or when initial access to database credentials is unavailable. It supports basic connection parameters like target host, port, and dictionary input, making it a lightweight option for Oracle-specific reconnaissance.

## Features

- Feature 1: Dictionary-driven SID guessing with customizable wordlists
- Feature 2: Support for specifying target host and port for Oracle listener
- Feature 3: Simple output indicating successful SID discoveries
- Feature 4: Low resource footprint suitable for prolonged enumeration sessions

## Installation

### Requirements

- Perl (version 5.x or higher, as the tool is Perl-based)
- Network access to the target Oracle listener (TCP/1521)
- A dictionary file with common Oracle SID names (e.g., ORCL, XE, PROD)

### Install Commands

```bash
# On Kali Linux or Ubuntu (assuming download from source)
wget https://example.com/sidguess.pl -O sidguess.pl
chmod +x sidguess.pl

# Or if available via package manager (rare, check repos)
# apt search sidguess (typically manual install)
```

For macOS:
```bash
brew install perl  # If not pre-installed
# Then download and run as above
```

The tool is not pre-installed on standard distributions and requires manual download from security tool repositories or the author's site.

## Basic Usage

```bash
./sidguess.pl -t target_ip -d dictionary.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -t | Target IP or hostname |
| -p | Port (default: 1521) |
| -d | Dictionary file path |
| -v | Verbose output for debugging |

## Examples

### Example 1: Basic Usage

```bash
./sidguess.pl -t 192.168.1.50 -p 1521 -d /usr/share/wordlists/oracle_sids.txt
```

This runs guesses against the target at the default port using a standard dictionary.

### Example 2: Advanced Usage

```bash
./sidguess.pl -t oracle-db.example.com -d custom_sids.txt -v
```

Enables verbose mode for detailed logging of each attempt.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Vulnerability Scanning (for database service enumeration)
- [[Gather Victim Host Information]] Gather Victim Host Information (identifying database configurations)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual TCP connections to port 1521 from non-standard sources, with high volume of failed service requests
- Detection method 2: Oracle listener logs showing repeated invalid SID attempts (monitor for patterns in TNS listener logs)
- Detection method 3: Network IDS alerts on Oracle protocol traffic spikes to a single listener

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sqlmap]] (for broader Oracle exploitation)
- [[tools/Nmap]] (for initial Oracle service discovery)

## References

- Original tool documentation: https://www.dbnetworks.com/tools/sidguess
- Oracle Listener Security: Oracle official docs on TNS configuration

*Last updated: 2023-05-29T16:48:53.029709+00:00*
