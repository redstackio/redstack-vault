---
url: 'https://github.com/0xacb/viewgen/blob/master/README.md'
tags:
  - rce
  - asp.net
  - viewstate
type: tool
platforms:
  - Windows
  - Web
description: >-
  Tool for generating ASP.NET viewstate to achieve remote code execution after
  extracting configuration via vulnerabilities like XXE.
id: 5d01c3dd-4905-4685-ad85-02e050712cfa
created_at: '2025-12-13T09:00:27.847Z'
updated_at: '2025-12-13T09:00:27.847Z'
verified: false
validated: true
submitted: true
---
# viewgen

**Status**: Unverified

## Overview

viewgen is a tool designed to generate ASP.NET viewstates based on extracted configuration files, commonly used in offensive security to escalate vulnerabilities like XXE to remote code execution.

## Description

It processes web.config files to create valid viewstates that can be used in attacks against ASP.NET applications, enabling code injection and execution.

## Features

- Viewstate generation from config files
- Support for RCE exploitation chains
- Integration with XXE outputs

## Installation

### Requirements

- Python environment
- Git

### Install Commands

```bash
git clone https://github.com/0xacb/viewgen.git
cd viewgen
pip install -r requirements.txt
```

## Basic Usage

```bash
python viewgen.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
python viewgen.py -c web.config -o viewstate.txt
```

### Example 2: Advanced Usage

```bash
python viewgen.py -c web.config --payload malicious_code -o exploit_viewstate.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for viewstate tampering in ASP.NET logs
- Detect anomalous config file accesses

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- https://github.com/0xacb/viewgen/blob/master/README.md
