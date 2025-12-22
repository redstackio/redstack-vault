---
type: command
executor: cmd
data: diskshadow.exe /s $_SCRIPT_PATH
output: null
platforms:
  - Windows
tags:
  - ad
  - credential-dump
  - shadow-copy
verified: true
validated: true
---

# diskshadow-execute-extraction-script

## Command

```cmd
diskshadow.exe /s $_SCRIPT_PATH
```

## Description

Executes a DiskShadow script file to create a persistent shadow copy of a volume, expose it as a drive, perform actions like file extraction, and clean up. Used here to indirectly access and copy protected files like NTDS.dit on Domain Controllers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SCRIPT_PATH | Path to the DiskShadow script file (e.g., C:\diskshadow.txt) | Yes |
| /s | Specifies the script file to run non-interactively | Built-in |

## Examples

### Basic Usage

```cmd
diskshadow.exe /s C:\diskshadow.txt
```

### Advanced Usage

Run from C:\Windows\System32 for privilege context:

```cmd
cd /d C:\Windows\System32 && diskshadow.exe /s C:\temp\shadow_script.txt
```

## Expected Output

Alias: someAlias, Shadow copy created successfully.
Exposing shadow copy as volume Z:.
Executed command: cmd.exe /c copy...
The specific shadow copy has been deleted.

Success: No errors; Z: drive temporarily available during execution.

## Related

- [[procedures/Dump-AD-Domain-Credentials-with-DiskShadow]]
- [[codes/DiskShadow-Script-for-NTDS-Extraction]]
