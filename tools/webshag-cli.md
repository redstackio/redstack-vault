---
id: 91df2a49-d03f-4041-86fa-65489db0ce3e
name: webshag-cli
type: tool
verified: true
created_at: '2019-08-28T21:17:27.496590+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-scanning
  - crawling
  - fuzzing
  - reconnaissance
url: 'https://sourceforge.net/projects/webshag/'
commands:
  - '[[commands/webshag-basic-scan]]'
  - '[[commands/webshag-crawl-website]]'
  - '[[commands/webshag-file-fuzzing]]'
  - '[[commands/webshag-url-scan-with-proxy]]'
validated: true
---

# webshag-cli

**Status**: Unverified

## Overview

Webshag is a multi-threaded, multi-platform web server audit tool written in Python. It provides functionalities for website crawling, URL scanning, and file fuzzing, making it suitable for reconnaissance and auditing of web applications in offensive security operations.

## Description

Webshag gathers essential features for web server auditing, including support for HTTP and HTTPS protocols, proxy usage, and HTTP authentication (Basic and Digest). It includes innovative IDS evasion techniques, such as using different random HTTP proxy servers per request to complicate request correlation. This tool is particularly useful for initial reconnaissance phases where mapping web structures and identifying potential entry points is key.

## Features

- Feature 1: Multi-threaded crawling to discover website structure efficiently.
- Feature 2: File and directory fuzzing with custom wordlists to uncover hidden resources.
- Feature 3: URL scanning with support for proxies and authentication to bypass basic protections.
- Feature 4: IDS evasion through randomized proxy selection per request.

## Installation

### Requirements

- Python 2.7 (note: legacy tool, may require older Python version)
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://sourceforge.net/projects/webshag/

# Navigate and install
cd webshag
python setup.py install

# Or run directly
python webshag.py
```

For Kali Linux: Not pre-installed; follow the above steps. For Ubuntu: Install Python 2.7 dependencies with `sudo apt install python2.7` before setup.

## Basic Usage

```bash
webshag --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -u | Specify target URL |
| --crawl | Enable crawling mode |
| --fuzz | Enable fuzzing mode |
| --proxy | Use a proxy server |
| --threads | Set number of threads (default: 10) |

## Examples

### Example 1: Basic Usage

```bash
webshag -u http://example.com
```

### Example 2: Advanced Usage

```bash
webshag -u http://example.com --crawl --depth 3 --threads 20 --proxy http://proxy:8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual multi-threaded HTTP requests from a single source.
- Detection method 2: Patterns of randomized proxy usage in web logs.
- Detection method 3: High volume of 404 responses from fuzzing attempts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[ZAP]]

## References

- Official SourceForge page: https://sourceforge.net/projects/webshag/
- Python documentation for dependencies.
