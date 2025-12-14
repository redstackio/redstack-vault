---
id: ac-sql-injection-airflow-priv-esc
tags:
  - sqli
  - apache-airflow
  - privilege-escalation
  - rce
  - web
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - >-
    [[procedures/Exploit-SQL-Injection-via-partition-clause-in-Airflow-DAG-Triggering]]
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Web Shell]]'
updated_at: '2025-12-14T03:46:26.129Z'
description: >-
  An authenticated user exploits an SQL Injection vulnerability in the
  partition_clause parameter of Apache Airflow's SQLTableCheckOperator to
  execute arbitrary SQL, leading to privilege escalation and potential remote
  code execution.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Web Shell]]'
---
# SQL Injection in Apache Airflow SQLTableCheckOperator for Privilege Escalation

Multi-stage attack chain demonstrating a complete attack workflow exploiting an SQL Injection in Apache Airflow's Common SQL Provider.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Execution]
    B --> C[Privilege Escalation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (UI-based exploitation)

### Target Environment

- Apache Airflow 2.10.5 or similar vulnerable version
- Web-based Airflow UI accessible
- SQL backend (e.g., PostgreSQL, MySQL) connected to Airflow
- No specific ports required beyond standard web access (typically port 8080)

### Initial Access Requirements

- Valid authenticated user credentials to Airflow UI
- Network access to the Airflow web server
- Prior knowledge of DAGs using SQLTableCheckOperator in a recommended triggering pattern

## Detailed Attack Procedures

### Step 1: Trigger DAG with Malicious Input
procedure: [[procedures/Exploit-SQL-Injection-via-partition-clause-in-Airflow-DAG-Triggering]]

**Objective**: Inject arbitrary SQL via the partition_clause parameter to execute unauthorized queries, escalating privileges and potentially enabling RCE.

**Instructions**: Log in to the Airflow UI as an authenticated user. Navigate to the DAG triggering interface where the SQLTableCheckOperator is used. In the partition_clause field, input a malicious SQL payload such as `' OR 1=1; DROP TABLE users; --` to manipulate the query construction. Trigger the DAG to execute the injected SQL against the backend database.

**Expected Output**: Successful execution of the injected SQL, visible in database logs or effects like data deletion/modification. Privilege escalation may manifest as elevated database permissions or Airflow task execution anomalies.

**Success Indicators**:
- Arbitrary SQL executed without errors (e.g., table altered or data exfiltrated)
- User gains elevated privileges in the SQL backend
- Potential RCE if the SQL leads to command execution in Airflow tasks

## Attack Chain Summary

### Key Achievements

1. Bypassed input sanitization in partition_clause for arbitrary SQL execution
2. Achieved privilege escalation from authenticated user to database admin-level access
3. Enabled potential remote code execution through manipulated DAG tasks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Web Shell]] Server Software Component: Web Server (adapted for SQL via web UI)

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01T00:00:00Z*
