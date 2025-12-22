---
id: 44eb4ea0-07dd-4ae5-a7e0-f916290dc879
type: tool
verified: true
created_at: '2019-08-28T21:17:29.408549+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web-scanning
  - vulnerability-assessment
  - penetration-testing
url: 'https://www.arachni-scanner.com/'
commands:
  - '[[commands/arachni-scan-url]]'
  - '[[commands/arachni-start-http-server]]'
  - '[[commands/arachni-generate-report]]'
validated: true
---

# Arachni

**Status**: Unverified

## Overview

Arachni is an open-source, modular, high-performance Ruby framework designed for evaluating the security of web applications. It assists penetration testers and administrators in identifying vulnerabilities through automated scanning, supporting use cases from command-line utilities to distributed scanning grids and web-based collaboration platforms.

## Description

Arachni is a feature-rich web application security scanner that adapts during audits by learning from HTTP responses. It performs meta-analysis to assess result trustworthiness and minimize false positives. Versatile in deployment, it can operate as a standalone CLI tool, a scalable grid for large-scale scans, a Ruby library for custom scripts, or a multi-user web platform for collaborative testing. Key strengths include support for various vulnerability checks like XSS, SQL injection, and path traversal, with customizable plugins and reporting formats.

## Features

- Feature 1: Adaptive scanning that learns from responses to improve accuracy and reduce false positives.
- Feature 2: Modular architecture with plugins for specific vulnerability checks and custom extensions.
- Feature 3: Multiple deployment modes, including CLI, HTTP server, and distributed grid for high-performance scans.
- Feature 4: Comprehensive reporting in formats like HTML, JSON, and XML, with detailed remediation guidance.
- Feature 5: Support for authenticated scans, custom headers, and session handling.

## Installation

### Requirements

- Ruby 2.7 or later
- Bundler (Ruby gem)
- Git for source installation

### Install Commands

```bash
# On Kali Linux (pre-installed or via package manager)
sudo apt update && sudo apt install arachni

# On Ubuntu (from source)
git clone https://github.com/Arachni/arachni.git
cd arachni
bundle install
rake install

# On macOS with Homebrew
brew install arachni
```

## Basic Usage

```bash
arachni --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and available options |
| `-v, --verbose` | Enable verbose logging for detailed output |
| `--checks` | Specify vulnerability checks to run (e.g., xss,sql) |
| `--timeout` | Set scan timeout in seconds |

## Examples

### Example 1: Basic Usage

```bash
arachni http://example.com --report-save-path=scan.afr
```

This performs a default scan on the target URL and saves results to an AFRS file.

### Example 2: Advanced Usage

```bash
arachni http://example.com --checks=* --authed-login-url=http://example.com/login --http-user=admin --http-pass=secret --report-save-path=full_scan.afr
```

Runs all checks with authentication and saves a comprehensive report.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of HTTP requests from a single user-agent containing 'Arachni' strings in headers or payloads.
- Detection method 2: Unusual patterns of probing for common vulnerabilities (e.g., repeated SQL injection attempts) logged in web server access files.
- Detection method 3: Presence of AFRS report files or Ruby processes named 'arachni' on compromised systems.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]
- [[tools/ZAP]]

## References

- Official documentation: https://www.arachni-scanner.com/docs/
- GitHub Repository: https://github.com/Arachni/arachni
- Related Commands: [[commands/arachni-scan-url]], [[commands/arachni-start-http-server]], [[commands/arachni-generate-report]]
