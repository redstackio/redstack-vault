---
id: uuid-placeholder-7890
url: 'https://wpscan.com/'
name: WPscan
tags:
  - scanning
  - wordpress
  - web-vuln
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.466Z'
validated: true
submitted: true
---
# WPscan

**Status**: Unverified

## Overview

WPscan is a black-box WordPress vulnerability scanner that detects security issues in WordPress core, plugins, and themes. It's commonly used in penetration testing to identify outdated components leading to exploits like CSRF and XSS.

## Description

WPscan automates the detection of known vulnerabilities by querying its database against a target site's files and versions. In offensive security, it's ideal for initial reconnaissance on public-facing WordPress sites, providing details on exploitable flaws without requiring authentication. Features include plugin enumeration, user detection, and config backup searches, making it a staple for web app assessments.

## Features

- Feature 1: Vulnerability enumeration for plugins, themes, and core
- Feature 2: Database-backed scanning with API integration for detailed CVEs
- Feature 3: Non-intrusive enumeration of users, media, and backups

## Installation

### Requirements

- Ruby 2.7 or higher
- Bundler gem
- Internet access for database updates

### Install Commands

```bash
# Install via RubyGems
gem install wpscan

# Or clone from GitHub
git clone https://github.com/wpscanteam/wpscan.git
cd wpscan
bundle install
```

## Basic Usage

```bash
wpscan --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output for detailed logging |
| `--update` | Update vulnerability database |

## Examples

### Example 1: Basic Usage

```bash
wpscan --url https://www.uberxgermany.com
```

### Example 2: Advanced Usage

```bash
wpscan --url https://www.uberxgermany.com --enumerate vp,vt,u --api-token TOKEN
```

> Scans for vulnerable plugins (vp), themes (vt), and users (u) with API for enhanced details.

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

- Network logs showing requests to /wp-content/plugins/ or /readme.html with WPscan user-agent
- IDS alerts on repeated HEAD requests to WordPress paths
- File access logs for enumeration attempts on admin areas

## Related Procedures

- [[procedures/Scan-WordPress-Site-for-Vulnerabilities-using-WPscan]]

## Related Tools

- [[Nikto]]
- [[Nuclei]]

## References

- Official documentation: https://github.com/wpscanteam/wpscan/wiki
- Related resources: WordPress security best practices
