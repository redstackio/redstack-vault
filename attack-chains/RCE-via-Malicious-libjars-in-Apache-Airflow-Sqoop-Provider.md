---
id: ac-rce-airflow-sqoop-libjars
tags:
  - rce
  - airflow
  - sqoop
  - libjars
  - hadoop
  - input-validation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Malicious-Sqoop-Connection-in-Airflow]]'
  - '[[procedures/Incorporate-Malicious-Connection-into-Airflow-DAG]]'
  - '[[procedures/Execute-DAG-to-Trigger-Sqoop-RCE]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:41.343Z'
description: >-
  Authenticated user exploits improper input validation in Apache Airflow Sqoop
  Provider to achieve remote code execution by injecting a malicious JAR via the
  libjars parameter in a Connection, tricking an admin into using it in a DAG.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unix Shell]]'
---
# RCE via Malicious libjars in Apache Airflow Sqoop Provider

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper input validation in the Apache Airflow Sqoop Provider (version 3.1.0) to achieve remote code execution on Hadoop MapReduce task machines.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious Connection] --> B[Incorporate into DAG]
    B --> C[Execute DAG for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- None (relies on Airflow UI access and Sqoop/Hadoop environment)

### Target Environment

- Apache Airflow with Sqoop Provider 3.1.0 installed
- Hadoop cluster with MapReduce enabled
- Linux-based OS for the MapReduce task machines
- Services: Apache Sqoop, Hadoop MapReduce
- Tech stack: Python, Apache Airflow, Apache Sqoop

### Initial Access Requirements

- Authenticated user access to Airflow web UI (e.g., via valid credentials)
- Ability to create Connections in Airflow
- Social engineering to trick admin into using the Connection (e.g., via phishing or collaboration)
- Network access to Airflow scheduler and Hadoop cluster

## Detailed Attack Procedures

### Step 1: Create Malicious Connection
procedure: [[procedures/Create-Malicious-Sqoop-Connection-in-Airflow]]

**Objective**: Set up a Sqoop Connection with a user-controlled libjars parameter pointing to a malicious JAR file containing arbitrary code execution payloads.

**Instructions**: Access the Airflow web UI, navigate to Admin > Connections, and create a new Sqoop connection. In the libjars field, specify a path to a JAR file hosted on an accessible location (e.g., internal file share or web server) that includes malicious code to execute system commands upon loading.

**Expected Output**: Connection created successfully, visible in the Connections list with the malicious libjars path.

**Success Indicators**:
- Connection saves without errors
- libjars field accepts arbitrary path (no validation)

### Step 2: Incorporate Malicious Connection into DAG
procedure: [[procedures/Incorporate-Malicious-Connection-into-Airflow-DAG]]

**Objective**: Trick or convince an administrator to reference the malicious Connection in an Airflow DAG that performs Sqoop operations, such as data import/export tasks.

**Instructions**: Share the malicious Connection ID or name with the admin (e.g., via email or shared DAG code). The admin then updates a DAG file (e.g., in Python) to use the Connection in a SqoopHook task, like SqoopOperator with connection_id set to the malicious one.

**Expected Output**: DAG updated and visible in the Airflow UI, ready for scheduling.

**Success Indicators**:
- Admin confirms DAG incorporation
- DAG parses without syntax errors

### Step 3: Execute DAG to Trigger RCE
procedure: [[procedures/Execute-DAG-to-Trigger-Sqoop-RCE]]

**Objective**: Run the DAG to invoke Sqoop operations, causing the malicious JAR to be added to the MapReduce classpath and execute arbitrary commands on the task machine.

**Instructions**: Trigger the DAG execution via the Airflow UI (e.g., manual trigger or scheduler). During execution, SqoopHook._prepare_command populates the -libjars option from the Connection, loading the JAR and running the payload on the Hadoop node performing the MapReduce task.

**Expected Output**: DAG runs, Sqoop command executes with -libjars including malicious path; evidence of command execution on the target machine (e.g., logs or reverse shell).

**Success Indicators**:
- DAG status shows success
- Arbitrary commands execute on MapReduce machine (e.g., whoami or file creation)
- Airflow logs show Sqoop command with -libjars option

## Attack Chain Summary

### Key Achievements

1. Bypassed input validation to inject malicious JAR path
2. Leveraged admin privileges indirectly via tricked DAG usage
3. Achieved RCE on Hadoop infrastructure without direct access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unix Shell]] Unix Shell

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
