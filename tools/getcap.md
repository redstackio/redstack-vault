---
id: 6d9374cc-5032-427c-bf14-7e897f14be19
name: getcap
type: tool
verified: true
created_at: '2020-02-19T06:33:14.866598+00:00'
updated_at: '2023-05-30T19:58:15.048012+00:00'
commands:
  - '[[commands/getcap-recursive-list-capabilities]]'
platforms:
  - Linux
tags:
  - '[[Enumeration]]'
  - '[[Permissions]]'
validated: true
---

# getcap

**Status**: ✓ Verified

## Overview

getcap is a Linux utility for displaying the name and capabilities of specified files or directories. It is particularly useful in security assessments for identifying files with extended privileges via Linux capabilities, which can be leveraged for privilege escalation by allowing specific privileged operations without full root access. Common use cases include enumerating system binaries for abuse potential during penetration testing.

## Description

Linux capabilities provide a fine-grained alternative to the traditional all-or-nothing root privilege model, dividing privileges into smaller, atomic units (e.g., cap_net_raw for raw network access). getcap queries the filesystem to reveal these capabilities on executables, helping attackers or testers spot misconfigurations like setuid-like behavior without the risks of setuid binaries. For more details on capabilities, refer to the man page: http://man7.org/linux/man-pages/man7/capabilities.7.html.

## Features

- Display capabilities for individual files or directories
- Recursive searching to scan entire filesystems for capability-enabled files
- Support for POSIX.1e capabilities on capability-aware kernels (Linux 2.2+)
- Integration with tools like find or scripts for automated enumeration

## Installation

### Requirements

- Linux kernel with capability support (standard since 2.2)
- libcap2 package or equivalent

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install libcap2-bin

# On Kali Linux (often pre-installed)
sudo apt install libcap2-bin

# On CentOS/RHEL/Fedora
sudo yum install libcap  # or dnf install libcap on newer versions
```

## Basic Usage

```bash
getcap --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -r, --recursive | Recursively list capabilities starting from the given directory |
| -v, --verbose | Provide verbose output |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Check capabilities on a specific file:

```bash
ggetcap /usr/bin/ping
```

### Example 2: Advanced Usage

Recursively search the root directory (as shown in related command):

```bash
ggetcap -r / 2>/dev/null | grep cap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation (identifying capability abuse)
- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery
- [[Privilege Escalation]] Privilege Escalation

## Detection

- Monitor execution of getcap in process logs (e.g., via auditd or Sysmon equivalents on Linux)
- Look for recursive searches from root (e.g., getcap -r /) in command-line auditing
- Capabilities themselves are visible in /proc/<pid>/status, but tool usage may indicate enumeration activity

## Related Procedures

- Procedures using this tool for Linux privilege escalation checks

## Related Tools

- [[tools/find]] (for SUID/SGID enumeration)
- [[lsattr]] (for immutable attributes)

## References

- Official man page: http://man7.org/linux/man-pages/man1/getcap.1.html
- Capabilities documentation: http://man7.org/linux/man-pages/man7/capabilities.7.html
