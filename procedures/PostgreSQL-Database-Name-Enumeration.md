---
type: procedure
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL-Database-Name]]'
  - '[[tags/PostgreSQL-injection]]'
commands:
  - '[[commands/postgresql-select-current-database]]'
tools: []
platforms:
  - PostgreSQL
skill_level: intermediate
impact_level: medium
detection_risk: high
verified: true
validated: true
---

# PostgreSQL-Database-Name-Enumeration

## Summary

This procedure demonstrates how to enumerate the name of the current database in a PostgreSQL server through SQL injection or direct query execution. It is useful in scenarios where an attacker has identified an injection point or gained limited query access, allowing discovery of database structure for further exploitation such as data exfiltration or privilege escalation.

## Description

PostgreSQL Database Name Enumeration involves injecting or executing SQL queries to reveal the current database name, providing critical information about the target's environment. This technique exploits vulnerabilities like insufficient input sanitization in web applications connected to PostgreSQL, enabling attackers to map the database schema. In a typical attack scenario, this occurs after initial access via SQL injection (SQLi) in a vulnerable parameter, such as a login form or search field. The extracted database name can guide subsequent attacks, like targeting specific tables or escalating to remote code execution. This procedure assumes the attacker has a vector for SQL execution, such as through a web app backend, and focuses on the query to retrieve the database name using the built-in `current_database()` function.

## Requirements

1. Network access to the PostgreSQL server or a vulnerable application frontend (e.g., via HTTP/HTTPS).
2. Identification of an SQL injection point (e.g., via error-based or blind SQLi testing).
3. Knowledge of PostgreSQL SQL syntax and basic database structure.
4. Tools for injecting queries, such as a web proxy like Burp Suite or direct psql client access if credentials are obtained.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements and parameterized queries in all application code to prevent SQL injection.
- Use web application firewalls (WAFs) to detect and block anomalous SQL patterns in inputs.
- Enable PostgreSQL logging for all queries and monitor for suspicious activity, such as repeated `current_database()` executions or injection attempts.
- Regularly audit database access logs and restrict query privileges to least necessary for application functions.

## Objectives

1. Extract the name of the current database from a PostgreSQL server.
2. Use the database name to inform further reconnaissance or exploitation of sensitive data.
3. Validate successful injection or query execution without triggering alerts.

## Instructions

### Step 1: Identify SQL Injection Point

**Context**: Before enumerating the database name, confirm an injectable parameter in the target application, such as a URL parameter, form input, or API endpoint. This step ensures the query can be delivered effectively.

Use error-based or time-based SQLi testing to verify vulnerability. For example, append a single quote (`'`) to inputs and observe database errors revealing PostgreSQL specifics.

> If no injection point is found, this procedure cannot proceed. Tools like sqlmap can automate detection but are not required here.

### Step 2: Inject or Execute the Database Name Query

**Context**: Once an injection vector is confirmed, craft a payload to execute `SELECT current_database()`. This reveals the active database name, which might indicate the application's data store (e.g., 'production_db'). In blind SQLi, extract results via conditional responses; in error-based, leverage error messages.

**Command** ([[commands/postgresql-select-current-database]]):

For direct psql access:
```sql
SELECT current_database();
```

For web-based injection, union or stacked query example (adapt to vulnerability type):
```sql
'; SELECT current_database(); --
```

**Code** ([[codes/postgresql-current-database-query]]):

Embed the query in the injection payload as needed.

> This command returns the database name as a string. In a successful injection, the response might display it directly, in an error, or inferred via boolean/time delays in blind scenarios. If using a tool like sqlmap, automate with: `sqlmap -u "http://target.com/page?id=1" --dbms=postgresql --technique=B --code=1` to dump database info.

### Step 3: Verify and Document Results

**Context**: Confirm the output provides the database name and assess if it enables next steps, like enumerating tables with `SELECT table_name FROM information_schema.tables WHERE table_schema = current_schema();`.

Parse the response for the database name (e.g., 'mydb'). If extraction fails, refine the payload for encoding or evasion (e.g., using hex: `SELECT current_database()::text;`).

> Success is indicated by a valid database name string. Log the result for chaining into further discovery procedures.
