---
id: d5c5a2ad-0d93-4f30-b052-2bd71fa94277
type: tool
verified: true
created_at: '2019-08-28T21:17:42.631360+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - osint
  - reconnaissance
  - username-check
  - email-search
url: 'https://github.com/i3visio/osrframework'
validated: true
---

# osrfconsole.py

**Status**: Unverified

## Overview

osrfconsole.py is the command-line interface for the OSRFramework, an open-source intelligence (OSINT) toolkit designed for gathering information from public sources. It enables tasks such as username verification across social media and websites, email address searches, DNS lookups, and extraction of leaked information. Commonly used in reconnaissance phases of security assessments to identify online footprints of individuals or entities without direct interaction.

## Description

OSRFramework provides a modular framework for OSINT operations, with osrfconsole.py serving as the interactive console to launch various modules. Modules include usufy for username checks on hundreds of platforms, mailfy for email reconnaissance, and others for deep web searches, regex-based extractions, and information leak detection. It supports graphical integration via Maltego transforms and web interfaces, but the console is ideal for scripted or batch OSINT workflows. The tool emphasizes ethical use for research, investigations, and red teaming, focusing on passive data collection from open sources.

## Features

- Username verification across 300+ social networks and sites
- Email address probing and associated account discovery
- DNS and domain information gathering
- Leaked credential searches and regex pattern matching
- Support for batch processing and output in various formats (CSV, JSON)
- Integration with Maltego for visual graphing of results

## Installation

### Requirements

- Python 3.6+
- pip and git
- Internet access for module dependencies

### Install Commands

```bash
# Clone the repository
git clone https://github.com/i3visio/osrframework.git
cd osrframework

# Install dependencies
pip install -r requirements.txt

# Install the framework
python setup.py install
```

On Kali Linux, it may be available via apt: `sudo apt update && sudo apt install osrframework`, but the GitHub method ensures the latest version.

For Windows/macOS, use the same pip-based installation within a virtual environment.

## Basic Usage

```bash
python osrfconsole.py --help
```

This displays available options and modules. The console is interactive: launch it with `python osrfconsole.py` and select modules via menu.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-l, --list` | List all available modules |
| `-n <module>, --name <module>` | Specify a module to run (e.g., usufy) |
| `-i <input>, --input <input>` | Input data (e.g., username or email) |
| `-o <output>, --output <output>` | Output file format (CSV, JSON) |

## Examples

### Example 1: Basic Usage

```bash
python osrfconsole.py -l
```

Lists all modules like usufy, mailfy, etc.

### Example 2: Advanced Usage

```bash
python osrfconsole.py -n usufy -i target_username -o results.csv
```

Runs the usufy module to check the username across platforms and saves results to CSV.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Social Media]] Search Open Websites and Services: Username
- [[Gather Victim Host Information]] Gather Victim Identity Information
- [[Search Open Websites-Domains]] Search Open Technical Databases

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to multiple social media APIs or whois services in short bursts
- Python processes named osrfconsole.py or importing OSRFramework modules
- Log entries for high-volume HTTP requests to OSINT endpoints
- File artifacts like CSV outputs with username/email scan results

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
- [[tools/recon-ng]]
- [[tools/SpiderFoot]]

## References

- Official GitHub: https://github.com/i3visio/osrframework
- Documentation: https://github.com/i3visio/osrframework/wiki
- Maltego Transforms: Integrated via OSRFramework's transforms directory
