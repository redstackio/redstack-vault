---
id: cf401157-96bd-4a0d-9eab-4e4f86d0aafe
name: verify-wsl-user-root
type: command
executor: powershell
data: wsl whoami
output: null
created_at: '2023-04-06T03:56:29.607660+00:00'
updated_at: '2023-04-10T20:37:54.958414+00:00'
platforms:
  - Windows
tags:
  - wsl
  - verification
verified: true
validated: true
---

# verify-wsl-user-root

## Command

```powershell
wsl whoami
```

## Description

Verifies that the WSL default user has been escalated to root after configuration changes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wsl | Invokes WSL | Yes |
| whoami | Prints current user | Yes |

## Examples

### Basic Usage

```powershell
wsl whoami
```

## Expected Output

root

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
