---
id: dd2343d1-dc0c-4ed9-9f78-50d60a1e1485
type: tool
verified: true
created_at: '2019-08-28T21:17:42.942561+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - leaked-credentials
  - osint
url: 'https://github.com/thewhiteh4t/pwndb'
validated: true
---

# pwndb

**Status**: Unverified

## Overview

pwndb is a Python-based command-line tool designed for searching leaked credentials across a dark web Onion service database. It is primarily used in reconnaissance and credential gathering phases of security assessments to identify compromised accounts, passwords, and other sensitive data from various breaches.

## Description

The tool interfaces with the pwndb.onion service, a search engine aggregating data from multiple data breaches. Users can query by email, domain, or hash to retrieve associated leaked information. It requires a Tor connection to access the Onion site and is useful for OSINT operations, red teaming, and validating credential exposure. Note that results depend on the database's coverage and may include outdated or false positives.

## Features

- Feature 1: Single or batch searches via email, domain, or hash queries
- Feature 2: JSON output support for integration with other tools/scripts
- Feature 3: Verbose mode for detailed logging during searches
- Feature 4: File-based input for bulk credential checking

## Installation

### Requirements

- Python 3.6+
- Tor service running on localhost:9050 (install via `apt install tor` on Debian-based systems)
- pip and git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/thewhiteh4t/pwndb.git
cd pwndb

# Install dependencies
pip3 install -r requirements.txt

# Start Tor (if not running)
sudo systemctl start tor
```

## Basic Usage

```bash
python3 pwndb.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `--file TEXT` | Specify a file with search terms |
| `--json` | Output in JSON format |
| `--verbose` | Enable verbose output |

## Examples

### Example 1: Basic Usage

```bash
python3 pwndb.py search user@example.com
```

### Example 2: Advanced Usage

```bash
python3 pwndb.py search --file targets.txt --json --verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Search Open Websites-Domains]] Search Open Technical Databases

### Tactics

- [[Collection]] Collection
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic to .onion domains via Tor (monitor SOCKS proxy connections on port 9050)
- Detection method 2: Process monitoring for pwndb.py or Python scripts accessing Tor
- Detection method 3: Logs of queries to pwndb.onion in Tor access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/tor]]
- [[tools/theHarvester]]

## References

- Official GitHub: https://github.com/thewhiteh4t/pwndb
- Tor Project: https://www.torproject.org

*Last updated: 2023-10-01T00:00:00+00:00*
