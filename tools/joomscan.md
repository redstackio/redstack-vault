---
id: 29cb873a-e35d-4de9-87af-9307fb2bf0cf
type: tool
verified: true
description: >-
  OWASP JoomScan is a Perl-based vulnerability scanner for Joomla CMS, detecting
  versions, components, and known vulnerabilities.
url: 'https://github.com/OWASP/joomscan'
created_at: '2019-08-28T21:17:29.339127+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - joomla
  - vulnerability-scanner
  - web
  - recon
validated: true
---

# joomscan

**Status**: Unverified

## Overview

OWASP JoomScan (Joomla Vulnerability Scanner) is an open-source Perl tool designed to scan Joomla Content Management System (CMS) installations for vulnerabilities, enumerate components, users, and plugins, and provide analysis of potential exploits. It is particularly useful during web application penetration testing to identify outdated or misconfigured Joomla sites.

## Description

JoomScan automates the detection of Joomla core versions, third-party extensions, and associated CVEs. It supports active scanning techniques like version fingerprinting, directory enumeration, and user discovery. The tool pulls from a regularly updated database of known vulnerabilities, making it effective for reconnaissance and vulnerability assessment phases of security testing. It is lightweight, command-line based, and integrates well with other web recon tools like Nikto or Burp Suite.

## Features

- Joomla version detection and CVE mapping
- Component, plugin, and template enumeration
- User account discovery via ID brute-forcing
- Configuration file scanning for sensitive data leaks
- Exploit suggestion for identified vulnerabilities
- Database update for latest threat intelligence

## Installation

### Requirements

- Perl 5 (with LWP::UserAgent and other standard modules)
- Git
- Internet access for database updates

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/OWASP/joomscan.git /opt/joomscan

# Make executable
cd /opt/joomscan
chmod +x joomscan.pl

# Or install via apt on Kali/Debian
sudo apt update && sudo apt install joomscan
```

For Ubuntu/Kali, it may be available in repositories; otherwise, use the git clone method.

## Basic Usage

```perl
./joomscan.pl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Target Joomla URL |
| -U | Update vulnerability database |
| -e | Enumerate users |
| -ec | Check for configuration issues |
| -v | Verbose output |

## Examples

### Example 1: Basic Usage

Scan a Joomla site for vulnerabilities:

```perl
./joomscan.pl -url http://target.com
```

### Example 2: Advanced Usage

Enumerate users and update DB first:

```perl
./joomscan.pl -U  # Update first
./joomscan.pl -url http://target.com --enumerate-users -ec
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual HTTP requests to Joomla paths (e.g., /administrator/, /components/)
- User-Agent strings containing "JoomScan" or Perl LWP
- Traffic patterns matching version checks or enumeration endpoints
- Log entries for failed user ID probes (e.g., 404s on /index.php?option=com_users&view=profile&id=X)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nikto]]
- [[tools/WPScan]]

## References

- Official GitHub: https://github.com/OWASP/joomscan
- OWASP Project Page: https://owasp.org/www-project-joomscan/
- Joomla Security Advises: https://developer.joomla.org/security.html
