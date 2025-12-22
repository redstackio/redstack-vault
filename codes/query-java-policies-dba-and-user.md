---
id: 8e46aa6b-6dc0-4cc0-a8f6-282aa2ff00ae
name: query-java-policies-dba-and-user
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.304917+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - oracle
  - java
  - policy
  - recon
validated: true
---

# query-java-policies-dba-and-user

## Code

```sql
select * from dba_java_policy
select * from user_java_policy
```

## Description

This SQL snippet combines queries to enumerate Java policies at both database-wide (DBA) and user-specific levels, providing a comprehensive view of permissions for potential exploitation in Oracle environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; direct queries | N/A |

## Usage

Execute in SQL*Plus or via injection to assess Java privileges before granting or exploiting. Useful in reconnaissance phase of database attacks to identify weak configurations.

## Detection

- Audit logs showing SELECT on *_JAVA_POLICY views.
- Anomalous queries from low-privilege users accessing DBA views.

## Related

- [[procedures/Oracle-SQL-and-Java-Command-Execution]]
