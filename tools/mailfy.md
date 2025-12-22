---
id: f64e2f29-b642-4bc7-9c13-4338c461a918
name: mailfy
type: tool
verified: true
created_at: '2019-08-28T21:17:36.772395+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - osint
  - reconnaissance
  - email-validation
url: 'https://github.com/i3visio/osrframework'
validated: true
---

# mailfy

**Status**: Unverified

## Overview

mailfy is a Python-based tool from the OSRFramework suite designed for Open Source Intelligence (OSINT) tasks. It specifically focuses on validating and checking email addresses across a wide range of online platforms, social networks, and services to determine if an email is registered or in use. This is useful for reconnaissance, identifying user accounts, and mapping digital footprints during security assessments or investigations.

## Description

As part of OSRFramework, mailfy performs automated checks against numerous websites (e.g., social media, forums, and professional networks) to see if a given email address yields positive hits, such as account existence confirmations or registration details. It supports single email checks, batch processing from files, and filtering by specific platforms. The tool outputs results in a structured format, often with details on which sites the email appears on, aiding in username and identity correlation. It's particularly valuable in red teaming for initial target profiling and in defensive OSINT for threat actor tracking.

## Features

- Email validation across 100+ platforms (e.g., Twitter, LinkedIn, GitHub)
- Support for single emails or bulk input from files
- Configurable output formats (JSON, CSV, plain text)
- Platform-specific filtering to focus checks
- Integration with other OSRFramework tools for chained OSINT workflows
- Proxy support for anonymity during queries

## Installation

### Requirements

- Python 3.6+
- pip and git
- Access to the internet for platform queries

### Install Commands

```bash
# Clone the OSRFramework repository (mailfy is included)
git clone https://github.com/i3visio/osrframework.git
cd osrframework

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (pre-built package available)
apt update && apt install osrframework
```

On Windows or macOS, use the git clone and pip install method. Ensure Python is in your PATH.

## Basic Usage

```bash
python3 mailfy.py -h
```

This displays the help menu with all available options.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show the help message and exit |
| `-v, --verbose` | Enable verbose output for detailed logging |
| `-o, --output` | Specify output file format (e.g., JSON, CSV) |
| `-p, --platform` | Check only specific platforms (e.g., twitter, linkedin) |
| `--proxy` | Use a proxy server for requests |

## Examples

### Example 1: Basic Usage

Check a single email across all supported platforms:

```bash
python3 mailfy.py -e "target@example.com"
```

### Example 2: Advanced Usage

Process a list of emails from a file and output to JSON, filtering to social media platforms:

```bash
python3 mailfy.py -f emails.txt -p twitter,facebook,linkedin -o results.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases
- [[Email Addresses]] Gather Victim Identity Information: Email Addresses

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to multiple social media and platform APIs from a single source
- High volume of registration/validation queries in web server logs
- Python processes with OSRFramework modules running on assessment machines
- Artifact: Temporary files or outputs containing email lists and platform hits

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
- [[OSINT-Framework]]

## References

- Official GitHub: https://github.com/i3visio/osrframework
- OSRFramework Documentation: https://github.com/i3visio/osrframework/wiki
