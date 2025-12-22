---
id: 61aa1952-16cd-47e9-8850-fd44eb4acd53
name: PostgreSQL-Password-Hash-Extraction-via-SQL-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.521362+00:00'
updated_at: '2023-04-10T20:23:12.814965+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/PostgreSQL-injection]]'
  - '[[tags/PostgreSQL-List-Password-Hashes]]'
commands:
  - '[[commands/postgresql-select-usename-passwd-from-pg_shadow]]'
platforms:
  - Web
  - Database
tools: []
validated: true
---

# PostgreSQL-Password-Hash-Extraction-via-SQL-Injection

## Summary

This procedure exploits SQL injection vulnerabilities in web applications connected to PostgreSQL databases to extract password hashes from the pg_shadow system table. By injecting a crafted SQL query, an attacker can retrieve usernames and their corresponding hashed passwords, enabling offline cracking attempts to recover plaintext credentials for further lateral movement or data access.

## Description

PostgreSQL stores user account information, including password hashes, in the pg_shadow system catalog table. This procedure targets web applications with unsanitized user inputs that allow SQL injection, such as login forms or search fields. Once injected, the query bypasses authentication and directly queries pg_shadow to dump sensitive credential data. The extracted hashes are typically in MD5 or SCRAM-SHA-256 format, which can be cracked using tools like Hashcat if weak passwords are used. This technique is effective in scenarios where the application runs with superuser privileges or has access to system tables, potentially exposing database administrator credentials or application users. Success depends on the injection point allowing SELECT privileges on pg_shadow.

## Requirements

1. Valid SQL injection vulnerability in a web application interfacing with PostgreSQL (e.g., via PHP, Python, or Node.js backends).
2. Network access to the vulnerable application endpoint.
3. Basic knowledge of SQL syntax and PostgreSQL schema, including the structure of pg_shadow (columns like usename and passwd).
4. Tools for crafting and sending HTTP requests, such as Burp Suite or sqlmap (though manual injection is covered here).
5. Optional: A proxy or interceptor to capture and modify requests.

## Defense

- Implement prepared statements and parameterized queries in application code to prevent SQL injection.
- Use database roles with least privilege; restrict application access to only necessary tables, excluding system catalogs like pg_shadow.
- Enable PostgreSQL logging for failed queries and monitor for anomalous SELECT statements on system tables.
- Enforce strong password policies and use salted, iterated hashing (e.g., SCRAM-SHA-256) to resist offline cracking.
- Deploy web application firewalls (WAFs) tuned to detect SQL injection patterns, and regularly audit database permissions.

## Objectives

1. Identify and exploit an SQL injection point to execute arbitrary queries against the PostgreSQL database.
2. Retrieve usernames and password hashes from the pg_shadow table.
3. Export the hashes for offline analysis and cracking to obtain plaintext passwords.
4. Use recovered credentials for escalated access, such as logging into the database or pivoting to other systems.

## Instructions

### Step 1: Identify the Injection Point

**Context**: Locate a user-controllable input field in the web application that interacts with the PostgreSQL backend without proper sanitization, such as a search box or login parameter. Test for vulnerability by appending a single quote (') to the input and observing if it causes a SQL error (e.g., syntax error near '') indicating unescaped inputs.

**Command** (Use a tool like curl to test, but focus on manual payload crafting):

No specific command here; use browser or proxy to input `' OR 1=1 --` and check for boolean-based injection success (e.g., all records returned).

> If errors reveal PostgreSQL specifics (e.g., "pg_atoi: error"), confirm the backend. Expected output: Database error messages confirming PostgreSQL and injection feasibility.

### Step 2: Craft and Inject the Extraction Query

**Context**: Once the injection point is confirmed, construct a UNION-based or error-based injection payload to append the SELECT query targeting pg_shadow. This step assumes a UNION injection; adjust for blind or time-based if needed. The goal is to execute the query without disrupting the application's normal response.

**Code** ([[codes/PostgreSQL-Extract-User-Hashes-from-pg_shadow]]):

```sql
SELECT usename, passwd FROM pg_shadow
```

**Command** ([[commands/postgresql-select-usename-passwd-from-pg_shadow]]):

Integrate into HTTP request, e.g., via Burp Repeater: Modify POST parameter like `username=admin' UNION SELECT usename, passwd FROM pg_shadow --`.

> Submit the request. The query retrieves usename (username) and passwd (hashed password). Hashes appear in responses if the column count matches the original query. Expected output: Response body containing usernames and hashes, e.g., `admin | md5a1b2c3d4e5f6...`.

### Step 3: Extract and Verify Output

**Context**: Parse the application's response to isolate the injected query results. Verify the data by checking for valid PostgreSQL usernames (e.g., postgres, app_user) and hash formats (starting with md5 or scram).

No specific command; manually copy results from the response.

> Save extracted data to a file like `pg_shadow_dumps.txt` for cracking. Expected output: List of credential pairs, e.g.,

```
usename: postgres
passwd: md5d41d8cd98f00b204e9800998ecf8427e
usename: appuser
passwd: scram-sha-256:iterations=4096:salt=...
```

If no output, iterate payload (e.g., add LIMIT 1 or use subqueries for blind extraction).

### Step 4: Offline Cracking Preparation

**Context**: Prepare the hashes for cracking tools. This step ensures the data is in a usable format, though actual cracking is a separate procedure.

No command here; format as `username:hash` for tools like Hashcat.

> Expected output: Formatted file ready for input into cracking software, confirming successful extraction by presence of multiple user entries.
