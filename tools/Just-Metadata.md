---
id: d512841e-398b-4c8c-8fd3-0f1fc7079695
type: tool
description: >-
  A tool for gathering and analyzing metadata about IP addresses from multiple
  OSINT sources to identify relationships between systems.
verified: true
created_at: '2019-08-28T21:17:25.548310+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - osint
  - ip-analysis
url: 'https://github.com/zer0-day/Just-Metadata'
commands:
  - '[[commands/just-metadata-single-ip-scan]]'
  - '[[commands/just-metadata-batch-ip-scan]]'
validated: true
---

# Just-Metadata

**Status**: Unverified

## Overview

Just-Metadata is an OSINT tool designed to collect and analyze metadata associated with IP addresses. It queries multiple public sources such as Shodan, VirusTotal, Censys, and others to gather details like open ports, geolocation, organization information, and potential relationships to other systems. Commonly used in reconnaissance phases of security assessments to map attack surfaces and identify interconnected infrastructure.

## Description

The tool automates the process of pulling disparate data from various APIs and databases, correlating it to reveal patterns such as shared ownership, common vulnerabilities, or network topologies. It supports single IP queries or batch processing, with output in formats like JSON, CSV, or XML for further analysis. Ideal for red teamers building target profiles without direct interaction.

## Features

- Feature 1: Queries 20+ OSINT sources including Shodan, VirusTotal, and Shadowserver
- Feature 2: Supports batch processing of IP lists for large-scale reconnaissance
- Feature 3: Configurable API keys for personalized access and rate limiting
- Feature 4: Output correlation to highlight relationships between IPs
- Feature 5: Modular design allowing custom source additions

## Installation

### Requirements

- Python 3.6+
- pip and git
- API keys for sources like Shodan and VirusTotal (optional but recommended for full functionality)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/zer0-day/Just-Metadata.git
cd Just-Metadata

# Install dependencies
pip3 install -r requirements.txt

# For Kali/Ubuntu (system-wide)
sudo apt update && sudo apt install python3-pip git
pip3 install -r requirements.txt
```

## Basic Usage

```bash
just-metadata --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -v, --verbose | Enable verbose output for debugging |
| --api-key | Specify API key for a source (e.g., --shodan-api-key KEY) |
| -o, --output | Set output file path |
| -f, --format | Choose output format (json, csv, xml) |

## Examples

### Example 1: Basic Usage

Scan a single IP:

```bash
just-metadata 8.8.8.8
```

### Example 2: Advanced Usage

Batch scan with JSON output and Shodan API:

```bash
just-metadata -i ip_list.txt -o results.json --shodan-api-key YOUR_SHODAN_KEY
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Gather Victim Network Information]] Gather Victim Network Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: API query spikes from known OSINT sources (e.g., Shodan rate limits)
- Detection method 2: Network traffic to Just-Metadata's queried endpoints (e.g., api.shodan.io)
- Detection method 3: Presence of Just-Metadata binaries or logs on assessment machines

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Shodan-CLI]]
- [[tools/VirusTotal-CLI]]

## References

- Official GitHub: https://github.com/zer0-day/Just-Metadata
- Documentation: https://github.com/zer0-day/Just-Metadata/wiki
