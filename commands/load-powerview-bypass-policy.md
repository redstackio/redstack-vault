---
id: f8c86c33-b7b3-4399-960c-6affe066c0f8-part2
name: load-powerview-bypass-policy
type: command
executor: powershell
data: powershell -ep bypass ./PowerView.ps1
output: null
created_at: '2023-04-06T03:56:23.962672+00:00'
updated_at: '2023-04-10T20:37:00.767168+00:00'
platforms:
  - Windows
tags:
  - powershell
  - powerview
  - defense-evasion
verified: true
validated: true
---

# load-powerview-bypass-policy

## Command

```powershell
powershell -ep bypass ./PowerView.ps1
```

## Description

Executes the PowerView.ps1 script in a new PowerShell instance while bypassing the execution policy for this run only. This allows loading unsigned reconnaissance tools without permanent policy changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-ep bypass` | Sets execution policy to Bypass for this process | Built-in |
| `./PowerView.ps1` | Path to the PowerView script file | Yes |

## Examples

### Basic Usage

```powershell
powershell -ep bypass ./PowerView.ps1
```

### Advanced Usage

Run from script directory: `cd C:\Tools; powershell -ep bypass PowerView.ps1`.

## Expected Output

Script loads without policy warnings; PowerView functions become available (e.g., `Get-Command Get-NetDomain` lists cmdlets). Errors if file not found.

## Related

- [[procedures/Bypass-PowerShell-Execution-Policy-for-PowerView]]
- [[commands/set-powershell-execution-policy-process-bypass]]
