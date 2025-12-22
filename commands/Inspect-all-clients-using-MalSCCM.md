---
id: 7ab0bbc8-fa8f-4e0e-86b2-291f7f0ef1f2
type: command
executor: powershell
data: MalSCCM.exe inspect /all
output: null
created_at: '2023-04-06T03:56:08.125771+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - sccm
  - discovery
verified: true
validated: true
---

# Inspect-all-clients-using-MalSCCM

## Command

```powershell
MalSCCM.exe inspect /all
```

## Description

Retrieves a complete list of all SCCM-managed clients, including computers, users, and groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /all | Flag to show all client types | Yes |

## Examples

### Basic Usage

```powershell
MalSCCM.exe inspect /all
```

## Expected Output

Client Type: Computer
Name: WS01.contoso.com
Last Check-in: 2023-10-01

Comprehensive table of clients.

## Related

- [[procedures/Create-and-Deploy-Malicious-Application-via-SCCM]]
