---
id: 85b02657-234c-4589-a0b0-80a09f5c7c70
name: wsl-install-kali-linux
type: command
executor: powershell
data: wsl --install -d kali-linux
output: null
created_at: '2023-04-06T03:56:28.325782+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - wsl
  - installation
  - kali
verified: true
validated: true
---

# wsl-install-kali-linux

## Command

```powershell
wsl --install -d kali-linux
```

## Description

This command installs the Kali Linux distribution into WSL from the online repository, setting up a persistent Linux environment on Windows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --install | Installs the specified distribution | Yes |
| -d | Specifies the distribution name | Yes |
| kali-linux | Name of the Kali distribution | Yes |

## Examples

### Basic Usage

```powershell
wsl --install -d kali-linux
```

Downloads and installs Kali; prompts for initial user setup on first run.

### Advanced Usage

Install with version 2 explicitly (if not default):

```powershell
wsl --install -d kali-linux --version 2
```

## Expected Output

Installing: kali-linux
...
Successfully installed.

Installation progress messages, ending with success confirmation.

## Related

- [[procedures/Install-and-Persist-via-WSL-with-Kali-Linux]]
