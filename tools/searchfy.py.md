---
type: tool
description: >-
  A Python script from the OSRFramework suite for performing username
  reconnaissance across multiple online platforms as part of OSINT operations.
url: 'https://github.com/i3visio/osrframework'
tags:
  - osint
  - reconnaissance
  - username-enumeration
platforms:
  - Linux
  - macOS
  - Windows
verified: true
validated: true
---

# searchfy.py

**Status**: Unverified

## Overview

searchfy.py is a command-line tool within the OSRFramework collection, designed for Open Source Intelligence (OSINT) tasks. It specializes in username checking by querying numerous websites and social platforms to determine if a given username exists, helping identify a target's digital footprint without direct interaction.

## Description

Part of the broader OSRFramework, which provides libraries and applications for OSINT activities including DNS lookups, information leak research, deep web searches, and regular expression-based extractions. searchfy.py focuses on username enumeration, supporting batch processing of username lists and integration with tools like Maltego for graphical analysis. It offers console and web interfaces for flexibility in red team reconnaissance phases.

## Features

- Feature 1: Batch username checking from input files
- Feature 2: Support for over 100 online platforms (e.g., social media, forums)
- Feature 3: Configurable output formats including JSON for parsing
- Feature 4: Integration with OSRFramework's ecosystem for chained OSINT workflows

## Installation

### Requirements

- Python 3.x
- pip package manager
- Internet access for platform queries

### Install Commands

```bash
# Install OSRFramework which includes searchfy.py
pip3 install osrframework

# Or clone from GitHub for latest version
git clone https://github.com/i3visio/osrframework.git
cd osrframework
pip3 install -r requirements.txt
```

On Kali Linux, it may be available via apt: `sudo apt install osrframework`.

## Basic Usage

```bash
python3 searchfy.py --help
```

This displays all available options, including input file handling and output configuration.

### Common Options

| Option | Description |
|--------|-------------|
| -p, --profile | Path to file with usernames (one per line) |
| -u, --user | Single username to check |
| -o, --output | Output file path |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

```bash
python3 searchfy.py -p usernames.txt
```

Processes all usernames in usernames.txt and prints results to console.

### Example 2: Advanced Usage

```bash
python3 searchfy.py -u target_user -o results.txt
```

Checks a single username and saves output to a file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Employee Names]] Gather Victim Identity Information: Credentials
- [[Gather Victim Network Information]] Gather Victim Network Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic patterns to multiple social media domains from a single source
- Detection method 2: Presence of OSRFramework Python packages in process lists or logs
- Detection method 3: Unusual query volumes to username check endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/osrframework]]
- [[tools/Maltego]]

## References

- Official GitHub: https://github.com/i3visio/osrframework
- OSRFramework Documentation: https://github.com/i3visio/osrframework/wiki
