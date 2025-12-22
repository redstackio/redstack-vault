---
id: a22b42b3-365a-472d-9299-24c8a53e8294
name: PostgreSQL-Privilege-Escalation-via-User-Enumeration
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.573427+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/PostgreSQL]]'
  - '[[tags/Privilege Escalation]]'
  - '[[tags/SQL Injection]]'
  - '[[tags/Database Enumeration]]'
commands:
  - '[[commands/postgresql-list-users-and-privileges]]'
platforms:
  - Linux
  - Database
tools: []
validated: true
---

# PostgreSQL-Privilege-Escalation-via-User-Enumeration

## Summary

This procedure demonstrates how to escalate privileges in a PostgreSQL database by first enumerating users and their privileges to identify potential superusers or misconfigurations, then exploiting vulnerabilities such as SQL injection to execute privileged actions. It is commonly used in scenarios where initial low-privilege access to the database is obtained, allowing attackers to map the privilege landscape and pivot to higher access for data exfiltration or further system compromise.

## Description

PostgreSQL privilege escalation involves exploiting database vulnerabilities, such as SQL injection in web applications connected to the database, to execute unauthorized queries that reveal or elevate user privileges. Once initial access is gained (e.g., via a vulnerable application), attackers enumerate database users, roles, and permissions using system catalogs like pg_user. This reveals superusers (usesuper=true) or users with create database privileges (usecreatedb=true), which can be targeted for credential dumping or role assumption. In a realistic attack, this leads to actions like creating backdoor users, modifying data, or executing OS commands if the database runs with elevated privileges. The target environment is typically a Linux-hosted PostgreSQL server (version 9.x+), accessible via network or local socket, often in web application backends.

## Requirements

1. Network or local access to the PostgreSQL instance (port 5432 TCP or Unix socket).
2. Valid low-privilege credentials or SQL injection point in a connected application.
3. Installed PostgreSQL client tools like psql on the attacker's machine or compromised host.
4. Knowledge of SQL syntax and PostgreSQL system catalogs.

## Defense

- Implement strict input validation and prepared statements in applications to prevent SQL injection.
- Regularly apply security patches to PostgreSQL to address known privilege escalation vulnerabilities.
- Use role-based access control (RBAC) with least privilege principles; avoid granting superuser rights unnecessarily.
- Enable logging of all database queries and monitor for anomalous privilege checks or user enumerations.
- Deploy database activity monitoring (DAM) tools to detect unauthorized access to system catalogs like pg_user.

## Objectives

1. Enumerate database users and their privileges to identify escalation targets.
2. Exploit misconfigurations or injections to assume higher privileges.
3. Perform unauthorized actions such as data extraction or user creation.

## Instructions

### Step 1: Connect to the PostgreSQL Database

**Context**: Establish a connection to the target PostgreSQL instance using a low-privilege account or via an SQL injection vector. This step verifies access and sets the stage for enumeration. Use psql if direct access is available, or inject via a web app proxy like Burp Suite.

**Command** ([[commands/postgresql-connect]]):
```bash
psql -h $_HOST -p $_PORT -U $_USERNAME -d $_DATABASE
```

> This connects to the database. Replace placeholders with target details (e.g., host=localhost, port=5432, username=app_user, database=webapp). Expected output includes a prompt like 'webapp=>', confirming connection. If using SQL injection, craft a payload like ' UNION SELECT ...' to execute from the app.

### Step 2: Enumerate Users and Privileges

**Context**: Query the pg_user system catalog to list all users, their superuser status, database creation privileges, and catalog update abilities. This identifies high-privilege accounts for targeting in escalation attempts, such as impersonating a superuser via injection.

**Command** ([[commands/postgresql-list-users-and-privileges]]):
```sql
SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user;
```

> Execute this query within the psql session or inject it. It retrieves user data from pg_user. Expected output is a table showing usernames and privilege flags (e.g., 'postgres | t | t | t' for a superuser). Look for 't' (true) in usesuper to prioritize targets. If no superusers are visible, check pg_roles for additional details.

### Step 3: Attempt Privilege Escalation via Injection

**Context**: If a SQL injection vulnerability exists, craft a payload to execute privileged actions, such as creating a new superuser or dumping sensitive data. This builds on the enumeration to exploit identified weak points.

**Command** ([[commands/postgresql-create-superuser-injection]]):
```sql
'; CREATE USER attacker WITH SUPERUSER PASSWORD 'weakpass'; --
```

> Append this to an injectable query (e.g., in a login form). It creates a new superuser. Expected output depends on the injection point; success is confirmed by logging in as the new user. If blocked, use enumerated privileges to pivot (e.g., if usecreatedb=true, create a database with extended rights).

### Step 4: Verify Escalation and Extract Data

**Context**: Test the escalated privileges by querying sensitive tables or performing restricted actions, confirming success and enabling further objectives like data exfiltration.

**Command** ([[commands/postgresql-dump-sensitive-data]]):
```sql
SELECT * FROM pg_shadow;
```

> Run as the escalated user. pg_shadow contains hashed passwords. Expected output includes user hashes, which can be cracked offline. Success: Access to restricted tables without errors.
