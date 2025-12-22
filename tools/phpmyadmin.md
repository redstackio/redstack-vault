---
url: 'https://www.phpmyadmin.net/'
tags:
  - mysql-admin
  - web-interface
type: tool
verified: false
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.365Z'
id: 8b818bd5-8fc8-4f2f-8403-0c2482b913f7
validated: true
submitted: true
---
# phpMyAdmin

**Status**: Unverified

## Overview

Web-based MySQL administration tool vulnerable to this attack if AllowArbitraryServer is enabled, allowing connections to rogue servers.

## Description

It provides a GUI for queries and server management. Exploitation occurs when users connect to a malicious host and run LOAD DATA LOCAL INFILE, triggering file exfiltration.

## Features

- Feature 1: Arbitrary server connection
- Feature 2: SQL query execution
- Feature 3: Table management

## Installation

### Requirements

- PHP and web server (Apache/Nginx)
- MySQL

### Install Commands

```bash
# Download and extract
wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.tar.gz
tar -xzvf phpMyAdmin-5.2.1-all-languages.tar.gz
mv phpMyAdmin-5.2.1-all-languages /var/www/html/phpmyadmin
```

## Basic Usage

Access via browser: http://localhost/phpmyadmin

### Common Options

| Option | Description |
|--------|-------------|
| AllowArbitraryServer | Enable custom server entry (dangerous)

## Examples

### Example 1: Basic Usage

Connect to default localhost MySQL.

### Example 2: Advanced Usage

In config.inc.php: $cfg['AllowArbitraryServer'] = true; then enter rogue host.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Web logs showing connections to external MySQL
- Config checks for AllowArbitraryServer

## Related Procedures

- [[procedures/Trick-Victim-into-Connecting-to-Rogue-MySQL-Server]]

## Related Tools

- [[tools/adminer]]

## References

- Official site: https://www.phpmyadmin.net/
