---
id: f13b91fd-829d-43a2-bccd-64780d1a8bf3
name: SQL-Injection-via-POST-Request-with-SQLMap
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:36.314510+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial-Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - sql-injection
  - sqlmap
  - post-request
  - web-exploitation
commands:
  - '[[commands/sqlmap-post-request-injection]]'
platforms:
  - Web
tools:
  - '[[tools/sqlmap]]'
validated: true
---

# SQL-Injection-via-POST-Request-with-SQLMap

## Summary

This procedure uses SQLMap, an automated tool for detecting and exploiting SQL injection vulnerabilities, to target POST requests in web applications. It focuses on injecting malicious SQL payloads into POST data or custom headers like X-Forwarded-For, allowing attackers to extract database information, escalate privileges, or achieve remote code execution on vulnerable backend databases such as MySQL, PostgreSQL, or Oracle.

## Description

SQL injection (SQLi) occurs when user-supplied input is improperly sanitized and concatenated into SQL queries, enabling attackers to manipulate database operations. This procedure targets web forms or APIs that send data via POST requests, where parameters like usernames, passwords, or custom headers can be intercepted and tampered with. SQLMap automates the process by sending crafted payloads to identify injectable points (marked by '*' in examples), fingerprinting the DBMS, enumerating database structure, and dumping sensitive data like user credentials or tables.

In a typical attack scenario, the target is a public-facing web application (e.g., login form) connected to a backend database. Prerequisites include capturing the POST request details using a proxy like Burp Suite. Successful exploitation can lead to data exfiltration or shell access, depending on DBMS privileges. From a business perspective, SQLi can result in data breaches, compliance violations (e.g., GDPR), and financial losses from stolen customer information.

## Requirements

1. Network access to the target web application's URL (e.g., http://example.com/login).
2. SQLMap installed on the attacker's system (Kali Linux pre-installs it; otherwise, clone from GitHub).
3. Captured POST request details, including parameters (e.g., username=admin&password=pass) and any custom headers, obtained via browser developer tools or a proxy like [[tools/Burp-Suite]].
4. Basic knowledge of HTTP requests and SQL syntax for interpreting results.

## Defense

- Implement prepared statements and parameterized queries in application code to separate SQL logic from user input.
- Use web application firewalls (WAFs) like ModSecurity to detect and block anomalous SQL payloads.
- Enforce least privilege on database accounts and regularly audit for vulnerabilities with tools like OWASP ZAP.
- Enable database logging and monitor for unusual queries or connection patterns from web servers.

## Objectives

1. Detect SQL injection vulnerabilities in POST request parameters or headers.
2. Enumerate and dump sensitive data from the backend database.
3. Escalate access to achieve remote shell or arbitrary command execution if possible.

## Instructions

### Step 1: Capture the Target POST Request

**Context**: Identify the exact URL, POST data, and headers of the vulnerable endpoint to prepare for injection testing. This step ensures SQLMap targets the correct injection points without alerting basic defenses.

Use a proxy tool like [[tools/Burp-Suite]] to intercept traffic. Navigate to the login or form page, submit data, and copy the request.

**Expected Output**: A raw HTTP request showing the POST method, URL, data payload (e.g., username=admin&password=pass), and headers (e.g., X-Forwarded-For: 127.0.0.1).

### Step 2: Run SQLMap to Detect and Exploit Injection

**Context**: Execute SQLMap against the captured POST request to automatically test for SQLi vulnerabilities. The tool will probe parameters and headers for injection points, starting with detection and progressing to exploitation if injectable.

**Command** ([[commands/sqlmap-post-request-injection]]):
```bash
sqlmap -u "http://example.com/login" --data "username=admin&password=pass" --headers="X-Forwarded-For:127.0.0.1*" --batch --dbs
```

> This command specifies the target URL (-u), POST data (--data), and a custom header with an injection marker (* in X-Forwarded-For). The --batch flag runs non-interactively, and --dbs enumerates databases upon success. SQLMap will output vulnerability details, DBMS type, and injectable parameters. If successful, it confirms injection (e.g., "Parameter: X-Forwarded-For (Custom header) is vulnerable") and lists databases.

**Expected Output**: Console output from SQLMap, including:
```
[INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
[INFO] Parameter: X-Forwarded-For (Custom header) is vulnerable. Do you want to keep testing the others (if any)? [y/N] (skipped due to --batch)
available databases [2]:
[*] information_schema
[*] webapp_db
```

### Step 3: Dump Data or Escalate

**Context**: If injection is confirmed, extend the attack to extract data or gain further access. This step builds on detection to achieve the procedure's objectives, such as dumping tables or executing OS commands.

Follow up with additional SQLMap flags based on Step 2 output. For example, to dump a specific database:

**Command** ([[commands/sqlmap-post-request-injection]]):
```bash
sqlmap -u "http://example.com/login" --data "username=admin&password=pass" --headers="X-Forwarded-For:127.0.0.1*" -D webapp_db --tables --batch
```

> This extracts table names from the identified database (webapp_db). For data dumping, add --dump; for shell, use --os-shell if privileges allow. Monitor for errors like privilege issues, which may require further enumeration.

**Expected Output**: List of tables (e.g., users, credentials) or dumped data in CSV format, confirming successful exfiltration.
