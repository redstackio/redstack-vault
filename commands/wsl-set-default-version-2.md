---
id: 85b02657-234c-4589-a0b0-80a09f5c7c71
name: wsl-set-default-version-2
type: command
executor: powershell
data: wsl --set-default-version 2
output: null
created_at: '2023-04-06T03:56:28.325782+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - wsl
  - configuration
verified: true
validated: true
---

# wsl-set-default-version-2

## Command

```powershell
wsl --set-default-version 2
```

## Description

This command sets the default version of WSL to 2 for all future distributions, enabling better performance and Linux kernel features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --set-default-version | Sets the default WSL version | Yes |
| 2 | Version number (1 or 2) | Yes |

## Examples

### Basic Usage

```powershell
wsl --set-default-version 2
```

Applies globally; verify with 'wsl --status'.

### Advanced Usage

No additional; can be run before installations.

## Expected Output

The operation completed successfully.

Brief confirmation message.

## Related

- [[procedures/Install-and-Persist-via-WSL-with-Kali-Linux]]
