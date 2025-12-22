---
id: 3736fab7-8a0c-421f-8b5b-f388e2d50089
type: tool
verified: true
created_at: '2019-08-28T21:17:42.308534+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Solaris
  - HPUX
  - FreeBSD
tags:
  - privilege-escalation
  - post-exploitation
  - unix
  - linux
  - assessment
url: 'https://www.foofus.net/~dl/files/unix-privesc-check.tar.gz'
validated: true
---

# Unix-Privesc-Checker

**Status**: Unverified

## Overview

Unix-privesc-checker is a lightweight shell script designed for assessing local privilege escalation vulnerabilities on Unix-like systems. It scans for common misconfigurations that could allow an unprivileged user to gain elevated access to other users, root, or local applications such as databases. The tool is particularly useful in post-exploitation phases of penetration testing to identify escalation paths. It supports a variety of Unix platforms including Linux distributions, Solaris 9, HPUX 11, and FreeBSD 6.2, and performs better when run as root due to increased file access permissions.

## Description

The script operates by checking system configurations, file permissions, SUID binaries, cron jobs, writable files in critical paths, and other vectors commonly exploited for privilege escalation. It outputs findings in a readable format, highlighting potential vulnerabilities without exploiting them directly. As a single shell script, it requires no compilation or complex setup, making it ideal for quick assessments on compromised hosts. Common use cases include red team engagements, vulnerability assessments, and compliance audits for Unix environments.

## Features

- Checks for SUID/SGID binaries with insecure permissions
- Identifies writable system files and directories
- Scans for world-writable cron jobs and scheduled tasks
- Detects weak or default database configurations
- Examines PATH variables and environment misconfigurations
- Supports logging and output redirection for analysis
- Runs in standard or exhaustive modes for different assessment depths

## Installation

### Requirements

- Bash-compatible shell (standard on most Unix systems)
- Read access to system files (full access recommended when run as root)
- No additional dependencies; self-contained script

### Install Commands

Download and prepare the script:

```bash
# Download the tarball (adjust URL if needed)
wget https://www.foofus.net/~dl/files/unix-privesc-check.tar.gz

tar -xzf unix-privesc-check.tar.gz
cd unix-privesc-check

# Make the script executable
chmod +x unix-privesc-check
```

For Kali Linux or Ubuntu:

```bash
# Pre-built packages may not exist; use manual download as above
apt update
# No specific package; manual install recommended
```

## Basic Usage

```bash
./unix-privesc-check
```

This runs the script in default mode, performing standard checks.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and usage |
| `-v, --version` | Show version information |
| `-s` | Run standard checks (default) |
| `-a` | Run all possible checks (more comprehensive but slower) |
| `-l logfile` | Log output to specified file |
| `-o outputfile` | Redirect findings to a file |
| `-d` | Daemon mode (background execution, limited use) |
| `-u user` | Check for escalations to specific user |
| `-g group` | Check group-based escalations |
| `-p path` | Specify custom path for checks |

## Examples

### Example 1: Basic Usage

Run standard privilege escalation checks on the local system:

```bash
./unix-privesc-check -s
```

### Example 2: Advanced Usage

Perform exhaustive checks and log results:

```bash
./unix-privesc-check -a -l /tmp/privesc_log.txt -o /tmp/results.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Process Discovery]] Process Discovery
- [[System Information Discovery]] System Information Discovery

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of the script file (unix-privesc-check) in temporary or user directories
- Execution of shell scripts with privilege escalation keywords in process lists (ps aux | grep privesc)
- Log entries for file permission checks or SUID scans in audit logs
- Unusual read attempts on system configuration files by non-root processes
- Network downloads of the tool's tarball from known sources

## Related Commands

- [[commands/unix-privesc-checker-run-standard]]
- [[commands/unix-privesc-checker-run-all-checks]]

## References

- Official download: https://www.foofus.net/~dl/files/unix-privesc-check.tar.gz
- GitHub mirror: https://github.com/vadim-hunter/Detection-ML-TF/tree/master/0_%20DarkSide/Attack%20Tools/Unix-Linux/unix-privesc-check
- Related tool: LinPEAS for Linux-specific checks
