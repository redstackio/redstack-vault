---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:33.646275+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/MSSQL Injection]]'
  - '[[tags/MSSQL List databases]]'
commands:
  - '[[commands/mssql-list-all-databases]]'
  - '[[commands/mssql-list-system-databases]]'
  - '[[commands/mssql-concatenate-database-names]]'
platforms:
  - Windows
  - MSSQL
tools: []
validated: true
---

# MSSQL-Database-Enumeration

## Summary

MSSQL Database Enumeration involves injecting SQL queries into a vulnerable MSSQL server to list all databases, including system and user databases. This technique is commonly used during reconnaissance to map the database structure and identify potential targets for further exploitation, such as extracting sensitive data from specific databases.

## Description

This procedure targets Microsoft SQL Server instances vulnerable to SQL injection, allowing an attacker to execute arbitrary queries to enumerate databases. By injecting queries into input fields, URLs, or forms that interact with the database, the attacker can retrieve a list of all databases on the server. This provides insight into the target's data architecture, revealing system databases like master and tempdb, as well as any custom user databases containing valuable information. The technique relies on blind or error-based SQL injection to bypass authentication and execute system catalog queries like those against sysdatabases. It is effective against web applications connected to MSSQL backends and can be performed manually or with tools like sqlmap. Prerequisites include identifying an injectable parameter and having network access to the target service, typically on port 1433 or via a web interface.

## Requirements

1. Network access to the target MSSQL server or a web application vulnerable to SQL injection that queries the database.
2. Knowledge of SQL injection techniques, including crafting payloads to execute system queries.
3. A SQL client tool such as sqlcmd, or a web proxy like Burp Suite for manual injection, or automated tools like sqlmap for exploitation.
4. Basic understanding of MSSQL system tables, such as master..sysdatabases.

## Defense

Defensive measures and detection strategies:

- Implement input validation and parameterized queries to prevent SQL injection attacks.
- Use web application firewalls (WAFs) to detect and block anomalous SQL payloads.
- Limit database user privileges to the minimum necessary, avoiding excessive permissions for application accounts.
- Enable SQL Server logging and monitor for unusual queries accessing system catalogs like sysdatabases.
- Regularly audit database configurations and apply patches for known vulnerabilities.

## Objectives

1. Identify all databases hosted on the target MSSQL server.
2. Distinguish between system and user databases to prioritize attack paths.
3. Gather intelligence on the database environment to inform subsequent enumeration or exploitation steps.

## Instructions

### Step 1: List All Databases Using sysdatabases

**Context**: This step executes a basic query to retrieve the names of all databases in the SQL Server instance, providing a complete inventory without additional processing. It targets the master database's sysdatabases view, which is accessible via injection if the vulnerability allows SELECT privileges.

**Command** ([[commands/mssql-list-all-databases]]):
```sql
SELECT name FROM master..sysdatabases;
```

> This query returns a result set with the 'name' column listing all databases. Use this in a SQL injection payload, such as appending ' UNION SELECT name FROM master..sysdatabases--' to an injectable parameter. If successful, the output will display database names in the application's response or error message.

### Step 2: Enumerate System Databases Using DB_NAME

**Context**: This step focuses on system databases by using the DB_NAME function with database IDs (N=0 for master, N=1 for tempdb, etc.). It is useful for verifying the presence of default system databases and understanding the server's configuration, especially in blind injection scenarios where full lists may be truncated.

**Command** ([[commands/mssql-list-system-databases]]):
```sql
SELECT DB_NAME(N); -- for N = 0, 1, 2, ...
```

> Replace N with sequential integers starting from 0 to query each database by ID. Inject this payload similarly, e.g., ' AND (SELECT DB_NAME(0))='master'--'. Success is indicated by matching known system database names like 'master', 'tempdb', 'model', and 'msdb' in the response.

### Step 3: Concatenate Database Names for Compact Output

**Context**: For SQL Server 2017 and later, this step aggregates all database names into a single delimited string, which is ideal for scenarios where response sizes are limited or when extracting data via time-based or boolean blind injection. It simplifies parsing multiple names from a constrained output.

**Command** ([[commands/mssql-concatenate-database-names]]):
```sql
SELECT STRING_AGG(name, ', ') FROM master..sysdatabases;
```

> This query uses the STRING_AGG function to join database names with a comma-space delimiter. Customize the delimiter as needed (e.g., ';'). Inject as ' UNION SELECT STRING_AGG(name, ', ') FROM master..sysdatabases--'. The output will be a single string like 'master, tempdb, model, msdb, userdb'.
