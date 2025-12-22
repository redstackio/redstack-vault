---
id: 49198249-9d17-440a-a7ec-5232bdbffe2c
name: grant-java-permissions-to-user
type: command
executor: sql
data: >-
  exec dbms_java.grant_permission('$_USERNAME',
  'SYS:java.io.FilePermission','<<ALL FILES>>','execute');\nexec
  dbms_java.grant_permission('$_USERNAME','SYS:java.lang.RuntimePermission',
  'writeFileDescriptor', '');\nexec
  dbms_java.grant_permission('$_USERNAME','SYS:java.lang.RuntimePermission',
  'readFileDescriptor', '');
output: null
created_at: '2023-04-06T03:56:35.305146+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - oracle
  - java
  - permissions
verified: true
validated: true
---

# grant-java-permissions-to-user

## Command

```sql
exec dbms_java.grant_permission('$_USERNAME', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('$_USERNAME','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('$_USERNAME','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```

## Description

This multi-statement command grants Java file execution and runtime descriptor permissions to a specified database user, enabling potential OS command execution via Java wrappers in Oracle.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target database username (e.g., SCOTT) | Yes |

## Examples

### Basic Usage

```sql
exec dbms_java.grant_permission('SCOTT', 'SYS:java.io.FilePermission','<<ALL FILES>>','execute');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'writeFileDescriptor', '');
exec dbms_java.grant_permission('SCOTT','SYS:java.lang.RuntimePermission', 'readFileDescriptor', '');
```

### Advanced Usage

For a different user:

```sql
exec dbms_java.grant_permission('PUBLIC', 'SYS:java.io.FilePermission','/tmp/*','read,write');
```

## Expected Output

No output on success; errors like ORA-01031 indicate insufficient privileges. Verify with policy queries showing new entries.

## Related

- [[procedures/Oracle-SQL-and-Java-Command-Execution]]
