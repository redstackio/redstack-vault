---
tags:
  - command-injection
  - airflow
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/echo-run-id-and-dag-run]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.493Z'
sub_techniques: []
id: 1c5d7c7d-748c-4907-b665-c1a4114266d6
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
---
# Set-Malicious-run_id-for-Injection

## Summary

Inject a shell command into the run_id parameter using backticks to exploit Jinja templating in the BashOperator.

## Description

The vulnerability stems from unsanitized interpolation of {{ run_id }} in the bash_command: echo "run_id={{ run_id }} | dag_run={{ dag_run }}". Backticks in run_id trigger shell substitution, allowing arbitrary commands like touch to execute on the server.

## Requirements

1. Configuration modal open
2. Knowledge of shell metacharacters (backticks for substitution)
3. Target Airflow < 2.4.0

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs in Jinja templates (e.g., use safe filters)
- Disable shell metacharacter processing in operators
- Scan configs for suspicious patterns like backticks before processing

## Objectives

1. Craft payload exploiting templating
2. Set run_id to trigger injection
3. Ensure payload evades basic validation

## Instructions

### Step 1: Enter Payload in run_id

**Context**: Use backticks to inject command into the echo statement.

In the JSON config, set "run_id": "`touch /tmp/success`".

> This will substitute into [[commands/echo-run-id-and-dag-run]], executing the touch.

### Step 2: Validate Payload Format

**Context**: Confirm JSON is valid before submission.

Check for syntax errors in the modal.

> No errors; payload ready.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/echo-run-id-and-dag-run]]

## Tools Used


## Tags

- [[command-injection]]
- [[airflow]]
- [[payload-injection]]
