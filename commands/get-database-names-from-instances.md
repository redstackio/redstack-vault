---
id: 036f1b08-a756-4010-92ec-25d56b5d35cb
name: get-database-names-from-instances
type: command
executor: powershell
data: Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
output: null
created_at: '2023-04-06T03:56:19.794893+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - sql-server
verified: true
validated: true
---

# get-database-names-from-instances

## Command

```powershell
Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
```

## Description

This command enumerates user databases on discovered SQL instances by piping instance data. The -NoDefaults flag excludes system databases, focusing on custom ones that may contain sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -NoDefaults (on Get-SQLDatabase) | Excludes default system databases like master and tempdb | No |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceDomain | Get-SQLDatabase -NoDefaults
```

### For Specific Instance

```powershell
$instance = Get-SQLInstanceDomain | Select-Object -First 1; $instance | Get-SQLDatabase -NoDefaults
```

## Expected Output

List of databases per instance, for example:

InstanceName : SERVER1
Name         : HR_Database
Name         : Finance_Prod

This reveals potential targets for data access attempts.

## Related

- [[procedures/Domain-SQL-Server-Discovery]]
- [[commands/get-sql-server-info-from-instances]]
