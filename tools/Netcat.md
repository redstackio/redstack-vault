---
url: 'https://nmap.org/ncat/'
tags:
  - network
  - exploitation
type: tool
platforms:
  - Linux
  - macOS
description: >-
  Networking utility for reading/writing across network connections, useful for
  raw HTTP requests.
id: 0d679ef1-1fa8-4baf-bb12-46e3d40871e6
created_at: '2025-12-13T09:01:22.508Z'
updated_at: '2025-12-13T09:01:22.508Z'
verified: false
validated: true
submitted: true
---
# netcat

**Status**: Unverified

## Overview

Netcat (nc) is a networking tool for creating TCP/UDP connections, often used in security for sending raw data and exploiting network vulnerabilities.

## Description

It allows low-level control over network packets, making it ideal for crafting custom HTTP requests in exploits like request smuggling.

## Features

- Feature 1: TCP/UDP client/server
- Feature 2: Raw data transmission
- Feature 3: Port scanning capabilities

## Installation

### Requirements

- Available on most Unix systems

### Install Commands

```bash
# On Debian/Ubuntu
sudo apt install netcat
```

## Basic Usage

```bash
nc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v` | Verbose mode |
| `-l` | Listen mode |

## Examples

### Example 1: Basic Usage

```bash
nc target.com 80
```

### Example 2: Advanced Usage

```bash
echo 'GET / HTTP/1.1\r\nHost: target.com\r\n\r\n' | nc target.com 80
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for nc processes in logs
- Detection method 2: Detect raw HTTP traffic anomalies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/curl]]

## References

- Official documentation: https://nmap.org/ncat/guide.html
