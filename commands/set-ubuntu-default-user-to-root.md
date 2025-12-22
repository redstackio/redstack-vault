---
id: 02d62b7d-a5f5-4016-82a7-65ac2e0a7efd
name: set-ubuntu-default-user-to-root
type: command
executor: powershell
data: ubuntu.exe config --default-user root
output: null
created_at: '2023-04-06T03:56:29.607602+00:00'
updated_at: '2023-04-10T20:37:54.958414+00:00'
platforms:
  - Windows
tags:
  - wsl
  - privilege-escalation
verified: true
validated: true
---

# set-ubuntu-default-user-to-root

## Command

```powershell
ubuntu.exe config --default-user root
```

## Description

This command configures the Ubuntu WSL distribution to start sessions as the root user by default, enabling privilege escalation without sudo.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ubuntu.exe | Path to Ubuntu WSL executable | Yes |
| config | Configuration subcommand | Yes |
| --default-user | Sets the default login user | Yes |
| root | Specifies root as the user | Yes |

## Examples

### Basic Usage

```powershell
ubuntu.exe config --default-user root
```

### For Specific Version

```powershell
ubuntu1604.exe config --default-user root
```

## Expected Output

No output on success; configuration updated silently.

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
