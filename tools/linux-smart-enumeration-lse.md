---
id: 847e65de-9f09-4fce-88fa-0d8d7f173cef
name: linux-smart-enumeration-lse
type: tool
verified: true
created_at: '2019-08-28T21:17:37.823444+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/lse-basic-enumeration-scan]]'
platforms:
  - Linux
tags:
  - '[[Enumeration]]'
  - '[[Linux]]'
url: 'https://github.com/diego-treitos/linux-smart-enumeration'
validated: true
---

# linux-smart-enumeration-lse

**Status**: Unverified

## Overview

Linux Smart Enumeration (LSE) is a bash script designed for local security enumeration on Linux systems. It gathers relevant information about the system's security posture, including users, sudo configurations, services, cron jobs, and potential privilege escalation vectors. LSE is particularly useful during post-exploitation phases to quickly identify misconfigurations and attack paths on compromised Linux hosts.

## Description

LSE automates the collection of system information that could reveal vulnerabilities or escalation opportunities. It categorizes output into sections like users, sudo, services, cron, and networking, making it easier to spot interesting findings without manual scripting. The tool supports three verbosity levels (-l 1 for basic, -l 2 for medium, -l 3 for full) to control the depth of enumeration, allowing users to start with a high-level overview and drill down as needed. It runs locally on the target system and can prompt for the current user's password to access restricted information.

## Features

- **Modular Enumeration**: Covers users, groups, sudoers, cron jobs, services, filesystem permissions, networking, and more.
- **Verbosity Levels**: -l 1 (basic info), -l 2 (includes password-protected checks), -l 3 (comprehensive, including historical data).
- **Color-Coded Output**: Uses indicators like [!] for critical findings, [*] for potential issues, and [i] for informational.
- **Password Integration**: Optionally uses provided password for deeper checks (e.g., sudo without password).
- **Skip Options**: Can skip sections with -s flag for focused scans.

## Installation

### Requirements

- Bash shell (standard on Linux)
- Git (for cloning)
- Target access (local execution on Linux host)

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/diego-treitos/linux-smart-enumeration.git

# Navigate to the directory
cd linux-smart-enumeration

# Make the script executable
chmod +x lse.sh

# Optional: Copy to a system path for easier access
sudo cp lse.sh /usr/local/bin/lse
```

For air-gapped environments, download the lse.sh script manually and transfer it to the target via SCP or other means.

## Basic Usage

```bash
./lse.sh -l 1
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l <level>` | Set verbosity level (1: basic, 2: medium, 3: full) |
| `-p <password>` | Provide current user password for restricted checks |
| `-s <section>` | Skip specific sections (e.g., -s net for networking) |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Run a level 1 scan without password prompts:

```bash
./lse.sh -l 1
```

### Example 2: Advanced Usage

Perform a full scan with password for deeper insights:

```bash
./lse.sh -l 3 -p "userpassword"
```

### Example 3: Skip Networking Section

```bash
./lse.sh -l 2 -s net
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Process Discovery]] Process Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of lse.sh in /tmp or user directories (check process listings with ps aux | grep lse).
- Unusual file reads (e.g., /etc/sudoers, /etc/passwd) via auditd or sysdig.
- Console output patterns matching LSE's section headers (e.g., "=====( users )=====") in logs.
- Network tools like Wireshark for any outbound connections if combined with other tools.

## Related Procedures

- [[procedures/Linux-Local-Enumeration]]
- [[procedures/Privilege-Escalation-Check]]

## Related Tools

- [[tools/linPEAS]]
- [[tools/LinEnum]]

## References

- Official GitHub: https://github.com/diego-treitos/linux-smart-enumeration
- Related resources: OSCP enumeration guides, HackTricks Linux priv-esc section
