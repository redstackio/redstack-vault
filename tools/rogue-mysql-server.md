---
url: >-
  https://github.com/allyshka/Rogue-MySql-Server/blob/master/rogue_mysql_server.py
tags:
  - rogue-server
  - exploitation
  - mysql
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.368Z'
id: f92fff57-283d-4108-bed3-113996db8a1c
validated: true
submitted: true
---
# Rogue MySQL Server

**Status**: Unverified

## Overview

A Python script simulating a MySQL server to exploit the LOAD DATA LOCAL INFILE protocol flaw by sending crafted FB packets for remote file disclosure.

## Description

It handles MySQL handshakes, accepts any login, detects LOAD DATA queries, and responds with an FB packet containing a victim filename, causing the client to exfiltrate the file.

## Features

- Feature 1: Arbitrary authentication
- Feature 2: FB packet crafting
- Feature 3: Payload logging

## Installation

### Requirements

- Python 2.7 or 3.x

### Install Commands

```bash
git clone https://github.com/allyshka/Rogue-MySql-Server.git
cd Rogue-MySql-Server
pip install -r requirements.txt  # If any
```

## Basic Usage

```bash
python rogue_mysql_server.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --host | Bind address (default 0.0.0.0)
| --port | Port (default 3306)
| --filename | Target file for FB packet

## Examples

### Example 1: Basic Usage

```bash
python rogue_mysql_server.py
```

### Example 2: Advanced Usage

```bash
python rogue_mysql_server.py --filename '/etc/shadow'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual MySQL servers on non-standard hosts
- Protocol mismatches in traffic

## Related Procedures

- [[procedures/Implement-Rogue-MySQL-Server-for-Exploitation]]
- [[procedures/Receive-and-Log-Exfiltrated-File-Contents]]

## Related Tools

- [[tools/mysql-client]]

## References

- GitHub repo: https://github.com/allyshka/Rogue-MySql-Server
