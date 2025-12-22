---
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/q82wmnbbpgc70ty3o7c6ktf8gfb0?response-content-disposition=attachment%3B%20filename%3D%22sqli.php%22%3B%20filename%2A%3DUTF-8%27%27sqli.php&response-content-type=application%2Fx-php
tags:
  - poc
  - sqli
  - php
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.561Z'
id: 36394375-6cd7-4071-96cf-34d8deb958cf
validated: true
submitted: true
---
# sqli-php

**Status**: Unverified

## Overview

Custom PHP CLI script for automating SQL injection exploitation in ImpressCMS, including token retrieval via auth bypass and boolean-based data extraction.

## Description

The sqli.php script targets ImpressCMS 1.4.2 vulnerabilities: it first exploits auth bypass (#1081137) for a token, then POSTs to /include/findusers.php with 'groups' array payloads for blind SQLi or stacked queries. Supports extracting emails/hashes from users table or inserting users. Ideal for unauthenticated web app pentesting.

## Features

- Feature 1: Automated token retrieval
- Feature 2: Boolean-based blind SQLi extraction
- Feature 3: Stacked query support for DB writes

## Installation

### Requirements

- PHP 7+ with cURL extension
- Access to target URL

### Install Commands

```bash
# Download from report attachment
wget "https://hackerone.../sqli.php" -O sqli.php
chmod +x sqli.php
```

## Basic Usage

```bash
php sqli.php --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --blind | Enable blind SQLi mode |
| --payload | Custom payload string |

## Examples

### Example 1: Basic Usage

```bash
php sqli.php http://localhost/impresscms/
```

### Example 2: Advanced Usage

```bash
php sqli.php http://target.com/ --extract-email --prefix i36fd6f18_
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing POST to /include/findusers.php with array 'groups'
- PHP execution traces or anomalous cURL requests
- Database query logs with injected semicolons or boolean conditions

## Related Procedures

- [[procedures/Exploit-SQL-Injection-in-findusers-php]]
- [[procedures/Extract-Data-or-Modify-Database-via-SQLi]]

## Related Tools


## References

- HackerOne Report #1081145
- ImpressCMS Documentation
