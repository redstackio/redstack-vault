---
id: uuid-placeholder
data: 'setx PATH "C:\\Dima\\;%PATH%" /M'
tags:
  - environment
  - path-modification
type: command
output: 'SUCCESS: Specified value was saved.'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.831Z'
verified: false
validated: true
submitted: true
---
# set-path-variable

## Command

```cmd
setx PATH "C:\\Dima\\;%PATH%" /M
```

## Description

Modifies the system PATH environment variable by prepending a new directory, used to hijack DLL search order in Windows applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PATH | The environment variable to set | Yes |
| "C:\\Dima\\;%PATH%" | New value prepending directory to existing PATH | Yes |
| /M | Apply to system-wide (machine) environment | Yes for persistence |

## Examples

### Basic Usage

```cmd
setx PATH "C:\\Temp\\;%PATH%" /M
```

### User-Level (No /M)

```cmd
setx PATH "C:\\Dima\\;%PATH%"
```

## Expected Output

SUCCESS: Specified value was saved. Changes require logoff/on or reboot.

## Related

- [[commands/echo-path]]
- [[procedures/Modify-PATH-Environment-for-DLL-Hijacking]]
