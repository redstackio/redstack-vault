---
id: 3c56b52d-c1e2-4237-9eea-cf7da0f48151
name: check-wsl-current-user
type: command
executor: powershell
data: wsl whoami
output: null
created_at: '2023-04-06T03:56:29.607547+00:00'
updated_at: '2023-04-10T20:37:54.958414+00:00'
platforms:
  - Windows
tags:
  - wsl
  - recon
verified: true
validated: true
---

# check-wsl-current-user

## Command

```powershell
wsl whoami
```

## Description

This command checks the current default user identity within the active WSL distribution (e.g., Ubuntu). It is used to assess the privilege level before attempting escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wsl | Invokes the WSL executable | Yes |
| whoami | Linux command to print current user | Yes |

## Examples

### Basic Usage

```powershell
wsl whoami
```

### With Specific Distribution

```powershell
wsl -d Ubuntu whoami
```

## Expected Output

user

(or 'root' if already elevated)

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
