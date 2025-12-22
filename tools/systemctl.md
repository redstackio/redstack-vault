---
id: 246d45f2-d6e1-4212-b6f9-7757243084d1
type: tool
verified: true
created_at: '2020-02-19T23:08:13.147049+00:00'
updated_at: '2023-05-30T19:45:23.367846+00:00'
platforms:
  - Linux
tags:
  - administrator
  - Operating Systems
  - persistence
  - systemd
commands:
  - '[[commands/systemctl-enable-and-start-service-by-file]]'
url: 'https://www.freedesktop.org/software/systemd/man/systemctl.html'
category: Post-Exploitation
validated: true
---

# systemctl

**Status**: ✓ Verified

## Overview

systemctl is the primary command-line utility for controlling the systemd system and service manager, which is the default init system on most modern Linux distributions (post-2015). It allows administrators and attackers to introspect, start, stop, enable, disable, and manage services, units, and system states. In security contexts, it is commonly used for persistence mechanisms by creating or modifying services to execute malicious payloads on boot or on-demand.

## Description

systemd manages system resources, services, and dependencies in a declarative way via unit files (e.g., .service files). systemctl provides an interface to these operations, requiring root privileges for most modifications. Attackers with elevated access can abuse it for privilege escalation or persistence by enabling custom services that run arbitrary code. It supports querying system status, reloading configurations, and masking units to prevent startup.

## Installation

### Requirements

- A Linux distribution using systemd (e.g., Ubuntu 16.04+, CentOS 7+, Fedora).
- Root or sudo access for service management.

### Install Commands

systemctl is bundled with systemd and installed by default on supported distributions. If needed on minimal systems:

```bash
# On Debian/Ubuntu
sudo apt update && sudo apt install systemd

# On RHEL/CentOS/Fedora
sudo dnf install systemd  # or yum on older versions
```

No additional installation is typically required as it comes pre-installed.

## Basic Usage

```bash
systemctl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help for systemctl |
| `--version` | Show version information |
| `--user` | Operate on user-specific units (no root needed) |
| `--all` | Show all units, including inactive ones |
| `--state=active` | Filter by state (active, inactive, failed) |

## Examples

### Example 1: Basic Usage - List Active Services

```bash
systemctl list-units --type=service --state=active
```

### Example 2: Advanced Usage - Start and Enable a Service

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Service]] Create or Modify System Process (Systemd Service)
- [[Windows Command Shell]] Windows Command Shell (analogous for Linux scripting via services)

### Tactics

- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor sudo/systemctl logs for unauthorized service creations/enables (e.g., /var/log/auth.log, journalctl).
- Audit new .service files in /etc/systemd/system/ or /lib/systemd/system/ for malicious payloads.
- Use tools like auditd to watch systemctl executions and file modifications.
- Check for unexpected services via `systemctl list-unit-files --type=service`.

## Related Commands

- [[commands/systemctl-enable-and-start-service-by-file]]

## References

- Official documentation: https://www.freedesktop.org/software/systemd/man/systemctl.html
- systemd unit file syntax: https://www.freedesktop.org/software/systemd/man/systemd.service.html
