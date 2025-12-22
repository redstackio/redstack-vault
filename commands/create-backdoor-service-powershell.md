---
id: 9372c9a9-71ed-4a80-9abd-96a586eb4585
name: create-backdoor-service-powershell
type: command
executor: powershell
data: >-
  New-Service -Name "$_SERVICE_NAME" -BinaryPathName "$_BINARY_PATH"
  -Description "$_DESCRIPTION" -StartupType $_STARTUP_TYPE
output: null
created_at: '2023-04-06T03:56:28.095200+00:00'
updated_at: '2023-04-10T20:37:29.727924+00:00'
platforms:
  - Windows
tags:
  - persistence
  - service
verified: true
validated: true
---

# create-backdoor-service-powershell

## Command

```powershell
New-Service -Name "$_SERVICE_NAME" -BinaryPathName "$_BINARY_PATH" -Description "$_DESCRIPTION" -StartupType $_STARTUP_TYPE
```

## Description

Creates a new Windows service using PowerShell's New-Service cmdlet, configured to execute a specified binary path with elevated privileges. Used for persistence by registering a backdoor executable as an auto-starting service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVICE_NAME | Name of the service (e.g., Backdoor) | Yes |
| $_BINARY_PATH | Full path to the executable (e.g., C:\Windows\Temp\backdoor.exe) | Yes |
| $_DESCRIPTION | Service description to blend in (e.g., Nothing to see here.) | No |
| $_STARTUP_TYPE | Startup type (Automatic, Manual, Disabled) | Yes |

## Examples

### Basic Usage

```powershell
New-Service -Name "Backdoor" -BinaryPathName "C:\Windows\Temp\backdoor.exe" -Description "Nothing to see here." -StartupType Automatic
```

### Manual Startup

```powershell
New-Service -Name "Backdoor" -BinaryPathName "C:\Windows\Temp\backdoor.exe" -StartupType Manual
```

## Expected Output

The command returns a ServiceController object if successful, e.g.:

Name: Backdoor
Status: Stopped
ServiceType: Win32OwnProcess

No output if errors occur; check $LASTEXITCODE for 0 (success).

## Related

- [[procedures/windows-elevated-services-backdoor-persistence]]
- [[commands/start-backdoor-service-sc]]
