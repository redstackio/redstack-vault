---
id: d0ec0703-b77a-45e3-bc11-ea5a5c367bc7
name: Retrieve-Server-Principals-with-Sysadmin-Role
type: command
executor: sql
data: >-
  SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE
  IS_SRVROLEMEMBER ('sysadmin',name) = 1
output: null
created_at: '2023-04-06T03:56:20.900610+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - discovery
verified: true
validated: true
---

# Retrieve-Server-Principals-with-Sysadmin-Role

## Command

```sql
SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1
```

## Description

This SQL command queries the MSSQL sys.server_principals system view to list all server principals that are members of the sysadmin fixed server role, providing details on privileged accounts for discovery in security assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query has no user-defined parameters; it is fixed to target the sysadmin role. | N/A |

## Examples

### Basic Usage

Execute directly in a SQL client connected to the MSSQL instance:

```sql
SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1;
GO
```

### Advanced Usage

Combine with output redirection in sqlcmd for logging:

```sql
-- In sqlcmd session
:output sysadmins.csv
SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1;
GO
:output
```

## Expected Output

A tabular result set displaying privileged principals:

name          | type_desc    | is_disabled
--------------|--------------|-------------
sa            | SQL_LOGIN    | 0
DOMAIN\Admin | WINDOWS_LOGIN | 0

Empty results indicate no sysadmin members or insufficient query permissions.

## Related

- [[procedures/Query-MSSQL-Server-for-Sysadmins]]
