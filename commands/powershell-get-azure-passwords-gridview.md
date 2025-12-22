---
type: command
executor: powershell
data: Get-AzurePasswords -Verbose | Out-GridView
output: null
platforms:
  - Azure
  - Windows
tags:
  - azure
  - credential-dump
  - gui
verified: true
validated: true
---

# powershell-get-azure-passwords-gridview

## Command

```powershell
Get-AzurePasswords -Verbose | Out-GridView
```

## Description

This pipes the output of Get-AzurePasswords to Out-GridView for a graphical display, allowing interactive sorting and filtering of retrieved Azure passwords. The -Verbose flag adds detailed execution logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Verbose | Enables detailed output during password retrieval | No |

## Examples

### Basic Usage

```powershell
Get-AzurePasswords -Verbose | Out-GridView
```

### With Export

```powershell
Get-AzurePasswords -Verbose | Out-GridView -PassThru | Export-Csv passwords.csv
```

## Expected Output

A pop-up Windows grid view with columns for credential details. Verbose console output includes API call progress; grid populates with data rows if passwords are found.

## Related

- [[procedures/Retrieve-Azure-Passwords-Using-Microburst]]
- [[tools/Microburst]]
