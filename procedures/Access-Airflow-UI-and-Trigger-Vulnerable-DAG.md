---
id: proc-uuid-002
name: Access-Airflow-UI-and-Trigger-Vulnerable-DAG
tags:
  - web-access
  - airflow
  - dag-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:36.848Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Airflow-UI-and-Trigger-Vulnerable-DAG

## Summary

This procedure covers logging into the Apache Airflow web UI as an authenticated user and navigating to trigger the vulnerable 'docker_sample_copy_data' DAG with a configuration payload.

## Description

The Airflow UI exposes an endpoint for triggering DAGs with custom JSON configs. An authenticated user can access this to prepare for payload injection. The target is the DAGs view at port 8080, requiring valid credentials but no special permissions beyond DAG execution rights. Successful access positions the attacker to submit the exploit payload.

## Requirements

1. Valid Airflow user credentials
2. Network access to Airflow webserver on port 8080
3. Web browser for UI interaction

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) to limit DAG triggering
- Monitor UI logs for frequent DAG triggers by users
- Use IP whitelisting for Airflow UI access

## Objectives

1. Authenticate and reach the DAGs management interface
2. Select and prepare the vulnerable example DAG for execution
3. Load the config input form without errors

## Instructions

### Step 1: Log In to Airflow UI

**Context**: Authenticate to gain access to administrative functions.

No command required; visit http://target:8080 and enter credentials.

> Successful login redirects to the dashboard.

### Step 2: Navigate to DAGs and Select Target

**Context**: Locate the 'docker_sample_copy_data' DAG in the list.

No command required; click on DAGs menu, find 'docker_sample_copy_data', and select 'Trigger DAG w/ config'.

> Endpoint: http://target:8080/trigger?dag_id=docker_sample_copy_data loads the form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-access
- airflow
- dag-trigger
