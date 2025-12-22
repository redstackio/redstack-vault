---
id: 0982b248-fff1-4716-9e8f-d9faa9e751b2
type: tool
verified: true
created_at: '2019-08-28T21:17:29.155805Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - reconnaissance
  - domains
  - redteam
  - c2
url: 'https://github.com/0x09AL/CatMyFish'
validated: true
---

# CatMyFish

**Status**: Unverified

## Overview

CatMyFish is a domain search tool designed for red teaming engagements. It helps identify categorized domains that are suitable for setting up command-and-control (C2) infrastructure, such as whitelisted or low-profile domains for Cobalt Strike beacons. By querying domain categorization services, it allows operators to find domains that blend in with legitimate traffic, reducing detection risks during operations.

## Description

CatMyFish leverages public and categorized domain databases to search for domains based on industry, reputation, or usage type. This is particularly useful in offensive security for evading network defenses that block known malicious domains. Common use cases include selecting domains for DNS over HTTPS (DoH) C2, HTTP/S beacons, or other covert channels. The tool supports filtering by category to ensure the domains appear benign to security tools.

## Features

- Feature 1: Category-based domain searching (e.g., tech, gaming, finance) to find whitelisted or neutral domains.
- Feature 2: Output to files for easy integration with other tools like DNS resolvers or C2 generators.
- Feature 3: Limit options to control the number of results returned.
- Feature 4: Cross-platform compatibility via Python.

## Installation

### Requirements

- Python 3.6+
- pip
- Internet access for API queries

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3-pip -y
git clone https://github.com/0x09AL/CatMyFish.git
cd CatMyFish

# Install dependencies
pip3 install -r requirements.txt

# Or install directly via pip (if available)
pip3 install catmyfish
```

For Windows, use similar steps with Git Bash or PowerShell, ensuring Python is in PATH.

## Basic Usage

```bash
catmyfish --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -c, --category | Specify the domain category to search |
| -o, --output | Output file for results |
| --limit | Limit the number of domains returned |

## Examples

### Example 1: Basic Usage

Search for tech category domains:

```bash
catmyfish -c tech -o tech_domains.txt
```

### Example 2: Advanced Usage

List categories and then search with limit:

```bash
catmyfish --list-categories
catmyfish -c gaming --limit 50 -o gaming_domains.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Host Information: Domain Properties
- [[Archive via Utility]] Archive Collected Data: Archive via Utility (for output handling)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic to domain categorization APIs (e.g., monitor queries to services like VirusTotal or Shodan).
- Detection method 2: Process monitoring for 'catmyfish' executable or Python scripts importing related modules.
- Detection method 3: Log analysis for unusual domain enumeration patterns during red team simulations.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Cobalt-Strike]]
- [[tools/dnsenum]]

## References

- Official GitHub: https://github.com/0x09AL/CatMyFish
- Red Team Infrastructure Guide: https://attack.mitre.org/techniques/T1071/
