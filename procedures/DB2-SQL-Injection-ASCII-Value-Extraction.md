---
id: 7549bb35-2027-4f56-bbde-016653d17887
name: DB2-SQL-Injection-ASCII-Value-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.942007+00:00'
updated_at: '2023-04-10T20:22:03.739650+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/Data from Information Repositories|T1213 - Data from
    Information Repositories]]
sub_techniques: []
tags:
  - '[[tags/ASCII Value]]'
  - '[[tags/DB2 Cheatsheet]]'
  - '[[tags/DB2 Injection]]'
  - sql-injection
  - data-exfiltration
commands:
  - '[[commands/db2-select-character-by-ascii]]'
platforms:
  - Database
  - DB2
  - Linux
  - Windows
tools: []
validated: true
---

# DB2-SQL-Injection-ASCII-Value-Extraction

## Summary

This procedure demonstrates how to perform SQL injection on an IBM DB2 database to extract data by converting ASCII values to characters using the CHR() function and the SYSIBM.SYSDUMMY1 table. It is useful for blind SQL injection scenarios where direct data retrieval is blocked, allowing attackers to exfiltrate information character by character through error messages, time delays, or response differences.

## Description

DB2 SQL injection targets vulnerabilities in applications connected to IBM DB2 databases, where unsanitized user input is passed to SQL queries. This technique focuses on extracting database content by querying ASCII values and converting them to readable characters via the built-in CHR() function against the SYSIBM.SYSDUMMY1 dummy table, which is always accessible and contains a single row for testing purposes. In a real attack, this would be injected into a vulnerable parameter (e.g., login form, search field) to bypass filters and retrieve sensitive data like usernames, passwords, or table contents. The approach is particularly effective in blind injection where boolean-based or union-based methods fail, enabling gradual enumeration of data. Prerequisites include identifying a injectable endpoint via tools like SQLMap or manual testing.

## Requirements

1. Access to a web application or API endpoint vulnerable to SQL injection targeting a DB2 backend.
2. Knowledge of the injection point (e.g., via error-based testing with payloads like ' OR 1=1 --).
3. A SQL client or proxy tool like Burp Suite to craft and send injected queries.
4. Basic understanding of DB2 syntax and ASCII encoding (e.g., CHR(65) returns 'A').

## Defense

- Implement prepared statements and parameterized queries to separate SQL code from user input.
- Use web application firewalls (WAFs) to detect and block common SQL injection patterns, including DB2-specific functions like CHR().
- Enforce least privilege on database accounts to limit query scope (e.g., deny access to SYSIBM tables if possible).
- Enable database logging and monitor for anomalous queries involving system tables or CHR() usage.
- Regularly scan for vulnerabilities using tools like SQLMap or Nessus.

## Objectives

1. Identify and confirm a SQL injection vulnerability in a DB2-connected application.
2. Inject payloads to extract ASCII-based data from the database.
3. Convert extracted numeric values to characters for readable output, enabling further enumeration or exfiltration.
4. Validate successful extraction without alerting defenses.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability

**Context**: Test the target input field to verify it accepts DB2 SQL injection by appending a comment to terminate the query and observe behavior changes, such as error messages or unexpected responses.

**Command** (Use a generic SQL injection test command like [[commands/sqlmap-db2-test]] if available, or manual via proxy):

Manually craft a payload in the vulnerable field, e.g., `username' --` and submit. If the query alters (e.g., bypasses auth), injection is possible.

> This step confirms the endpoint is vulnerable without executing data extraction. Expected output: Authentication bypass or DB2 error revealing version (e.g., "DB2 SQL Error: SQLCODE=-104").

### Step 2: Enumerate Database Information

**Context**: Use a basic injection to confirm DB2 backend and gather schema details, such as current user or database name, to prepare for ASCII extraction.

**Command** (Manual injection example):

Inject: `'; SELECT USER FROM SYSIBM.SYSDUMMY1 --`

> This queries the current database user. Expected output: Response includes username (e.g., via error or page content), confirming DB2 access.

### Step 3: Extract Character Using ASCII Value

**Context**: Inject the core payload to select a character by its ASCII code from the dummy table. This is the key step for blind extraction; repeat for each character position in target data (e.g., to build a password by testing CHR(97) for 'a', etc.). In a full attack, wrap in a conditional like CASE WHEN (condition) THEN CHR(ASCII) ELSE NULL to extract specific data.

**Command** ([[commands/db2-select-character-by-ascii]]):

```sql
select chr(65) from sysibm.sysdummy1
```

> The CHR() function converts the ASCII code (65 for 'A') to the character, selected from the single-row SYSIBM.SYSDUMMY1 table. In injection context: `' UNION SELECT CHR(65) FROM SYSIBM.SYSDUMMY1 --`. Expected output: The character 'A' appears in the response, error, or inferred via boolean/time-based differences. For blind: Use in SUBSTRING extraction, e.g., `AND ASCII(SUBSTRING((SELECT password FROM users LIMIT 1),1,1))=65` to check first char.

### Step 4: Iterate for Data Exfiltration

**Context**: Build on Step 3 to extract full strings by looping through ASCII ranges (32-126) for each position, using conditional logic to confirm matches without direct output.

**Command** (Adapt [[commands/db2-select-character-by-ascii]] for iteration):

For position 1 of a password: Inject payloads testing `CHR(32)` to `CHR(126)` in a boolean condition.

> Expected output: True response (e.g., page loads) when ASCII matches, allowing reconstruction of the full string offline. Success: Full data string (e.g., password) enumerated character-by-character.
