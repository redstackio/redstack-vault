---
id: d14ef438-0c0c-41de-8b72-2f140437b201
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - osint
  - reconnaissance
  - framework
url: 'https://github.com/datasploit/datasploit'
validated: true
---

# datasploit

**Status**: Unverified

## Overview

DataSploit is an open-source OSINT framework designed for automated reconnaissance on various targets including domains, email addresses, phone numbers, and Bitcoin addresses. It integrates multiple APIs, scrapers, and tools to gather, correlate, and visualize intelligence, making it ideal for initial phases of penetration testing, threat intelligence, and investigative research.

## Description

DataSploit automates the collection of public data from sources like WHOIS, DNS records, social media, breach databases, and blockchain explorers. It processes raw data to identify relationships, such as linking emails to domains or phone numbers to social profiles, and outputs results in user-friendly formats like HTML reports with graphs, JSON for scripting, and CSV for analysis. Commonly used in red teaming for target profiling without direct interaction, it supports ethical OSINT operations while requiring API keys for enhanced functionality.

## Features

- Feature 1: Multi-target support (domains, emails, phones, Bitcoin, people, companies)
- Feature 2: Data correlation and visualization (graphs showing entity relationships)
- Feature 3: Multiple output formats (HTML, JSON, CSV, MongoDB export)
- Feature 4: Modular design with 25+ integrated OSINT modules
- Feature 5: API key integration for premium sources (e.g., Shodan, HaveIBeenPwned)

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- MongoDB (for data storage)
- API keys for services like Hunter.io, VirusTotal (optional but recommended)

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/datasploit/datasploit.git
cd datasploit

# Install dependencies (Python 2/3)
sudo pip install -r requirements.txt

# For Ubuntu/Kali
sudo apt update && sudo apt install python-pip mongodb
sudo service mongodb start

# For macOS (using Homebrew)
brew install mongodb
brew services start mongodb
pip3 install -r requirements.txt
```

Initialize the database:
```bash
python setup_db.py
```

## Basic Usage

```bash
python datasploit.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t | Target domain |
| -e | Target email |
| -p | Target phone |
| -b | Target Bitcoin address |
| -br | Generate browser report (HTML) |
| -o | Output directory |
| --api-key | Specify API key for a service |

## Examples

### Example 1: Basic Usage

Domain reconnaissance:
```bash
python datasploit.py -t example.com -br
```

### Example 2: Advanced Usage

Email OSINT with custom output:
```bash
python datasploit.py -e user@example.com -br -o ./reports --api-key hunter:yourkey
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

- Detection method 1: High volume of API requests to OSINT services (e.g., monitor Hunter.io, Shodan logs)
- Detection method 2: MongoDB insertions from unknown Python processes
- Detection method 3: Network traffic to GitHub for cloning or update checks
- Detection method 4: File artifacts like datasploit.py or generated .html reports in temp directories

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

- Official GitHub: https://github.com/datasploit/datasploit
- Documentation: https://github.com/datasploit/datasploit/wiki
- Related resources: OSINT Framework (osintframework.com)
