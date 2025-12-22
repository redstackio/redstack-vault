---
id: tool-sqlite
url: 'https://www.sqlite.org/'
tags:
  - database
  - query
  - analysis
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.734Z'
validated: true
submitted: true
---
# sqlite

**Status**: Unverified

## Overview

sqlite3 is the command-line interface for SQLite databases, used to query and manipulate lightweight DB files, common in applications like Grafana for local storage.

## Description

It provides SQL execution on .db files, ideal for post-exploitation analysis of downloaded databases to extract user data or configurations.

## Features

- Feature 1: Interactive shell for SQL queries
- Feature 2: Export/import data
- Feature 3: Schema inspection

## Installation

### Requirements

- Standard on Linux; binaries for others

### Install Commands

```bash
# Ubuntu/Debian
apt update && apt install sqlite3

# From source
wget https://www.sqlite.org/2023/sqlite-autoconf-3450100.tar.gz && tar -xzf sqlite-autoconf-3450100.tar.gz && cd sqlite-autoconf-3450100 && ./configure && make && make install
```

## Basic Usage

```bash
sqlite3 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| .help | Show help |
| .tables | List tables |
| .quit | Exit shell |

## Examples

### Example 1: Basic Usage

```bash
sqlite3 database.db "SELECT * FROM table;"
```

### Example 2: Advanced Usage

Interactive:

```bash
sqlite3 database.db
sqlite> .tables
sqlite> SELECT * FROM user;
sqlite> .quit
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System
- [[Data from Information Repositories]] Data from Information Repositories

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- File system monitoring for sqlite3 processes on downloaded DBs
- Audit logs of database file access
- Memory forensics for SQL queries

## Related Procedures


## Related Tools

- [[tools/mysql]]
- [[tools/psql]]

## References

- Official documentation: https://www.sqlite.org/cli.html
- Related resources: SQLite security analysis guides
