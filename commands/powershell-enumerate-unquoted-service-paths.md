---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: powershell-enumerate-unquoted-service-paths
type: command
executor: powershell
data: >-
  Get-WmiObject win32_service | Select-Object Name, PathName | Where-Object {
  $_.PathName -notlike '*\"*\"*' -and $_.PathName -match '\\s' } | Format-Table
  -AutoSize
output: null
created_at: '2023-10-01T12:00:00.000000+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - privilege-escalation
verified: true
validated: true
---

# powershell-enumerate-unquoted-service-paths

## Command

```powershell
Get-WmiObject win32_service | Select-Object Name, PathName | Where-Object { $_.PathName -notlike '*\"*\"*' -and $_.PathName -match '\\s' } | Format-Table -AutoSize
```

## Description

This PowerShell command enumerates Windows services using WMI, selecting only those with ImagePath values that contain spaces but lack surrounding quotes, indicating potential unquoted service path vulnerabilities for privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Get-WmiObject win32_service | Queries WMI for all services | Yes |
| Select-Object Name, PathName | Outputs service name and path | Yes |
| Where-Object { ... } | Filters for unquoted paths with spaces | Yes |
| Format-Table -AutoSize | Formats output as a table | No |

## Examples

### Basic Usage

```powershell
Get-WmiObject win32_service | Select-Object Name, PathName | Where-Object { $_.PathName -notlike '*\"*\"*' -and $_.PathName -match '\\s' } | Format-Table -AutoSize
```

### Advanced Usage

```powershell
Get-WmiObject win32_service | Where-Object { $_.PathName -notlike '*\"*\"*' -and $_.PathName -match '\\s' -and $_.State -eq 'Running' } | Select-Object Name, PathName, State
```

Adds filter for running services only.

## Expected Output

```

Name                PathName
----                -------
VulnerableService   C:\Program Files\App\service.exe
AnotherService      C:\Tools With Spaces\binary.exe

```

A table of vulnerable service names and their unquoted paths.

## Related

- [[procedures/Windows-Unquoted-Service-Path-Privilege-Escalation]]
