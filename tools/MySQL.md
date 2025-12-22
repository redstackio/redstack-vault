---
url: 'https://www.mysql.com/'
tags:
  - database
  - sql
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Relational database management system for hosting the test environment and
  executing vulnerable queries.
id: 5d2a6273-61e2-4235-b0f6-8fc65dd72835
created_at: '2025-12-14T03:46:15.027Z'
updated_at: '2025-12-14T03:46:15.027Z'
verified: false
validated: true
submitted: true
---
# MySQL

**Status**: Unverified

## Overview

MySQL is an open-source RDBMS used in this scenario to set up a vulnerable test database, allowing demonstration of SQL injection impacts through the Node.js module.

## Description

It supports SQL standards and is common in web apps. Version 5.7 on macOS is mentioned, with localhost connection (root user, empty password, 'test' DB) for POC isolation.

## Features

- Feature 1: ACID-compliant transactions
- Feature 2: High performance with InnoDB
- Feature 3: Replication and clustering

## Installation

### Requirements

- OS with package manager (e.g., Homebrew on macOS)

### Install Commands

```bash
# On macOS
brew install mysql
brew services start mysql
mysql_secure_installation
```

## Basic Usage

```bash
mysql --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u` | Username |
| `-p` | Password prompt |
| `-h` | Host |

## Examples

### Example 1: Basic Usage

```bash
mysql -u root -p test
```

### Example 2: Advanced Usage

```bash
mysql -u root -h localhost -e "SELECT * FROM user;"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Port 3306 listening
- Log entries for anomalous queries

## Related Procedures

- [[procedures/Setup-Test-MySQL-Database]]

## Related Tools

- [[MariaDB]]

## References

- Official documentation: https://dev.mysql.com/doc/
