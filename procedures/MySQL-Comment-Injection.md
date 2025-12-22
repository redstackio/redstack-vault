---
id: b6660d4b-7797-4421-be96-ac0392f7bbc4
name: MySQL-Comment-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.209682+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/MySQL-comment]]'
  - '[[tags/MySQL-Injection]]'
  - sqli
  - injection
commands: []
platforms:
  - Web
  - Linux
  - Database
tools: []
validated: true
---

# MySQL-Comment-Injection

## Summary

MySQL Comment Injection is a SQL injection technique that leverages MySQL's comment syntax to bypass input validation filters and execute unauthorized database commands. By embedding malicious payloads within comments, attackers can obscure keywords that might be blocked by web application firewalls or input sanitization, allowing for data extraction, modification, or privilege escalation in vulnerable MySQL-backed applications.

## Description

This procedure targets web applications connected to MySQL databases where user inputs are directly concatenated into SQL queries without proper parameterization. Attackers identify injectable points, such as login forms or search fields, and use comments to hide parts of the payload. For example, single-line comments (--) can terminate legitimate queries early, while multi-line (/* */) or version-specific (/*! */) comments can encapsulate blocked terms like 'UNION' or 'SELECT'. This is particularly effective against applications that filter specific strings but overlook comment structures. The technique aligns with exploiting public-facing applications and can lead to full database compromise if combined with other SQLi vectors. Prerequisites include a vulnerable endpoint and basic SQL knowledge; it works on MySQL versions supporting these comment types (most modern versions).

## Requirements

1. Access to a web application with a MySQL backend and unsanitized user inputs (e.g., via browser or proxy like Burp Suite).
2. Knowledge of the application's SQL query structure, often inferred through error messages or time-based blind injection.
3. Tools for sending crafted HTTP requests (browser dev tools or [[tools/Burp-Suite]] for interception).
4. Target MySQL version supporting comments (3.23+ for special comments).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and use prepared statements or parameterized queries to separate code from data.
- Deploy web application firewalls (WAFs) configured to detect comment-based obfuscation patterns in SQL payloads.
- Enable MySQL query logging and monitor for anomalous queries containing comment sequences near sensitive operations.
- Regularly audit and patch MySQL installations, and use least-privilege database accounts to limit impact.

## Objectives

1. Identify and confirm a SQL injection vulnerability in a MySQL-connected application.
2. Bypass input filters using comment syntax to inject and execute malicious SQL payloads.
3. Achieve unauthorized data access, modification, or command execution on the database.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Probe the target application to find inputs that influence SQL queries, such as search boxes or authentication forms. Look for error messages revealing MySQL usage or behaviors indicating injection (e.g., unexpected results).

Test with a classic SQLi payload to confirm vulnerability:

```sql
' OR '1'='1
```

> Submit this via the input field. If the application returns all records or logs a MySQL error, it's likely vulnerable. This step verifies the injection point without comments yet.

### Step 2: Understand and Craft Comment Payloads

**Context**: MySQL supports three comment types to obfuscate payloads: single-line (--), multi-line (/* */), and version-specific (/*! */). Use these to bypass filters that block keywords like 'UNION SELECT'. The space after -- is required to activate the comment.

Embed the example syntax in your payload. For instance, to extract database version while bypassing a filter on 'VERSION()':

**Code** ([[codes/MySQL-Comment-Syntax-Examples]]):

```sql
# MYSQL Comment
-- comment [Note the space after the double dash]
/* MYSQL Comment */
/*! MYSQL Special SQL */
/*!32302 10*/ Comment for MYSQL version 3.23.02
```

> Adapt this into an injection: `' UNION SELECT version()--`. The -- comments out the rest of the query. For multi-line: `' UNION /*filter bypass*/ SELECT database() */`. Special comments like /*!50000 version() */ execute only on MySQL 5.0+, ignoring them on older versions. Test iteratively to see which evades filters.

### Step 3: Execute Injection and Verify

**Context**: Submit the crafted payload via the vulnerable input and observe responses. Use blind techniques if no direct output (e.g., time delays with SLEEP()).

Example payload for data exfiltration:

```sql
' UNION SELECT user(),database()--
```

> If successful, the response may leak user and database names. For blind confirmation: `' AND IF(1=1,SLEEP(5),0)--`. A 5-second delay indicates execution. Escalate by dumping tables: `' UNION SELECT table_name FROM information_schema.tables--`.

### Step 4: Escalate and Extract Data

**Context**: Once injection works, chain comments with advanced queries to dump sensitive data or execute system commands if the DB user has FILE privileges.

Example for file read (if enabled):

```sql
' UNION SELECT LOAD_FILE('/etc/passwd')--
```

> Expected success: Data appears in the application response. If errors occur, adjust comments to close the query properly. Always verify with low-impact tests first to avoid detection.
