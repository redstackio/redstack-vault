---
id: 18900955-d771-49d4-a3d4-e17b460c451a
type: command
executor: powershell
data: MalSCCM.exe inspect /groups
output: null
created_at: '2023-04-06T03:56:08.125942+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - discovery
verified: true
validated: true
---

# Inspect-group-clients-using-MalSCCM

## Command

```powershell
MalSCCM.exe inspect /groups
```

## Description

Lists all group-based clients or collections in SCCM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /groups | Flag to filter to groups | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe inspect /groups
```

## Expected Output

Group: All Workstations
Member Count: 200

Group summaries.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
