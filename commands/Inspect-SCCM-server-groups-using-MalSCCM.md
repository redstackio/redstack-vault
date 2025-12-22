---
id: a3410de7-b7ae-4737-bcd9-ec25a8b00dd0
type: command
executor: powershell
data: 'MalSCCM.exe inspect /server:<DistributionPoint-Server-FQDN> /groups'
output: null
created_at: '2023-04-06T03:56:08.125652+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - discovery
verified: true
validated: true
---

# Inspect-SCCM-server-groups-using-MalSCCM

## Command

```powershell
MalSCCM.exe inspect /server:$_SERVER_FQDN /groups
```

## Description

Enumerates device collections and groups on a specified SCCM distribution point via WMI. Requires admin privileges; helps identify existing targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /server:$_SERVER_FQDN | FQDN of the SCCM server (e.g., sccm.contoso.com) | Yes |
| /groups | Flag to list groups only | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe inspect /server:sccm.contoso.com /groups
```

## Expected Output

Group Name: All Systems
Members: 150 devices
Group Name: Domain Controllers
Members: 5 devices

Lists groups with membership counts.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
