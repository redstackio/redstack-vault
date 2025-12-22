---
id: ed5ccccc-7287-4d53-be0a-b6e165c674d7
name: Set Terminal Services Work Directory
type: command
executor: powershell
data: $UserObject.TerminalServicesWorkDirectory = "$_WORK_DIRECTORY"
output: null
created_at: '2023-04-06T03:56:06.779505+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - rds
  - persistence
verified: true
validated: true
---

# Set Terminal Services Work Directory

## Command

```powershell
$UserObject.TerminalServicesWorkDirectory = "$_WORK_DIRECTORY"
```

## Description

This command sets the TerminalServicesWorkDirectory attribute on an AD user object to define the working directory for the initial program executed during RDP sessions. It complements the initial program setting for reliable payload execution and requires a bound $UserObject.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_WORK_DIRECTORY | The working directory path, e.g., C:\ or C:\Windows\Temp | Yes |

## Examples

### Basic Usage

```powershell
$UserObject.TerminalServicesWorkDirectory = "C:\"
```

### Advanced Usage

With path validation:

```powershell
if (Test-Path "$_WORK_DIRECTORY") { $UserObject.TerminalServicesWorkDirectory = "$_WORK_DIRECTORY" } else { Write-Error "Invalid directory" }
```

## Expected Output

Silent on success. The attribute updates in the $UserObject instance. Check with `$UserObject.TerminalServicesWorkDirectory`. Persistence requires calling SetInfo(). Permission errors if GenericWrite is lacking.

## Related

- [[Abuse AD ACLs GenericWrite to Configure RCM Persistence]]
- [[commands/Set Terminal Services Initial Program]]
