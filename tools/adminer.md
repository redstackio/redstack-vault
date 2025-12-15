---
url: 'https://www.adminer.org/'
tags:
  - mysql-admin
  - lightweight
type: tool
verified: false
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.362Z'
id: 2edf23bd-d66a-44c9-b6a9-657e0c69bec5
validated: true
submitted: true
---
# Adminer

**Status**: Unverified

## Overview

Lightweight PHP-based database management tool for MySQL, used as an attack vector due to its ability to connect to arbitrary servers and execute queries.

## Description

Similar to phpMyAdmin but single-file; vulnerable clients can be tricked into connecting to rogue MySQL servers, leading to file exfiltration via LOAD DATA LOCAL INFILE.

## Features

- Feature 1: Single PHP file deployment
- Feature 2: Multi-DB support including MySQL
- Feature 3: Query execution interface

## Installation

### Requirements

- PHP-enabled web server

### Install Commands

```bash
# Download single file
wget https://www.adminer.org/latest.php -O /var/www/html/adminer.php
```

## Basic Usage

Access via browser: http://localhost/adminer.php

### Common Options

| Option | Description |
|--------|-------------|
| Server | Custom MySQL host entry

## Examples

### Example 1: Basic Usage

Enter localhost credentials.

### Example 2: Advanced Usage

Enter rogue server IP:3306 and run LOAD DATA query.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of adminer.php on web root
- Logs of external DB connections

## Related Procedures

- [[procedures/Trick-Victim-into-Connecting-to-Rogue-MySQL-Server]]

## Related Tools

- [[tools/phpmyadmin]]

## References

- Official site: https://www.adminer.org/
