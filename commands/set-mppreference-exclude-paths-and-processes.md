---
id: ae368eea-e0d0-433b-9191-53f0d52d400c
name: set-mppreference-exclude-paths-and-processes
type: command
executor: powershell
data: |-
  Add-MpPreference -ExclusionPath "C:\Temp"
  Add-MpPreference -ExclusionPath "C:\Windows\Tasks"
  Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"
output: null
created_at: '2023-04-06T03:56:26.616599+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - evasion
  - exclusions
verified: true
validated: true
---

# set-mppreference-exclude-paths-and-processes

## Command

```powershell
Add-MpPreference -ExclusionPath "C:\Temp"
Add-MpPreference -ExclusionPath "C:\Windows\Tasks"
Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"
```

## Description

Adds folder paths and process names to Defender's exclusion list, preventing scans of specified locations and running processes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ExclusionPath | Path to exclude from scanning | Yes |
| "C:\Temp" | Example path; replace with target | Yes |
| -ExclusionProcess | Comma-separated process names to exclude | Yes |
| "word.exe", "vmwp.exe" | Example processes; customize as needed | Yes |

## Examples

### Basic Usage

```powershell
Add-MpPreference -ExclusionPath "C:\Payloads"
```

### Advanced Usage

Multiple exclusions:

```powershell
Set-MpPreference -ExclusionProcess "powershell.exe", "cmd.exe"
```

## Expected Output

No output on success. Verify with: Get-MpPreference | Select ExclusionPath, ExclusionProcess

```
ExclusionPath      : {C:\Temp, C:\Windows\Tasks}
ExclusionProcess   : {word.exe, vmwp.exe}
```

## Related

- [[procedures/Discover-and-Impair-Windows-Defender-Antivirus]]
