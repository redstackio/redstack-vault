---
type: tool
verified: true
created_at: '2019-08-28T21:17:17.890737+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/mdb-tables-list-tables-in-mdb-database]]'
  - '[[commands/mdb-export-export-table-to-csv]]'
platforms:
  - Linux
tags:
  - data-exposure
  - extract
url: 'https://github.com/mdbtools/mdbtools'
validated: true
---

# mdb-export

**Status**: Unverified

## Overview

mdb-export is a command-line utility from the mdbtools package designed to extract data from Microsoft Access (.mdb) database files and output it in CSV (comma-separated value) format. It is commonly used in security testing for data exfiltration, forensic analysis, or migrating legacy database contents to modern formats like spreadsheets or other databases.

## Description

The tool reads the structure and data from .mdb tables and converts them into portable CSV files, preserving field types where possible. It supports options for customizing delimiters, headers, and quoting, making it versatile for handling various import scenarios. In offensive security contexts, it aids in dumping sensitive information from compromised Access databases found on Windows systems.

## Features

- Feature 1: Exports specific tables or entire databases to CSV
- Feature 2: Customizable output formats (e.g., tab-delimited, quoted fields)
- Feature 3: Handles binary data and memo fields with appropriate escaping

## Installation

### Requirements

- Linux/Unix environment (e.g., Ubuntu, Kali)
- Basic build tools if compiling from source

### Install Commands

```bash
# On Debian/Ubuntu/Kali
sudo apt update
sudo apt install mdbtools
```

For other platforms, compile from source:

```bash
wget https://github.com/mdbtools/mdbtools/archive/refs/heads/master.zip
unzip master.zip
cd mdbtools-master
./autogen.sh
./configure
make
sudo make install
```

## Basic Usage

```bash
mdb-export --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -H, --noheader | Suppress column headers in output |
| -I, --separator CHAR | Set field separator (default: comma) |
| -Q, --quote | Quote all fields |
| -d, --delimiter | Specify delimiter for quoted fields |

## Examples

### Example 1: Basic Usage

First, list tables:

```bash
mdb-tables database.mdb
```

Then export a table:

```bash
mdb-export database.mdb users > users.csv
```

### Example 2: Advanced Usage

Export with tab separation and no headers:

```bash
mdb-export -I '\t' -H database.mdb accounts > accounts.tsv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]] Data from Local System

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for mdbtools processes (e.g., mdb-export, mdb-tables) on Linux systems via ps or audit logs
- Detection method 2: File system monitoring for .csv outputs from .mdb files or unexpected database access

## Related Procedures

- [[procedures/Enumerate-Tables-and-Contents-in-MS-Access-MDB-File]]

## Related Tools

- [[tools/mdbtools]]

## References

- Official GitHub: https://github.com/mdbtools/mdbtools
- Man page: man mdb-export
