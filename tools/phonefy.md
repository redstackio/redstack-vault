---
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
  - phone
url: 'https://github.com/i3visio/osrframework'
validated: true
---

# phonefy

**Status**: Unverified

## Overview

Phonefy is a specialized OSINT tool from the OSRFramework suite designed for gathering intelligence on phone numbers. It queries multiple public online sources, including social media platforms, search engines, and directories, to identify associated profiles, locations, and other personal information. Commonly used in reconnaissance phases of security assessments to build target profiles.

## Description

Phonefy automates the process of searching phone numbers across a wide array of websites and databases, providing a consolidated report of findings. It supports both single queries and batch processing from files, making it efficient for investigative work. As part of OSRFramework, it integrates well with other OSINT tools for username, email, and domain reconnaissance. Key capabilities include handling international phone formats, customizable output formats, and avoiding rate limits through built-in delays.

## Features

- Feature 1: Searches over 30+ sources including Facebook, LinkedIn, Twitter, Google, and phone directories.
- Feature 2: Batch processing for multiple phone numbers from input files.
- Feature 3: Configurable output in text, JSON, or CSV formats for easy integration with other tools.
- Feature 4: Proxy support and user-agent rotation to evade basic detection.

## Installation

### Requirements

- Python 3.6+
- pip and git installed
- Internet access for querying online sources

### Install Commands

```bash
# Install via pip (recommended)
pip install osrframework

# Or clone from GitHub
mkdir -p ~/tools && cd ~/tools
git clone https://github.com/i3visio/osrframework.git
cd osrframework && pip install -r requirements.txt
```

For Kali Linux: The OSRFramework suite is available in the repositories.

```bash
sudo apt update && sudo apt install osrframework
```

## Basic Usage

```bash
python phonefy.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -p, --phone | Specify a single phone number to search |
| -f, --file | Input file with phone numbers (one per line) |
| -o, --output | Output file for results |
| --format | Output format (txt, json, csv) |
| --proxy | Use a proxy server for requests |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Search a single phone number:

```bash
python phonefy.py -p +1-555-123-4567
```

### Example 2: Advanced Usage

Batch search from a file with JSON output:

```bash
python phonefy.py -f phone_list.txt -o results.json --format json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Employee Names]] Gather Victim Identity Information: Credentials (phone-based reconnaissance)
- [[Gather Victim Host Information]] Gather Victim Host Information (extended to personal identifiers)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic to multiple social media and directory sites with phone query patterns.
- Detection method 2: Python process spawning with 'phonefy.py' or OSRFramework imports in process lists.
- Detection method 3: Unusual API calls or search queries from automated scripts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Maltego]] (for graphical OSINT transforms)
- [[tools/theHarvester]] (complementary email/domain OSINT)

## References

- Official GitHub: https://github.com/i3visio/osrframework
- OSRFramework Documentation: https://github.com/i3visio/osrframework/wiki
