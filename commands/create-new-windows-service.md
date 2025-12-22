---
id: 5c139318-9b9e-4124-8c50-7a25bb75f637
name: Create-New-Windows-Service
type: command
executor: powershell
data: >-
  New-Service -Name $_SERVICE_NAME -BinaryPathName $_BINARY_PATH -StartupType
  $_STARTUP_TYPE
output: null
created_at: '2023-04-06T03:56:26.429007+00:00'
updated_at: '2023-04-10T20:37:06.785363+00:00'
platforms:
  - Windows
tags:
  - powershell
  - service
verified: true
validated: true
---

# Create-New-Windows-Service

## Command

```powershell
New-Service -Name $_SERVICE_NAME -BinaryPathName $_BINARY_PATH -StartupType $_STARTUP_TYPE
```

## Description

Creates a new Windows service entry in the registry and Service Control Manager, allowing delegated service management in a JEA session without broader system access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name | Unique name for the service (e.g., 'TestService') | Yes |
| -BinaryPathName | Full path to the executable (e.g., 'C:\Windows\System32\notepad.exe') | Yes |
| -StartupType | Startup behavior (Automatic, Manual, Disabled) | No (defaults to Manual) |
| -DisplayName | Friendly name for the service | No |

## Examples

### Basic Usage

```powershell
New-Service -Name 'TestService' -BinaryPathName 'C:\Windows\System32\notepad.exe'
```

### Advanced Usage

```powershell
New-Service -Name 'MyService' -BinaryPathName 'C:\path\to\exe.exe' -StartupType Automatic -DisplayName 'My Custom Service'
```

## Expected Output

The service 'TestService' was created successfully.

## Related

- [[procedures/implement-jea-to-limit-powershell-cmdlet-usage]]
