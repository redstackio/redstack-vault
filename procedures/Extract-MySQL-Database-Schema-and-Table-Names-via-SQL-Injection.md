---
id: 51b957e2-6bb2-412b-ae0b-5247609af4e6
name: Extract-MySQL-Database-Schema-and-Table-Names-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.945263+00:00'
updated_at: '2023-04-10T20:22:57.296345+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
sub_techniques: []
tags:
  - sql-injection
  - mysql
  - database-enumeration
  - fast-exploitation
commands: []
platforms:
  - Web
  - MySQL
tools: []
validated: true
---

# Extract-MySQL-Database-Schema-and-Table-Names-via-SQL-Injection

## Summary

This procedure demonstrates how to exploit a SQL injection vulnerability in a MySQL-backed web application to rapidly extract the database schema and table names from the INFORMATION_SCHEMA system tables. By injecting a crafted SQL query, an attacker can enumerate the structure of the target database, enabling further targeted exploitation such as data extraction or manipulation.

## Description

SQL injection attacks on MySQL databases allow attackers to inject malicious SQL code into input fields of web applications, bypassing authentication or extracting sensitive information. This specific technique targets the INFORMATION_SCHEMA.TABLES view, which contains metadata about all tables across schemas. The query uses JSON aggregation to compactly return schema and table names in a single response, making it efficient for blind or time-based injections where output is limited. This is particularly useful in fast exploitation scenarios during penetration testing or red team engagements to map the database layout quickly. The procedure assumes a confirmed injection point, such as a login form or search parameter, and focuses on the extraction phase. For defensive purposes, it highlights common mitigations to prevent such enumerations.

## Requirements

1. Access to a web application with a confirmed SQL injection vulnerability in a MySQL backend.
2. Knowledge of the injection point (e.g., URL parameter, POST data field).
3. Tools for crafting and sending HTTP requests, such as a browser, curl, or Burp Suite.
4. Basic understanding of SQL syntax and MySQL INFORMATION_SCHEMA structure.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, sanitization, and parameterization using prepared statements or ORM frameworks like PDO in PHP.
- Use web application firewalls (WAFs) to detect and block common SQL injection patterns, including JSON aggregation attempts.
- Enable MySQL query logging and monitor for anomalous queries accessing INFORMATION_SCHEMA.
- Regularly audit application code for unsanitized inputs and apply least-privilege database accounts that restrict access to metadata tables.

## Objectives

1. Confirm the ability to inject and execute arbitrary SQL in the target MySQL database.
2. Extract a comprehensive list of database schemas and their associated table names.
3. Use the enumerated information to identify high-value targets for further database exploitation, such as user tables or sensitive data stores.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability

**Context**: Before extracting schema information, verify that the injection point allows arbitrary SQL execution. This step ensures the vulnerability is exploitable and helps determine the injection type (e.g., union-based, blind).

Use a standard SQLi test payload to check for errors or boolean responses indicating successful injection.

**Example Test Payload** (inject into vulnerable parameter, e.g., ?id=1):

```sql
1' AND 1=1 --
```

> If the query returns normal results, injection is likely possible. If it causes an error or alters behavior (e.g., no results for 1=2), proceed. Expected output: Database response without errors for true conditions, errors or no results for false.

### Step 2: Craft the Schema Extraction Query

**Context**: Prepare the SQL query to retrieve schema and table names. This uses INFORMATION_SCHEMA.TABLES to list all schemas and tables, concatenated with a colon separator and aggregated into a JSON array for compact output suitable for limited response channels.

**Code** ([[codes/MySQL-Extract-Table-Schemas-and-Names]]):

```sql
SELECT json_arrayagg(concat_ws(0x3a,table_schema,table_name)) from INFORMATION_SCHEMA.TABLES;
```

> The concat_ws function joins schema and table names with ':' (0x3a is hex for colon). json_arrayagg bundles results into a JSON array, e.g., ["schema1:table1","schema2:table2"]. This step provides the raw query; no execution here.

### Step 3: Inject the Query into the Vulnerable Endpoint

**Context**: Deliver the crafted query via the confirmed injection point. For union-based injections, append it to a subquery; for blind, use conditional extraction if needed. Monitor the response for the JSON array.

Inject the full query, e.g., in a URL parameter: ?id=1'; [QUERY HERE] --

**Expected Output**: A JSON array in the application response, such as ["information_schema:TABLES","mysql:user","app_db:users","app_db:orders"]. If no output (blind injection), use time-based or boolean techniques to infer results.

### Step 4: Parse and Analyze the Extracted Data

**Context**: Once the JSON array is returned, decode it to map schemas to tables. This reveals the database structure for prioritizing further attacks, like dumping specific tables.

Manually parse the JSON (or use a tool like jq if piped to a script). Look for schemas like 'information_schema' (system) vs. custom ones.

**Expected Output**: A structured list, e.g., Schema: app_db, Tables: users, orders, logs. Success if at least system schemas are enumerated; full custom schema indicates high privileges.

### Step 5: Verify Completeness and Escalate

**Context**: Confirm all schemas/tables are captured and check for privileges. If partial results, refine the query (e.g., filter by schema).

Re-run if needed, or extend to [[codes/MySQL-Extract-Column-Information]] for deeper enum.

**Expected Output**: No truncation in JSON array; all expected system tables present.

**Success Indicators**:
- JSON array returned without SQL errors.
- Custom application schemas and tables identified.
- No WAF blocks or rate limiting triggered.
