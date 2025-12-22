---
id: a89d3839-34ee-40e1-a590-6a89df177b98
name: usufy
type: tool
verified: true
created_at: '2019-08-28T21:17:18.757180+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - osint
  - username-enumeration
  - reconnaissance
url: 'https://github.com/i3visio/osrframework/tree/master/usufy'
validated: true
---

# usufy

**Status**: Unverified

## Overview

usufy is a Python script within the OSRFramework suite designed for Open Source Intelligence (OSINT) tasks, specifically focused on enumerating and verifying usernames across hundreds of social media platforms, websites, and online services. It automates the process of checking username availability or presence, making it invaluable for reconnaissance phases in security assessments, investigations, and target profiling.

## Description

OSRFramework provides a collection of tools for OSINT operations, and usufy.py stands out for its extensive database of over 300 platforms including Twitter, GitHub, Facebook, Instagram, and more niche sites. It supports both interactive and non-interactive modes, allowing users to query single usernames or process lists in batch. The tool fetches profile pages or API endpoints to determine if a username is registered, providing URLs for confirmed hits. This helps identify online footprints without manual browsing, while respecting rate limits to avoid detection. usufy is particularly useful in red teaming for social engineering preparation, threat actor attribution, or vulnerability research involving user accounts.

## Features

- Feature 1: Checks usernames against 300+ platforms with customizable profiles
- Feature 2: Supports single username queries, batch processing from files, and output in multiple formats (text, JSON, CSV)
- Feature 3: Built-in rate limiting and proxy support to evade basic defenses
- Feature 4: Integration with other OSRFramework tools for chained OSINT workflows
- Feature 5: Verbose logging and error handling for unreliable sites

## Installation

### Requirements

- Python 3.6+
- pip and git
- Internet access for platform queries

### Install Commands

```bash
# Clone the OSRFramework repository
git clone https://github.com/i3visio/osrframework.git
cd osrframework

# Install dependencies
pip3 install -r requirements.txt

# For Ubuntu/Debian
sudo apt update
sudo apt install python3-pip git

# For Kali Linux (pre-built packages may be available)
sudo apt install osrframework
```

## Basic Usage

```python
python usufy.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -n, --name | Specify a single username to check |
| -iL, --input-list | Read usernames from a file |
| -o, --output | Specify output file |
| --profile | Use a specific platform profile (e.g., social, tech) |
| -v, --verbose | Enable detailed logging |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Check a single username:

```python
python usufy.py -n john_doe
```

### Example 2: Advanced Usage

Process a list of usernames and output to JSON:

```python
python usufy.py -iL usernames.txt -o results.json --format json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information
- [[Gather Victim Network Information]] Gather Victim Network Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic patterns showing queries to multiple social media domains from a single IP (e.g., via SIEM rules for OSINT tool signatures)
- Detection method 2: User-agent strings in web logs matching OSRFramework defaults; monitor for high-volume username-related requests
- Detection method 3: Endpoint protection alerts on Python scripts with OSRFramework imports or git clones from the repository

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
- [[tools/Sherlock]]
- [[tools/osrframework]]

## References

- Official GitHub: https://github.com/i3visio/osrframework
- Documentation: https://github.com/i3visio/osrframework/wiki
- Related resources: OSINT Framework (osintframework.com)
