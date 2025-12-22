---
type: command
executor: powershell
data: Get-SQLInstanceLocal
platforms:
  - Windows
tags:
  - discovery
  - mssql
  - sql-server
verified: true
validated: true
---

# get-local-sql-instances-powershell

## Command

```powershell
Get-SQLInstanceLocal
```

## Description

This PowerShell command enumerates all locally installed Microsoft SQL Server instances, retrieving details such as instance names, versions, editions, and service states. It is ideal for initial discovery during penetration testing to identify database targets on a compromised Windows host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | No parameters required; scans local system by default. | No |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceLocal
```

### Advanced Usage

For verbose output or filtering (if function supports extensions):
```powershell
Get-SQLInstanceLocal | Select-Object Name, Version, Edition, IsRunning
```

## Expected Output

A table or list of SQL instances, for example:

InstanceName : MSSQLSERVER
Version      : 15.0.2000.5
Edition      : Enterprise Edition
IsClustered  : False
IsRunning    : True

If no instances:
No SQL Server instances found on this machine.

## Related

- [[procedures/Discover-Local-MSSQL-Server-Instances]]
