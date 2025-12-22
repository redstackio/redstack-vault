---
id: 9c3ea6e3-47b9-4f22-a645-4737a9ff7443
name: get-sql-instance-domain-verbose
type: command
executor: powershell
data: Get-SQLInstanceDomain -Verbose
output: null
created_at: '2023-04-06T03:56:19.880785+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - sql-server
verified: true
validated: true
---

# get-sql-instance-domain-verbose

## Command

```powershell
Get-SQLInstanceDomain -Verbose
```

## Description

This command enumerates SQL Server instances within the current Windows domain using the SqlServer PowerShell module. It queries domain controllers or SQL Browser services to discover registered instances, useful for mapping database infrastructure during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose | Enables verbose logging to show discovery details and connection attempts | No |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceDomain -Verbose
```

### Without Verbose

```powershell
Get-SQLInstanceDomain
```

## Expected Output

A list of discovered SQL instances, for example:

InstanceName          : SERVER1
ServerName            : SERVER1
InstanceName          : SQLEXPRESS
IsClustered           : False
Version               : 14.0.1000.169

This output can be piped to other commands for further details.

## Related

- [[procedures/Domain-SQL-Server-Discovery]]
- [[commands/get-sql-server-info-from-instances]]
