---
id: c4db6739-7970-4c2b-8ed6-34e76b103d08
name: Connect-AzAccount-As-Service-Principal-Using-Secret
type: command
executor: powershell
data: >-
  $password = ConvertTo-SecureString '<SECRET/PASSWORD>' -AsPlainText -Force

  $creds = New-Object System.Management.Automation.PSCredential('<AppID>',
  $password)

  Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '<TenantID>'
output: null
created_at: '2023-05-24T20:21:06.337686+00:00'
updated_at: '2023-05-24T20:21:06.612131+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - service-principal
  - authentication
verified: true
validated: true
---

# Connect-AzAccount-As-Service-Principal-Using-Secret

## Command

```powershell
$password = ConvertTo-SecureString '<SECRET/PASSWORD>' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('<AppID>', $password)
Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '<TenantID>'
```

## Description

This multi-line PowerShell command creates a secure credential object from an Azure AD app secret and uses it to authenticate to Azure as a service principal via the Az module. It enables non-interactive access to Azure resources assigned to the app, useful for automation or attacker persistence after secret addition.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| '<SECRET/PASSWORD>' | The client secret value generated for the app (replace placeholder) | Yes |
| '<AppID>' | The Application (client) ID of the Azure AD app registration | Yes |
| '<TenantID>' | The Azure AD tenant ID (GUID) for the target environment | Yes |
| -ServicePrincipal | Specifies service principal authentication mode | Yes (built-in flag) |
| -Credential | PSCredential object containing AppID and secret | Yes |

## Examples

### Basic Usage

```powershell
$password = ConvertTo-SecureString 'abc123def456~' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('12345678-1234-1234-1234-123456789012', $password)
Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '87654321-4321-4321-4321-210987654321'
```

### Advanced Usage

With error handling and subscription selection:

```powershell
$password = ConvertTo-SecureString 'abc123def456~' -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential('12345678-1234-1234-1234-123456789012', $password)
try {
    Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '87654321-4321-4321-4321-210987654321' -ErrorAction Stop
    Get-AzSubscription  # Verify access
} catch {
    Write-Error "Authentication failed: $_"
}
```

## Expected Output

Environment                   Account                           TenantId                             SubscriptionId                     SubscriptionName

AzureCloud                    12345678-1234-1234-1234-123456789012 87654321-4321-4321-4321-210987654321 00000000-0000-0000-0000-000000000000 Pay-As-You-Go

Success is indicated by a table showing the connected account details, tenant, and available subscriptions. Errors may include invalid credentials or insufficient app permissions.

## Related

- [[procedures/Add-Azure-AD-App-Secret-for-Service-Principal-Authentication]]
- [[commands/Add-AzADAppSecret-Using-GraphToken]]
