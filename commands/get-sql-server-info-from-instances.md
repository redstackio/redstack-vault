---
id: 36a6b9f9-cd11-49cb-9796-a7753d0640b2
name: get-sql-server-info-from-instances
type: command
executor: powershell
data: Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
output: null
created_at: '2023-04-06T03:56:19.794831+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - discovery
  - sql-server
verified: true
validated: true
---

# get-sql-server-info-from-instances

## Command

```powershell
Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
```

## Description

This command pipes domain SQL instances to retrieve detailed server information, including version, edition, and configuration. It connects to each instance to gather properties, helping identify exploitable versions or configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose (on Get-SQLServerInfo) | Provides detailed output on connections and properties | No |

## Examples

### Basic Usage

```powershell
Get-SQLInstanceDomain | Get-SQLServerInfo -Verbose
```

### With Specific Instance

```powershell
$instances = Get-SQLInstanceDomain; $instances | Get-SQLServerInfo -Verbose
```

## Expected Output

Detailed properties per instance, for example:

Name                  : SERVER1
Version               : 15.0.2000.5
Edition               : Enterprise Edition
IsFullTextInstalled   : True

Use this to assess patch levels and features.

## Related

- [[procedures/Domain-SQL-Server-Discovery]]
- [[commands/get-sql-instance-domain-verbose]]
