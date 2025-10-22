---
id: 5ed39934-925d-43c4-be73-08cfa37d9eda
name: PostgreSQL File Read Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:35.941985+00:00'
updated_at: '2023-04-10T20:23:15.880619+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Discovery|TA0007 - Discovery]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[File and Directory Discovery|T1083 - File and Directory Discovery]]'
- '[[File Permissions Modification|T1222 - File Permissions Modification]]'
- '[[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]'
tags:
- '[[PostgreSQL File Read]]'
- '[[PostgreSQL injection]]'
commands:
- '[[Copy data from /etc/passwd into temp table]]'
- '[[Create temp table]]'
- '[[Import /etc/passwd file into PostgreSQL as a large object]]'
- '[[List directory and read file]]'
- '[[List directory contents]]'
- '[[Retrieve all large objects and their data from the pg_largeobject system table]]'
- '[[Retrieve the large object with the specified OID]]'
- '[[Select first row from temp table]]'
---

# PostgreSQL File Read Procedure

## Summary

The PostgreSQL File Read Procedure is used for extracting sensitive data from a PostgreSQL server. This technique involves exploiting a vulnerability in the server that allows for the injection of malicious code. Once the vulnerability is exploited, the attacker can read files from the server, incl

## Description

# Description

The PostgreSQL File Read Procedure is used for extracting sensitive data from a PostgreSQL server. This technique involves exploiting a vulnerability in the server that allows for the injection of malicious code. Once the vulnerability is exploited, the attacker can read files from the server, including configuration files and other sensitive data. This procedure can be used to gain access to confidential information, such as passwords or other credentials, that can be used to further compromise the system.

Technical Explanation: The PostgreSQL File Read Procedure is a type of SQL injection attack that exploits a vulnerability in the PostgreSQL server. By injecting malicious code into the server, the attacker can access and read files from the server. This technique can be used to extract sensitive data, including configuration files and other confidential information.

Business Value: The PostgreSQL File Read Procedure can be used by attackers to gain access to sensitive information that can be used to further compromise the system. This information can be used to steal confidential data, such as passwords or other credentials, and can be used for financial gain or other malicious purposes.

## Requirements

1. Access to a vulnerable PostgreSQL server

1. Knowledge of SQL injection techniques

1. Access to tools for exploiting the vulnerability

## Defense

1. Ensure that the PostgreSQL server is up-to-date with the latest security patches

1. Implement strong access controls and authentication mechanisms to limit access to the server

1. Monitor the server for suspicious activity and implement intrusion detection and prevention measures

## Objectives

1. Extract sensitive data from a PostgreSQL server

1. Gain access to confidential information such as passwords or other credentials

# Instructions

1. This command lists all the files and directories in the current directory of the PostgreSQL server. It then reads the contents of the 'PG_VERSION' file, starting from byte 0 and ending at byte 200.

**Code**: [[select pg_ls_dir('./');
select pg_read_file('PG_VE]]

> The first command 'pg_ls_dir' takes one argument which is the directory path. In this case, './' represents the current directory. The second command 'pg_read_file' takes three arguments: the file name, the starting byte, and the number of bytes to read. In this case, 'PG_VERSION' is the file name, 0 is the starting byte, and 200 is the number of bytes to read. This command is useful for checking the version of PostgreSQL that is currently installed on the server.

**Command** ([[List directory and read file]]):

```bash
select pg_ls_dir('./');
select pg_read_file('PG_VERSION', 0, 200);
```

2. The pg_read_file function allows you to read the contents of a file on the PostgreSQL server's file system. The function takes a single argument, which is the path to the file you want to read. The path can be either relative to the server's data directory or an absolute path. If the file does not exist or the user does not have permission to read it, an error will be thrown.

**Code**: [[pg_read_file]]

> The pg_read_file function can be useful for reading configuration files, logs, or other files stored on the server's file system. However, it is important to use caution when using this function, as it can potentially expose sensitive information or allow unauthorized access to the server's file system.

3. pg_ls_dir [path]

**Code**: [[pg_ls_dir]]

> The 'pg_ls_dir' command is used to list the contents of a directory. It takes an optional argument 'path' which specifies the directory to list. If 'path' is not specified, the current directory is listed. This command can be useful for navigating and exploring the file system.

**Command** ([[List directory contents]]):

```bash
pg_ls_dir /path/to/directory/
```

4. To read server files, use the following command:

**Code**: [[default_role_read_server_files]]

> This command grants the permission to read server files to super users or users in the default role. The command can be used with the file/filepath name as an argument to read the contents of the file/filepath. Note that only users with the required permission can execute this command.

5. To retrieve the first row from a table, first create a temporary table with the desired columns. Then, use the COPY command to populate the temporary table with data from a file. Finally, use the SELECT statement to retrieve the first row from the temporary table. The 'limit 1 offset 0' clause limits the result set to one row and specifies that the first row should be returned. 

**Code**: [[CREATE TABLE temp(t TEXT);
COPY temp FROM '/etc/pa]]

> The CREATE TABLE command creates a new table with the specified columns. The COPY command copies data from a file into a table. The SELECT statement retrieves data from a table based on specified criteria. In this case, the 'limit 1 offset 0' clause limits the result set to one row and specifies that the first row should be returned.

**Command** ([[Create temp table]]):

```bash
CREATE TABLE temp(t TEXT);
```

**Command** ([[Copy data from /etc/passwd into temp table]]):

```bash
COPY temp FROM '/etc/passwd';
```

**Command** ([[Select first row from temp table]]):

```bash
SELECT * FROM temp limit 1 offset 0;
```

6. To import a file as a large object in PostgreSQL, use the lo_import() function followed by the file path. To retrieve a large object, use the lo_get() function followed by the OID returned from the lo_import() function. To retrieve all large objects and their data, query the pg_largeobject system table.

**Code**: [[SELECT lo_import('/etc/passwd'); -- This command i]]

> The lo_import() function creates a new large object in PostgreSQL and returns the OID of the object. The lo_get() function retrieves the data of a large object with the specified OID. The pg_largeobject system table contains information about all large objects in the database, including their OID, size, and data.

**Command** ([[Import /etc/passwd file into PostgreSQL as a large object]]):

```bash
SELECT lo_import('/etc/passwd');
```

**Command** ([[Retrieve the large object with the specified OID]]):

```bash
SELECT lo_get(16420);
```

**Command** ([[Retrieve all large objects and their data from the pg_largeobject system table]]):

```bash
SELECT * from pg_largeobject;
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Discovery|TA0007 - Discovery]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[File and Directory Discovery|T1083 - File and Directory Discovery]]
- [[File Permissions Modification|T1222 - File Permissions Modification]]
- [[Signed Binary Proxy Execution|T1218 - Signed Binary Proxy Execution]]

## Commands Used

- [[Copy data from /etc/passwd into temp table]]
- [[Create temp table]]
- [[Import /etc/passwd file into PostgreSQL as a large object]]
- [[List directory and read file]]
- [[List directory contents]]
- [[Retrieve all large objects and their data from the pg_largeobject system table]]
- [[Retrieve the large object with the specified OID]]
- [[Select first row from temp table]]

## Tags

- [[PostgreSQL File Read]]
- [[PostgreSQL injection]]
