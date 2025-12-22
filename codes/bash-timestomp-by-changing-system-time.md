---
id: e55f35d6-0337-4499-bae7-207e8343aefd
name: bash-timestomp-by-changing-system-time
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:17.808936+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - timestomping
  - system-time-manipulation
validated: true
---

# bash-timestomp-by-changing-system-time

## Code

```bash
ORIG_TIME=$(date)
date -s "2022-10-31 23:59:59"
touch -a -m "example"
date -s "${ORIG_TIME}"
```

## Description

This Bash script temporarily alters the system clock to a past date, updates the timestamps of a file using `touch`, and then restores the original system time. It enables creating files that appear historically dated, useful for evading timeline forensics in root-access scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ORIG_TIME | Captures current system time for restoration | Mon Oct  2 12:00:00 UTC 2023 |
| 2022-10-31 23:59:59 | Target historical date/time | Any valid date string |
| example | Target file name | payload.sh |

## Usage

Execute as root on a Linux target during post-exploitation to timestomp files without direct timestamp tools. Integrate into scripts for automated payload deployment where file age must match system history. Start with `sudo bash script.sh` after substituting parameters.

## Detection

- Kernel logs (/var/log/kern.log) or auditd events showing `settimeofday` syscalls.
- NTP daemon logs indicating time drifts or manual adjustments.
- File system anomalies where ctime doesn't match mtime/atime due to system-wide changes.
- Process monitoring for `date -s` executions.

## Related

- [[procedures/Linux-Timestomping-Evasion]]
