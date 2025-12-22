---
id: f4f47150-536e-41ff-92a6-aaebb71b233f
type: tool
verified: true
created_at: '2019-08-28T21:17:36.557598+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-recon
  - robots-txt
  - bing-search
  - reconnaissance
url: 'https://github.com/ricardojoserf/parsero'
validated: true
---

# parsero

**Status**: Unverified

## Overview

Parsero is a Python-based reconnaissance tool designed to analyze a web server's robots.txt file, extract Disallow entries, and automatically check the HTTP status codes of those paths to identify accessible restricted directories or files. It helps uncover potential information disclosure by verifying if disallowed paths are publicly reachable despite directives to search engines. Additionally, it integrates Bing search to detect if any disallowed content has been indexed without authorization.

## Description

Parsero automates the process of parsing robots.txt, which web administrators use to instruct search engine crawlers on what not to index (e.g., sensitive directories like /admin or /backup). By testing each Disallow entry directly, it reveals misconfigurations where paths are blocked from indexing but remain accessible via direct URL access. The Bing integration scans for unauthorized indexing, providing insights into exposed sensitive information. This tool is particularly useful in the initial reconnaissance phase of web application testing to map hidden attack surfaces.

## Features

- Feature 1: Parses robots.txt and extracts all Disallow directives
- Feature 2: Performs HTTP status checks on each disallowed path to assess accessibility
- Feature 3: Searches Bing for indexed content from disallowed paths to identify exposures
- Feature 4: Outputs results in a readable format highlighting potential vulnerabilities

## Installation

### Requirements

- Python 3.x
- Git
- Internet access for Bing queries

### Install Commands

```bash
# Clone the repository
git clone https://github.com/ricardojoserf/parsero.git

# Navigate to the directory
cd parsero

# No additional installation needed; run directly with Python
python3 parsero.py --help
```

For Windows, use Git Bash or PowerShell with Python installed. On macOS, ensure Python 3 is available via Homebrew if needed.

## Basic Usage

```bash
python3 parsero.py www.example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| (No verbose flag; output is concise by default) | Standard output includes status codes and Bing results |

## Examples

### Example 1: Basic Usage

Scan a target website for robots.txt exposures:

```bash
python3 parsero.py www.target.com
```

Expected: List of Disallow paths with status codes (e.g., 200 for accessible, 404 for missing).

### Example 2: Advanced Usage

Parsero runs Bing searches automatically; no separate flag needed. For help:

```bash
python3 parsero.py --help
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Search Victim-Owned Websites]] Search Victim-Owned Websites

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP requests to /robots.txt from reconnaissance IPs
- Detection method 2: Bing API-like queries or patterns in logs searching site-specific content
- Detection method 3: Python process spawning network requests to target domains

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dirb]]
- [[tools/Gobuster]]

## References

- Official GitHub: https://github.com/ricardojoserf/parsero
- Python documentation for HTTP requests used internally
