---
url: 'https://www.sqlite.org/cli.html'
tags:
  - database
  - sqlite
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.628Z'
id: f64c8453-8060-4ee0-8c81-de05e29e0c48
validated: true
submitted: true
---
# sqlite3

**Status**: Unverified

## Overview

sqlite3 is a command-line interface for SQLite databases, used here to query and modify Django's cache storage for payload injection in deserialization attacks.

## Description

SQLite3 provides a shell for executing SQL commands on lightweight databases like Django's default db.sqlite3. In offensive security, it's used for direct data manipulation in PoCs, such as updating pickled cache values to exploit vulnerabilities.

## Features

- Feature 1: Interactive SQL execution
- Feature 2: Direct file-based database access
- Feature 3: Export/import capabilities

## Installation

### Requirements

- Standard on most Unix-like systems

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt install sqlite3

# On macOS (if not present)
brew install sqlite
```

## Basic Usage

```bash
sqlite3 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| -header | Enable column headers in output |
| -line | Output one value per line |

## Examples

### Example 1: Basic Usage

```bash
sqlite3 db.sqlite3 "SELECT * FROM table;"
```

### Example 2: Advanced Usage

```bash
sqlite3 db.sqlite3
sqlite> .tables
sqlite> SELECT * FROM my_cache_table;
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for sqlite3 executions on database files
- File system audits for direct db.sqlite3 access

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://www.sqlite.org/cli.html
- Related resources: SQLite in Django docs
