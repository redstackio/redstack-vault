---
id: 04fbfa25-ca59-41e0-9799-34f2e5c296d6-part1
name: reg-add-globalflag-for-notepad
type: command
executor: cmd
data: >-
  reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File
  Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
output: null
created_at: '2023-04-06T03:56:28.047726+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - registry
  - persistence
verified: true
validated: true
---

# reg-add-globalflag-for-notepad

## Command

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
```

## Description

This command adds a DWORD registry value named GlobalFlag set to 512 under the Image File Execution Options key for notepad.exe, enabling silent process exit monitoring for persistence purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe | Registry path for Notepad.exe's execution options | Yes |
| /v GlobalFlag | Specifies the value name to add or modify | Yes |
| /t REG_DWORD | Sets the value type to DWORD (32-bit integer) | Yes |
| /d 512 | Sets the data value to 512 (enables monitoring) | Yes |

## Examples

### Basic Usage

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\notepad.exe" /v GlobalFlag /t REG_DWORD /d 512
```

### Advanced Usage

To target a different process like explorer.exe:

```cmd
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\explorer.exe" /v GlobalFlag /t REG_DWORD /d 512
```

## Expected Output

The command outputs:

```
The operation completed successfully.
```

If the key already exists, it updates the value without error.

## Related

- [[procedures/Elevated-Registry-Persistence-with-GlobalFlag]]
- [[commands/reg-add-reportingmode-for-notepad]]
