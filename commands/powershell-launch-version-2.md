---
id: cdb1ce24-5810-405a-95cb-46ebba89d888
name: powershell-launch-version-2
type: command
executor: powershell
data: powershell -version 2
output: null
created_at: '2023-04-06T03:56:23.987207+00:00'
updated_at: '2023-10-10T20:37:00.452402+00:00'
platforms:
  - Windows
tags:
  - powershell
  - evasion
verified: true
validated: true
---

# powershell-launch-version-2

## Command

```powershell
powershell -version 2
```

## Description

This command launches a new interactive PowerShell version 2.0 session, which operates in Full Language mode and bypasses Constrained Language Mode restrictions enforced on newer PowerShell versions. Use this to evade defenses during execution of restricted scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -version 2 | Specifies PowerShell version 2.0 (legacy mode). | Yes |

## Examples

### Basic Usage

```powershell
powershell -version 2
```

### With Input/Output Redirection

```powershell
powershell -version 2 -Command "Get-Process"
```

## Expected Output

PS C:\> (prompt for new v2 shell, unrestricted)

## Related

- [[procedures/Check-and-Bypass-PowerShell-Constrained-Language-Mode]]
