---
id: bce52f64-029a-4317-8014-b5a61cc6b48f
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - osint
  - reconnaissance
  - footprinting
url: 'https://www.spiderfoot.net/'
commands:
  - '[[commands/spiderfoot-scan-target]]'
  - '[[commands/spiderfoot-list-modules]]'
  - '[[commands/spiderfoot-start-server]]'
validated: true
---

# SpiderFoot

**Status**: Unverified

## Overview

SpiderFoot is an open-source intelligence (OSINT) automation tool designed for footprinting and reconnaissance. It automates the collection of information from over 200 public data sources, including DNS records, search engines, social media, and threat intelligence feeds, to map out a target's digital footprint.

## Description

SpiderFoot excels in passive reconnaissance by querying external sources without direct interaction with the target, reducing detection risk. It supports targets like domains, IP addresses, email addresses, and phone numbers, producing correlated results in formats like JSON, HTML, or timelines. Commonly used in red teaming for initial target assessment, vulnerability identification through exposed data, and building attack surface maps.

## Features

- Feature 1: Modular architecture with 200+ modules for different data sources (e.g., DNS, WHOIS, Google dorks, Shodan).
- Feature 2: Correlation engine to link findings (e.g., IP to domain to email leaks).
- Feature 3: Web-based GUI for interactive scans and CLI for automation/scripting.
- Feature 4: Export options including graphs, timelines, and human-readable reports.
- Feature 5: API integration for embedding in larger toolchains.

## Installation

### Requirements

- Python 3.7+
- pip and git
- Approximately 500MB disk space for modules and data

### Install Commands

```bash
# Clone the repository
git clone https://github.com/smicallef/spiderfoot.git
cd spiderfoot

# Install dependencies
python3 -m pip install -r requirements.txt

# For Kali Linux (pre-built package available)
sudo apt update && sudo apt install spiderfoot

# For Ubuntu (from source as above)

# For Windows/macOS: Use the source installation with Python
```

Verify installation by running `sf --help`.

## Basic Usage

```bash
sf --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -s, --source | Target to scan (domain, IP, etc.) |
| -o, --output | Output file (JSON, HTML, etc.) |
| -f, --filter | Modules to include/exclude |
| -m, --maxthreads | Maximum threads for parallel queries |
| --server | Start web server |

## Examples

### Example 1: Basic Usage

```bash
sf -s example.com -o results.json
```

Run a full scan on example.com and save results to JSON.

### Example 2: Advanced Usage

```bash
sf -s example.com -o report.html -f sfp_dns,sfp_googlesearch --maxthreads 50
```

Scan with specific modules, HTML output, and higher concurrency.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Gather Victim Network Information]] Gather Victim Network Information
- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of queries to public APIs (e.g., Google, VirusTotal) from a single IP.
- Detection method 2: Network logs showing DNS/WHOIS lookups for target-related domains.
- Detection method 3: Presence of spiderfoot directories or sf.py process on compromised hosts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Maltego]]
- [[tools/theHarvester]]
- [[tools/Shodan]]

## References

- Official documentation: https://www.spiderfoot.net/documentation/
- GitHub repository: https://github.com/smicallef/spiderfoot
- Related resources: OWASP OSINT guide
