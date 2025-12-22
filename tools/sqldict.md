---
id: 63353b1f-c979-467e-ae6a-d11a31ef8a3e
type: tool
verified: true
created_at: '2019-08-28T21:17:31.042227+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - brute-force
  - sql-server
  - credential-access
url: 'https://github.com/lorenzog/SqlDict'
commands:
  - '[[commands/sqldict-perform-dictionary-attack]]'
validated: true
---

# SQLdict

**Status**: Unverified

## Overview

SQLdict is a specialized dictionary attack tool for brute-forcing authentication credentials on Microsoft SQL Server instances. It is commonly used in penetration testing to identify weak or default credentials on exposed SQL servers, aiding in initial access or privilege escalation scenarios.

## Description

SQLdict automates the process of testing username-password combinations from dictionary files against a target SQL Server. It supports both local and domain accounts, multiple instances, and provides output indicating successful logins. This tool is particularly useful for red team operations targeting Windows environments with SQL Server deployments, mapping to MITRE ATT&CK techniques like Brute Force (T1110).

## Features

- Dictionary-based brute-forcing of SQL Server logins
- Support for domain-integrated authentication
- Configurable for specific SQL instances (e.g., named instances)
- Verbose logging of attempts and successes
- Lightweight Python implementation for easy integration

## Installation

### Requirements

- Python 2.7 or 3.x
- Impacket library (for SQL Server protocol handling)
- Kali Linux or similar distribution recommended

### Install Commands

```bash
# On Kali Linux (pre-packaged)
sudo apt update && sudo apt install sqldict

# Manual installation from source
sudo apt install git python3-pip
pip3 install impacket
git clone https://github.com/lorenzog/SqlDict.git
cd SqlDict
python3 setup.py install
```

## Basic Usage

```bash
sqldict --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for attempt logging |
| -t, --threads | Number of threads for parallel attempts (default: 1) |

## Examples

### Example 1: Basic Usage

```bash
sqldict -u users.txt -p passlist.txt -s target-server-ip
```

### Example 2: Advanced Usage

```bash
sqldict -u users.txt -p passlist.txt -s 192.168.1.50 -d CORP -i REPORTING -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual connection attempts to port 1433 (default SQL Server) from external IPs
- Failed login audits in SQL Server error logs (Event ID 18456)
- Network traffic patterns showing repeated authentication requests
- Process monitoring for sqldict.py or impacket usage on attacker machines

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Hydra]]
- [[tools/Medusa]]

## References

- Official GitHub Repository: https://github.com/lorenzog/SqlDict
- Kali Tools Documentation: https://tools.kali.org/password-attacks/sqldict
