---
type: command
executor: bash
data: >-
  ls -la /etc/ | grep cron; ls -la /etc/cron*; cat /etc/crontab 2>/dev/null; ls
  -alh /var/spool/cron/ 2>/dev/null; crontab -l 2>/dev/null
platforms:
  - Linux
tags:
  - enumeration
  - cron
verified: true
validated: true
---

# enumerate-cron-jobs-and-directories

## Command

```bash
ls -la /etc/ | grep cron; ls -la /etc/cron*; cat /etc/crontab 2>/dev/null; ls -alh /var/spool/cron/ 2>/dev/null; crontab -l 2>/dev/null
```

## Description

This command chain enumerates cron-related directories, the system crontab, user spool, and current user crontab to identify scheduled jobs and their permissions for potential privilege escalation vectors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Chained built-in bash commands; no arguments needed | N/A |

## Examples

### Basic Usage

```bash
ls -la /etc/ | grep cron; ls -la /etc/cron*; cat /etc/crontab 2>/dev/null; ls -alh /var/spool/cron/ 2>/dev/null; crontab -l 2>/dev/null
```

### Advanced Usage

Run as different user if possible: su - user -c 'crontab -l'

## Expected Output

Directory listings and file contents, e.g.:
total 64
drwxr-xr-x 2 root root 4096 Apr 10 12:00 cron.d
drwxr-xr-x 2 root root 4096 Apr 10 12:00 cron.daily
# /etc/crontab
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
...
crontab: no crontab for user

## Related

- [[procedures/Linux-Privilege-Escalation-via-Scheduled-Tasks]]
- [[commands/view-cron-access-control-files]]
