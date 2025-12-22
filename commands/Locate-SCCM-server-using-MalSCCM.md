---
id: 64eb65e1-6bba-4e35-8248-fa170f93852b
type: command
executor: powershell
data: MalSCCM.exe locate
output: null
created_at: '2023-04-06T03:56:08.125546+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - reconnaissance
verified: true
validated: true
---

# Locate-SCCM-server-using-MalSCCM

## Command

```powershell
MalSCCM.exe locate
```

## Description

Queries the local environment to identify the SCCM primary site server or management point that clients communicate with. Useful for initial reconnaissance in SCCM abuse scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; runs default query on local machine | No |

## Examples

### Basic Usage

```powershell
MalSCCM.exe locate
```

## Expected Output

Server FQDN or IP: sccm.contoso.com
Management Point: mp.contoso.com

Success indicated by resolved server details; errors if no SCCM client detected.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
