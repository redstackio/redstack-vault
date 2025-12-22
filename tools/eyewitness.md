---
id: 21e5e4da-39c4-4c56-8633-68fcc5856dd0
type: tool
verified: true
created_at: '2019-08-28T21:17:32.553841+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reconnaissance
  - web
  - screenshot
  - enumeration
url: 'https://github.com/FortyNorthSecurity/EyeWitness'
validated: true
---

# EyeWitness

**Status**: Unverified

## Overview

EyeWitness is a Python-based tool for automated web reconnaissance. It captures screenshots of websites using headless browsers, extracts HTTP server headers, and optionally tests for default credentials. Commonly used in penetration testing to quickly visualize and document web application attack surfaces without manual browsing.

## Description

EyeWitness automates the process of visiting multiple URLs, rendering pages with a browser engine (like Xvfb on Linux), and saving visual and textual artifacts. This helps identify technologies, titles, status codes, and potential login pages. It's particularly useful for large-scale subdomain enumeration follow-ups or mapping web footprints in red team engagements.

## Features

- Feature 1: Headless screenshot capture of HTTP/HTTPS sites with JavaScript rendering.
- Feature 2: HTTP header extraction including server type, content-type, and custom headers.
- Feature 3: Optional default credential brute-forcing against detected login forms.
- Feature 4: Multi-threaded scanning for efficiency on URL lists.
- Feature 5: Generates browsable HTML reports with embedded images and data exports (JSON/CSV).

## Installation

### Requirements

- Python 3.6+
- Required packages: Pillow, requests, PyVirtualDisplay (for headless browsing)
- Xvfb or similar for headless display on Linux (optional but recommended)

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install -y python3-pip xvfb  # For Ubuntu/Kali

# Install EyeWitness
git clone https://github.com/FortyNorthSecurity/EyeWitness.git
cd EyeWitness
sudo python3 setup.py install

# Or via pip (if available)
pip3 install eyewitness-py
```

For Windows: Use Git Bash or WSL, and ensure Python is in PATH. macOS: Use Homebrew for dependencies (`brew install python3 xvfb`).

## Basic Usage

```bash
python3 EyeWitness.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| --single-url | Scan a single URL |
| --url-file | Scan URLs from a file (one per line) |
| --creds | Enable default credential testing |
| --username-file | Path to usernames file |
| --password-file | Path to passwords file |
| --threads | Number of concurrent threads (default: 2) |
| --timeout | Request timeout in seconds (default: 10) |
| --output | Output directory for reports |
| --open | Automatically open the generated report in browser |

## Examples

### Example 1: Basic Usage

```bash
python3 EyeWitness.py --single-url http://example.com --output /tmp/eyewitness
```

This scans one site and saves results to /tmp/eyewitness.

### Example 2: Advanced Usage

```bash
python3 EyeWitness.py --url-file targets.txt --creds --username-file users.txt --password-file passwords.txt --output /tmp/eyewitness --threads 10 --timeout 15 --open
```

Scans a list with credential checks and opens the report.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual headless browser traffic (e.g., Xvfb processes on servers) or rapid HTTP requests from a single IP.
- Detection method 2: Web server logs showing requests to multiple paths with screenshot-like user-agents (e.g., Python-urllib).
- Detection method 3: Failed default credential attempts in auth logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/httpx]]

## References

- Official GitHub: https://github.com/FortyNorthSecurity/EyeWitness
- Documentation: README in the repo for advanced config like custom user-agents.
