---
id: 646ed796-8e93-4241-be5d-b1ab9d8b4eb8
type: command
executor: powershell
data: MalSCCM.exe inspect /primaryusers
output: null
created_at: '2023-04-06T03:56:08.125875+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - discovery
verified: true
validated: true
---

# Inspect-primary-user-clients-using-MalSCCM

## Command

```powershell
MalSCCM.exe inspect /primaryusers
```

## Description

Enumerates primary user clients associated with devices in SCCM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /primaryusers | Flag to filter to primary users | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe inspect /primaryusers
```

## Expected Output

User: jdoe@contoso.com
Primary Device: WS01

User-device mappings.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
