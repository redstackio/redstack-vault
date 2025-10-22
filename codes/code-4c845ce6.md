---
id: 4c845ce6-a9b6-4da0-a944-dabb8375edbe
type: code
language: Powershell
verified: false
created_at: '2023-05-23T19:33:04.680319+00:00'
updated_at: '2023-05-23T19:33:22.281560+00:00'
---

# Code Snippet 4c845ce6

**Language**: Powershell

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
