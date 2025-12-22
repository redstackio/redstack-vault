---
id: 2e2f6b9b-9791-467d-8858-44759f2bc702
type: command
executor: powershell
data: MalSCCM.exe inspect /computers
output: null
created_at: '2023-04-06T03:56:08.125839+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - discovery
verified: true
validated: true
---

# Inspect-computer-clients-using-MalSCCM

## Command

```powershell
MalSCCM.exe inspect /computers
```

## Description

Lists only computer/device clients in SCCM for targeting deployments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /computers | Flag to filter to computer clients | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe inspect /computers
```

## Expected Output

Computer: WS01
OS: Windows Server 2016
Site: CONTOSO

Device details only.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
