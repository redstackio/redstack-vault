---
data: reg query HKLM\SYSTEM\CurrentControlSet\Services /s /f Rockstar*
tags:
  - registry
  - enumerate
type: command
output: Lists matching service keys
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.145Z'
id: a25182b8-91f7-48f0-a4cf-01c31b93b3d9
verified: false
validated: true
submitted: true
---
# reg-enumerate-services

## Command

```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services /s /f Rockstar*
```

## Description

Enumerates registry keys under Services filtered for Rockstar-related entries to discover service configurations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /s | Recurse subkeys | Yes |
| /f Rockstar* | Filter pattern | Yes |

## Examples

### Basic Usage

```cmd
reg query HKLM\SYSTEM\CurrentControlSet\Services /s /f Rockstar*
```

## Expected Output

List of keys like `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\RockstarService`.

## Related

- [[Related Procedure: Examine-Windows-Registry-for-Rockstar-Service]]
