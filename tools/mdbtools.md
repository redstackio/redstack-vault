---
id: 99ce2973-7659-4c3b-bd28-b7415717c39a
type: tool
verified: true
created_at: '2019-08-28T21:17:26.587008+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
tags:
  - database-enumeration
  - data-extraction
url: 'https://github.com/mdbtools/mdbtools'
commands:
  - '[[commands/mdb-tables-list-tables-in-database]]'
  - '[[commands/mdb-export-export-table-contents]]'
validated: true
---

# mdbtools

**Status**: Unverified

## Overview

mdbtools is an open-source suite of programs designed to read and manipulate Microsoft Access databases (.mdb and .accdb files). It is commonly used in security testing for offline analysis of Access databases obtained during data exfiltration or forensic investigations, allowing enumeration of tables, schemas, and extraction of data without needing Microsoft Access software.

## Description

The mdbtools suite provides utilities like mdb-tables for listing database structure, mdb-export for dumping table contents, mdb-schema for generating SQL schemas, and mdb-sql for querying data. It supports reading data types, indexes, and relationships, making it valuable for discovering sensitive information such as credentials, user data, or configuration details stored in legacy Access databases. Primarily used in post-exploitation scenarios where an attacker has obtained a .mdb file from a target system.

## Features

- Feature 1: Table enumeration and schema inspection without proprietary software
- Feature 2: Data export to CSV, SQL, or XML formats for analysis
- Feature 3: Support for querying databases using SQL-like syntax
- Feature 4: Handling of various Access versions (Jet 3.0 to 4.0)

## Installation

### Requirements

- GCC compiler and development libraries (for building from source)
- Unix-like environment (native on Linux, via Cygwin/MSYS2 on Windows)

### Install Commands

```bash
# On Debian/Ubuntu/Kali
sudo apt update
sudo apt install mdbtools

# On macOS (via Homebrew)
brew install mdbtools

# On Windows (via MSYS2)
pacman -S mingw-w64-x86_64-mdbtools

# From source (all platforms)
git clone https://github.com/mdbtools/mdbtools.git
cd mdbtools
./autogen.sh
./configure
make
sudo make install
```

## Basic Usage

```bash
mdb-tables --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-H, --help` | Show help message |
| `-V, --version` | Display version information |
| `-1` | Use one line per table (for scripting) |

## Examples

### Example 1: Basic Usage

List tables in a database:

```bash
mdb-tables database.mdb
```

### Example 2: Advanced Usage

Export a table while piping output:

```bash
mdb-export database.mdb users > users.csv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories (for database enumeration and extraction)
- [[Data from Local System]] Data from Local System (offline analysis of stolen databases)

### Tactics

- [[Collection]] Collection
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for mdb-tools binaries on Linux/Windows systems
- Detection method 2: File system watches for .mdb files being accessed or copied
- Detection method 3: Network logs showing database file transfers (if exfiltrated)
- Detection method 4: CSV/SQL dumps created in temporary directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/sqlmap]] (for online SQL database exploitation)
- [[tools/strings]] (for quick text extraction from binaries)

## References

- Official GitHub: https://github.com/mdbtools/mdbtools
- Documentation: https://mdbtools.github.io/
