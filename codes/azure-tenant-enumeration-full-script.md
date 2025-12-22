---
type: code
language: powershell
verified: true
platforms:
  - Cloud
tags:
  - az-powershell
  - enumeration-script
  - cloud-azure
validated: true
---

# Azure Tenant Enumeration Full Script

## Code

```powershell
PS> $passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force
PS> $creds = New-Object System.Management.Automation.PSCredential ("test@<TENANT NAME>.onmicrosoft.com", $passwd)
PS Az> Connect-AzAccount -Credential $creds

PS Az> Get-AzResource
PS Az> Get-AzRoleAssignment -SignInName test@<TENANT NAME>.onmicrosoft.com
PS Az> Get-AzVM | fl
PS Az> Get-AzWebApp | ?{$_.Kind -notmatch "functionapp"}
PS Az> Get-AzFunctionApp
PS Az> Get-AzStorageAccount | fl
PS Az> Get-AzKeyVault
```

## Description

This PowerShell script performs complete Azure tenant enumeration by connecting with credentials and running a sequence of Get-Az cmdlets to list resources, roles, VMs, web apps, function apps, storage, and key vaults. It serves as a one-stop script for initial discovery in red team engagements or audits.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <PASSWORD> | Plaintext password for authentication | MyP@ssw0rd |
| <TENANT NAME> | Tenant name in Azure AD | contoso |

## Usage

Execute in a PowerShell session after importing Az module. Replace placeholders and run line-by-line or as a .ps1 file. Ideal for post-credential acquisition to map the environment quickly. Follow with exports (e.g., | Export-Csv) for analysis.

## Detection

- Azure AD sign-in logs showing legacy auth from PowerShell.
- API calls to ARM endpoints (Get-Az* patterns) in Azure Monitor.
- Unusual resource queries from low-privilege accounts.

## Related

- [[azure-tenant-enumeration-with-az-powershell-creds]]
- [[tools/az-powershell-module]]
