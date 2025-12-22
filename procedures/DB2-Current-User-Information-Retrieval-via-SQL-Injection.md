---
id: 17f8e2a1-90f8-4ee2-a0e7-1bd581948121
name: DB2-Current-User-Information-Retrieval-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.599155+00:00'
updated_at: '2023-04-10T20:21:57.597075+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Information-Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/Current User]]'
  - '[[tags/DB2]]'
  - '[[tags/SQL Injection]]'
  - '[[tags/Database Discovery]]'
commands: []
platforms:
  - Databases
  - DB2
tools: []
validated: true
---

# DB2-Current-User-Information-Retrieval-via-SQL-Injection

## Summary

This procedure demonstrates how to retrieve information about the current user, session user, and system user in a DB2 database through SQL injection. By injecting these queries into a vulnerable application, an attacker can enumerate user privileges and context, aiding in further discovery and potential privilege escalation within the database environment.

## Description

In a typical attack scenario, an application connected to a DB2 database fails to properly sanitize user inputs, allowing SQL injection. The attacker crafts payloads to execute queries against system tables like SYSIBM.SYSDUMMY1 to extract user details. This reveals the effective user under which the application runs, the session-specific user, and the underlying system user. Such information is crucial for mapping database access levels, identifying misconfigurations, and planning subsequent attacks like privilege escalation or data exfiltration. This technique targets DB2-specific functions and is effective in environments where the database handles authentication or session management.

## Requirements

1. Valid access to a web application or interface that interacts with the DB2 database and is vulnerable to SQL injection.
2. Knowledge of SQL injection techniques, including payload construction and evasion of basic filters.
3. Tools for testing and exploiting SQL injection, such as a proxy like Burp Suite or direct input manipulation.
4. Understanding of DB2 syntax and system tables.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to block malicious SQL payloads, using libraries like OWASP ESAPI.
- Use prepared statements or parameterized queries in application code to separate SQL logic from user input.
- Enable database logging for SQL queries and monitor for anomalies, such as unexpected SELECTs on system tables.
- Regularly audit application code and database configurations for injection vulnerabilities, and apply patches to DB2 and the application stack.
- Deploy web application firewalls (WAFs) tuned to detect SQL injection patterns targeting DB2-specific queries.

## Objectives

1. Inject SQL queries to retrieve the current database user, session user, and system user.
2. Analyze the retrieved information to understand the application's execution context and privileges.
3. Use the insights to inform further database reconnaissance or exploitation.

## Instructions

### Step 1: Identify SQL Injection Point

**Context**: Locate an input field in the application (e.g., login form, search box) that is vulnerable to SQL injection. Test with basic payloads like ' OR 1=1 -- to confirm injection is possible.

> Probe the endpoint using manual input or automated tools to ensure the injection alters the query behavior without breaking the application.

### Step 2: Craft and Inject User Enumeration Payload

**Context**: Construct a payload that appends the DB2 user queries to the original SQL statement. This step executes the queries to fetch user details, leveraging the SYSIBM.SYSDUMMY1 dummy table which requires no real data.

**Code** ([[codes/DB2-Retrieve-Current-User-Session-and-System-Info]]):

```sql
select user from sysibm.sysdummy1;
select session_user from sysibm.sysdummy1;
select system_user from sysibm.sysdummy1;
```

> Inject the payload into the vulnerable parameter, e.g., via a UNION-based injection if the original query returns results: ' UNION SELECT user FROM sysibm.sysdummy1 --. The queries return the current user (effective database user), session_user (authorization ID for the session), and system_user (OS-level user). Success is indicated by the application displaying or leaking these values in responses, error messages, or logs. If no output, check for blind injection techniques like time-based delays.
