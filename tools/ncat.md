---
id: tool-uuid-001
url: 'https://nmap.org/ncat/'
tags:
  - network
  - tcp
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.964Z'
validated: true
submitted: true
---
# ncat

**Status**: Unverified

## Overview

ncat is a versatile networking utility from the Nmap project, used for reading/writing data over TCP/UDP/SSL, ideal for sending custom HTTP requests in DoS PoCs.

## Description

ncat supports scripting and automation for offensive operations like flooding servers with crafted packets. In this context, it's used to pipe HTTP requests to vulnerable Apache servers for Range header exploitation.

## Features

- Feature 1: TCP/UDP/SSL support for flexible connections
- Feature 2: Scripting integration with bash for loops and payloads
- Feature 3: Verbose output for debugging network interactions

## Installation

### Requirements

- Nmap suite or standalone ncat package

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt install nmap
# Or download from nmap.org
```

## Basic Usage

```bash
ncat example.com 80
```

### Common Options

| Option | Description |
|--------|-------------|
| --ssl | Enable SSL/TLS |
| -v | Verbose mode |
| -C | Send CRLF line endings |

## Examples

### Example 1: Basic Usage

```bash
ncat owncloud.com 80
```

### Example 2: Advanced Usage

```bash
cat request.txt | ncat --ssl owncloud.com 443
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing repeated TCP connections from same source
- Process monitoring for ncat executions
- SSL handshake anomalies in traffic

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

- Official documentation: https://nmap.org/ncat/
- Related resources: Nmap project site
