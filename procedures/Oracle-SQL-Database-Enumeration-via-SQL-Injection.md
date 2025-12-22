---
id: df4609d5-ab2d-44e3-bbc5-c878a5691f09
name: Oracle-SQL-Database-Enumeration-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.176138+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
  - >-
    [[techniques/Data-from-Information-Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - '[[tags/Oracle-SQL-Injection]]'
  - '[[tags/Oracle-SQL-List-Databases]]'
  - database-enumeration
  - sql-injection
commands:
  - '[[commands/oracle-select-distinct-owners-from-all-tables]]'
platforms:
  - Oracle Database
tools: []
validated: true
---

# Oracle-SQL-Database-Enumeration-via-SQL-Injection

## Summary

This procedure demonstrates how to enumerate databases and table owners in an Oracle SQL database server by exploiting SQL injection vulnerabilities. Using a UNION-based injection payload, attackers can extract metadata such as distinct table owners from the 'all_tables' view, providing insights into the database structure and potential targets for further exploitation.

## Description

Oracle SQL Database Enumeration targets Oracle database servers vulnerable to SQL injection (SQLi), allowing attackers to append malicious queries to user input processed by the database. The core technique leverages the UNION operator to combine legitimate query results with an attacker-controlled SELECT statement that queries system views like 'all_tables'. This reveals schema information, such as unique table owners, which indicates database users and schemas containing sensitive data.

In a typical attack scenario, this occurs in web applications connected to Oracle backends where input fields (e.g., search boxes, login forms) are not properly sanitized. The enumeration helps map the environment for subsequent actions like data extraction or privilege escalation. Prerequisites include confirmed SQLi access, often validated via tools like SQLMap or manual testing with Burp Suite. Expected outcomes include a list of owners, aiding in identifying high-value schemas (e.g., HR, SYS).

This maps to discovery tactics in MITRE ATT&CK, focusing on gathering system and repository data without direct registry queries.

## Requirements

1. Confirmed SQL injection vulnerability in a web application backed by Oracle Database.
2. Network access to the vulnerable endpoint (e.g., via browser, proxy like Burp Suite, or automated tool like SQLMap).
3. Basic knowledge of SQL syntax and Oracle system views.
4. Tools for injecting and intercepting requests (e.g., [[tools/Burp-Suite]] or [[tools/sqlmap]]).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and parameterization (e.g., use prepared statements in application code) to prevent SQLi.
- Deploy a Web Application Firewall (WAF) configured to detect UNION-based payloads and anomalous query patterns.
- Enforce least privilege principles: Limit database user permissions to essential views and tables, restricting access to metadata like 'all_tables'.
- Enable database auditing and logging for query monitoring; alert on unexpected SELECTs from system views.
- Regularly scan for SQLi vulnerabilities using tools like OWASP ZAP or Nessus.

## Objectives

1. Identify all distinct table owners (schemas) within the Oracle database to map the environment.
2. Understand the database structure for targeted data extraction or escalation.
3. Validate the extent of SQLi exploitation without causing denial of service.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability

**Context**: Before enumeration, verify the endpoint is vulnerable to SQLi by testing for error-based or union-based responses. This ensures the injection point can accept appended queries.

**Command** (use a basic SQLi test command like [[commands/sqlmap-basic-test]] or manual injection):

Append a single quote or comment to trigger errors:

```sql
' OR 1=1 --
```

> If successful, the application returns unexpected data or errors revealing database type (e.g., ORA- errors confirming Oracle). If no response change, try blind SQLi techniques.

### Step 2: Determine Number of Columns for UNION

**Context**: UNION requires matching column counts between the original query and the injected SELECT. Use ORDER BY to probe the column count iteratively.

**Instructions**: Inject payloads incrementally via the vulnerable parameter (e.g., in a URL or POST body using Burp Repeater):

1. Start with ORDER BY 1--, increase until error (e.g., ORA-01785: ORDER BY item must be number of SELECT list).

Example payload for a search parameter:

```http
GET /search?q=abc' ORDER BY 1-- HTTP/1.1
```

> Expected: Successful up to the correct column count (e.g., ORDER BY 5 works, 6 fails). Adjust UNION SELECT accordingly.

### Step 3: Inject UNION Payload to Enumerate Owners

**Context**: Craft a UNION SELECT to query 'all_tables' for distinct owners. This step executes the core enumeration, assuming column count matches (pad with NULLs if needed).

**Command** ([[commands/oracle-select-distinct-owners-from-all-tables]]):

```sql
SELECT DISTINCT owner FROM all_tables;
```

> Embed in injection: Replace with the full payload, e.g., for a 3-column original query: `' UNION SELECT NULL, NULL, DISTINCT owner FROM all_tables --`. Execute via the vulnerable input. The 'all_tables' view is accessible to most users and lists table metadata. DISTINCT ensures unique owners only.

**Code** ([[codes/oracle-distinct-owners-sql-query]]):

The embedded SQL snippet above is the key payload.

> Expected: Response includes owner names (e.g., SYS, HR, APP_USER) blended into legitimate results. In blind SQLi, infer via boolean responses or time delays.

### Step 4: Interpret and Validate Results

**Context**: Analyze output to confirm enumeration success and plan next steps. Cross-reference owners with known Oracle schemas.

**Instructions**: If results appear, note owners like SYS (system) or custom schemas. Verify by injecting follow-up queries (e.g., SELECT * FROM all_users WHERE username='OWNER').

> If no output, adjust payload (e.g., handle case sensitivity or privileges). Success confirms database mapping; proceed to table/column enumeration.

### Step 5: Mitigate Detection During Execution

**Context**: Reduce footprint by limiting query scope and using evasion techniques.

**Instructions**: Use comments to obfuscate (e.g., /**/ instead of spaces), or encode payloads if WAF present. Limit to one injection per session.

> Expected: No alerts triggered; results obtained without session termination.
