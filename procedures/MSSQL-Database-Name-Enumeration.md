---
id: a9a8733b-9eea-4153-92c2-bde94f066a9c
name: MSSQL-Database-Name-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.614996+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/MSSQL]]'
  - '[[tags/Database-Enumeration]]'
  - '[[tags/SQL-Injection]]'
commands:
  - '[[commands/mssql-select-db-name]]'
platforms:
  - Windows
  - Database
tools: []
validated: true
---

# MSSQL-Database-Name-Enumeration

## Summary

This procedure demonstrates how to enumerate the name of the current Microsoft SQL Server (MSSQL) database through SQL injection or direct query execution. It is typically used during reconnaissance to map the target database environment, identify potential data stores, and inform subsequent attacks such as targeted data extraction or privilege escalation.

## Description

MSSQL Database Name Enumeration involves injecting or executing a SQL query to retrieve the name of the active database instance. This technique exploits vulnerabilities in web applications or direct database access to reveal internal configuration details. In an attack scenario, an adversary with access to a SQL injection point (e.g., via an unauthenticated web form) can append the query to extract sensitive system information without authentication. The query targets the DB_NAME() function, which returns the current database context. This information aids in understanding the target's data architecture, such as distinguishing between user databases, system databases like 'master' or 'tempdb', and custom application databases. The procedure assumes a vulnerable input field susceptible to SQL injection and focuses on blind or error-based injection methods where output is inferred from application responses.

## Requirements

1. Access to a web application or endpoint vulnerable to SQL injection (e.g., login form, search field).
2. Knowledge of MSSQL syntax and injection techniques, including union-based or boolean-based methods.
3. Tools for testing injections, such as a browser, proxy like Burp Suite, or sqlmap.
4. Network connectivity to the target MSSQL server (default port 1433).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on all user inputs to block malicious SQL payloads.
- Use parameterized queries or prepared statements in application code to prevent injection attacks.
- Enable SQL Server auditing to log query executions and monitor for anomalous SELECT statements targeting system functions like DB_NAME().
- Deploy web application firewalls (WAFs) to detect and block common SQL injection patterns.
- Regularly scan for vulnerabilities using tools like SQLMap or Nessus.

## Objectives

1. Extract the name of the current MSSQL database to map the target environment.
2. Confirm the presence of a vulnerable injection point.
3. Gather intelligence for follow-on discovery or exploitation activities.

## Instructions

### Step 1: Identify the SQL Injection Point

**Context**: Locate a user input field in the target application that accepts SQL queries without proper sanitization, such as a search box or login form. Test for vulnerability using a single quote (') to trigger errors, confirming MSSQL as the backend if error messages reveal server details.

**Command** ([[commands/mssql-select-db-name]]):

Use a basic injection test like appending `' OR 1=1 --` to bypass authentication or enumerate basics.

> If an error like "Unclosed quotation mark after the character string" appears, the endpoint is vulnerable to SQLi. This step verifies injectability before proceeding to enumeration.

### Step 2: Inject the Database Name Query

**Context**: Once the injection point is confirmed, craft a payload to execute the DB_NAME() function. This can be done via union-based injection if the query returns visible output, or boolean-based if blind. The goal is to append the query to the original statement without disrupting it.

**Command** ([[commands/mssql-select-db-name]]):
```sql
'; SELECT DB_NAME() --
```

> Inject this payload into the vulnerable parameter. For union-based, ensure column count matches (e.g., `UNION SELECT DB_NAME() --`). Expected response includes the database name in the output or inferred via time delays in blind injection. Success is indicated by the application echoing or behaving as if the query executed, revealing names like 'AdventureWorks' or 'master'.

### Step 3: Verify and Extract Output

**Context**: Analyze the application's response for the database name. In error-based injection, the name may appear in stack traces; in union-based, it concatenates to legitimate results.

> If the name is retrieved (e.g., 'MyAppDB'), document it for further enumeration like table listing via `SELECT name FROM sys.databases`. If no output, refine the payload for stacked queries (`;`) or use tools like sqlmap for automation: `sqlmap -u "http://target.com/search?q=1" --dbms=mssql --technique=B --dbs`.
