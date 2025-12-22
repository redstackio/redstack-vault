---
id: ab65fee0-e59c-4ade-a384-c53a2a01a45c
type: tool
verified: true
created_at: '2019-08-28T21:17:31.513343+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - osint
  - scraping
  - pii
  - reconnaissance
url: 'https://github.com/dxa4481/skiptracer'
validated: true
---

# skiptracer

**Status**: Unverified

## Overview

Skiptracer is an open-source OSINT scraping framework designed for gathering personally identifiable information (PII) on targets from paywall-protected websites. It leverages Python's BeautifulSoup library for web scraping to compile passive reconnaissance data affordably, without requiring paid subscriptions to services like Intelius or Spokeo. Commonly used in ethical hacking, investigations, and red teaming for initial target profiling.

## Description

Skiptracer automates the extraction of public and semi-public data such as names, addresses, phone numbers, relatives, and social profiles by simulating user interactions on OSINT sites. It handles basic anti-scraping measures and outputs structured JSON results for easy parsing. The tool is lightweight, budget-friendly ("ramen noodle budget"), and focuses on passive collection to minimize detection risk. It's particularly useful for reconnaissance phases in penetration testing or threat intelligence gathering.

## Features

- **Multi-Site Support**: Scrapes from popular PII databases like Intelius, Spokeo, BeenVerified, and more.
- **Flexible Inputs**: Searches by name, email, phone, or username.
- **Structured Output**: Generates JSON files with categorized PII data.
- **Customizable Depth**: Adjustable scraping intensity to balance speed and comprehensiveness.
- **Proxy Support**: Optional integration with proxies to avoid IP bans.
- **Error Handling**: Gracefully skips failed scrapes and logs issues.

## Installation

### Requirements

- Python 3.6+ with pip
- BeautifulSoup4, requests, and lxml libraries
- Optional: Tor or proxies for anonymity

### Install Commands

```bash
# Clone the repository
git clone https://github.com/dxa4481/skiptracer.git
cd skiptracer

# Install dependencies
pip install -r requirements.txt

# For Ubuntu/Debian (if needed)
sudo apt update && sudo apt install python3-pip git
```

On Kali Linux, it's often available via apt or can be installed similarly.

## Basic Usage

```bash
python skiptracer.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| --name | Search by full name |
| --email | Search by email address |
| --output | Specify output file (JSON) |
| --sites | Comma-separated list of sites to scrape |
| --proxy | Use a proxy server for requests |

## Examples

### Example 1: Basic Usage

```bash
python skiptracer.py --name "John Doe" --output results.json
```

This performs a default scrape for "John Doe" across supported sites and saves results to results.json.

### Example 2: Advanced Usage

```bash
python skiptracer.py --email john@example.com --sites intelius,spokeo --output email_data.json --proxy http://127.0.0.1:8080
```

Searches email-linked data from specific sites using a proxy.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]] Search Open Websites/Domains
- [[Determine Physical Locations]] Gather Victim Identity Information: Identify Business Interests

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual web requests to PII sites from automated scripts (high request volume).
- Python processes with BeautifulSoup imports in network forensics.
- JSON files containing scraped PII on investigator machines.
- Proxy or Tor traffic patterns matching OSINT scraping.

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

## References

- Official GitHub: https://github.com/dxa4481/skiptracer
- Documentation: README in the repository
- Related OSINT Resources: https://osintframework.com
