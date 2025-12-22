---
type: tool
description: >-
  A Linux command-line tool for monitoring process executions without root
  privileges, ideal for discovering cron jobs, user commands, and system
  activities during security assessments.
url: 'https://github.com/DominicBreuker/pspy'
verified: true
platforms:
  - Linux
tags:
  - process-monitoring
  - discovery
  - post-exploitation
  - account-monitoring
commands:
  - '[[commands/pspy-download-x86-64-binary]]'
  - '[[commands/pspy-run-process-monitoring]]'
validated: true
---

# pspy

**Status**: ✓ Verified

## Overview

pspy is a lightweight Linux command-line tool designed to monitor and snoop on running processes without requiring root permissions. It provides real-time visibility into process creations, including those triggered by cron jobs, other users, or system services, making it valuable for reconnaissance and post-exploitation in red team operations.

## Description

pspy operates by leveraging /proc filesystem monitoring to detect new process executions. It displays detailed information such as timestamps, command lines, PIDs, PPIDs, user IDs, and process hierarchies. This tool is particularly useful for identifying automated tasks (e.g., cron jobs that reveal credentials or perform backups) or lateral movement opportunities without alerting defenders through privileged operations. Supported on 32-bit and 64-bit architectures, with static binaries for easy deployment.

## Features

- **No Root Required**: Monitors processes using unprivileged access to /proc.
- **Real-Time Output**: Streams process creation events as they occur.
- **Filtering Options**: Supports PID following (-pf), interval adjustments (-i), and timestamp inclusion (-t).
- **Portable Binaries**: Statically compiled, no dependencies needed.
- **Process Tree Visualization**: Shows parent-child relationships for spawned processes.

## Installation

### Requirements

- Linux system with wget or curl for download.
- No additional dependencies; static binary.

### Install Commands

Use the download command to fetch the binary:

```bash
[[commands/pspy-download-x86-64-binary]]
```

For ARM architecture, modify the URL to pspyarm:

```bash
wget https://github.com/DominicBreuker/pspy/releases/latest/download/pspyarm -O /tmp/pspy
```

After download, make executable:

```bash
chmod +x /tmp/pspy
```

## Basic Usage

Run the binary to start monitoring:

```bash
./pspy64
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and options. |
| `-p` | Print process details (default behavior). |
| `-i <seconds>` | Set monitoring interval (default 1 second). |
| `-t` | Include timestamps in output. |
| `-pf <PID>` | Follow processes spawned by a specific PID. |
| `-c` | Clear screen between updates. |
| `-l` | List all current processes initially. |

## Examples

### Example 1: Basic Usage

Start monitoring all new processes:

```bash
[[commands/pspy-run-process-monitoring]]
```

### Example 2: Advanced Usage

Monitor processes spawned by PID 1 (init/systemd) with timestamps:

```bash
./pspy64 -pf 1 -t
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery
- [[Scheduled Task]] Scheduled Task/Job: Scheduled Task

### Tactics

- [[Discovery]] Discovery
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of pspy binary in temporary directories (e.g., /tmp/pspy).
- Unusual reads from /proc filesystem by unprivileged processes.
- Process monitoring patterns in audit logs (e.g., via auditd).
- Network downloads from GitHub releases matching pspy signatures.
- YARA rules for the binary or behavioral detection of process enumeration without sudo.

## Related Procedures

No specific procedures linked yet. Consider creating a procedure for "Monitor Scheduled Tasks with pspy" under post-exploitation.

## Related Tools

- [[tools/procmon]] (Windows equivalent for process monitoring)
- [[tools/sysdig]] (Advanced system call tracing)

## References

- Official GitHub Repository: [https://github.com/DominicBreuker/pspy](https://github.com/DominicBreuker/pspy)
- Releases Page: [https://github.com/DominicBreuker/pspy/releases](https://github.com/DominicBreuker/pspy/releases)
