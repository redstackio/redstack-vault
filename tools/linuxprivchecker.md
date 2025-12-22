---
id: b83d3105-5ed2-4c80-b2d7-58d67644c867
name: linuxprivchecker
type: tool
verified: true
created_at: '2020-02-22T02:53:00.013490+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - Enumeration
  - File System
  - Known Vulnerability
  - Misconfiguration
url: 'https://github.com/mzet-/linuxprivchecker'
commands:
  - '[[commands/linuxprivchecker-run-privilege-escalation-scan]]'
validated: true
---

# linuxprivchecker

**Status**: ✓ Verified

## Overview

linuxprivchecker is a Python script designed for local privilege escalation enumeration on Linux systems. It scans the target filesystem for common vectors such as world-writable files and directories, misconfigurations in services and cron jobs, clear-text credentials, and potential kernel exploits. The tool is particularly useful during post-exploitation phases to identify paths to root access. Note that the built-in exploit suggester relies on signatures last updated in 2016, making it less effective for modern systems but still valuable for legacy environments.

## Description

This tool performs a comprehensive check of the local Linux environment to uncover privilege escalation opportunities. It gathers system information like kernel version, hostname, and OS details, then enumerates potential weaknesses including SUID binaries, writable system files, scheduled tasks with elevated privileges, and environment variables that could lead to escalation. Users transfer and execute the script directly on the compromised host for stealthy enumeration without relying on external network calls.

## Features

- System information gathering (kernel, OS, users, processes)
- Enumeration of SUID/SGID binaries and capabilities
- Detection of world-writable files, directories, and scripts
- Identification of misconfigured services, cron jobs, and PATH variables
- Search for clear-text passwords in common locations
- Kernel exploit suggestion based on version (outdated database)
- Checks for NFS mounts, LDAP configs, and sudoers misconfigurations

## Installation

### Requirements

- Python 2.7 or 3.x (compatible with both)
- Target access (local execution on compromised Linux host)
- No additional dependencies; self-contained script

### Install Commands

Transfer the script to the target system via SCP, wget, or manual upload:

```bash
# On attacker machine: Clone the repository
mkdir -p ~/tools
cd ~/tools
git clone https://github.com/mzet-/linuxprivchecker.git

# Transfer to target (example using SCP, replace with actual IPs/paths)
scp linuxprivchecker.py user@target-ip:/tmp/

# On target: Make executable if needed
chmod +x /tmp/linuxprivchecker.py
```

For air-gapped environments, download and manually copy the .py file.

## Basic Usage

```bash
python linuxprivchecker.py
```

Run the script directly on the target without arguments for a full scan. Output is printed to stdout and can be redirected to a file for later analysis.

### Common Options

| Option | Description |
|--------|-------------|
| None | The script has no command-line options; it performs all checks automatically upon execution |

## Examples

### Example 1: Basic Usage

Execute on the target to generate the enumeration report:

```bash
python /tmp/linuxprivchecker.py > privcheck_output.txt
```

### Example 2: Quick Check in Memory

Run without saving output for immediate review:

```bash
python linuxprivchecker.py
```

## Related Commands

- [[commands/linuxprivchecker-run-privilege-escalation-scan]]

## References

- Official GitHub Repository: https://github.com/mzet-/linuxprivchecker
- Original Author: mzet-
