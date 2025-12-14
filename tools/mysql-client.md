---
url: 'https://dev.mysql.com/doc/refman/8.0/en/mysql.html'
tags:
  - mysql
  - database-client
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.370Z'
id: af534c39-0e7c-4ce8-8e36-a3b23594c991
validated: true
submitted: true
---
# mysql Client

**Status**: Unverified

## Overview

The native mysql command-line client for interacting with MySQL servers, used here to execute LOAD DATA LOCAL INFILE queries during protocol testing.

## Description

It supports connecting to servers, running SQL queries, and handling local file operations. Vulnerable implementations echo filenames in responses, enabling exploitation.

## Features

- Feature 1: SQL query execution
- Feature 2: Local file import via LOAD DATA LOCAL
- Feature 3: Protocol handshake and authentication

## Installation

### Requirements

- MySQL server package

### Install Commands

```bash
# On Ubuntu
sudo apt install mysql-client

# Or with full MySQL
sudo apt install mysql-server
```

## Basic Usage

```bash
mysql --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u | Username
| -p | Prompt for password
| -h | Host

## Examples

### Example 1: Basic Usage

```bash
mysql -u root -p -h localhost
```

### Example 2: Advanced Usage

```bash
mysql -u root -p -e "LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn;"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor mysql process arguments for LOCAL INFILE
- Log client connections

## Related Procedures

- [[procedures/Analyze-MySQL-LOAD-DATA-LOCAL-INFILE-Protocol-with-tcpdump]]

## Related Tools

- [[tools/rogue-mysql-server]]

## References

- Official documentation: https://dev.mysql.com/doc/refman/8.0/en/mysql.html
