---
id: ca55cb17-69e8-492b-87cb-cde316928141
name: Create-a-Windows-Service
type: command
executor: command_prompt
data: sc.exe create $_SERVICE_NAME binpath= "$_PATH\$_PROGRAM"
output: |-
  C:\Windows\system32>sc.exe create pwnSVC binpath= "C:\Windows\Tasks\runme.bat"
  [SC] CreateService SUCCESS
created_at: '2020-04-28T21:10:21.094620+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - persistence
  - privilege-escalation
verified: true
validated: true
---

# Create-a-Windows-Service

## Command

```command_prompt
sc.exe create $_SERVICE_NAME binpath= "$_PATH\$_PROGRAM"
```

## Description

This command creates a new Windows service using the Service Control Manager (sc.exe). It registers the service to execute a specified program or script (e.g., a batch file) when started, typically running under SYSTEM privileges. Useful for persistence or privilege escalation in post-exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVICE_NAME | Name of the service to create (e.g., pwnSVC) | Yes |
| $_PATH | Directory path to the executable/script (e.g., C:\\Windows\\Tasks) | Yes |
| $_PROGRAM | Filename of the executable/script (e.g., runme.bat) | Yes |
| binpath= | Specifies the binary path; quotes required for paths with spaces | Built-in |

## Examples

### Basic Usage

```command_prompt
sc.exe create pwnSVC binpath= "C:\Windows\Tasks\runme.bat"
```

### Advanced Usage

```command_prompt
sc.exe create UpdateService binpath= "C:\Temp\update.exe" start= auto
```

(Adds auto-start on boot with the 'start= auto' parameter.)

## Expected Output

Description of what output to expect when the command runs successfully.

```
C:\Windows\system32>sc.exe create pwnSVC binpath= "C:\Windows\Tasks\runme.bat"
[SC] CreateService SUCCESS
```

If successful, the service is registered and can be queried with 'sc query $_SERVICE_NAME'.

## Related

- [[commands/Start-a-Windows-Service]]
- [[commands/Delete-a-Windows-Service]]
- [[procedures/Create-and-Run-Windows-Service-as-SYSTEM-Administrator]]
