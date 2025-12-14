---
tags:
  - airflow
  - umask
  - preparation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/umask-0]]'
  - '[[commands/cd-to-scheduler-logs]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:09.514Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 983b67c9-8afb-4d98-9890-79282410d386
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Prepare-Airflow-Environment-and-Set-Umask

## Summary

This procedure sets an insecure umask to simulate Apache Airflow's daemon mode vulnerability and navigates to the scheduler logs directory, preparing the environment for symlink-based exploitation.

## Description

In Apache Airflow daemon mode, components inherit a umask of 0, creating world-writable files and directories in the home path. This procedure explicitly sets umask 0 (for PoC) and changes to the logs directory (/home/airflow/logs/scheduler/latest/native_dags/example_dags), where logs are generated and exploitable. Prerequisites include local shell access on the Airflow host and knowledge of the $TARGET path (e.g., /home/airflow). Expected outcome: Environment ready for file manipulation without permission denials.

## Requirements

1. Local shell access to the target Linux host running Airflow
2. Environment variable $TARGET set to Airflow home (e.g., export TARGET=/home/airflow)
3. Airflow services running in daemon mode

## Defense

Defensive measures and detection strategies:

- Set explicit umask 0022 in Airflow startup scripts to mask write permissions
- Monitor file creation in logs directories for unexpected symlinks using auditd or inotify
- Run Airflow processes with minimal privileges and containerization (e.g., Docker with read-only volumes)

## Objectives

1. Ensure world-writable permissions for exploitation simulation
2. Position in the correct directory for log manipulation
3. Avoid permission errors in subsequent steps

## Instructions

### Step 1: Set Insecure Umask

**Context**: Mimics the automatic umask 0 in daemon mode, allowing full permissions on new files.

**Command** ([[commands/umask-0]]):
```bash
umask 0
```

> Sets the file creation mask to 0, making new files world-readable/writable/executable. Expected output: No output; verify with `umask` showing 0000.

### Step 2: Navigate to Logs Directory

**Context**: Moves to the scheduler's log path where world-writable example_dags logs reside.

**Command** ([[commands/cd-to-scheduler-logs]]):
```bash
cd $TARGET/logs/scheduler/latest/native_dags/example_dags
```

> Changes working directory to the exploitable path. Expected output: No output; verify with `pwd`.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- [[commands/umask-0]]
- [[commands/cd-to-scheduler-logs]]

## Tools Used

- None

## Tags

- [[airflow]]
- [[umask]]
- [[preparation]]
