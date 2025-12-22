---
id: 0a1be574-ebe8-4dcd-8691-15e47c796e0b
type: tool
verified: true
created_at: '2019-08-28T21:17:38.345926+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - osint
  - reconnaissance
  - linkedin
  - enumeration
url: 'https://github.com/laramies/linkscrape'
commands:
  - '[[commands/linkscrape-enumerate-company-employees]]'
  - '[[commands/linkscrape-scrape-user-profile]]'
validated: true
---

# linkScrape

**Status**: Unverified

## Overview

linkScrape is an open-source Python tool designed for OSINT reconnaissance on LinkedIn. It automates the scraping of company employee lists and individual user profiles by simulating searches and extracting public data. Commonly used in red teaming for victim identity gathering and social engineering preparation.

## Description

linkScrape leverages LinkedIn's public search functionality to enumerate employees by company name or scrape detailed profiles by username. It outputs results in CSV format for easy analysis. The tool requires a LinkedIn account for authentication in some modes but can operate in guest mode for basic enumeration. It is particularly useful for mapping organizational structures and identifying key personnel during reconnaissance phases of penetration testing.

## Features

- Feature 1: Company employee enumeration via search scraping
- Feature 2: Individual profile data extraction (name, title, location, connections)
- Feature 3: CSV export for integration with other OSINT tools
- Feature 4: Support for guest access (no login required for basic use)
- Feature 5: Rate limiting to avoid detection

## Installation

### Requirements

- Python 3.6+
- pip and git
- Optional: Selenium for advanced browser automation (if using full scraping mode)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/laramies/linkscrape.git
cd linkscrape

# Install dependencies
pip install -r requirements.txt

# For Ubuntu/Kali (ensure Python and pip are available)
sudo apt update
sudo apt install python3-pip git
```

## Basic Usage

```bash
python linkscrape.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -c | Specify company name for employee enumeration |
| -u | Specify username for profile scraping |
| -o | Output file path (CSV) |
| --guest | Use guest mode (no login) |
| --limit | Limit number of results to scrape |

## Examples

### Example 1: Basic Usage

Enumerate employees for a company:

```bash
python linkscrape.py -c "Microsoft" -o microsoft_employees.csv
```

### Example 2: Advanced Usage

Scrape a user profile with limit:

```bash
python linkscrape.py -u "satya-nadella" --limit 50 -o profile.csv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information
- [[Gather Victim Host Information]] Gather Victim Host Information (via inferred org data)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual LinkedIn search patterns from single IP (e.g., repeated company queries)
- Detection method 2: CSV exports or scraped data in logs if using proxy
- Detection method 3: Browser automation signatures if Selenium is enabled (e.g., headless Chrome user-agent)
- Detection method 4: Rate limiting triggers on LinkedIn side leading to CAPTCHAs or bans

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
- [[LinkedIn-OSINT-Tools]]

## References

- Official GitHub: https://github.com/laramies/linkscrape
- LinkedIn Terms of Service (note: scraping may violate TOS)
- OSINT Framework: https://osintframework.com/
