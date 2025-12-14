---
id: proc-uuid-004
name: Verify-RCE-Execution-via-Logs-and-File-Creation
tags:
  - verification
  - rce
  - logs
  - airflow
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:36.838Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Verify-RCE-Execution-via-Logs-and-File-Creation

## Summary

This procedure validates the success of the RCE by inspecting Airflow task logs for command execution traces and confirming filesystem changes on the worker host.

## Description

After triggering the DAG, logs will show the bash_command expansion including the injected 'touch' command. Direct access to the worker (e.g., via SSH) allows checking for /tmp/thisistest, proving OS-level execution. This confirms the vulnerability's exploitability and potential for further payload escalation.

## Requirements

1. Access to Airflow logs (UI or file system)
2. SSH or console access to the Airflow worker host
3. DAG run ID from trigger step

## Defense

Defensive measures and detection strategies:

- Centralize logging with tools like ELK for anomaly detection in bash executions
- File integrity monitoring on worker hosts for unexpected creations
- Audit DAG runs for configs with suspicious strings

## Objectives

1. Review logs for evidence of injected command
2. Validate side effects like file creation
3. Assess execution permissions and scope

## Instructions

### Step 1: Check Airflow Logs

**Context**: Locate task logs in the UI for the triggered DAG run.

No command required; in Airflow UI, go to the DAG run, select the task, and view logs.

> Look for output showing 'touch /tmp/thisistest' execution and find command results.

### Step 2: Verify Filesystem on Worker

**Context**: Confirm the injected command's effect.

No command required; SSH to worker and run ls /tmp/thisistest.

> File existence indicates successful RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- rce
- logs
- airflow
