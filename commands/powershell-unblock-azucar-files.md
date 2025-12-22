---
id: 01a73a29-b4c6-4b41-8163-341c0c274c43
type: command
executor: powershell
data: Get-ChildItem -Recurse $_PATH | Unblock-File
output: null
created_at: '2023-04-06T03:56:14.585735+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - unblock
  - powershell
verified: true
validated: true
---

# powershell-unblock-azucar-files

## Command

```powershell
Get-ChildItem -Recurse $_PATH | Unblock-File
```

## Description

Unblocks PowerShell files downloaded for Azucar to bypass execution policy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Recurse | Recursive search | Yes |
| $_PATH | Directory path (e.g., c:\Azucar_V10) | Yes |

## Examples

### Basic Usage

```powershell
Get-ChildItem -Recurse c:\Azucar_V10 | Unblock-File
```

## Expected Output

Files unblocked silently.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azucar]]
