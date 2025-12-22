---
id: c6fbcfbe-3070-466b-9824-094c91c24545
type: command
executor: powershell
data: MalSCCM.exe inspect /deployments
output: null
created_at: '2023-04-06T03:56:08.126740+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - discovery
verified: true
validated: true
---

# Inspect-deployments-using-MalSCCM

## Command

```powershell
MalSCCM.exe inspect /deployments
```

## Description

Reviews active and historical application deployments in SCCM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /deployments | Flag to list deployments | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe inspect /deployments
```

## Expected Output

Deployment: demodeployment
App: demoapp
Targets: TargetGroup (2 devices)
Status: Available

Deployment summary.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
