---
type: command
executor: powershell
data: Get-SQLInstanceBroadcast -Verbose
output: null
created_at: '2023-04-06T03:56:19.826486+00:00'
updated_at: '2023-04-10T20:36:47.895751+00:00'
platforms:
  - Windows
tags:
  - discovery
  - mssql
  - network-scan
verified: true
validated: true
---

# get-sqlinstance-broadcast

## Command

```powershell
Get-SQLInstanceBroadcast -Verbose
```

## Description

This PowerShell command sends a UDP broadcast request to the SQL Server Browser service (port 1434) on the local subnet to discover all running SQL Server instances. It is used during reconnaissance to identify potential database targets without prior knowledge of hostnames.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose | Enables detailed output showing scan progress and responses | No |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceBroadcast
```

### Verbose Usage

```powershell
Get-SQLInstanceBroadcast -Verbose
```

## Expected Output

A list of discovered SQL instances, including hostnames, instance names, and TCP ports. Example:

InstanceName : MSSQLSERVER
TcpPort : 1433
IsClustered : False
Version : 15.0.2000.5

If no instances are found, it returns empty or indicates no responses.

## Related

- [[procedures/MSSQL-Instance-Discovery]]
- [[commands/get-sqlinstance-scan-udp-threaded]]
