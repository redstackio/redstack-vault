---
type: tool
description: >-
  OSINT enumeration tool used to gather information on an organization,
  including emails, subdomains, hosts, employee names, open ports, and banners
  from various sources like Google, Bing, and LinkedIn.
url: 'https://github.com/laramies/theHarvester'
tags:
  - osint
  - reconnaissance
  - data-exposure
platforms:
  - Linux
commands:
  - '[[commands/theharvester-google-osint-search]]'
verified: true
validated: true
---

# theHarvester

**Status**: Unverified

## Overview

theHarvester is an OSINT enumeration tool primarily used for passive reconnaissance on target organizations. It collects publicly available information such as emails, subdomains, hosts, employee names, open ports, and banners from multiple sources including search engines and social platforms.

## Description

theHarvester excels in initial reconnaissance phases of security assessments by querying OSINT sources like Google, Bing, Baidu, LinkedIn, Twitter, and Netcraft. It supports domain-based searches and can output results in various formats for further analysis, making it ideal for mapping an organization's digital footprint without direct interaction with the target.

## Features

- Feature 1: Supports multiple data sources (Google, Bing, Shodan, etc.) for comprehensive OSINT collection
- Feature 2: Gathers emails, subdomains, hosts, and IP addresses passively
- Feature 3: DNS resolution and hostname verification for discovered assets
- Feature 4: Output options including XML, JSON, and CSV for integration with other tools

## Installation

### Requirements

- Python 3.7+ with pip
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/laramies/theHarvester.git
cd theHarvester

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (often pre-installed or via apt)
apt update && apt install theharvester
```

## Basic Usage

```bash
theHarvester -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -d, --domain | Target domain to search |
| -l, --limit | Limit the number of results to work with (default: 500) |
| -b, --source | Backend to use (e.g., google, bing, linkedin) |
| -f, --filename | File to save output to (XML format) |
| -v, --verbose | Display verbose output |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

See related command for detailed example:

- [[commands/theharvester-google-osint-search]]

### Example 2: Advanced Usage

```bash
theHarvester -d example.com -l 100 -b all -f advanced_results.xml
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Gather Victim Identity Information]] Gather Victim Identity Information
- [[Search Open Websites-Domains]] Search Open Technical Databases

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual query patterns to search engines from assessment machines
- Detection method 2: Presence of theHarvester binary or Python scripts querying public APIs
- Detection method 3: Network logs showing repeated DNS resolutions for target domains

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
- [[tools/Shodan]]

## References

- Official GitHub: https://github.com/laramies/theHarvester
- Documentation: Included in repository README
