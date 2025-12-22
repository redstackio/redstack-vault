---
id: b5e9c804-c9ea-4944-bae8-b6e8dff6d8b2
name: LinEnum
type: tool
verified: true
created_at: '2019-08-28T21:17:20.688503+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - Enumeration
  - File System
  - Misconfiguration
url: 'https://github.com/rebootuser/LinEnum'
validated: true
---

# LinEnum

**Status**: Unverified

## Overview

LinEnum is a Bash script designed for automated enumeration on Linux and BSD systems. It performs comprehensive scans to identify potential vulnerabilities, misconfigurations, and points of interest for further investigation during security assessments, such as privilege escalation paths or system weaknesses.

## Description

LinEnum systematically gathers information across multiple categories to aid in offensive security operations. It is particularly useful in post-exploitation scenarios where an initial foothold has been gained, helping to map out the environment for deeper exploitation. The script runs locally on the target system and outputs findings in a structured format, highlighting anomalies like weak permissions, outdated software, or exposed sensitive files.

## Features

- Kernel Information: Enumerates kernel version, modules, and potential exploits.
- System Information: Collects details on architecture, hostname, processes, and services.
- User Information: Lists users, groups, sudo configurations, and cron jobs.
- Privileged Access: Checks for SUID/SGID binaries, capabilities, and PATH issues.
- Environmental Variables: Inspects environment for leaks or misconfigurations.
- Jobs and Services: Reviews running jobs, network connections, and scheduled tasks.
- Version Information: Gathers software versions for vulnerability assessment.
- Default/Weak Credentials: Scans for common weak passwords or default accounts.
- Notable Files and Folders: Identifies sensitive files like SSH keys, config files, and world-writable directories.

## Installation

### Requirements

- Bash shell (standard on Linux/BSD).
- Target system access (local execution required).
- No additional dependencies beyond core utilities.

### Install Commands

```bash
# Clone the repository
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh -O LinEnum.sh
# Or download via git
curl -s https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh > LinEnum.sh
chmod +x LinEnum.sh
```

On Kali Linux, it may be available via package managers, but manual download is recommended for the latest version.

## Basic Usage

```bash
./LinEnum.sh
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help and usage information |
| `-t <mode>` | Set thoroughness: 0 (Standard), 1 (Thorough with file timing), 2 (Thorough with file timing and web checks) |
| `-e` | Enable extended checks for additional enumeration |
| `-r <repo>` | Specify custom repository path for output |
| `-l` | Log output to file |

## Examples

### Example 1: Basic Usage

```bash
./LinEnum.sh
```

This runs the standard enumeration scan, outputting results to the console.

### Example 2: Advanced Usage

```bash
./LinEnum.sh -t 1 -e -l /tmp/linenum.log
```

This performs a thorough scan with extended checks and logs output to a file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery
- [[System Information Discovery]] System Information Discovery
- [[File and Directory Discovery]] File and Directory Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of LinEnum.sh in temporary directories or downloads.
- Bash process spawning with arguments like `-t 1` or script execution patterns.
- Unusual file reads (e.g., /etc/passwd, /proc, cron files) from a single process.
- Log entries for script execution in audit logs or process monitoring tools like Sysdig or auditd.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/enum4linux]]
- [[tools/linPEAS]]

## References

- Official GitHub Repository: https://github.com/rebootuser/LinEnum
- Related Resources: Offensive Security Enumeration Guides
