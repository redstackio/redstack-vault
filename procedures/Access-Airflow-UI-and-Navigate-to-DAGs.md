---
tags:
  - airflow
  - ui-access
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
updated_at: '2025-12-14T17:23:54.523Z'
sub_techniques: []
id: 6a9990ea-b47d-44a6-a674-cb42e88d6993
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Airflow-UI-and-Navigate-to-DAGs

## Summary

This procedure outlines logging into the Apache Airflow web UI and navigating to the DAGs section to prepare for triggering vulnerable workflows.

## Description

In the context of exploiting command injection in Airflow's example DAGs, initial access to the web interface is required for authenticated users. This step assumes valid credentials and focuses on reaching the DAG management area where the example_bash_operator.py can be targeted. No technical exploits occur here; it's prerequisite navigation.

## Requirements

1. Valid Airflow user credentials with DAG trigger permissions
2. Web browser with network access to Airflow UI (typically http://localhost:8080)
3. Airflow instance running and UI enabled

## Defense

Defensive measures and detection strategies:

- Enforce strong authentication (e.g., LDAP, OAuth) for UI access
- Monitor login attempts and UI navigation logs for anomalous patterns
- Restrict UI access to trusted IP ranges via reverse proxy (e.g., Nginx)

## Objectives

1. Establish authenticated session in Airflow UI
2. Reach the DAGs dashboard
3. Prepare for DAG selection without triggering alerts

## Instructions

### Step 1: Log In to Airflow UI

**Context**: Authenticate to gain access to administrative features.

No command; use web browser to navigate to the Airflow login page and enter credentials.

> Successful login redirects to the dashboard.

### Step 2: Navigate to DAGs Menu

**Context**: Locate the section for managing and triggering DAGs.

Click the "DAGs" link in the left sidebar.

> DAGs list loads, displaying available workflows including example_bash_operator.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[airflow]]
- [[ui-access]]
