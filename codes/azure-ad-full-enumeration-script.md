---
id: ce438f03-afd1-45f0-ac49-a13018723f5b
name: azure-ad-full-enumeration-script
type: code
language: powershell
verified: true
created_at: '2023-05-23T19:33:22.161895+00:00'
updated_at: '2023-05-23T19:33:22.780170+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - enumeration
  - script
validated: true
---

# Azure AD Full Enumeration Script

## Code

```powershell
Import-Module C:\Tools\AzureAD\AzureAD.psd1
Import-Module C:\Tools\AzureADPreview\AzureADPreview.psd1

# Convert password to secure string
$passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force

# Create credentials object
$creds = New-Object System.Management.Automation.PSCredential("test@<TENANT NAME>.onmicrosoft.com", $passwd)

# Connect to Azure AD
Connect-AzureAD -Credential $creds

# Get all Azure AD users
Get-AzureADUser -All $true

# Get all Azure AD users and select only their User Principal Name
Get-AzureADUser -All $true | select UserPrincipalName

# Get all Azure AD groups
Get-AzureADGroup -All $true

# Get all Azure AD devices
Get-AzureADDevice

# Get all members of the Global Administrator role
Get-AzureADDirectoryRole -Filter "DisplayName eq 'Global Administrator'" | Get-AzureADDirectoryRoleMember

# Get all custom role definitions
Get-AzureADMSRoleDefinition | ?{$_.IsBuiltin -eq $False} | select DisplayName
```

## Description

This PowerShell script performs a complete enumeration of an Azure AD tenant using credentials. It imports necessary modules, authenticates, and runs multiple cmdlets to extract users, groups, devices, admin members, and custom roles in sequence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <PASSWORD> | Plaintext password for authentication | P@ssw0rd123 |
| <TENANT NAME> | Azure AD tenant name | contoso |
| test@<TENANT NAME>.onmicrosoft.com | UPN for the account (replace 'test' with actual username) | admin@contoso.onmicrosoft.com |

## Usage

Save as .ps1 file, update placeholders with real values, and execute in PowerShell after installing modules via Install-Module AzureAD. Run on a machine with internet access to Azure endpoints. Ideal for initial reconnaissance after credential acquisition; pipe outputs to files for analysis (e.g., Get-AzureADUser -All $true | Export-Csv users.csv).

## Detection

- Azure AD sign-in logs showing PowerShell client app usage from unusual locations.
- Audit logs for Get-AzureAD* cmdlet executions.
- Network traffic to login.microsoftonline.com with credential auth patterns.
- EDR alerts on module imports or PSCredential object creation in non-admin sessions.

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
- [[tools/azure-ad-powershell-module]]
