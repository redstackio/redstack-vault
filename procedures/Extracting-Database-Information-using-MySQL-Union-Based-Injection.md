---
id: 4169a74f-9201-493c-98a3-883efeb94e2b
name: Extracting-Database-Information-using-MySQL-Union-Based-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.356733+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
  - '[[techniques/Data from Local System|T1005 - Data from Local System]]'
sub_techniques: []
tags:
  - '[[tags/mysql-injection]]'
  - '[[tags/union-based-injection]]'
  - '[[tags/database-extraction]]'
  - '[[tags/information-schema]]'
commands: []
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# Extracting-Database-Information-using-MySQL-Union-Based-Injection

## Summary

This procedure demonstrates how to exploit a MySQL union-based SQL injection vulnerability in a web application to extract database metadata and sensitive data using the information_schema system database. By injecting crafted UNION SELECT statements, attackers can concatenate and retrieve schema names, table names, column names, and actual data without direct database access.

## Description

MySQL union-based SQL injection involves appending a malicious UNION SELECT query to a legitimate query in a vulnerable web application parameter, such as a search field or URL parameter. This allows the attacker to leverage the application's existing database connection to query the information_schema database, which stores metadata about all databases, tables, and columns in the MySQL instance. The technique relies on matching the number of columns in the original query with the injected one and using functions like GROUP_CONCAT to combine results into a single output column for exfiltration via the web response. This is typically used after identifying a blind or error-based injection point but here focuses on union-based for direct data retrieval. The target environment is a web application backed by MySQL, often on Linux servers, with insufficient input sanitization.

## Requirements

1. Access to a vulnerable web application endpoint susceptible to SQL injection (e.g., via GET/POST parameters).
2. Knowledge of the injection point and the number of columns in the original query (determined via order-by or similar techniques).
3. A tool or browser for sending HTTP requests, such as Burp Suite or curl (though not required, recommended for interception).
4. Basic understanding of MySQL syntax and the information_schema structure.

## Defense

- Use parameterized queries or prepared statements in application code to separate SQL logic from user input.
- Implement web application firewalls (WAFs) to detect and block common SQL injection patterns, including UNION keywords.
- Apply least privilege to database users, restricting access to information_schema and sensitive tables.
- Enable MySQL query logging and monitor for anomalous queries involving GROUP_CONCAT or information_schema.

## Objectives

1. Enumerate database names, table structures, and column details from the MySQL instance.
2. Extract actual data from targeted tables using concatenated queries.
3. Map the full database schema to facilitate further exploitation or data theft.

## Instructions

### Step 1: Determine Injection Point and Column Count

**Context**: Identify the vulnerable parameter and match the number of columns in the UNION query to the original SELECT statement to avoid syntax errors. This step ensures the injection blends seamlessly.

Inject test payloads like ' UNION SELECT 1,2,3--' incrementally increasing numbers until no error occurs, revealing the column count (e.g., 4 columns).

> Use a proxy like Burp Suite to intercept and modify requests. Expected output: Web page renders without SQL errors, possibly displaying NULL or numbers in output fields.

### Step 2: Extract Database Names

**Context**: Query the schemata table in information_schema to list all databases, using GROUP_CONCAT to pipe-delimit results for easy parsing.

Inject the following SQL payload into the vulnerable parameter, replacing '...' with the matched column count and database name if filtering:

Reference: [[codes/MySQL-Union-Based-Database-Extraction-Queries]]

```sql
' UNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,schema_name,0x7c) FROM information_schema.schemata--
```

> This concatenates schema names separated by '|' (0x7c is hex for |). Expected output: Response includes a pipe-separated list of database names (e.g., |information_schema|mysql|app_db|).

### Step 3: Extract Table Names

**Context**: Once a target database is identified (e.g., 'app_db'), query the tables table filtered by table_schema to list tables, again using GROUP_CONCAT.

Inject the payload, replacing '...' with column count and the target schema:

Reference: [[codes/MySQL-Union-Based-Database-Extraction-Queries]]

```sql
' UNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,table_name,0x7c) FROM information_schema.tables WHERE table_schema='app_db'--
```

> Expected output: Pipe-separated table names (e.g., |users|products|orders|).

### Step 4: Extract Column Names

**Context**: For a specific table (e.g., 'users'), query the columns table to reveal data types and names, aiding in targeted data extraction.

Inject the payload, replacing with table name:

Reference: [[codes/MySQL-Union-Based-Database-Extraction-Queries]]

```sql
' UNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,column_name,0x7c) FROM information_schema.columns WHERE table_name='users'--
```

> Expected output: Pipe-separated columns (e.g., |id|username|password|email|).

### Step 5: Extract Table Data

**Context**: Finally, dump actual data from a table by selecting and concatenating column values, limited by GROUP_CONCAT length if needed (use SUBSTRING for large results).

Inject the payload for the target table and columns:

Reference: [[codes/MySQL-Union-Based-Database-Extraction-Queries]]

```sql
' UNION SELECT 1,2,3,4,...,GROUP_CONCAT(0x7c,username,0x7c,password,0x7c) FROM users--
```

> Expected output: Concatenated sensitive data (e.g., |admin|hashedpass123|user2|weakpass|). If results are truncated, iterate with LIMIT or OFFSET.
