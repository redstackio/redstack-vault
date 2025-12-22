---
id: 46226e4e-c5ae-4ddf-bd56-3da0d0e8759c
name: Retrieve-MSSQL-User-Information-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.522484+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/MSSQL]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/User-Discovery]]'
commands:
  - '[[commands/mssql-select-current-user]]'
  - '[[commands/mssql-select-user-name]]'
  - '[[commands/mssql-select-system-user]]'
  - '[[commands/mssql-select-user]]'
platforms:
  - Database
  - MSSQL
tools: []
validated: true
---

# Retrieve-MSSQL-User-Information-via-SQL-Injection

## Summary

This procedure demonstrates how to extract user information from a Microsoft SQL Server (MSSQL) database through SQL injection vulnerabilities. By injecting specific SQL queries, an attacker can retrieve details about the current database user, system user, and other account identifiers, aiding in reconnaissance, privilege assessment, and further exploitation such as privilege escalation or lateral movement.

## Description

In scenarios where an application connected to an MSSQL backend is vulnerable to SQL injection, attackers can append or replace queries to probe database metadata. This procedure focuses on querying built-in MSSQL functions and variables like CURRENT_USER, user_name(), system_user, and user to gather account details from the sysusers table or equivalent system views. These queries reveal the context of the database session, including the effective user for the connection, which is crucial for understanding access levels (e.g., sa vs. limited user). The technique assumes blind or error-based SQL injection points, such as in login forms, search fields, or API endpoints. Success depends on the injection point allowing SELECT statements without immediate detection. This information can inform subsequent attacks like credential dumping or exploiting misconfigurations in user privileges.

## Requirements

1. Valid SQL injection vulnerability in an application interfacing with MSSQL (e.g., union-based, blind boolean, or time-based).
2. Network access to the target application and underlying database port (default TCP 1433).
3. Tools for injecting and observing SQL payloads, such as a proxy (e.g., Burp Suite) or direct DB client if credentials are obtained.
4. Basic knowledge of MSSQL syntax and injection evasion techniques (e.g., comment obfuscation).

## Defense

- Implement strict input validation and sanitization to block SQL injection attempts, using prepared statements or ORM frameworks.
- Use least-privilege database accounts for application connections to limit information disclosure.
- Enable SQL Server auditing for suspicious queries targeting system views like sysusers or functions like CURRENT_USER.
- Deploy web application firewalls (WAFs) tuned to detect common SQLi patterns, and monitor database logs for anomalous SELECT statements on user metadata.

## Objectives

1. Identify the current database user executing queries to assess session privileges.
2. Enumerate system and login user details for reconnaissance.
3. Gather sufficient account information to support privilege escalation or targeted attacks.
4. Validate injection success without alerting defenses.

## Instructions

### Step 1: Inject Query for Current Database User

**Context**: This step retrieves the name of the user currently logged into the database session, helping determine the effective privileges available through the injection point. Use this in a blind injection by observing response differences or errors.

**Command** ([[commands/mssql-select-current-user]]):
```sql
SELECT CURRENT_USER
```

> This query returns the database user name for the current session. If injected successfully, the output will appear in the application's response (e.g., via union select or error message). If no output, confirm via boolean/time-based techniques (e.g., append AND 1=1 after injection).

### Step 2: Inject Query for Current User Name Function

**Context**: The user_name() function provides the current user's database username, which may differ from the system login in impersonation scenarios. This is useful for verifying if the app runs under a service account.

**Command** ([[commands/mssql-select-user-name]]):
```sql
SELECT user_name()
```

> Expect a single value representing the username. In union-based injection, stack it with legitimate query columns (e.g., SELECT col1, user_name() FROM table). Success is indicated by the username appearing in the response without syntax errors.

### Step 3: Inject Query for System User

**Context**: system_user returns the Windows login account executing the SQL command, revealing OS-level context (e.g., DOMAIN\username). This aids in mapping the database host's environment for lateral movement.

**Command** ([[commands/mssql-select-system-user]]):
```sql
SELECT system_user
```

> Output is the full system login string. If the database is not integrated with Windows auth, it may return NULL or the SQL login. Use in error-based injection to force output via RAISERROR if needed.

### Step 4: Inject Query for User Variable

**Context**: The 'user' variable is synonymous with CURRENT_USER in MSSQL, providing redundant confirmation of the database user. Execute this to cross-verify results from Step 1.

**Command** ([[commands/mssql-select-user]]):
```sql
SELECT user
```

> Returns the same as CURRENT_USER. This step validates consistency across queries and can be batched with others for efficiency in a single injection payload.

### Step 5: Combine Queries for Comprehensive Enumeration

**Context**: To minimize injection attempts, batch all queries using the provided code snippet. This retrieves all user details in one payload, reducing detection risk from multiple probes.

**Code** ([[codes/mssql-user-information-queries]]):
```sql
SELECT CURRENT_USER
SELECT user_name();
SELECT system_user;
SELECT user;
```

> Execute via multi-statement injection (if supported, e.g., ; separated). Expected results: Multiple result sets with user details. If blind, use conditional logic to infer each output (e.g., IF (SELECT CURRENT_USER)='sa' THEN sleep(5)).

### Step 6: Analyze and Escalate

**Context**: Review outputs to identify high-privilege users (e.g., 'sa'). If admin access is confirmed, proceed to dump more data (e.g., SELECT * FROM sys.sql_logins).

> No specific command; manually interpret results. Decision point: If user is low-priv, attempt privilege escalation via other injections; else, exploit for data exfiltration.
