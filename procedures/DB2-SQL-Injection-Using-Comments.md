---
id: b7e648c4-fd77-48a5-9b34-ed5554cc631c
name: DB2-SQL-Injection-Using-Comments
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - sql-injection
  - db2
  - comments
  - database-exploitation
commands:
  - '[[commands/sqlmap-db2-comment-injection]]'
platforms:
  - Databases
  - DB2
tools: []
validated: true
---

# DB2-SQL-Injection-Using-Comments

## Summary

This procedure demonstrates how to perform SQL injection attacks on IBM DB2 databases by leveraging SQL comments to filter out or neutralize parts of queries that might trigger security filters or detection mechanisms. It allows attackers to bypass basic input validation, evade web application firewalls (WAFs), and extract sensitive data from vulnerable applications connected to DB2 backends.

## Description

DB2 SQL injection involves injecting malicious SQL code into user inputs that are concatenated into SELECT queries executed by the database. In this technique, comments (using '--' for line comments in DB2) are used to comment out the remainder of the original query after the injection point, effectively replacing or appending to the intended SQL without causing syntax errors. This is particularly useful when the application appends conditions or clauses that could break the injection payload. For example, if the app adds 'AND 1=1' after the input, commenting it out with '--' neutralizes it. The procedure targets web applications with unsanitized inputs to DB2, such as login forms or search fields, enabling data exfiltration like user credentials or table contents. Prerequisites include identifying a vulnerable endpoint via error-based or blind injection testing. Expected outcomes include successful query manipulation leading to unauthorized data access.

## Requirements

1. Network access to a web application or service connected to a DB2 database.
2. Identification of a vulnerable input parameter (e.g., via manual testing or tools like sqlmap) that influences a SELECT query.
3. Basic knowledge of DB2 SQL syntax, including comment usage ('--' for single-line comments).
4. Tools like sqlmap installed for automated injection testing.

## Defense

- Implement strict input validation and sanitization, escaping special characters like '-' in user inputs.
- Use parameterized queries or prepared statements in application code to separate SQL logic from data inputs.
- Deploy web application firewalls (WAFs) configured to detect comment-based obfuscation in SQL payloads.
- Enable DB2 logging for all queries and monitor for anomalous patterns, such as unexpected comment usage or data exfiltration attempts.
- Regularly audit application code for dynamic SQL construction and apply least-privilege database accounts.

## Objectives

1. Identify and exploit a SQL injection vulnerability in a DB2-backed application.
2. Use SQL comments to bypass query filters or appended conditions, enabling payload execution.
3. Extract sensitive data, such as table schemas, user records, or credentials, without triggering errors or alerts.
4. Maintain stealth by avoiding detectable injection patterns.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Begin by probing the target application to find inputs susceptible to SQL injection, focusing on those that interact with DB2 SELECT queries. Use error-based or time-based tests to confirm DB2 as the backend.

**Command** ([[commands/sqlmap-db2-comment-injection]]):

Use sqlmap to test for DB2-specific injection points, specifying the DBMS to optimize payloads.

```bash
sqlmap -u "http://target.com/search?q=$_QUERY" --dbms=ibm --technique=B --batch
```

> This step scans the URL parameter for blind injection vulnerabilities. Replace $_QUERY with a test value like '1'. Expected output includes detection of DB2 and vulnerability confirmation, such as "Parameter: q (GET) is vulnerable to boolean-based blind."

### Step 2: Craft Injection Payload with Comments

**Context**: Once a vulnerability is confirmed, construct a payload using DB2 comments to neutralize the rest of the query. For example, inject ' UNION SELECT username, password FROM users --' to append a data-extracting subquery and comment out any trailing application logic.

Embed the following example SQL snippet into the vulnerable parameter:

```sql
select blah from foo -- comment like this (double dash)
```

> In a real injection, replace 'blah' and 'foo' with actual column and table names discovered via prior enumeration. The '--' comments out everything after, preventing syntax errors from appended clauses like 'WHERE id=1'. Expected output: The database executes the injected SELECT, returning data in the application response, such as unioned results from the users table.

### Step 3: Execute and Verify Injection

**Context**: Submit the payload via the vulnerable input and verify success by observing data leakage or delayed responses in blind scenarios. Iterate to extract more data, such as using SUBSTRING or HEX encoding for evasion.

**Command** ([[commands/sqlmap-db2-comment-injection]]):

Automate the injection with a comment-based payload.

```bash
sqlmap -u "http://target.com/search?q=$_QUERY" --dbms=ibm --technique=U --union-cols=$_COLS --dump -D $_DB -T $_TABLE --batch
```

> Specify $_COLS as the number of columns (e.g., 2), $_DB as the database name, and $_TABLE as the target table. This dumps data using UNION injection, with comments implicitly handled by sqlmap's payload generation. Expected output: Dumped table contents, e.g., rows of usernames and hashed passwords, confirming successful exfiltration.
