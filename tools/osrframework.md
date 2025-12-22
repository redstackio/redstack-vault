---
id: c3c8b26d-d672-4952-979d-5d343087af69
name: osrframework
type: tool
verified: true
created_at: '2019-08-28T21:17:35.615854+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - osint
  - reconnaissance
  - username-check
  - email-search
  - phone-lookup
url: 'https://github.com/i3visio/osrframework'
commands:
  - '[[commands/osrframework-usufy-username-search]]'
  - '[[commands/osrframework-mailfy-email-search]]'
  - '[[commands/osrframework-phonefy-phone-lookup]]'
validated: true
---

# osrframework

**Status**: Unverified

## Overview

OSRFramework is a comprehensive suite of open-source intelligence (OSINT) tools and libraries designed for gathering and analyzing publicly available information. It excels in tasks such as username enumeration across social platforms, email verification, phone number lookups, DNS research, and deep web searches, making it ideal for reconnaissance phases in security assessments.

## Description

OSRFramework provides a modular framework with multiple applications for OSINT operations. Users can perform targeted searches for identities, domains, and leaks using command-line tools, a console interface (OSRFConsole), or integrate with visualization tools like Maltego via transforms. It's particularly useful for ethical hacking, threat intelligence, and investigative research, supporting automated checks against hundreds of websites and services.

## Features

- Username checking across 300+ platforms (via usufy)
- Email address validation and association discovery (via mailfy)
- Phone number enrichment from public sources (via phonefy)
- DNS and subdomain enumeration (via dnspopcorn)
- Regular expression-based data extraction from inputs
- Maltego integration for graphical OSINT workflows
- Web-based interface for non-CLI users
- Support for deep web and information leak searches

## Installation

### Requirements

- Python 3.6+
- pip and git
- Internet access for querying external sources

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/i3visio/osrframework.git /opt/osrframework
cd /opt/osrframework

# Install dependencies
sudo pip3 install -r requirements.txt

# For Ubuntu/Debian
sudo apt update && sudo apt install python3-pip git

# For Kali Linux (pre-built packages may be available)
sudo apt install osrframework
```

## Basic Usage

```bash
# Launch the console interface
python3 osrconsole.py

# Run help for a specific module
python3 usufy.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -o, --output | Specify output file for results |
| --info | Provide additional details on findings |

## Examples

### Example 1: Basic Usage

```bash
python3 usufy.py -n target_user
```

### Example 2: Advanced Usage

```bash
python3 mailfy.py -e target@example.com -o results.txt --mode full
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information
- [[Gather Victim Network Information]] Gather Victim Network Information
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual API calls or HTTP requests to social media endpoints from a single IP
- Python processes with osrframework modules in process lists
- Network traffic patterns matching OSINT query signatures (e.g., rapid username checks)
- Log entries for git clones or pip installs of osrframework

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
- [[tools/SpiderFoot]]

## References

- Official GitHub: https://github.com/i3visio/osrframework
- Documentation: https://github.com/i3visio/osrframework/wiki
- Maltego Transforms: Included in the repository for graphical use
