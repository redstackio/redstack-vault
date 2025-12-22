---
id: bfd75c6c-7fcc-4555-9ef4-cac655b11845
type: tool
verified: true
created_at: '2019-08-28T21:17:28.370737+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - forensics
  - browser-analysis
  - collection
  - post-exploitation
url: 'https://github.com/abelcheung/dumpzilla'
validated: true
---

# dumpzilla

**Status**: Unverified

## Overview

Dumpzilla is a Python 3.x-based forensic tool for extracting and analyzing artifacts from Firefox, Iceweasel, and SeaMonkey browsers. It is commonly used in red team operations for collecting sensitive data like saved credentials and session information from compromised systems, or in digital forensics for investigating browser activity.

## Description

Dumpzilla extracts a wide range of browser data for analysis, including cookies, history, and passwords. It runs in a command-line interface on Unix and Windows (32/64-bit) systems, allowing output to be piped to tools like grep or sed for filtering. The tool generates SHA256 hashes for each extracted file and provides a summary with totals. Some sections, such as DOM storage, preferences, addons, passwords, thumbnails, and sessions, do not support date-based filtering. It can also visualize live user activity, such as open tabs and form usage.

## Features

- Cookies and DOM Storage (HTML5) extraction
- User preferences (domain permissions, proxy settings)
- Download history
- Web form data (searches, emails, comments)
- Browsing history with search customization
- Bookmarks
- HTML5 Cache visualization and extraction (offline cache)
- Visited sites thumbnails visualization and extraction
- Addons/extensions with paths and URLs
- Browser saved passwords
- SSL certificates added as exceptions
- Session data (webs, reference URLs, text in forms)
- Live user surfing visualization (URLs in tabs/windows, form usage)
- SHA256 hashing of extracted files
- Summary with extraction totals

## Installation

### Requirements

- Python 3.x
- Access to browser profile directories (e.g., administrative privileges on target)

### Install Commands

```bash
# Clone the repository (Kali/Ubuntu)
git clone https://github.com/abelcheung/dumpzilla.git
cd dumpzilla

# No additional installation needed; run directly with Python
python --version  # Ensure Python 3.x
```

For Windows, download the script and run with Python 3.x installed.

## Basic Usage

```bash
python dumpzilla.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available sections |
| -o, --output <dir> | Specify output directory for extracted files (default: current dir) |
| --cookies | Extract only cookies and DOM storage |
| --passwords | Extract only saved passwords |
| --history | Extract only browsing history |
| --all | Extract all sections (default) |

## Examples

### Example 1: Basic Usage

```bash
python dumpzilla.py /home/user/.mozilla/firefox/abc123.default
```

This performs a full extraction and displays all sections in the console.

### Example 2: Advanced Usage

```bash
python dumpzilla.py --passwords /path/to/profile > passwords.txt
```

Extracts only passwords and saves to a file for further analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers
- [[LSASS Memory]] LSASS Memory (for related credential dumping)

### Tactics

- [[Collection]] Collection
- [[Command and Control]] Command and Control (for exfiltrating dumped data)

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes accessing browser profile paths (e.g., %APPDATA%\Mozilla\Firefox\Profiles on Windows, ~/.mozilla on Linux)
- File creation in temporary directories with browser artifact dumps
- Console output or logs containing SHA256 hashes and browser section headers (e.g., "Cookies + DOM Storage")
- Network exfiltration of dumped files (passwords, cookies)
- Monitor for python.exe spawning with dumpzilla.py arguments via EDR tools

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]] (for broader credential dumping)
- [[tools/LaZagne]] (multi-browser credential extractor)

## References

- Official GitHub Repository: https://github.com/abelcheung/dumpzilla
- SANS DFIR Resources (original development context)
- MITRE ATT&CK: Browser Credential Techniques
