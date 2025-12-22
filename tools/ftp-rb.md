---
url: null
tags:
  - exfiltration
  - oob
  - ftp
type: tool
platforms:
  - Linux
description: >-
  Ruby script for running an FTP server to capture out-of-band exfiltrated data
  in XXE attacks.
id: 3d8b807f-7aa4-45f3-938a-344fd0081e70
created_at: '2025-12-13T09:00:27.526Z'
updated_at: '2025-12-13T09:00:27.526Z'
verified: false
validated: true
submitted: true
---
# ftp.rb

**Status**: Unverified

## Overview

ftp.rb is a custom Ruby script used to set up a simple FTP server for receiving data exfiltrated via out-of-band techniques in vulnerabilities like XXE.

## Description

The tool listens on a specified port and captures incoming FTP connections, logging or storing the received data. It is commonly used in penetration testing to confirm data leakage from blind exploits.

## Features

- Feature 1: Starts a basic FTP server
- Feature 2: Captures and logs incoming data
- Feature 3: Supports OOB exfiltration scenarios

## Installation

### Requirements

- Ruby installed
- Network access for listening

### Install Commands

```bash
# No installation needed; run the script directly
```

## Basic Usage

```bash
ruby ftp.rb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--port` | Specify listening port |
| `--host` | Specify listening host |

## Examples

### Example 1: Basic Usage

```bash
ruby ftp.rb
```

### Example 2: Advanced Usage

```bash
ruby ftp.rb --port 21
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unexpected FTP traffic
- Detection method 2: Scan for Ruby processes listening on ports

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

- HackerOne report: https://hackerone.com/reports/106797
