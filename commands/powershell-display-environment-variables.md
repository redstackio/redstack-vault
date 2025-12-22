---
id: ebbeedb6-8f82-4047-a2ae-1f30567c93b5
name: powershell-display-environment-variables
type: command
executor: powershell
data: 'dir env:'
output: null
created_at: '2023-05-24T16:00:22.702828+00:00'
updated_at: '2023-05-24T16:00:22.979060+00:00'
platforms:
  - Windows
tags:
  - environment-variables
  - discovery
verified: true
validated: true
---

# powershell-display-environment-variables

## Command

```powershell
dir env:
```

## Description

This PowerShell command lists all environment variables as directory entries, ideal for identifying Azure Managed Identity variables on a Windows host during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; enumerates all variables | No |

## Examples

### Basic Usage

```powershell
dir env:
```

### Advanced Usage

```powershell
dir env: | Where-Object { $_.Name -like '*IDENTITY*' }
```

## Expected Output

Directory listing of variables, such as:

```

    Name                           Value

    ----                           -----

    PATH                           C:\Windows\system32;...
    IDENTITY_ENDPOINT              http://169.254.169.254/metadata/identity/oauth2/token
    IDENTITY_HEADER                secret_value_here
```

## Related

- [[procedures/Azure-Managed-Identity-Token-Theft-via-Environment-Variables]]
