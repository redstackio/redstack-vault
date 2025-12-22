---
id: 00af63a0-a9f2-4ce5-882c-6a395f5e75ad
type: tool
verified: true
created_at: '2019-08-28T21:17:31.254300+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - brute-force
  - credential-access
  - enumeration
url: 'https://github.com/lanjelot/patator'
commands:
  - '[[commands/patator-ssh-login-brute-force]]'
  - '[[commands/patator-ftp-login-brute-force]]'
  - '[[commands/patator-http-fuzz-brute-force]]'
  - '[[commands/patator-smtp-vrfy-enumerate-users]]'
validated: true
---

# patator

**Status**: Unverified

## Overview

Patator is a multi-purpose brute-forcer tool designed for flexible and modular brute-force attacks and enumerations. It supports various protocols and services, making it useful for credential stuffing, user enumeration, and fuzzing in penetration testing and red team operations.

## Description

Patator features a modular design allowing brute-forcing across multiple services like FTP, SSH, Telnet, SMTP, HTTP, POP3, IMAP, LDAP, SMB, databases (MSSQL, Oracle, MySQL, PostgreSQL), VNC, DNS, SNMP, and more. It handles wordlists efficiently, supports threading for speed, and includes options for ignoring specific error responses to focus on successful hits.

## Features

- Modular support for 20+ protocols and services
- Flexible wordlist handling with positional arguments (0=users, 1=passwords)
- Multi-threading for faster execution
- Customizable ignore rules for error codes/messages
- Persistent connections and session management
- Output formatting for hits and statistics

## Installation

### Requirements

- Python 3.x
- pip

### Install Commands

```bash
# Clone from GitHub
sudo apt update && sudo apt install git python3 python3-pip -y
git clone https://github.com/lanjelot/patator.git
cd patator

# Or install via pip (if available)
pip3 install patator

# For Kali Linux (pre-built package)
sudo apt install patator
```

For Ubuntu/Debian: Follow the git clone steps above. For Windows: Use WSL or a Python environment with git.

## Basic Usage

```bash
python3 patator.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --threads=N | Number of concurrent threads |
| -x ignore:code=XXX | Ignore specific response codes |
| -x ignore:mesg='MSG' | Ignore specific error messages |
| --timeout=N | Connection timeout in seconds |

## Examples

### Example 1: Basic Usage

See related commands for specific module examples, such as [[commands/patator-ssh-login-brute-force]].

### Example 2: Advanced Usage

```bash
python3 patator.py ssh_login host=192.168.1.100 0=users.txt 1=passlist.txt --threads=50 -x ignore:mesg='Authentication failed.'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[System Information Discovery]] System Information Discovery (for enumeration modules)

### Tactics

- [[Credential Access]] Credential Access
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual high-volume connections to services (e.g., SSH, FTP) from a single source
- Failed login attempts logged in service logs (auth.log, secure.log)
- Network traffic patterns showing rapid credential attempts
- Python process with patator.py in process lists or command history

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
- [[tools/medusa]]

## References

- Official GitHub: https://github.com/lanjelot/patator
- Documentation: Included in repo README
