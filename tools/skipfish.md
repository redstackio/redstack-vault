---
id: 1fcad131-5b8c-4317-879f-cdd71a191c8f
name: skipfish
type: tool
verified: true
created_at: '2019-08-28T21:17:30.434421+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/skipfish-scan-for-known-signatures]]'
platforms:
  - Web
tags:
  - enumeration
  - fingerprint
  - network
url: 'https://code.google.com/archive/p/skipfish/'
validated: true
---

# skipfish

**Status**: Unverified

## Overview

Skipfish is an active web application security reconnaissance tool designed for efficient and thorough scanning of web sites. It performs recursive crawling and dictionary-based probes to build an interactive sitemap, which is then annotated with results from non-disruptive security checks. The tool is particularly useful for identifying potential vulnerabilities during penetration testing and security assessments.

## Description

Skipfish operates by launching a series of dictionary-based probes against a target web application, following links and forms to map the site's structure. It supports various probing modes, including signature-based checks for known issues like directory traversal, file inclusion, and other common web vulnerabilities. The output is an indexed report in HTML format, making it easy to navigate and analyze findings. Skipfish is optimized for speed and low false positives, making it suitable for large-scale scans in offensive security operations.

## Features

- Feature 1: Recursive crawling with configurable depth limits to map site structure without overwhelming the target.
- Feature 2: Dictionary-based probing using customizable wordlists for discovering hidden directories, files, and parameters.
- Feature 3: Active security checks for common web vulnerabilities, including signature matching for known issues.
- Feature 4: Interactive HTML reports with sitemaps, annotations, and exportable data for further analysis.
- Feature 5: Support for HTTP/HTTPS, cookie handling, and exclusion rules to fine-tune scan scope.

## Installation

### Requirements

- Linux distribution with apt package manager (e.g., Ubuntu, Kali Linux)
- Internet access for downloading packages
- Sufficient disk space for wordlists and output reports

### Install Commands

```bash
# On Kali Linux (pre-installed in many cases)
sudo apt update && sudo apt install skipfish

# On Ubuntu/Debian
sudo apt update && sudo apt install skipfish
```

After installation, wordlists are available in /usr/share/skipfish/dictionaries/. Verify installation with `skipfish --help`.

## Basic Usage

```bash
skipfish --help
```

This displays the full list of options, including crawl limits, output formats, and probing configurations.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -m <depth> | Set maximum crawl recursion depth |
| -o <dir> | Specify output directory for reports |
| -S <wordlist> | Use specified dictionary for probing |
| -V | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

```bash
skipfish -m 5 -o basic_scan http://example.com
```

This performs a basic scan with default settings, limiting depth to 5 levels and saving results to 'basic_scan'.

### Example 2: Advanced Usage

```bash
skipfish -m 10 -o advanced_scan -LY -S /usr/share/skipfish/dictionaries/complete.wl -X exclude.txt https://target.com
```

This uses a complete wordlist, disables some session features (-LY), excludes paths from 'exclude.txt', and scans HTTPS.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of HTTP requests from a single IP with patterns matching dictionary probes (e.g., fuzzing common paths like /admin, /backup).
- Detection method 2: Web server logs showing recursive crawling and probing for vulnerabilities, often with user-agent 'Mozilla/5.0 (compatible; Skipfish)'.
- Detection method 3: Network traffic analysis revealing rapid requests to multiple endpoints on the same host.

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
- [[tools/Nikto]]
- [[tools/zap]]

## References

- Official documentation: https://code.google.com/archive/p/skipfish/
- GitHub mirror: https://github.com/spinkham/skipfish
- Related resources: OWASP Testing Guide for web reconnaissance techniques
