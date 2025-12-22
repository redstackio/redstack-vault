---
id: 705cc3fa-7c71-4476-ba43-89b7222a0fa5
name: HexorBase
type: tool
verified: true
created_at: '2019-08-28T21:17:41.408260+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - database
  - bruteforce
  - administration
  - auditing
url: 'https://github.com/hexorbase/hexorbase'
validated: true
---

# HexorBase

**Status**: Unverified

## Overview

HexorBase is an open-source database administration and auditing tool designed for managing multiple database servers from a single interface. It supports common databases like MySQL, SQLite, Microsoft SQL Server, Oracle, and PostgreSQL. Primarily used in penetration testing for SQL query execution and credential bruteforcing, it also facilitates routing traffic through proxies or Metasploit for accessing hidden networks.

## Description

HexorBase provides a centralized GUI for connecting to remote databases, executing SQL queries, and performing automated bruteforce attacks to test credential strength. It excels in scenarios where direct access is restricted, allowing integration with proxies or pivoting techniques via Metasploit. The tool is Python-based with a Tkinter interface, making it lightweight for offensive security operations like database enumeration, data extraction, and access validation during red team engagements.

## Features

- Feature 1: Multi-database support (MySQL, SQLite, MSSQL, Oracle, PostgreSQL) for unified management.
- Feature 2: Built-in bruteforce module for credential testing against database logins.
- Feature 3: Proxy and pivoting support to reach inaccessible servers in local subnets.
- Feature 4: SQL query execution and result auditing from a single dashboard.
- Feature 5: Logging and export capabilities for audit trails.

## Installation

### Requirements

- Python 2.7 or 3.x (Tkinter for GUI)
- Git for cloning the repository
- Database-specific drivers (e.g., pymysql for MySQL)

### Install Commands

```bash
# Clone the repository
sudo apt update
git clone https://github.com/hexorbase/hexorbase.git
cd hexorbase

# Install dependencies (for Ubuntu/Kali)
sudo apt install python3-tk python3-pip
pip3 install -r requirements.txt

# Install the tool
sudo python3 setup.py install
```

For Kali Linux, some dependencies may be pre-installed.

## Basic Usage

```bash
tool-name --help
```

Launch the GUI:

```python
python /opt/hexorbase/hexorbase.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and available databases |
| `--proxy` | Enable proxy routing for connections |
| `--bruteforce` | Initiate bruteforce mode from CLI |

## Examples

### Example 1: Basic Usage

Launch the application and add a MySQL connection:

```python
python hexorbase.py
```

In the GUI, enter host, port, credentials, and execute queries.

### Example 2: Advanced Usage

Bruteforce a MySQL instance via CLI:

```python
python /opt/hexorbase/bruteforce.py -t 192.168.1.50 -u users.txt -w passwords.txt --db mysql
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (for credential attacks)
- [[Exploitation of Remote Services]] Exploitation of Remote Services (database exploitation)

### Tactics

- [[Credential Access]] Credential Access
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for multiple failed database login attempts from a single source IP.
- Detection method 2: Network traffic to database ports (3306 for MySQL, 1433 for MSSQL) with proxy chaining.
- Detection method 3: Presence of HexorBase binaries or Python processes with Tkinter GUI on compromised hosts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]]
- [[tools/sqlmap]]

## References

- Official GitHub: https://github.com/hexorbase/hexorbase
- Documentation: Included in repository README
