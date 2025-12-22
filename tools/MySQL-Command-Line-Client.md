---
url: 'https://dev.mysql.com/doc/refman/5.7/en/mysql.html'
tags:
  - database
  - mysql
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.046Z'
id: a123d13b-82b8-4025-9920-b0037dccbf9b
validated: true
submitted: true
---
# MySQL-Command-Line-Client

**Status**: Unverified

## Overview

The mysql CLI is a command-line interface for interacting with MySQL databases, used here to setup tables and data for SQL injection testing against Node.js modules.

## Description

It allows executing SQL statements, managing schemas, and querying data. In security contexts, it's essential for simulating vulnerable databases and verifying injection payloads.

## Features

- Feature 1: Interactive SQL execution
- Feature 2: Batch script running
- Feature 3: Connection with credentials

## Installation

### Requirements

- MySQL server 5.7.13

### Install Commands

```bash
# On Ubuntu: sudo apt install mysql-client
# Verify: mysql --version
```

## Basic Usage

```bash
mysql --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -u, --user | Username |
| -p, --password | Prompt for password |
| -h, --host | Hostname |

## Examples

### Example 1: Basic Usage

```bash
mysql -u root -p
```

### Example 2: Advanced Usage

```bash
mysql -u root -p test < setup.sql
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Server Software Component]] Server Software Component: Database Services

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- mysql process running
- SQL logs with DDL/DML
- Port 3306 connections

## Related Procedures

- [[procedures/Setup-Test-MySQL-Database-and-Table]]
- [[procedures/Populate-Database-with-Sample-Data]]

## Related Tools

- [[MySQL Workbench]]
- [[phpMyAdmin]]

## References

- Official documentation: https://dev.mysql.com/doc/refman/5.7/en/mysql.html
