---
url: 'https://bl4de.000webhostapp.com/'
tags:
  - hosting
  - exfiltration-server
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.665Z'
id: e155b067-7c25-4d51-93f3-950fea6b268d
validated: true
submitted: true
---
# 000webhost

**Status**: Unverified

## Overview

000webhost is a free web hosting service used to quickly deploy PHP scripts for receiving and logging data, such as stolen cookies in XSS attacks, without needing paid infrastructure.

## Description

It provides basic PHP and MySQL support, file upload via control panel, and public URLs for endpoints. In offensive security, it's ideal for temporary C2 or exfiltration servers due to ease of setup and anonymity. Limitations include bandwidth caps and potential downtime.

## Features

- Feature 1: Free PHP hosting with one-click installs
- Feature 2: File manager for uploading scripts like cookie loggers
- Feature 3: Public domain for img src callbacks in JS payloads

## Installation

### Requirements

- Email for account signup
- Basic web knowledge

### Install Commands

No install; sign up at 000webhost.com and create a site.

## Basic Usage

Upload PHP files via panel; access via provided URL.

### Common Options

| Option | Description |
|--------|-------------|
| File Manager | Upload/edit scripts |
| MySQL | Optional DB for advanced logging |

## Examples

### Example 1: Basic Usage

Create site, upload php-cookie-logger.php, access https://site.000webhostapp.com/logger.php?c=test.

### Example 2: Advanced Usage

Configure subdomain for stealth; add .htaccess for URL rewriting.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous traffic to free hosting domains from internal networks
- File uploads to suspicious hosts in proxy logs

## Related Procedures

- [[procedures/Verify-Cookie-Exfiltration-on-Attacker-Server]]

## Related Tools

- [[tools/Chrome]]

## References

- Official site: https://www.000webhost.com/
