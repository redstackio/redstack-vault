---
id: d7f7dbda-c15d-4fc9-a074-3bd7718fbf72
type: tool
verified: true
created_at: '2019-08-28T21:17:28.906685+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - bruteforce
  - credential-access
  - automation
url: 'https://github.com/x90skysn3k/brutespray'
validated: true
---

# brutespray

**Status**: Verified

## Overview

BruteSpray is an automated tool for brute-forcing network services discovered via Nmap scans. It parses Nmap GNMAP or XML output to identify open services (including non-standard ports via -sV) and attempts default credential logins using Medusa. Ideal for initial credential access in penetration testing and red team operations targeting weak default configurations.

## Description

BruteSpray streamlines post-scan brute-forcing by integrating Nmap results directly, supporting services like SSH, FTP, Telnet, HTTP, and more. It uses Medusa as the backend for parallel authentication attempts and can handle custom user/password lists, though defaults to common pairs. This tool is particularly useful in reconnaissance-to-exploitation workflows where manual credential testing would be time-consuming.

## Features

- Feature 1: Parses Nmap GNMAP and XML outputs for service detection
- Feature 2: Supports brute-forcing on non-standard ports identified by Nmap -sV
- Feature 3: Integrates Medusa for multi-protocol credential testing (SSH, FTP, SNMP, etc.)
- Feature 4: Configurable threads for performance tuning
- Feature 5: Outputs successful logins for further exploitation

## Installation

### Requirements

- Python 2.7 or 3.x
- Nmap installed
- Medusa (for brute-forcing backend)
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/x90skysn3k/brutespray.git
cd brutespray

# Install dependencies (if any)
pip install -r requirements.txt

# For Kali Linux (often pre-built or easy install)
# Or use: apt install brutespray (if available in repos)
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install nmap medusa git python3
# Then clone as above
```

## Basic Usage

```bash
tool-name --help
```

BruteSpray is run as a Python script:

```python
python brutespray.py -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Input Nmap file (GNMAP or XML) |
| -t, --threads | Number of threads for Medusa |
| -u, --users | Custom username list file |
| -p, --pass | Custom password list file |
| -e, --extensions | Password extensions (e.g., .txt,123) |
| -m, --modules | Specific modules (ssh,ftp,etc.) |

## Examples

### Example 1: Basic Usage

First, generate Nmap output:

```bash
nmap -sV -oG scan.gnmap 192.168.1.0/24
```

Then run BruteSpray:

```python
python brutespray.py -f scan.gnmap
```

### Example 2: Advanced Usage

With custom threads and modules:

```python
python brutespray.py -f scan.xml -t 10 -m ssh,ftp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Password Spraying]] Password Spraying

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of failed login attempts from a single source (e.g., via logs in SSH/FTP)
- Detection method 2: Network traffic patterns matching Medusa's multi-threaded probes
- Detection method 3: Presence of BruteSpray binaries or Python scripts in process lists
- Detection method 4: Anomalous authentication attempts on non-standard ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/medusa]]

## References

- Official GitHub: https://github.com/x90skysn3k/brutespray
- Nmap Documentation: https://nmap.org/book/man.html
