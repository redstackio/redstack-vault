---
id: 1e3a1e8b-d828-4cdc-810a-40335e8b0a4d
name: ps
type: tool
verified: true
created_at: '2020-02-28T00:46:12.508465+00:00'
updated_at: '2023-05-30T19:54:31.775981+00:00'
commands:
  - '[[commands/ps-list-all-running-processes]]'
platforms:
  - Linux
tags:
  - Enumeration
  - process
validated: true
---

# ps

**Status**: ✓ Verified

## Overview

ps is a command-line utility in Unix-like operating systems that displays information about active processes. It is commonly used for process enumeration, monitoring system resource usage, and identifying running services or applications during security assessments or system administration.

## Description

The ps command provides snapshots of current processes and their status, including details like process ID (PID), user, CPU/memory usage, and command arguments. It supports various output formats (BSD, System V, GNU) and can filter processes based on user, terminal, or other criteria. In offensive security, ps is essential for discovering running services, identifying potential privilege escalation vectors, or verifying if specific processes are active after exploitation.

## Features

- Feature 1: Flexible output formatting with BSD-style (-aux) or System V-style (ps -ef) options.
- Feature 2: Filtering by user, PID, or process group to target specific processes.
- Feature 3: Integration with pipes and grep for quick searching of process lists.

## Installation

### Requirements

- Standard on most Unix-like systems; no additional dependencies.

### Install Commands

ps is typically pre-installed on Linux distributions. If missing:

```bash
# On Debian/Ubuntu (part of procps package)
apt update && apt install procps

# On Red Hat/CentOS/Fedora
yum install procps-ng  # or dnf install procps-ng on newer versions
```

## Basic Usage

```bash
ps --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -a | Select all processes except session leaders (BSD style). |
| -u | Display user-oriented format. |
| -x | Include processes without controlling ttys. |
| -f | Full-format listing (System V style). |
| -e | Show all processes (System V style). |
| -o | Specify output format (e.g., -o pid,ppid,cmd). |

## Examples

### Example 1: Basic Usage

```bash
ps aux
```

This lists all processes in user-oriented format.

### Example 2: Advanced Usage

```bash
ps -eo pid,ppid,cmd,user | grep apache
```

This shows PID, parent PID, command, and user for processes matching 'apache'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

- Detection method 1: Process auditing tools like auditd can log executions of ps, though it's a standard system command and often whitelisted.
- Detection method 2: Monitor for unusual piping with grep or awk on ps output, which may indicate targeted enumeration (e.g., via Sysmon or EDR tools).

## Related Procedures

No related procedures linked yet.

## Related Tools

- [[tools/top]]
- [[tools/htop]]

## References

- Official man page: man ps
- GNU Coreutils documentation: https://www.gnu.org/software/coreutils/ps
