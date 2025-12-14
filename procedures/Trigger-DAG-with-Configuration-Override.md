---
tags:
  - airflow
  - dag-trigger
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
updated_at: '2025-12-14T17:23:54.505Z'
sub_techniques: []
id: 938e43e1-8ed0-4f96-8dc7-22715896cf25
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-DAG-with-Configuration-Override

## Summary

Initiate a DAG run with custom configuration to allow overriding parameters like run_id for injection.

## Description

Airflow's UI supports triggering DAGs with JSON config overrides, which is abused here to set a malicious run_id. This step opens the modal for payload input without executing anything yet.

## Requirements

1. Access to DAG detail page
2. Permissions to trigger DAGs
3. UI version supporting config overrides (standard in Airflow)

## Defense

Defensive measures and detection strategies:

- Validate config inputs server-side before templating
- Log all trigger attempts with config payloads
- Disable config overrides for sensitive DAGs

## Objectives

1. Open configuration interface for parameter manipulation
2. Prepare for payload insertion
3. Avoid immediate execution

## Instructions

### Step 1: Access Trigger Dropdown

**Context**: Locate the option for advanced triggering.

Click the "Trigger DAG" button and select "w/ config" from the dropdown.

> Modal dialog opens with JSON editor.

### Step 2: Prepare Config Field

**Context**: Ready the input for run_id override.

Ensure the modal shows fields for conf, including run_id.

> Empty JSON template appears for filling.

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
- [[dag-trigger]]
