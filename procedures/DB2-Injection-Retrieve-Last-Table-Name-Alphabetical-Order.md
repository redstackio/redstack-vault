---
id: 08eb8a31-3319-46d5-af40-30af8811dd1a
name: DB2-Injection-Retrieve-Last-Table-Name-Alphabetical-Order
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.865841+00:00'
updated_at: '2023-04-10T20:22:00.819180+00:00'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
  - '[[tags/Select Nth Row]]'
  - sql-injection
  - database-schema-enumeration
commands: []
platforms:
  - DB2
  - Web
tools: []
validated: true
---

# DB2-Injection-Retrieve-Last-Table-Name-Alphabetical-Order

## Summary

This procedure demonstrates a SQL injection technique targeting IBM DB2 databases to retrieve the last table name in alphabetical order from the system catalog. By injecting a crafted SQL query into a vulnerable application parameter, an attacker can enumerate database schema information, which is useful for mapping the database structure and identifying potential targets for further exploitation such as data extraction or privilege escalation.

## Description

SQL injection in DB2 allows attackers to manipulate queries executed against the database by injecting malicious SQL code through unsanitized user inputs in web applications. This specific technique focuses on querying the SYSIBM.SYSTABLES system catalog table, which stores metadata about all tables in the database. The query uses a subquery to select the first N rows ordered alphabetically ascending, then reverses the order to fetch the last one descending, effectively retrieving the last table name without needing full enumeration. This is particularly effective in blind SQL injection scenarios where direct output is not visible, but error messages or timing can confirm success. The attack assumes a vulnerable input field (e.g., login form or search parameter) that concatenates user input directly into a SELECT statement. Successful execution provides schema reconnaissance, aiding in targeted attacks like extracting sensitive data from identified tables. This maps to discovery tactics in offensive operations, with a moderate skill level required for crafting and injecting the payload.

## Requirements

1. Access to a web application with a SQL injection vulnerability interacting with an IBM DB2 backend database.
2. Knowledge of the injection point, such as a parameter in a URL, POST request, or form field that influences a SELECT query.
3. Basic understanding of DB2 SQL syntax and system catalogs; no special privileges needed beyond the injection vulnerability.
4. Tools for testing injections, such as a browser, proxy (e.g., Burp Suite), or manual input methods; network connectivity to the target application.

## Defense

- Implement strict input validation and sanitization using prepared statements or parameterized queries to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns in requests.
- Regularly audit database logs for unusual queries accessing system catalogs like SYSIBM.SYSTABLES.
- Limit application database permissions to read-only where possible and monitor for schema enumeration attempts.

## Objectives

1. Identify and exploit a SQL injection vulnerability in a DB2-backed application.
2. Retrieve the last table name in alphabetical order to gain insights into the database schema.
3. Use the enumerated information to plan subsequent attacks, such as targeting specific tables for data exfiltration.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a vulnerable input in the application where user-supplied data is directly concatenated into a SQL query without sanitization. Common points include search fields, authentication forms, or URL parameters.

Test for injection by appending a single quote (') to the input and observing if the application returns a SQL error (e.g., DB2 syntax error). If confirmed, proceed to craft the payload.

**Expected Output**: Database error message indicating unclosed quote or syntax issue, confirming the vulnerability.

### Step 2: Craft the Payload Using the Retrieval Query

**Context**: Construct the SQL injection payload that balances the original query and appends the schema enumeration logic. The goal is to close the original statement and inject a subquery to fetch from SYSIBM.SYSTABLES.

Use the following code snippet for the core query: [[codes/DB2-SQL-Query-Retrieve-Last-Table-Name]]

Replace 'N' with a small number like 1 for the last table, or higher to retrieve from a subset if the full alphabet is too broad. For example, in a URL parameter like ?id=1', inject: 1'; [injected query] --

**Expected Output**: The application response includes the table name (e.g., 'USERS' or 'Z_TABLE') if output is reflected, or a change in behavior (e.g., no error, delayed response) in blind scenarios.

### Step 3: Inject and Execute the Payload

**Context**: Deliver the payload to the vulnerable endpoint via the identified input method (e.g., GET/POST request). Use a proxy tool to intercept and modify if needed, ensuring the injection terminates the original query properly with a comment (--).

Submit the full payload, such as: Original input ' ; select name from (select * from sysibm.systables order by name asc fetch first 1 rows only) order by name desc fetch first row only --

Monitor the response for the extracted data or use boolean/time-based techniques if direct output is filtered.

**Expected Output**: Successful injection returns the last table name in the response body, error message, or inferred via side channels.

### Step 4: Verify and Iterate

**Context**: Confirm the retrieved name is valid by cross-referencing with known DB2 schema patterns or attempting follow-up queries on that table. If N>1, adjust to narrow down.

If the output is a system table (e.g., starting with SYS), increase N or refine the query to filter user tables (e.g., add WHERE type='T').

**Expected Output**: Valid user table name confirmed, enabling further enumeration like column names from SYSCOLUMNS.
