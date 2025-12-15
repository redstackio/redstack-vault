---
tags:
  - airflow
  - dag-selection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.516Z'
sub_techniques: []
id: 1dcf130d-7c3e-4fb0-af4f-f2736bdf341a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Select-Example-Bash-Operator-DAG

## Summary

This procedure involves selecting the vulnerable example_bash_operator DAG from the Airflow UI to set up for exploitation.

## Description

The example_bash_operator.py DAG contains the BashOperator with unsanitized Jinja templating for run_id, enabling command injection. Selecting this DAG positions the attacker to trigger it with a malicious payload. This step is UI-based and requires no additional tools.

## Requirements

1. Authenticated session in Airflow UI
2. example_bash_operator DAG loaded and enabled in Airflow
3. Permissions to view DAG details

## Defense

Defensive measures and detection strategies:

- Disable or remove example DAGs in production
- Log all DAG views and selections
- Use RBAC to limit DAG access to necessary users

## Objectives

1. Isolate the target DAG for triggering
2. View DAG details without execution
3. Confirm vulnerability presence via UI

## Instructions

### Step 1: Locate DAG in List

**Context**: Identify the specific vulnerable DAG among others.

Scroll or search for "example_bash_operator" in the DAGs list.

> DAG entry highlights on hover.

### Step 2: Open DAG Detail View

**Context**: Access trigger options and configuration.

Click on the DAG name to load its graph and history.

> Detail page shows task structure, including the vulnerable BashOperator.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[airflow]]
- [[dag-selection]]
