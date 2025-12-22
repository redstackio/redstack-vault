---
id: b934e239-ea9e-4256-bf37-3caa9d209737
name: List-of-Interesting-Linux-Files
type: code
language: text
verified: true
created_at: '2023-04-06T03:55:57.982824+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - file-list
validated: true
---

# List-of-Interesting-Linux-Files

## Code

```
/etc/issue
/etc/passwd
/etc/shadow
/etc/group
/etc/hosts
/etc/motd
/etc/mysql/my.cnf
/proc/[0-9]*/fd/[0-9]*   (first number is the PID, second is the filedescriptor)
/proc/self/environ
/proc/version
/proc/cmdline
/proc/sched_debug
/proc/mounts
/proc/net/arp
/proc/net/route
/proc/net/tcp
/proc/net/udp
/proc/self/cwd/index.php
/proc/self/cwd/main.py
/home/$USER/.bash_history
/home/$USER/.ssh/id_rsa
/run/secrets/kubernetes.io/serviceaccount/token
/run/secrets/kubernetes.io/serviceaccount/namespace
/run/secrets/kubernetes.io/serviceaccount/certificate
/var/run/secrets/kubernetes.io/serviceaccount
/var/lib/mlocate/mlocate.db
/var/lib/mlocate.db
```

## Description

This is a curated list of common interesting file paths on Linux systems that attackers check during enumeration. These files often contain system configuration, user data, network info, or secrets like tokens in containerized environments. Use it as a checklist to prioritize inspection in procedures like file enumeration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $USER | Current username for home directory paths | ubuntu |
| [0-9]* | PID placeholders in /proc paths | Actual process IDs |
| [0-9]* | File descriptor numbers | Actual FDs |

## Usage

In a Linux enumeration procedure, reference this list to guide cat or ls commands on accessible files. For example, after gaining shell access, systematically check /etc files first, then /proc for runtime info, and user homes for history or keys. Script it by looping over the list with a bash for-loop: for file in $(cat list.txt); do [ -r "$file" ] && cat "$file"; done.

## Detection

- Monitor access to sensitive paths via auditd rules on /etc/*, /proc/*, and /home/*
- Log anomalous reads of shadow files or Kubernetes secrets
- File access logs showing patterns of sequential checks on multiple config files

## Related

- [[procedures/Linux-File-Enumeration]]
- [[commands/cat-etc-passwd]]
