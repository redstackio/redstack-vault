---
id: c31d2b86-9fb4-4643-964b-37f727c92fa1
type: tool
verified: true
created_at: '2019-08-28T21:17:36.321950+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
description: >-
  A Python-based tool for identifying expired or available domains suitable for
  phishing and command-and-control (C2) infrastructure by analyzing domain
  expiration status, BlueCoat categorization, and historical snapshots from
  Archive.org.
url: 'https://github.com/TechnicalM2/domainhunter'
tags:
  - reconnaissance
  - phishing
  - c2
  - domain-enumeration
platforms:
  - Linux
  - macOS
  - Windows
commands:
  - '[[commands/domain-hunter-basic-scan]]'
  - '[[commands/domain-hunter-category-check]]'
  - '[[commands/domain-hunter-archive-history]]'
category: Reconnaissance
validated: true
---

# Domain Hunter

**Status**: Unverified

## Overview

Domain Hunter is a reconnaissance tool designed to help security professionals and red teams identify potential domain names for phishing campaigns or C2 servers. It automates the process of checking domain expiration dates, categorizing domains using BlueCoat's web filtering database, and reviewing historical content via Archive.org to ensure domains have a clean or desirable history (e.g., no prior malicious associations that could trigger alerts).

Common use cases include:
- Generating lists of expired domains from keyword-based searches.
- Filtering domains to avoid blacklisted or categorized ones.
- Assessing domain history to minimize detection risks during operations.

## Description

The tool operates by taking input keywords or domain lists, querying domain registrars for expiration status, cross-referencing with BlueCoat for content categorization (e.g., ensuring domains aren't flagged as malware or phishing sites), and fetching Wayback Machine snapshots from Archive.org to review past website content. This helps in selecting 'clean' domains that blend in with legitimate traffic. It's particularly useful in the initial reconnaissance phase of phishing or infrastructure setup, aligning with MITRE ATT&CK tactics like Reconnaissance (TA0043).

## Features

- **Domain Expiration Checks**: Queries WHOIS data to find recently expired or soon-to-expire domains matching keywords.
- **BlueCoat Categorization**: Integrates with BlueCoat's API or databases to categorize domains and filter out risky ones.
- **Archive.org Integration**: Pulls historical snapshots to analyze past usage and avoid domains with suspicious history.
- **Output Formatting**: Generates CSV or JSON reports with scores for suitability (e.g., low categorization risk, clean history).
- **Keyword-Based Searching**: Supports input files with keywords to generate domain suggestions.

## Installation

### Requirements

- Python 3.6+
- pip-installed dependencies: requests, whois, beautifulsoup4
- Access to internet for API queries (no special API keys required for basic use, but BlueCoat may need configuration).

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3-pip -y
git clone https://github.com/TechnicalM2/domainhunter.git
cd domainhunter

# Install dependencies
pip3 install -r requirements.txt
```

For Windows/macOS, use equivalent package managers (e.g., brew on macOS) and run without sudo.

## Basic Usage

```bash
python3 domainhunter.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-f, --file` | Input file with keywords or domains |
| `-o, --output` | Output file for results (CSV/JSON) |
| `--bluecoat` | Enable BlueCoat categorization check |
| `--archive` | Enable Archive.org history check |
| `-t, --threads` | Number of threads for faster querying (default: 10) |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Run a basic scan on a keyword file to find expired domains:

```bash
python3 domainhunter.py -f keywords.txt -o results.csv
```

This queries for expired domains related to keywords in `keywords.txt` and outputs to CSV.

### Example 2: Advanced Usage

Perform a full check including categorization and history:

```bash
python3 domainhunter.py -f keywords.txt -o full_results.json --bluecoat --archive -t 20
```

This enables BlueCoat and Archive.org checks with 20 threads for efficiency on larger lists.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information (domain reconnaissance)
- [[T1583.001]] Acquire Infrastructure: Domains

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to WHOIS servers (e.g., whois.iana.org) or Archive.org API endpoints.
- High volume of domain queries from a single IP, potentially triggering rate limits.
- File artifacts like `keywords.txt` or output CSVs with domain lists in user directories.
- Process monitoring for `python3 domainhunter.py` executions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/theHarvester]] (for broader OSINT collection)
- [[tools/Sublist3r]] (for subdomain enumeration)
- [[tools/amass]] (for domain intelligence gathering)

## References

- Official GitHub Repository: https://github.com/TechnicalM2/domainhunter
- BlueCoat Documentation: https://www.bluecoat.com/
- Archive.org API: https://archive.org/help/wayback_api.php
