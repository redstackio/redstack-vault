---
id: 7d59b080-bdff-4fa0-bafb-08cf4d60fbe3
name: List-Open-Named-Pipes-PowerShell
type: command
executor: powershell
data: '[System.IO.Directory]::GetFiles("\\.\pipe\")'
output: |-
  PS C:\> [System.IO.Directory]::GetFiles("\\.\pipe\")
  \\.\pipe\InitShutdown
  \\.\pipe\lsass
  \\.\pipe\ntsvcs
  \\.\pipe\scerpc
  \\.\pipe\Winsock2\CatalogChangeListener-2b8-0
  \\.\pipe\Winsock2\CatalogChangeListener-3a8-0
  \\.\pipe\epmapper
  \\.\pipe\Winsock2\CatalogChangeListener-210-0
  \\.\pipe\LSM_API_service
  \\.\pipe\atsvc
  ...
created_at: '2020-04-29T00:05:04.345714+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
verified: true
validated: true
---

# List-Open-Named-Pipes-PowerShell

## Command

```powershell
[System.IO.Directory]::GetFiles("\\.\pipe\")
```

## Description

This PowerShell command uses the .NET System.IO.Directory class to list all open named pipes on a Windows system by treating the \\.\pipe\ path as a directory. It is useful for reconnaissance to identify active inter-process communication channels without needing external tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | This command has no parameters; it directly queries the fixed pipe directory path. | N/A |

## Examples

### Basic Usage

```powershell
[System.IO.Directory]::GetFiles("\\.\pipe\")
```

### Advanced Usage

To filter or process the output, pipe to Select-Object or Where-Object:

```powershell
[System.IO.Directory]::GetFiles("\\.\pipe\") | Select-Object -ExpandProperty Name
```

## Expected Output

The command returns an array of strings representing the full paths to open named pipes. A successful execution on a typical Windows system might show:

```
PS C:\> [System.IO.Directory]::GetFiles("\\.\pipe\")
\\.\pipe\InitShutdown
\\.\pipe\lsass
\\.\pipe\ntsvcs
\\.\pipe\scerpc
\\.\pipe\Winsock2\CatalogChangeListener-2b8-0
\\.\pipe\Winsock2\CatalogChangeListener-3a8-0
\\.\pipe\epmapper
\\.\pipe\Winsock2\CatalogChangeListener-210-0
\\.\pipe\LSM_API_service
\\.\pipe\atsvc
...
```

Look for system pipes like \\.\pipe\lsass (Local Security Authority) or unusual pipes that may indicate custom applications or malware.

## Related

- [[procedures/List-Open-Named-Pipes-on-Windows-PowerShell]]
