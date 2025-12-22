---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL]]'
  - '[[tags/SQL-Injection]]'
  - '[[tags/User-Enumeration]]'
commands:
  - '[[commands/postgresql-select-current-user]]'
  - '[[commands/postgresql-select-getpgusername]]'
  - '[[commands/postgresql-select-session-user]]'
  - '[[commands/postgresql-list-all-postgresql-users]]'
  - '[[commands/postgresql-select-user]]'
platforms:
  - Database
  - PostgreSQL
tools: []
verified: true
validated: true
---

# PostgreSQL-Current-User-Information-Gathering

## Summary

This procedure outlines how to gather information about the current user and all users in a PostgreSQL database via SQL injection. By injecting targeted SQL queries into vulnerable input fields, an attacker can extract user details to assess access levels, identify administrative accounts, and plan privilege escalation or further database compromise.

## Description

In a typical attack scenario, an attacker identifies a SQL injection vulnerability in a web application connected to a PostgreSQL backend. Through blind or error-based injection, they execute queries to retrieve the current session's user context and enumerate all database users. This reveals the attacker's effective privileges (e.g., superuser vs. regular user) and potential targets for credential attacks. The technique leverages PostgreSQL's built-in functions and system catalogs like pg_user. Success depends on the injection point allowing SELECT statements and the application's error handling exposing results. This is commonly used in web penetration testing to map database permissions without direct console access.

## Requirements

1. Valid SQL injection vulnerability in a web application or API endpoint connected to PostgreSQL.
2. Knowledge of the injection point (e.g., login form, search field) and basic SQL syntax.
3. Tools for crafting and sending payloads, such as Burp Suite or sqlmap.
4. Network access to the target application.

## Defense

- Implement prepared statements and parameterized queries to sanitize inputs and prevent injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns.
- Apply least privilege principles: Limit database user permissions and avoid running applications as superuser.
- Enable PostgreSQL logging for failed queries and monitor for unusual SELECT patterns on system tables.

## Objectives

1. Identify the current database user executing the injected queries.
2. Enumerate all users in the PostgreSQL cluster to map potential privilege escalation paths.
3. Assess the access level of the compromised session for further exploitation.

## Instructions

### Step 1: Inject Query to Retrieve Current User

**Context**: Start by determining the name of the user under which the injected queries execute. This helps understand the session's privileges. Use a basic injection payload to append the query to an existing SQL statement, such as in a login or search form.

**Command** ([[commands/postgresql-select-current-user]]):
```sql
SELECT current_user;
```

> This query returns the name of the user executing the current statement. In an injection context, wrap it in a payload like `' OR 1=1; SELECT current_user; --` to bypass authentication and execute. Expected output: A single value like "postgres" or "app_user", often reflected in application errors or responses.

### Step 2: Inject Query to Retrieve Session User

**Context**: Verify the original session owner, which may differ from the current user if role switching occurred. This is useful for detecting impersonation or role-based access.

**Command** ([[commands/postgresql-select-session-user]]):
```sql
SELECT session_user;
```

> Append to an injectable parameter, e.g., `' UNION SELECT session_user; --`. Expected output: The session owner's username, such as "webapp", helping identify the application's default user.

### Step 3: Inject Query to Retrieve Current Username via Function

**Context**: Use PostgreSQL's built-in function for an alternative way to get the current user, which can bypass restrictions on direct SELECT statements in some hardened environments.

**Command** ([[commands/postgresql-select-getpgusername]]):
```sql
SELECT getpgusername();
```

> Inject as `' OR getpgusername()='admin'; --` or in a UNION-based attack. Expected output: The current username, confirming consistency with prior queries and revealing any function-level restrictions.

### Step 4: Inject Query to List All Users

**Context**: Enumerate all database users to identify high-privilege accounts like superusers. This expands reconnaissance beyond the current session.

**Command** ([[commands/postgresql-list-all-postgresql-users]]):
```sql
SELECT usename FROM pg_user;
```

> Use a blind injection technique if outputs aren't visible, or UNION to stack results: `' UNION SELECT usename FROM pg_user; --`. Expected output: A list of usernames (e.g., postgres, app_user, readonly_user), including roles and potential targets for further attacks.

### Step 5: Cross-Verify with Basic User Query

**Context**: Perform a quick check using the simplest query alias to validate results and ensure the injection is stable. This can serve as a baseline for more complex enumerations.

**Command** ([[commands/postgresql-select-user]]):
```sql
SELECT user;
```

> Equivalent to current_user; inject as `' OR 1=1; SELECT user; --`. Expected output: Matches the current user from Step 1, confirming query execution without errors.

### Step 6: Compile All Queries for Comprehensive Gathering

**Context**: For efficiency in automated tools like sqlmap, combine queries into a single injectable block to retrieve all information at once. This reduces multiple injection attempts.

**Code** ([[codes/PostgreSQL-User-Enumeration-Queries]]):

> Execute the combined queries via a stacked injection: `' ; [queries here] ; --`. Expected output: Multiple result sets showing current user, session user, and full user list, enabling quick privilege assessment.
