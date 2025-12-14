---
id: proc-uuid-003
name: Submit-Malicious-Payload-to-Inject-Commands
tags:
  - payload-injection
  - command-injection
  - rce
  - airflow
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/find-directory-with-injected-touch-command]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:36.843Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Submit-Malicious-Payload-to-Inject-Commands

## Summary

This procedure exploits the command injection by submitting a JSON payload with shell metacharacters in the 'source_location' parameter, causing arbitrary command execution during DAG runtime.

## Description

The vulnerability stems from Jinja2 rendering the user-supplied 'source_location' directly into the bash_command without escaping, allowing semicolon-separated injections. The payload {"source_location":";touch /tmp/thisistest;"} appends a 'touch' command to create a test file, demonstrating RCE. This executes on the Airflow worker with its OS permissions, potentially leading to full host compromise.

## Requirements

1. Authenticated session in Airflow UI
2. Access to the DAG trigger config form
3. Knowledge of shell injection techniques

## Defense

Defensive measures and detection strategies:

- Sanitize all params in DAG templates with Airflow's safe rendering
- Disable or remove example DAGs in production
- Log and alert on suspicious payloads containing shell metacharacters

## Objectives

1. Inject commands via JSON config to bypass validation
2. Trigger DAG execution to run the injected bash
3. Achieve initial RCE confirmation through side effects

## Instructions

### Step 1: Construct Payload

**Context**: Build JSON with injection in source_location.

No command required; prepare {"source_location":";touch /tmp/thisistest;"}.

> Semicolon separates the injected command from the original find.

### Step 2: Submit and Trigger

**Context**: Enter payload and initiate execution.

Execute the injection using [[commands/find-directory-with-injected-touch-command]] via the UI form, then click 'Trigger'.

```bash
find ;touch /tmp/thisistest; -type f -printf "%f\n" | head -1
```

> The command runs on the worker; monitor for DAG run ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/find-directory-with-injected-touch-command]]

## Tools Used


## Tags

- payload-injection
- command-injection
- rce
- airflow
