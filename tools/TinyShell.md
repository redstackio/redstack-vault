---
id: 2b9c8c66-e3f2-4b69-a850-f16b4dbf78a4
type: tool
verified: true
created_at: '2019-08-28T21:17:29.076929Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - Web
tags:
  - web-shell
  - post-exploitation
  - framework
url: 'https://github.com/example/tinyshell'
validated: true
---

# TinyShell

**Status**: Unverified

## Overview

TinyShell is a lightweight web shell framework designed for post-exploitation in web environments. It allows security testers to generate, deploy, and interact with minimalistic PHP-based web shells for executing commands on compromised servers without requiring complex setups.

## Description

TinyShell provides a simple Python-based generator for creating obfuscated or basic PHP web shells. Once uploaded to a target web server (e.g., via file upload vulnerabilities), it enables remote command execution, file management, and basic persistence. Commonly used in red team engagements for maintaining access after initial exploitation of web applications. It supports password protection and basic encoding to evade simple detection.

## Features

- Feature 1: Easy generation of PHP web shells with customizable options like password authentication.
- Feature 2: Support for command execution, file upload/download, and directory listing via HTTP requests.
- Feature 3: Lightweight footprint, minimizing detection risks compared to full-featured shells like Weevely.

## Installation

### Requirements

- Python 3.x
- PHP on target (for shell execution)
- Access to a web server for deployment

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/tinyshell.git
cd tinyshell
pip install -r requirements.txt  # If any dependencies like cryptography for obfuscation
```

For Kali Linux: Often available via custom scripts or can be built from source.

For Ubuntu: Follow the clone steps above.

## Basic Usage

```bash
tinyshell.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --generate-basic | Generate a basic shell |
| --password | Set authentication password |
| --obfuscate | Obfuscate the PHP code |

## Examples

### Example 1: Basic Usage

Generate a simple shell:

```bash
python3 tinyshell.py --generate-basic --output shell.php
```

Upload shell.php to the target via a vulnerable endpoint, then interact:

```bash
curl "http://target.com/shell.php?cmd=id"
```

### Example 2: Advanced Usage

Generate a password-protected shell:

```bash
python3 tinyshell.py --generate-basic --password secret123 --output protected.php
```

Interact with authentication:

```bash
curl "http://target.com/protected.php?pass=secret123&cmd=uname -a"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Web Shell]] Web Shell
- [[JavaScript]] JavaScript (for client-side interaction if extended)

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual PHP files with system() or exec() calls in web roots.
- Detection method 2: Web application firewall (WAF) rules for command injection patterns in GET/POST parameters.
- Detection method 3: File integrity monitoring (FIM) alerts on new .php files in upload directories.
- Network logs showing repeated HTTP requests to the same PHP file with varying 'cmd' parameters.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/weevely]]
- [[b374k]]

## References

- Official documentation: Assumed GitHub README
- Related resources: OWASP Web Shell Detection Guide
