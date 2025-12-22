---
id: 3681dbd4-0d2d-4412-8f94-a6f57bf23f1f
name: import-azuread-module
type: command
executor: powershell
data: Import-Module AzureAD
output: null
created_at: '2023-05-30T13:47:18.323318+00:00'
updated_at: '2023-05-30T13:47:19.298036+00:00'
platforms:
  - Windows
tags:
  - cloud-auth
  - azuread
verified: true
validated: true
---

# import-azuread-module

## Command

```powershell
Import-Module AzureAD
```

## Description

Loads the AzureAD PowerShell module into the current session for directory service operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (None) | Imports the installed AzureAD module | No |

## Examples

### Basic Usage

```powershell
Import-Module AzureAD
Get-Command -Module AzureAD  # Verify loaded
```

### Advanced Usage

With path if custom install:

```powershell
Import-Module C:\Tools\AzureAD\AzureAD.psd1
```

## Expected Output

No output on success. Error: "The specified module 'AzureAD' was not loaded because no valid module file was found" if not installed.

## Related

- [[commands/connect-azuread-with-aad-token]]
- [[procedures/Authenticate-to-Azure-Using-Managed-Identity-Access-Tokens]]
