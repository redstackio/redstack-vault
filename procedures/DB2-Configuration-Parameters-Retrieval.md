---
id: b57defa0-8e88-458a-992d-ce6cbb669256
name: DB2-Configuration-Parameters-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.213247+00:00'
updated_at: '2023-04-10T20:22:01.172393+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
  - '[[tags/System Config]]'
  - database
  - sql-injection
  - configuration
commands:
  - '[[commands/db2-retrieve-automatic-maintenance-settings]]'
  - '[[commands/db2-retrieve-all-configuration-parameters]]'
platforms:
  - Linux
  - Web
tools: []
validated: true
---

# DB2-Configuration-Parameters-Retrieval

## Summary

This procedure retrieves sensitive configuration parameters from an IBM DB2 database server, including automatic maintenance settings stored in memory and all parameters stored on disk. It is typically used by attackers who have gained initial access to a web application backed by DB2 through SQL injection or similar vulnerabilities, allowing extraction of usernames, passwords, and other configuration details for further compromise.

## Description

DB2 Configuration Parameters Retrieval involves querying the sysibmadm.dbcfg system view to extract database configuration details. Attackers exploit this after compromising a web application with a DB2 backend, often via SQL injection, to obtain parameters like database manager settings, authentication details, and maintenance policies. These can reveal credentials or paths for lateral movement, privilege escalation, or data exfiltration. The technique targets multi-partition DB2 environments (e.g., DB2 DataPartitioning Feature) and requires elevated privileges on the database. In a red team scenario, this aids in mapping the database environment and identifying weak configurations. Prerequisites include authenticated access or injection point to execute SQL queries directly or indirectly.

## Requirements

1. Access to a vulnerable web application using a DB2 database backend, typically via SQL injection vulnerability.
2. Sufficient database privileges to query sysibmadm.dbcfg (e.g., SELECT on administrative views).
3. SQL execution capability, either direct (e.g., via db2 command line) or indirect (e.g., through application inputs).
4. Knowledge of the target database partition numbers if in a multi-partition setup.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and prepared statements in web applications to prevent SQL injection.
- Enforce least privilege on database accounts, restricting access to sysibmadm views.
- Enable database auditing and logging for queries on configuration views; monitor for anomalous SELECTs on sysibmadm.dbcfg.
- Use database activity monitoring (DAM) tools to alert on configuration queries from unexpected sources.

## Objectives

1. Extract automatic maintenance settings from in-memory configuration to identify scheduling and policy details.
2. Retrieve all disk-stored configuration parameters, including potential credentials and paths.
3. Use extracted information for privilege escalation, lateral movement, or deeper system compromise.

## Instructions

### Step 1: Retrieve Automatic Maintenance Settings

**Context**: This step queries the in-memory configuration for parameters starting with 'auto_', such as automatic maintenance policies across all database partitions. It helps identify active settings that might reveal operational details or misconfigurations.

**Command** ([[commands/db2-retrieve-automatic-maintenance-settings]]):
```sql
select dbpartitionnum, name, value from sysibmadm.dbcfg where name like 'auto_%';
```

> This command requires appropriate privileges and returns partition-specific automatic settings. Execute it via a SQL injection payload or direct DB2 client to gather in-memory config data.

### Step 2: Retrieve All Configuration Parameters

**Context**: This step fetches all database configuration parameters stored on disk, including deferred values like usernames, passwords, and file paths. It provides a comprehensive view for identifying sensitive information across partitions.

**Command** ([[commands/db2-retrieve-all-configuration-parameters]]):
```sql
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg;
```

> This command requires privileges and outputs all disk-based parameters. Use the results to parse for credentials or paths; combine with Step 1 for full coverage.
