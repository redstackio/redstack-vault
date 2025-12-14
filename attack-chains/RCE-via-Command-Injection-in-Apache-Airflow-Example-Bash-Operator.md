---
tags:
  - rce
  - command-injection
  - airflow
  - bash
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Airflow-UI-and-Navigate-to-DAGs]]'
  - '[[procedures/Select-Example-Bash-Operator-DAG]]'
  - '[[procedures/Trigger-DAG-with-Configuration-Override]]'
  - '[[procedures/Set-Malicious-run_id-for-Injection]]'
  - '[[procedures/Execute-Injected-Command-via-DAG-Trigger]]'
step_count: 5
techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:54.529Z'
description: >-
  Multi-stage attack exploiting command injection in Apache Airflow's
  example_bash_operator.py DAG to achieve remote code execution on the server
  for authenticated users.
id: bfbd3ce3-457d-482f-b880-333e7a000828
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
---
# RCE via Command Injection in Apache Airflow Example Bash Operator

Multi-stage attack chain demonstrating remote code execution through command injection in the example_bash_operator.py DAG of Apache Airflow versions prior to 2.4.0. An authenticated user with UI access can inject shell commands via the unsanitized run_id parameter, leading to arbitrary OS command execution on the Airflow server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access UI] --> B[Select DAG]
    B --> C[Trigger with Config]
    C --> D[Inject Payload]
    D --> E[Execute RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome)

### Target Environment

- Apache Airflow < 2.4.0 installed
- Web UI accessible
- example_bash_operator.py DAG enabled
- Server running on Linux (Bash shell)

### Initial Access Requirements

- Authenticated user account with permissions to trigger DAGs via UI
- Network access to Airflow web interface (default port 8080)
- No prior server access needed beyond UI authentication

## Detailed Attack Procedures

### Step 1: Access Airflow UI and Navigate to DAGs
procedure: [[procedures/Access-Airflow-UI-and-Navigate-to-DAGs]]

**Objective**: Gain entry to the Airflow web interface and locate the vulnerable DAG.

**Instructions**: Open a web browser and log in to the Airflow UI using valid credentials. Once authenticated, click on the "DAGs" menu in the left sidebar to view the list of available DAGs.

**Expected Output**: Display of the DAGs dashboard showing all loaded DAGs, including example_bash_operator.

**Success Indicators**:
- Successful login to Airflow UI
- DAGs menu visible and accessible

### Step 2: Select Example Bash Operator DAG
procedure: [[procedures/Select-Example-Bash-Operator-DAG]]

**Objective**: Identify and select the vulnerable example_bash_operator DAG for triggering.

**Instructions**: In the DAGs list, locate and click on the "example_bash_operator" entry to open its detail view.

**Expected Output**: DAG detail page loads, showing task graph and run history for example_bash_operator.

**Success Indicators**:
- DAG detail page opens
- Trigger options are visible

### Step 3: Trigger DAG with Configuration Override
procedure: [[procedures/Trigger-DAG-with-Configuration-Override]]

**Objective**: Initiate the DAG run with the option to provide custom configuration for parameter injection.

**Instructions**: On the DAG detail page, click the "Trigger DAG" dropdown and select "Trigger DAG w/ config" to open the configuration modal.

**Expected Output**: Configuration modal appears, allowing JSON input for overriding parameters like run_id.

**Success Indicators**:
- Configuration modal opens
- Input field for run_id is available

### Step 4: Set Malicious run_id for Injection
procedure: [[procedures/Set-Malicious-run_id-for-Injection]]

**Objective**: Inject a shell command payload into the run_id parameter to exploit the command injection vulnerability.

**Instructions**: In the configuration modal, set the "run_id" field to a malicious value such as "`touch /tmp/success`". This uses backticks for shell command substitution, which will be interpolated into the BashOperator's command.

**Expected Output**: Configuration JSON reflects the injected run_id value.

**Success Indicators**:
- Malicious payload entered without validation errors
- Configuration ready for submission

### Step 5: Execute Injected Command via DAG Trigger
procedure: [[procedures/Execute-Injected-Command-via-DAG-Trigger]]

**Objective**: Submit the trigger to execute the DAG, resulting in the injected command running on the server.

**Instructions**: Click the "Trigger" button in the modal to start the DAG run. Monitor the task logs in the UI to confirm execution.

**Expected Output**: DAG run initiates, and upon completion, the injected command (e.g., [[commands/touch-success-file]]) executes, creating /tmp/success on the server.

**Success Indicators**:
- DAG run status shows success
- File /tmp/success exists on the server (verify via SSH or logs)
- Logs show command output without errors

## Attack Chain Summary

### Key Achievements

1. Authenticated access to Airflow UI
2. Successful injection of shell command via run_id parameter
3. Arbitrary RCE on the Airflow server, demonstrated by file creation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Unix Shell]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
