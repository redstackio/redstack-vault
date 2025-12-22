---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - oracle-sql
  - database-enumeration
  - sql-injection
  - discovery
commands:
  - '[[commands/oracle-retrieve-global-database-name]]'
  - '[[commands/oracle-retrieve-database-name]]'
  - '[[commands/oracle-retrieve-instance-name]]'
  - '[[commands/oracle-retrieve-system-database-name]]'
platforms:
  - Oracle Database
tools: []
validated: true
---

# Oracle-SQL-Database-Name-Enumeration

## Summary

This procedure enumerates key identifiers of an Oracle SQL database, including the global name, database name, instance name, and system database name, using targeted SQL queries. It is typically employed during reconnaissance phases of penetration testing or attack simulations to gather infrastructure details that can inform vulnerability research and subsequent exploitation strategies.

## Description

In scenarios involving access to an Oracle SQL server, such as through SQL injection vulnerabilities or compromised credentials, attackers can query dynamic performance views and system functions to extract database metadata. This information reveals the target's database configuration, which may expose version-specific weaknesses or aid in crafting more precise attacks. The procedure leverages standard Oracle system tables like V$DATABASE, V$INSTANCE, and DUAL, assuming the attacker has sufficient privileges to execute SELECT statements. It is particularly useful in web application contexts where SQL injection allows blind or error-based extraction of this data.

## Requirements

1. Valid access to the Oracle SQL server, such as through a SQL client (e.g., sqlplus) or an exploited SQL injection point.
2. Knowledge of SQL injection techniques if injecting via a web application, or direct database credentials.
3. Basic familiarity with Oracle SQL syntax and system views.
4. Tools like sqlplus or a database management tool for execution.

## Defense

Defensive measures and detection strategies:

- Apply the latest Oracle security patches to mitigate known injection vulnerabilities and restrict access to sensitive views.
- Implement input validation and parameterized queries in applications to prevent SQL injection.
- Enable database auditing and monitor logs for anomalous SELECT queries against V$ views or DUAL table.
- Use database roles with least privilege, denying SELECT on performance views to untrusted users.

## Objectives

1. Extract the global database name to understand the full Oracle SID and domain configuration.
2. Retrieve the local database name and instance details for identifying the specific deployment.
3. Collect this reconnaissance data to map the target's infrastructure and identify potential attack vectors.
4. Verify successful enumeration without triggering alerts.

## Instructions

### Step 1: Retrieve Global Database Name

**Context**: Begin by querying the global_name view to obtain the fully qualified database identifier, which includes the SID and domain. This provides a unique identifier across distributed Oracle environments.

**Command** ([[commands/oracle-retrieve-global-database-name]]):
```sql
SELECT global_name FROM global_name;
```

> This query accesses the global_name view, which is publicly accessible. It returns the concatenated DB_NAME and DB_DOMAIN values. Use this in error-based SQL injection by forcing an error that leaks the result, or execute directly if connected.

### Step 2: Retrieve Local Database Name

**Context**: Query the V$DATABASE view to get the core database name (DB_NAME), excluding domain specifics. This is essential for matching against known vulnerable configurations.

**Command** ([[commands/oracle-retrieve-database-name]]):
```sql
SELECT name FROM V$DATABASE;
```

> The V$DATABASE view requires SELECT privileges, often granted to public roles. In injection scenarios, union-based or blind techniques can extract this. Expected result is a single row with the DB_NAME.

### Step 3: Retrieve Instance Name

**Context**: Use the V$INSTANCE view to identify the current instance name, useful in Real Application Clusters (RAC) or multi-instance setups to pinpoint the targeted node.

**Command** ([[commands/oracle-retrieve-instance-name]]):
```sql
SELECT instance_name FROM V$INSTANCE;
```

> This view provides instance-specific details. It may require DBA privileges in restricted setups, but is often readable. Combine with prior steps for a complete picture.

### Step 4: Retrieve System Database Name

**Context**: As a verification step, call the SYS.DATABASE_NAME function via the DUAL table to confirm the database name using a built-in Oracle function, which can bypass some view restrictions.

**Command** ([[commands/oracle-retrieve-system-database-name]]):
```sql
SELECT SYS.DATABASE_NAME FROM DUAL;
```

> DUAL is a special one-row table always available. This function returns the DB_NAME and serves as a lightweight alternative. In injections, it's ideal for stacked queries.
