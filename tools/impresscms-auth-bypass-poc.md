---
url: 'https://hackerone.com/reports/1081986'
tags:
  - exploit
  - php
  - auth-bypass
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.870Z'
id: 594c57e3-5069-46ae-b258-7a081908f941
validated: true
submitted: true
---
# impresscms-auth-bypass-poc

**Status**: Unverified

## Overview

Custom PHP CLI script for exploiting the ImpressCMS autologin type juggling vulnerability by automating HTTP requests with incremental timestamp cookies to find MD5 collisions.

## Description

This PoC targets ImpressCMS 1.4.2's /plugins/preloads/autologin.php, using curl to send requests with 'autologin_uname' and evolving 'autologin_pass' values. It computes MD5 hashes locally to check for '0e' prefixes, enabling loose equality bypass for unauthorized login. Primarily used in penetration testing for web app auth flaws.

## Features

- Feature 1: Automatic timestamp incrementation for brute-forcing
- Feature 2: MD5 collision detection via PHP's loose comparison simulation
- Feature 3: Cookie attachment and HTTP response validation for success

## Installation

### Requirements

- PHP 7+ with curl extension
- Access to ImpressCMS source for DB config inference

### Install Commands

```bash
# Save as auth-bypass.php and ensure executable
chmod +x auth-bypass.php
```

## Basic Usage

```bash
php auth-bypass.php --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show usage and parameters |
| `-v, --verbose` | Enable detailed logging of requests |

## Examples

### Example 1: Basic Usage

```bash
php auth-bypass.php http://localhost/impresscms/ admin
```

### Example 2: Advanced Usage

```bash
php auth-bypass.php -v https://target.com/impresscms/ user
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]
- [[Brute Force]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of POST/GET requests to autologin endpoint with varying timestamps
- Unusual User-Agent or PHP curl signatures in logs
- Failed MD5 computations logged if server-side monitoring enabled

## Related Procedures

- [[procedures/Brute-Force-Timestamps-with-Auth-Bypass-POC]]
- [[procedures/Craft-Malicious-Autologin-Cookies-for-MD5-Collision]]

## Related Tools

- [[Burp Suite]]
- [[curl]]

## References

- HackerOne Report: https://hackerone.com/reports/1081986
- PHP Type Juggling Docs: https://www.php.net/manual/en/types.comparisons.php
