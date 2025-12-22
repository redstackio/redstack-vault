---
id: 00bd5b96-5709-49d4-825e-eee5b352cea5
name: PostgreSQL-List-Tables-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.695228+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL injection]]'
  - '[[tags/PostgreSQL List Tables]]'
  - sql-injection
  - database-discovery
commands:
  - '[[commands/postgresql-select-tables-from-information-schema]]'
platforms:
  - Web
  - PostgreSQL
tools: []
validated: true
---

# PostgreSQL-List-Tables-via-SQL-Injection

## Summary

This procedure demonstrates how to perform an SQL injection attack on a PostgreSQL database to extract a list of all tables, revealing the database structure for further reconnaissance or exploitation. It targets vulnerable input parameters in web applications connected to PostgreSQL, using a crafted query to query the information_schema.tables view.

## Description

SQL injection vulnerabilities in web applications allow attackers to inject malicious SQL code into queries, potentially exposing database metadata. In PostgreSQL, the information_schema.tables system view contains details about all tables in the current database. By injecting a UNION-based or error-based payload that appends this query, an attacker can retrieve table names without direct database access. This technique is useful during web application penetration testing to map the database schema, identify sensitive tables (e.g., users, credentials), and plan subsequent attacks like data extraction. It assumes the application uses a vulnerable dynamic SQL query and the attacker has identified an injectable parameter, such as a search field or URL parameter. Success depends on the application's error handling and the database user's permissions, typically requiring at least read access to information_schema.

## Requirements

1. Access to a web application with a SQL injection vulnerability interacting with a PostgreSQL backend.
2. Knowledge of the injectable parameter (e.g., via tools like [[tools/sqlmap]] or manual testing).
3. Basic understanding of SQL syntax and PostgreSQL specifics.
4. A proxy tool like [[tools/Burp-Suite]] for intercepting and modifying requests (optional but recommended).
5. The database user must have SELECT privileges on information_schema.tables.

## Defense

Defensive measures and detection strategies:

- Use prepared statements and parameterized queries in application code to prevent injection.
- Implement web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Regularly update PostgreSQL and the application framework to patch known vulnerabilities.
- Enable database logging for failed queries and monitor for unusual SELECTs on system views.
- Apply least-privilege principles: Restrict application database users to only necessary tables and views.

## Objectives

1. Identify and exploit a SQL injection point in the target application.
2. Extract the list of table names from the PostgreSQL database.
3. Gather metadata to inform further database attacks, such as column enumeration or data dumping.
4. Validate the injection without causing denial of service.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Begin by confirming the vulnerability. Test a parameter (e.g., a search input) with a single quote (') to trigger a SQL error, indicating dynamic query construction. Use boolean-based or time-based blind techniques if no direct output is visible.

**Command** (Use a basic test payload via browser or curl):

No specific command here; manually append ' OR 1=1 -- to the parameter and observe for data leakage or errors.

> If an error like "syntax error at or near '"'" appears, the point is injectable. Proceed to craft the payload.

### Step 2: Craft and Inject the Table Listing Query

**Context**: Construct a UNION SELECT payload to append the table listing query to the original application's query. Assume the original query returns a single column (e.g., IDs); match the number of columns in your UNION. Inject via the vulnerable parameter, URL-encoding if necessary.

**Command** ([[commands/postgresql-select-tables-from-information-schema]]):

Embed the query in the injection payload, e.g., for a search parameter: search=' UNION SELECT table_name FROM information_schema.tables --

```sql
SELECT table_name FROM information_schema.tables
```

> This query retrieves table names from the current database's information_schema. When injected, it should return table names in the application's response (e.g., as search results). If the application echoes results, you'll see names like "users", "orders". For blind injection, use conditional payloads to infer names character-by-character.

### Step 3: Verify and Extract Results

**Context**: Analyze the response for the injected data. If no direct output, use error-based injection (e.g., CAST to force errors revealing data) or follow up with column enumeration on discovered tables.

No specific command; parse the HTTP response for table names.

> Success is indicated by unexpected table names appearing in the output. Save the list for further procedures like [[procedures/PostgreSQL-Enumerate-Columns-via-SQL-Injection]]. If permissions are insufficient, you may get empty results—escalate privileges if possible.
