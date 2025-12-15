---
tags:
  - access-control-bypass
  - dag
  - source-code-leak
  - airflow
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:44.979Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 85ba6f3d-7fab-4db8-a264-2a59a71699a6
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Bypass-DAG-Permission-to-Access-Source-Code

## Summary

This procedure exploits a permission verification bypass in Apache Airflow (< 2.8.1) to retrieve the source code of DAGs that the authenticated user is not authorized to access, potentially exposing sensitive Python workflow code.

## Description

The vulnerability stems from inadequate permission checks in the DAG source code retrieval endpoint of the Airflow web UI/API. An authenticated user can directly request the code for any DAG by specifying its ID, bypassing RBAC restrictions. This occurs in the web interface or API, targeting Python-based DAG files stored in the Airflow environment. Prerequisites include an active session from authentication. Expected outcomes include full access to the DAG's Python source, revealing configurations, secrets, or logic that could aid further attacks.

## Requirements

1. Active authenticated session with limited DAG permissions
2. Knowledge of the target DAG's ID (e.g., from partial dashboard access or enumeration)
3. Access to the Airflow web UI or API endpoint

## Defense

Defensive measures and detection strategies:

- Upgrade to Apache Airflow 2.8.1 or later to patch the verification logic
- Implement endpoint-level access logging and anomaly detection for DAG code requests
- Use DAG-level encryption or obfuscation for sensitive code

## Objectives

1. Retrieve source code of unauthorized DAGs
2. Expose sensitive workflow details without triggering access denials
3. Analyze code for further vulnerabilities or secrets

## Instructions

### Step 1: Identify Target DAG

**Context**: Determine the ID of a restricted DAG to target.

From the dashboard or API, note a DAG ID not visible to the user (e.g., 'restricted_workflow').

> Confirm restriction by attempting normal view, which should fail.

### Step 2: Request Source Code Endpoint

**Context**: Directly access the source code view, exploiting the bypass.

Navigate in the browser to `/code?dag_id=restricted_workflow` or use an API tool to GET `/api/v1/dags/restricted_workflow/code`.

> The response returns the full Python source code without permission checks, displaying it in the UI or as JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[access-control-bypass]]
- [[dag]]
- [[source-code-leak]]
- [[airflow]]
