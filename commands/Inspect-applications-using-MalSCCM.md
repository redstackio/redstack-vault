---
id: 3e98d234-05a2-4659-9bc2-6b087b9a1251
type: command
executor: powershell
data: MalSCCM.exe inspect /applications
output: null
created_at: '2023-04-06T03:56:08.126551+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - discovery
verified: true
validated: true
---

# Inspect-applications-using-MalSCCM

## Command

```powershell
MalSCCM.exe inspect /applications
```

## Description

Lists all applications registered in SCCM, including custom ones.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /applications | Flag to list applications | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe inspect /applications
```

## Expected Output

App Name: demoapp
UNC Path: \\server\share\exe

Application details table.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
