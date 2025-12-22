---
id: 6e17548e-80ea-45a5-b270-5c8aba8fbe5e
type: tool
verified: true
created_at: '2019-08-28T21:17:39.335936+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - osint
  - reconnaissance
  - domain-enumeration
  - whois
url: 'https://github.com/i3visio/osrframework'
validated: true
---

# domainfy

**Status**: Unverified

## Overview

Domainfy is a Python script within the OSRFramework suite designed for Open Source Intelligence (OSINT) tasks. It generates potential domain name variations based on input usernames (e.g., appending .com, .net, or username-based permutations) and performs WHOIS lookups to check their registration status. This tool is commonly used in reconnaissance phases to identify domains potentially associated with a target individual or organization, aiding in footprinting and identity gathering.

## Description

OSRFramework is a collection of libraries and tools for OSINT operations, including username enumeration, DNS research, and information leakage detection. Domainfy specifically focuses on domain-related intelligence by automating the creation of domain name lists from usernames and querying WHOIS databases to determine availability or ownership details. It supports batch processing of username lists and outputs structured results for further analysis. The tool integrates well with other OSRFramework components and can be extended via Maltego transforms for graphical workflows or used via console interfaces.

## Features

- Username-to-domain permutation generation (e.g., john -> john.com, john123.net)
- Batch WHOIS queries for registration status
- Configurable output formats (text, JSON)
- Integration with OSRFramework's entity reconciliation
- Support for custom domain extensions and patterns
- Timeout and rate-limiting options to avoid abuse

## Installation

### Requirements

- Python 3.6+
- pip and git
- Access to WHOIS services (no special API keys needed)

### Install Commands

```bash
# Install OSRFramework via pip (includes domainfy)
pip3 install osrframework

# Or clone from GitHub for latest version
git clone https://github.com/i3visio/osrframework.git
cd osrframework
pip3 install -r requirements.txt
```

On Kali Linux, it may be available via apt: `sudo apt install osrframework`.

## Basic Usage

```bash
python3 domainfy.py --help
```

This displays available options, including input/output flags and configuration settings.

### Common Options

| Option | Description |
|--------|-------------|
| -i, --input | Input file with usernames |
| -o, --output | Output file for results |
| --profile | Use a specific profile for queries |
| --whois-timeout | Set timeout for WHOIS lookups |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Create a file `usernames.txt` with content:

john_doe
jane.smith

Then run:

```bash
python3 domainfy.py -i usernames.txt -o domain_results.txt
```

This generates and checks domains like john_doe.com, jane-smith.net, etc., saving results to domain_results.txt.

### Example 2: Advanced Usage

```bash
python3 domainfy.py -i usernames.txt -o domain_results.json --output-format json
```

Outputs in JSON for easier parsing in scripts.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Org Information]] Gather Victim Host Information (domain enumeration via WHOIS)
- [[Email Addresses]] Gather Victim Identity Information: Email Addresses (via username-domain links)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to WHOIS servers (e.g., whois.iana.org, port 43)
- High volume of WHOIS queries from a single IP
- Python processes with osrframework modules loaded
- Log entries for domainfy.py execution in command history

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/usufy]] (OSRFramework username checker)
- [[tools/theHarvester]] (General OSINT reconnaissance)
- [[WHOIS]] (Standalone WHOIS client)

## References

- Official GitHub: https://github.com/i3visio/osrframework
- OSRFramework Documentation: https://github.com/i3visio/osrframework/wiki
- WHOIS Protocol: RFC 3912
