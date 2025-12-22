---
type: command
executor: powershell
data: >-
  $url =
  "https://codeload.github.com/Meatballs1/ms16-032/zip/refs/heads/master";
  Invoke-WebRequest -Uri $url -OutFile "ms16-032.zip"
output: null
created_at: '2023-04-06T03:56:30Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - download
  - exploit
verified: true
validated: true
---

# download-ms16-032-source-zip

## Command

```powershell
$url = "https://codeload.github.com/Meatballs1/ms16-032/zip/refs/heads/master"; Invoke-WebRequest -Uri $url -OutFile "ms16-032.zip"
```

## Description

Downloads the ZIP archive of the MS16-032 C source code from GitHub to the current directory. This is for building the binary exploit on a development machine (requires Visual Studio), then transferring the compiled .exe to the target. Useful if PowerShell is restricted.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $url | GitHub codeload URL for the ZIP (fixed). | No |
| -OutFile | Local filename for the ZIP. | Yes |
| -Uri | Download URL (set via $url). | Yes |

## Examples

### Basic Usage

```powershell
$url = "https://codeload.github.com/Meatballs1/ms16-032/zip/refs/heads/master"; Invoke-WebRequest -Uri $url -OutFile "ms16-032.zip"
```

### Download to Temp

```powershell
$url = "https://codeload.github.com/Meatballs1/ms16-032/zip/refs/heads/master"; Invoke-WebRequest -Uri $url -OutFile "C:\temp\ms16-032.zip"
```

## Expected Output

```
StatusCode        : 200
StatusDescription : OK
...
ms16-032.zip
```

Extract with Expand-Archive ms16-032.zip -DestinationPath .

## Related

- [[procedures/MS16-032-Local-Privilege-Escalation]]
