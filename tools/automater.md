---
type: tool
description: >-
  Automater is an OSINT tool for automated analysis of URLs, IP addresses, and
  MD5 hashes, querying multiple threat intelligence sources to aid intrusion
  analysts.
url: 'https://github.com/TechniquesForRecon/Automater'
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - osint
  - reconnaissance
  - url-analysis
  - ip-analysis
  - hash-analysis
validated: true
---

# automater

**Status**: Unverified

## Overview

Automater is a Python-based OSINT tool designed to streamline the analysis of URLs, domains, IP addresses, and MD5 hashes. It automates queries to various public threat intelligence sources, making it valuable for security analysts investigating potential indicators of compromise during reconnaissance or incident response phases.

## Description

Automater takes a single target or a file of targets as input and returns aggregated results from sources including IPvoid.com, Robtex.com, FortiGuard.com, unshorten.me, URLVoid.com, AlienVault Labs, ThreatExpert, VxVault, and VirusTotal. It supports verbose output and customizable source selection, helping to quickly assess reputation, malware associations, and related metadata without manual browsing.

## Features

- Feature 1: Automated querying of 10+ OSINT sources for URLs, IPs, and hashes
- Feature 2: Batch processing from input files for efficient analysis of multiple targets
- Feature 3: Verbose and customizable output formats, including HTML reports
- Feature 4: URL unshortening and redirection handling
- Feature 5: Support for domain, IP, and MD5 hash inputs

## Installation

### Requirements

- Python 2.7 or 3.x (Python 3 recommended)
- pip and git
- Internet access for querying external APIs

### Install Commands

```bash
# Clone the repository
git clone https://github.com/TechniquesForRecon/Automater.git
cd Automater

# Install dependencies (if any, typically minimal)
pip install -r requirements.txt

# For Kali Linux: Available in repositories or install via git as above
sudo apt update && sudo apt install automater
```

On Ubuntu or other Debian-based distros, use the git clone method. For macOS, use Homebrew to install git and Python, then clone.

## Basic Usage

```bash
python automater.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for detailed results |
| -o, --output | Specify output file for results |
| --sources | Select specific sources (e.g., vt,urlvoid) |

## Examples

### Example 1: Basic Usage

```python
python automater.py -u http://example.com
```

### Example 2: Advanced Usage

```python
python automater.py -f targets.txt -o report.html -v --sources all
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Search Open Websites-Domains]] Search Open Technical Databases
- [[Search Victim-Owned Websites]] Search Victim-Owned Websites

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic to OSINT APIs (e.g., VirusTotal, URLVoid) from analysis workstations
- Detection method 2: Process monitoring for python automater.py executions in security tools directories
- Detection method 3: Log analysis for batch API queries from single IP

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/theHarvester]]
- [[tools/Maltego]]
- [[tools/recon-ng]]

## References

- Official GitHub Repository: https://github.com/TechniquesForRecon/Automater
- Kali Linux Tools Page: https://www.kali.org/tools/automater
- Original Author Documentation: Included in repo README
