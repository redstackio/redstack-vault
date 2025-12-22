---
id: 85b02657-234c-4589-a0b0-80a09f5c7c69
name: wsl-list-online-distributions
type: command
executor: powershell
data: wsl --list --online
output: null
created_at: '2023-04-06T03:56:28.325782+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - wsl
  - installation
verified: true
validated: true
---

# wsl-list-online-distributions

## Command

```powershell
wsl --list --online
```

## Description

This command queries and lists all available Linux distributions that can be installed via WSL from Microsoft's online repository. It is used to verify availability of distributions like Kali Linux before installation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --list | Lists installed distributions (base flag) | Yes |
| --online | Fetches from online store instead of local | Yes |

## Examples

### Basic Usage

```powershell
wsl --list --online
```

Lists all online distributions, including Ubuntu, Debian, Kali.

### Advanced Usage

No additional options typically needed; pipe to grep for filtering:

```powershell
wsl --list --online | Select-String "kali"
```

## Expected Output

NAME                   FRIENDLY NAME
Ubuntu                 Ubuntu
Debian                 Debian GNU/Linux
kali-linux             Kali Linux Rolling
...

A table of available distributions with names usable in --install.

## Related

- [[procedures/Install-and-Persist-via-WSL-with-Kali-Linux]]
