---
id: 43b74816-fae8-4a0d-8c00-aefaf38b3dec
name: List-MSSQL-Database-Tables
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:20.800163+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/List all tables]]'
  - '[[tags/Manual SQL Server Queries]]'
  - '[[tags/MSSQL Server]]'
commands:
  - '[[commands/sqlcmd-execute-mssql-query]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/sqlcmd]]'
validated: true
---

# List-MSSQL-Database-Tables

## Summary

This procedure allows an attacker with access to a Microsoft SQL Server (MSSQL) instance to query the database and retrieve a list of all tables present. This discovery technique helps identify potential data stores containing sensitive information, such as user credentials, financial records, or configuration data, enabling further enumeration or exfiltration in a compromised environment.

## Description

In scenarios where initial access to an MSSQL server has been gained (e.g., via valid credentials or SQL injection), listing database tables provides visibility into the schema and potential targets for deeper exploitation. The procedure uses standard SQL queries against the INFORMATION_SCHEMA views, which are accessible to users with basic SELECT permissions on the database. This is particularly useful in internal network pivoting or lateral movement phases, where understanding the database structure can reveal high-value assets. Success depends on having at least db_datareader role or equivalent permissions; administrative access is not required but enhances results.

## Requirements

1. Valid credentials (username and password) for an MSSQL account with SELECT permissions on the target database.
2. Network access to the MSSQL server instance (default port 1433/TCP, or custom port).
3. Installed sqlcmd utility on the attacker's machine for remote querying.
4. Knowledge of the target server name or IP address and database name.

## Defense

- Restrict database access using principle of least privilege; grant SELECT on INFORMATION_SCHEMA only to necessary roles.
- Enable SQL Server auditing for query events and monitor for anomalous SELECT statements targeting metadata views.
- Implement network segmentation to limit lateral access to database servers and use firewalls to restrict port 1433.
- Enforce multi-factor authentication (MFA) for SQL logins and regularly rotate credentials.

## Objectives

1. Enumerate all user and system tables within the current MSSQL database.
2. Identify tables that may contain sensitive data for subsequent queries or exfiltration.
3. Verify successful access to the database schema without triggering alerts.

## Instructions

### Step 1: Connect to the MSSQL Server and Execute Table Enumeration Query

**Context**: Establish a connection to the target MSSQL instance using sqlcmd and run a SQL query to list all tables. This step assumes you have the server details and credentials; replace placeholders with actual values. The query targets the INFORMATION_SCHEMA.TABLES view, which is standard and less likely to raise suspicion than querying system catalogs directly.

**Command** ([[commands/sqlcmd-execute-mssql-query]]):

First, ensure sqlcmd is available, then execute the command with your parameters.

**Code** ([[codes/MSSQL-List-Tables-SQL-Query]]):

The SQL query embedded in the command is:

```sql
select table_name from information_schema.tables
```

> This command connects to the MSSQL server and executes the query, retrieving table names from the current database. If the database context is not set, specify it with -d DATABASE_NAME. Expected output includes a list of table names; pipe to a file (e.g., | tee tables.txt) for later analysis. If authentication fails, check credentials and server connectivity.

### Step 2: Verify and Analyze Results

**Context**: Review the output for relevant tables, such as those with names indicating users, admins, or configs (e.g., Users, Credentials). This helps prioritize follow-on actions like querying specific tables.

No specific command needed here; manually inspect the output from Step 1. Look for patterns like 'dbo.' prefixed tables, which are user-created.

> Success is indicated by a non-empty list of tables without errors like 'Login failed' or 'Access denied'. If no tables appear, confirm the current database context with a preliminary query like SELECT DB_NAME().
