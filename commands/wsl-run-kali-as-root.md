---
id: 9f132aff-e64b-4b2b-9256-3ed432b8c24a
name: wsl-run-kali-as-root
type: command
executor: powershell
data: wsl kali-linux --user root
output: null
created_at: '2023-04-06T03:56:28.325899+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - wsl
  - execution
  - privilege-escalation
verified: true
validated: true
---

# wsl-run-kali-as-root

## Command

```powershell
wsl kali-linux --user root
```

## Description

This command launches the Kali Linux WSL distribution directly as the root user, providing elevated privileges for unrestricted execution of Linux tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| kali-linux | Distribution name | Yes |
| --user root | Specifies the user to run as | Yes |

## Examples

### Basic Usage

```powershell
wsl kali-linux --user root
```

Drops into root shell.

### Advanced Usage

Run a specific command as root:

```powershell
wsl kali-linux --user root whoami
```

Outputs 'root'.

## Expected Output

root@kali:/mnt/c/Users# 

Linux shell prompt as root.

## Related

- [[procedures/Install-and-Persist-via-WSL-with-Kali-Linux]]
