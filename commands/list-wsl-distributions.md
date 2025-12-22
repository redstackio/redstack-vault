---
id: ee97a811-1204-4bb3-934b-1e7ee25e4778
name: list-wsl-distributions
type: command
executor: powershell
data: wsl -l -v
output: null
created_at: '2023-04-06T03:56:29.608018+00:00'
updated_at: '2023-04-10T20:37:54.958414+00:00'
platforms:
  - Windows
tags:
  - wsl
  - verification
verified: true
validated: true
---

# list-wsl-distributions

## Command

```powershell
wsl -l -v
```

## Description

Lists all installed WSL distributions with their versions to verify installation and status.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | List distributions | Yes |
| -v | Show version info | Yes |

## Examples

### Basic Usage

```powershell
wsl -l -v
```

## Expected Output

  NAME                   STATE           VERSION
* Ubuntu                 Running         2

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
