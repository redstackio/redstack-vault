---
id: 8453370e-ecdf-4509-a9a3-3d11267a96b7
name: query-safe-dll-search-mode
type: command
executor: cmd
data: >-
  reg query "HKLM\\System\\CurrentControlSet\\Control\\Session Manager" /v
  SafeDllSearchMode
output: SafeDllSearchMode    REG_DWORD    0x0
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.181Z'
platforms:
  - Windows
tags:
  - registry-query
  - dll-hijacking
verified: false
validated: true
submitted: true
---

# query-safe-dll-search-mode

## Command

```cmd
reg query "HKLM\System\CurrentControlSet\Control\Session Manager" /v SafeDllSearchMode
```

## Description

Queries the Windows registry for the SafeDllSearchMode value to determine if DLL search order hijacking is possible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /v | Specifies the value name to query | Yes |
| Key path | Registry key path | Yes |

## Examples

### Basic Usage

```cmd
reg query "HKLM\System\CurrentControlSet\Control\Session Manager" /v SafeDllSearchMode
```

### Advanced Usage

```cmd
reg query "HKLM\..." /v SafeDllSearchMode /se
```

## Expected Output

HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\SafeDllSearchMode    REG_DWORD    0x0 (vulnerable) or 0x1 (safe).

## Related

- [[Related Procedure: Perform-DLL-Hijacking-in-UniFi-Video-for-SYSTEM-Access]]
