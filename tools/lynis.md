---
id: 5f468925-8c11-40a2-b09a-a77785e78313
type: tool
verified: true
created_at: '2019-08-28T21:17:31.144393Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - auditing
  - hardening
  - compliance
url: 'https://cisofy.com/lynis/'
validated: true
---

# lynis

**Status**: Unverified

## Overview

Lynis is an open-source security auditing and hardening tool designed for Unix and Linux-based systems. It performs extensive system scans to identify vulnerabilities, configuration weaknesses, and compliance issues, providing actionable recommendations to improve security posture.

## Description

Lynis scans systems by executing hundreds of tests across categories like authentication, networking, file permissions, and software management. It aligns with standards such as CIS benchmarks, NIST, and PCI-DSS. Results include warnings, suggestions, and links to remediation controls. While primarily used for defensive auditing, it can inform offensive security assessments by revealing potential entry points.

## Features

- Comprehensive test library covering kernel, services, and applications
- Customizable profiles for specific environments (e.g., servers, containers)
- Report generation in text, HTML, or JSON formats
- Plugin support for extending functionality
- Non-intrusive scanning with no system modifications

## Installation

### Requirements

- Unix/Linux operating system
- Root or sudo access for full scans
- Perl (usually pre-installed)

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install lynis

# On CentOS/RHEL/Fedora
sudo yum install epel-release && sudo yum install lynis
# Or for newer versions: sudo dnf install lynis

# Manual install from GitHub
wget https://downloads.cisofy.com/lynis/lynis-2.6.10.tar.gz
sudo tar -xzf lynis-2.6.10.tar.gz -C /usr/local/
sudo ln -s /usr/local/lynis/lynis /usr/local/bin/lynis
```

## Basic Usage

```bash
lynis --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-V, --version` | Display version information |
| `-c, --check-all` | Run all available tests |
| `-Q, --quick` | Perform a quick scan |
| `-o, --output` | Specify output format (screen, file, json) |

## Examples

### Example 1: Basic Usage

```bash
lynis audit system
```

This runs a full system audit and displays results on screen.

### Example 2: Advanced Usage

```bash
lynis audit system --profile /path/to/custom-profile --output json:report.json
```

Audits using a custom profile and saves output to JSON.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software Discovery]] Software Discovery (for identifying installed software during audits)
- [[System Information Discovery]] System Information Discovery (gathering system details)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'lynis' executions
- Log entries from /var/log/lynis.log
- File system changes in /usr/local/lynis if manually installed
- Network activity if remote profiles are fetched

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/openvas]]
- [[tools/nessus]]

## References

- Official website: https://cisofy.com/lynis/
- GitHub repository: https://github.com/CISOfy/lynis
- Documentation: https://cisofy.com/documentation/lynis/
