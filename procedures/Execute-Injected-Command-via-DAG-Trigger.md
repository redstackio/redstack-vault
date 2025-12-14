---
tags:
  - rce
  - airflow
  - command-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/touch-success-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:54.485Z'
sub_techniques: []
id: 07c7c402-380b-424d-acf0-6b346550701c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-Injected-Command-via-DAG-Trigger

## Summary

Submit the DAG trigger to run the injected command, achieving RCE on the Airflow server.

## Description

Upon triggering, the BashOperator executes the templated command with the malicious run_id, performing shell substitution and running the injected payload. This grants arbitrary OS command execution with the privileges of the Airflow worker process.

## Requirements

1. Malicious config set in modal
2. Permissions to trigger and view logs
3. Server access for verification (optional, via SSH)

## Defense

Defensive measures and detection strategies:

- Run Airflow workers in isolated environments (e.g., containers)
- Monitor task logs for unexpected command outputs
- Implement command whitelisting in operators

## Objectives

1. Initiate DAG execution
2. Confirm RCE via file creation or logs
3. Validate impact without further escalation

## Instructions

### Step 1: Submit Trigger

**Context**: Start the DAG run to process the payload.

Click "Trigger" in the modal.

> DAG run ID generated; tasks queue.

### Step 2: Monitor Execution and Verify

**Context**: Check logs for command output and proof.

View task logs in UI; verify /tmp/success exists using [[commands/touch-success-file]] impact.

> Logs show echo output; file created confirms RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/touch-success-file]]

## Tools Used


## Tags

- [[rce]]
- [[airflow]]
- [[command-execution]]
