---
url: 'https://github.com/joaomatosf/jexboss'
tags:
  - exploit
  - rce
  - java
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Tool for exploiting Java deserialization vulnerabilities in JBoss to gain
  remote code execution.
id: aab67648-cfa0-4480-a3e8-59a4b02b5e2c
created_at: '2025-12-11T06:10:24.626Z'
updated_at: '2025-12-11T06:10:24.626Z'
verified: false
validated: true
submitted: true
---
# jexboss

**Status**: Unverified

## Overview

Jexboss is a tool designed to test and exploit vulnerabilities in JBoss Application Server, particularly Java deserialization flaws leading to RCE.

## Description

It automates the detection and exploitation of deserialization issues in JBoss consoles, allowing attackers to gain shell access on vulnerable servers. Commonly used in web application penetration testing.

## Features

- Feature 1: Automatic vulnerability scanning
- Feature 2: Payload delivery for RCE
- Feature 3: Support for multiple JBoss versions

## Installation

### Requirements

- Python 2.x or 3.x
- Git

### Install Commands

```bash
git clone https://github.com/joaomatosf/jexboss.git
cd jexboss
pip install -r requires.txt
```

## Basic Usage

```bash
python jexboss.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-u` | Target URL |

## Examples

### Example 1: Basic Usage

```bash
python jexboss.py -u "http://target/web-console"
```

### Example 2: Advanced Usage

```bash
python jexboss.py -u "http://target/josso/%5C../web-console" --auto-exploit
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for requests to /web-console with unusual payloads
- Detection method 2: Log Java deserialization attempts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Metasploit]]
- [[Burp Suite]]

## References

- Official GitHub repository
- JBoss vulnerability documentation
