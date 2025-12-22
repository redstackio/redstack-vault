---
type: command
executor: bash
data: sudo -l
output: null
platforms:
  - Linux
tags:
  - privilege-escalation
  - enumeration
verified: true
validated: true
---

# sudo-list-privileges

## Command

```bash
sudo -l
```

## Description

This command lists the sudo privileges and allowed commands for the current user, helping identify potential privilege escalation paths by revealing misconfigured rules in /etc/sudoers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | List the user's current sudo privileges | Yes |

## Examples

### Basic Usage

```bash
sudo -l
```

### Advanced Usage

```bash
sudo -l -U username
```

This variant lists privileges for a specific user (requires appropriate permissions).

## Expected Output

Description of what output to expect when the command runs successfully.

Example output:

```
User joe may run the following commands on hostname:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/perl
```

This indicates the user can run any command as any user, and specifically perl as root without a password.

## Related

- [[procedures/Abuse-Sudo-Rules-for-Privesc]]
- [[tools/sudo]]
