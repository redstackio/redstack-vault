---
tags:
  - scheduler
  - restart
  - execution
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/os-system-id]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:09.500Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4022c252-17dc-42d3-b103-f2ee661e6b95
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Trigger-Airflow-Scheduler-Restart-for-Execution

## Summary

This procedure restarts the Airflow scheduler to force processing of the injected DAG, executing the malicious code and achieving RCE as the Airflow user.

## Description

The scheduler in daemon mode periodically scans DAGs; restarting triggers immediate parse and execution of poc.py, running the os.system command. No direct command for restart in PoC, but uses service management. Target: Airflow services. Prerequisites: Malicious DAG injected. Expected outcome: Command execution, output in /tmp/pwned confirming priv esc.

## Requirements

1. Root or service control access to restart scheduler
2. Airflow installed with systemd/supervisor
3. /tmp writable

## Defense

Defensive measures and detection strategies:

- Disable daemon mode or use supervised restarts with validation
- Audit scheduler restarts and DAG parses for anomalies
- Run scheduler in isolated environment (e.g., non-root user, no shell access)

## Objectives

1. Initiate DAG processing to trigger payload
2. Verify RCE via output file
3. Escalate privileges if Airflow has elevated access

## Instructions

### Step 1: Restart Scheduler

**Context**: Restarts service to process new DAGs.

**Command** (systemctl restart):
```bash
sudo systemctl restart airflow-scheduler
```

> Restarts daemon. Expected output: Service status active.

### Step 2: Verify Execution

**Context**: Checks for RCE output from injected command.

**Command** ([[commands/os-system-id]]):
```bash
cat /tmp/pwned
```

> Displays id output. Expected output: uid=1000(airflow) gid=1000(airflow)...

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Unix Shell]] Unix Shell
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- [[commands/os-system-id]]

## Tools Used

- None

## Tags

- [[scheduler]]
- [[restart]]
- [[Execution]]
