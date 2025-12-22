---
id: 183a59a2-dfc0-46a1-86ba-8382b315a455
name: cmd-dir-laps-dll
type: command
executor: cmd
data: 'dir "C:\Program Files\LAPS\CSE\Admpwd.dll"'
output: |2-
      Directory: C:\Program Files\LAPS\CSE


  Mode                 LastWriteTime         Length Name
  ----                 -------------         ------ ----
  -a----        2022-05-06  10:20 PM         244898 Admpwd.dll
created_at: '2023-01-12T19:12:06.789118+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - filesystem
verified: true
validated: true
---

# cmd-dir-laps-dll

## Command

```cmd
dir "C:\Program Files\LAPS\CSE\Admpwd.dll"
```

## Description

This Command Prompt command lists details of the Admpwd.dll file in the LAPS directory, confirming LAPS deployment. It's a native alternative to PowerShell for environments with restricted scripting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "C:\Program Files\LAPS\CSE\Admpwd.dll" | Path to the LAPS DLL file | Yes |

## Examples

### Basic Usage

```cmd
dir "C:\Program Files\LAPS\CSE\Admpwd.dll"
```

### Advanced Usage

To suppress errors if not found:
```cmd
dir "C:\Program Files\LAPS\CSE\Admpwd.dll" 2>nul
```

## Expected Output

If the file exists:
```
    Directory: C:\Program Files\LAPS\CSE


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        2022-05-06  10:20 PM         244898 Admpwd.dll
```

If not found:
```
File Not Found
```

## Related

- [[procedures/Enumerate-LAPS-Artifacts-on-Local-Machine]]
