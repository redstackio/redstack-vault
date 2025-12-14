---
data: >-
  reg query "HKLM\SYSTEM\CurrentControlSet\Services\RockstarService" /v
  ImagePath
tags:
  - registry
  - query
type: command
output: >-
  HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\RockstarService\n   
  ImagePath    REG_EXPAND_SZ    C:\Program Files\Rockstar
  Games\Launcher\Rocker.exe
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.150Z'
id: c099207b-f505-4025-8f33-9a6821150574
verified: false
validated: true
submitted: true
---
# reg-query-service-imagepath

## Command

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services\RockstarService" /v ImagePath
```

## Description

Queries the Windows Registry for the ImagePath value of the Rockstar Game Library Service, used to identify service executable paths during vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| query | Registry query operation | Yes |
| HKLM\... | Specific key path | Yes |
| /v ImagePath | Specifies the value name to retrieve | Yes |

## Examples

### Basic Usage

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services\RockstarService" /v ImagePath
```

### Advanced Usage

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services" /v ImagePath /s
```

## Expected Output

Registry value output showing the unquoted path, e.g., `ImagePath    REG_EXPAND_SZ    C:\Program Files\Rockstar Games\Launcher\Rocker.exe`.

## Related

- [[Related Procedure: Examine-Windows-Registry-for-Rockstar-Service]]
