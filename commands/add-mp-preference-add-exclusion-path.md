---
id: e4a2da5b-0c80-4cea-baf3-5a220578c3e7
type: command
executor: powershell
data: Add-MpPreference -ExclusionPath "$_PATH"
output: >
  PS C:\> Add-MpPreference -ExclusionPath
  "C:\\Windows\\System32\\spool\\drivers\\color"
created_at: '2020-03-04T18:38:21.956539+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - defender
  - defense-evasion
verified: true
validated: true
---

# add-mp-preference-add-exclusion-path

## Command

```powershell
Add-MpPreference -ExclusionPath "$_PATH"
```

## Description

This PowerShell command adds a specified file or folder path to the Windows Defender exclusion list, preventing real-time and on-demand scans of that location. It is useful in red team operations for defense evasion, allowing tools or payloads to run without triggering alerts. The command requires execution in an elevated PowerShell session (as Administrator) and takes effect immediately.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ExclusionPath | The parameter specifying the path to exclude from Defender scans | Yes |
| $_PATH | The full path to the file or folder (e.g., "C:\\Tools\\payload.exe" or "C:\\Temp"; use quotes for paths with spaces) | Yes |

## Examples

### Basic Usage

Exclude a specific folder from scanning:

```powershell
Add-MpPreference -ExclusionPath "C:\Temp\Payloads"
```

### Advanced Usage

Exclude a system directory (requires admin rights):

```powershell
Add-MpPreference -ExclusionPath "C:\Windows\System32\spool\drivers\color"
```

## Expected Output

The command produces no stdout output on success, silently adding the exclusion. To verify, run `Get-MpPreference | Select-Object -ExpandProperty ExclusionPath` which should list the new path. Errors include "Access is denied" if not elevated, or "The parameter is incorrect" for invalid paths. In verbose mode (`-Verbose`), it confirms: "Exclusion path added successfully."

## Related

- [[tools/Add-MpPreference]]
- [[commands/get-mp-preference-list-exclusions]]
