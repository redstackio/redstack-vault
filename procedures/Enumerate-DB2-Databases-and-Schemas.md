---
id: b716ba85-9ebb-4f79-86f5-d7b70485a756
name: Enumerate-DB2-Databases-and-Schemas
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.753406+00:00'
updated_at: '2023-04-10T20:21:59.771710+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File-and-Directory-Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/DB2]]'
  - '[[tags/Database-Enumeration]]'
  - '[[tags/SQL-Query]]'
commands:
  - '[[commands/db2-list-databases]]'
  - '[[commands/db2-list-schemas]]'
platforms:
  - Database
  - DB2
tools: []
validated: true
---

# Enumerate-DB2-Databases-and-Schemas

## Summary

This procedure enumerates all available databases and schemas within a DB2 database instance using targeted SQL queries against system catalogs. It is useful in penetration testing or red team operations to map the data architecture for further discovery, such as identifying sensitive tables or planning data exfiltration.

## Description

DB2 Enumeration involves querying the system's metadata tables to retrieve information about databases (via table_catalog) and schemas (via schemanata). This can be performed with authorized credentials through a DB2 client or exploited via SQL injection in vulnerable applications. The technique reveals the structure of the database environment, aiding in lateral movement or collection phases of an attack. It assumes access to the DB2 instance, either direct or through an exploited vector, and targets IBM DB2 on Linux, Windows, or Unix platforms. Success provides a list of databases and schemas, which can guide subsequent queries for tables, users, or data.

## Requirements

1. Valid credentials or SQL injection access to the DB2 instance.
2. A DB2 client tool (e.g., db2 command-line or SQL client like DBeaver).
3. Network connectivity to the DB2 server port (default 50000).
4. Basic knowledge of SQL syntax for system catalog queries.

## Defense

- Implement strict input validation and use parameterized queries to prevent SQL injection.
- Restrict database access to least privilege, disabling unnecessary system catalog queries for non-admin users.
- Enable DB2 auditing and logging for SELECT statements on sysibm and syscat tables.
- Use database firewalls or WAFs to monitor and block anomalous enumeration queries.

## Objectives

1. Retrieve a list of all databases in the DB2 instance.
2. Identify all available schemas for further exploration.
3. Map the database architecture to support targeted attacks on sensitive data.

## Instructions

### Step 1: Connect to the DB2 Instance

**Context**: Establish a connection to the target DB2 database to execute enumeration queries. This step verifies access and sets the context for system catalog queries.

Use a DB2 client to connect:

```bash
db2 connect to $_DATABASE user $_USERNAME using $_PASSWORD
```

> Replace $_DATABASE with the target database name (if known), $_USERNAME and $_PASSWORD with valid credentials. Expected output: Connection successful message, confirming session establishment.

### Step 2: List Available Databases

**Context**: Query the sysibm.tables catalog to extract distinct database names (table_catalog), revealing the full set of databases in the instance.

**Command** ([[commands/db2-list-databases]]):

```sql
select distinct(table_catalog) from sysibm.tables;
```

> This query scans the tables metadata to list unique database catalogs. It is performed after connection and targets the current instance. Expected output: A result set with column TABLE_CATALOG containing database names like 'SAMPLE', 'PRODDB'.

### Step 3: List Available Schemas

**Context**: Query the syscat.schemata catalog to enumerate all schemas, which act as namespaces for objects and indicate potential areas for data discovery or privilege checks.

**Command** ([[commands/db2-list-schemas]]):

```sql
SELECT schemaname FROM syscat.schemata;
```

> This retrieves schema names from the system catalog. Run it in the same session as Step 2. Expected output: A result set with column SCHEMANAME listing entries like 'SYSIBM', 'DB2INST1', 'USER_SCHEMA'.

### Step 4: Verify and Document Results

**Context**: Review the outputs to confirm enumeration success and note any high-value targets (e.g., production schemas). Disconnect securely to avoid leaving traces.

Export results if needed:

```sql
-- For databases
select distinct(table_catalog) from sysibm.tables; export to databases.csv OF DEL;

-- For schemas
SELECT schemaname FROM syscat.schemata; export to schemas.csv OF DEL;
```

> Expected output: CSV files with enumerated data. Success is indicated by complete lists without errors; if access denied, credentials may lack sufficient privileges.
