---
id: tool-wpscan
url: 'https://wpscan.com/'
tags:
  - wordpress
  - scanner
  - bruteforce
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.637Z'
validated: true
submitted: true
---
# WPScan

**Status**: Unverified

## Overview

WPScan is a Ruby-based vulnerability scanner for WordPress, primarily used for enumerating users, detecting plugins/themes vulnerabilities, and brute forcing logins in penetration testing.

## Description

It identifies exposures like username enumeration via response analysis and supports password attacks. Common in offensive security for auditing WP sites.

## Features

- Feature 1: User enumeration without auth
- Feature 2: Vulnerability database integration
- Feature 3: Brute force via login or XML-RPC

## Installation

### Requirements

- Ruby 2.7+ and Bundler
- Git

### Install Commands

```bash
sudo gem install wpscan
```

## Basic Usage

```bash
wpscan --url https://example.com --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--enumerate u` | Enumerate users |
| `--api-token` | Use WPScan API |

## Examples

### Example 1: Basic Usage

```bash
wpscan --url https://nextcloud.com --enumerate u
```

### Example 2: Advanced Usage

```bash
wpscan --url https://nextcloud.com -U frank -P wordlist.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Brute Force]] Brute Force

### Tactics

- [[Discovery]] Discovery
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- User-Agent: "WPScan"
- High volume of /wp-login.php requests
- XML-RPC method calls

## Related Procedures

- [[procedures/Enumerate-WordPress-Usernames-with-WPScan]]
- [[procedures/Brute-Force-WordPress-Admin-Login-with-WPScan]]

## Related Tools

- [[Nikto]]
- [[Dirbuster]]

## References

- Official documentation: https://github.com/wpscanteam/wpscan
- Related resources: WordPress security guides
