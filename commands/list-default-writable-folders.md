---
id: 0f264c60-89a0-482d-a5df-f9b09830ad6b
name: list-default-writable-folders
type: command
executor: powershell
data: |-
  $writableFolders = @(
      'C:\Windows\System32\Microsoft\Crypto\RSA\MachineKeys',
      'C:\Windows\System32\spool\drivers\color',
      'C:\Windows\System32\spool\printers',
      'C:\Windows\System32\spool\servers',
      'C:\Windows\tracing',
      'C:\Windows\Temp',
      'C:\Users\Public',
      'C:\Windows\Tasks',
      'C:\Windows\System32\tasks',
      'C:\Windows\SysWOW64\tasks',
      'C:\Windows\System32\tasks_migrated\microsoft\windows\pls\system',
      'C:\Windows\SysWOW64\tasks\microsoft\windows\pls\system',
      'C:\Windows\debug\wia',
      'C:\Windows\registration\crmlog',
      'C:\Windows\System32\com\dmp',
      'C:\Windows\SysWOW64\com\dmp',
      'C:\Windows\System32\fxstmp',
      'C:\Windows\SysWOW64\fxstmp'
  )
  $writableFolders | ForEach-Object { Write-Output $_ }
output: null
created_at: '2023-04-06T03:56:28.775247+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - privilege-escalation
verified: true
validated: true
---

# list-default-writable-folders

## Command

```powershell
$writableFolders = @(
    'C:\Windows\System32\Microsoft\Crypto\RSA\MachineKeys',
    'C:\Windows\System32\spool\drivers\color',
    'C:\Windows\System32\spool\printers',
    'C:\Windows\System32\spool\servers',
    'C:\Windows\tracing',
    'C:\Windows\Temp',
    'C:\Users\Public',
    'C:\Windows\Tasks',
    'C:\Windows\System32\tasks',
    'C:\Windows\SysWOW64\tasks',
    'C:\Windows\System32\tasks_migrated\microsoft\windows\pls\system',
    'C:\Windows\SysWOW64\tasks\microsoft\windows\pls\system',
    'C:\Windows\debug\wia',
    'C:\Windows\registration\crmlog',
    'C:\Windows\System32\com\dmp',
    'C:\Windows\SysWOW64\com\dmp',
    'C:\Windows\System32\fxstmp',
    'C:\Windows\SysWOW64\fxstmp'
)
$writableFolders | ForEach-Object { Write-Output $_ }
```

## Description

This command defines and outputs a list of default writable folders in Windows environments. Use it during privilege escalation assessments to quickly identify locations where low-privileged users can write files, potentially enabling DLL hijacking or payload injection into privileged processes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The list is hardcoded; no parameters needed. | No |

## Examples

### Basic Usage

```powershell
$writableFolders = @('C:\Windows\Temp', 'C:\Users\Public')
$writableFolders | ForEach-Object { Write-Output $_ }
```

### Advanced Usage

Pipe the output to a file for further analysis:

```powershell
... | Out-File -FilePath writable_folders.txt
```

## Expected Output

C:\Windows\System32\Microsoft\Crypto\RSA\MachineKeys  
C:\Windows\System32\spool\drivers\color  
C:\Windows\System32\spool\printers  
C:\Windows\System32\spool\servers  
C:\Windows\tracing  
C:\Windows\Temp  
C:\Users\Public  
C:\Windows\Tasks  
C:\Windows\System32\tasks  
C:\Windows\SysWOW64\tasks  
C:\Windows\System32\tasks_migrated\microsoft\windows\pls\system  
C:\Windows\SysWOW64\tasks\microsoft\windows\pls\system  
C:\Windows\debug\wia  
C:\Windows\registration\crmlog  
C:\Windows\System32\com\dmp  
C:\Windows\SysWOW64\com\dmp  
C:\Windows\System32\fxstmp  
C:\Windows\SysWOW64\fxstmp

## Related

- [[procedures/Exploit-Windows-Default-Writable-Folders-for-Privilege-Escalation]]
