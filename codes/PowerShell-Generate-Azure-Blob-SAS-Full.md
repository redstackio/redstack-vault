---
type: code
language: powershell
verified: true
created_at: '2023-05-24T22:34:09.705264+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Cloud
tags:
  - azure
  - storage
  - sas
validated: true
---

# PowerShell-Generate-Azure-Blob-SAS-Full

## Code

```powershell
# Install the AZ Module
Install-Module -Name Az -AllowClobber -Scope CurrentUser

# Login to the Azure Account and generate a SAS token
Connect-AzAccount
$context = (Get-AzStorageAccount -ResourceGroupName "myresourcegroup" -Name "mystorageaccount").Context
$token = New-AzStorageContainerSASToken -Name "mycontainer" -Context $context -Permission "rwdl" -ExpiryTime (Get-Date).AddHours(2)
$url = "https://mystorageaccount.blob.core.windows.net/mycontainer" + $token
```

## Description

This complete PowerShell script installs the Az module, authenticates to Azure, retrieves the storage context, generates a SAS token for a Blob container with rwdl permissions expiring in 2 hours, and constructs the full SAS URL. It is designed for quick generation of temporary storage access in testing or attack simulations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| myresourcegroup | Azure resource group name | rg-production |
| mystorageaccount | Storage account name | sa-blobstore |
| mycontainer | Blob container name | documents |
| rwdl | Permissions (read/write/delete/list) | r (read-only alternative) |
| (Get-Date).AddHours(2) | Expiry time relative to now | (Get-Date).AddDays(1) |

## Usage

Run the entire script in PowerShell after substituting parameters. Use the resulting $url to access the container via HTTP clients like curl (e.g., curl $url/file.txt). Ideal for red team data staging or exfiltration in Azure pentests. For non-interactive use, replace Connect-AzAccount with service principal auth.

## Detection

- Azure AD sign-in logs showing Az PowerShell usage from unusual IPs
- Storage account management operations in Azure Activity Logs
- Network traffic to Azure endpoints with PowerShell user-agent
- Anomalous SAS token generations via diagnostic logs

## Related

- [[procedures/Generate-Azure-Blob-Storage-SAS-URLs]]
- [[tools/Az-PowerShell]]
