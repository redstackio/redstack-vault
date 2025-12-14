---
url: 'https://github.com/whotwagner/logrotten'
tags:
  - exploit
  - race-condition
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.943Z'
id: 83928cf8-afbc-41ac-96e3-095bea1118d0
validated: true
submitted: true
---
# logrotten

**Status**: Unverified

## Overview

Logrotten is a custom exploit tool for winning time-of-check-to-time-of-use (TOCTOU) races in logrotate by monitoring log files, renaming directories, and creating symlinks during the rotation process run as root.

## Description

Designed for scenarios like GitLab where log dirs are writable by non-root users but rotation elevates to root. It targets specific logs, waits for rotation signals, and exploits the brief window to redirect rotated files to sensitive locations like /etc/. Commonly used in privilege escalation tests on Linux systems with misconfigured logrotate.

## Features

- Feature 1: Monitors logrotate invocations in real-time
- Feature 2: Automates directory rename and symlink creation
- Feature 3: Targets specific log paths with -c flag

## Installation

### Requirements

- gcc for compilation
- Linux with logrotate

### Install Commands

```bash
# Clone and compile
git clone https://github.com/whotwagner/logrotten.git /tmp/logrotten
cd /tmp/logrotten
gcc -o logrotten logrotten.c
```

## Basic Usage

```bash
./logrotten --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -c, --config | Target log file path |
| -h, --help | Show help |

## Examples

### Example 1: Basic Usage

```bash
./logrotten -c /var/log/app/something.log
```

### Example 2: Advanced Usage

```bash
./logrotten -c /path/to/log -t /sensitive/dir
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### Tactics

- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for rapid dir renames/symlinks in /var/log/ via inotify
- Process listings showing logrotten binary
- Audit logrotate executions for anomalies

## Related Procedures

- [[procedures/Compile-and-Execute-Logrotten-Exploit]]

## Related Tools

- [[tools/nc]]
- [[tools/gcc]]

## References

- GitHub repo: https://github.com/whotwagner/logrotten
- HackerOne report: https://hackerone.com/reports/578119
