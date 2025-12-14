---
id: uuid-placeholder
data: echo %PATH%
tags:
  - environment
  - verification
type: command
output: 'C:\Dima\;C:\Python38\Scripts\;...'
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:22.829Z'
verified: false
validated: true
submitted: true
---
# echo-path

## Command

```cmd
echo %PATH%
```

## Description

Displays the current PATH environment variable to verify modifications for DLL hijacking setups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %PATH% | Expands to the PATH variable | Yes |

## Examples

### Basic Usage

```cmd
echo %PATH%
```

## Expected Output

Path string with directories separated by semicolons, e.g., C:\Dima\;C:\Windows\system32;...

## Related

- [[commands/set-path-variable]]
- [[procedures/Modify-PATH-Environment-for-DLL-Hijacking]]
