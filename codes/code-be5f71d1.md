---
id: be5f71d1-48be-4358-9eba-fa1a6dd28012
type: code
language: Powershell
verified: false
created_at: '2023-05-24T22:31:34.039275+00:00'
updated_at: '2023-05-24T22:32:46.958559+00:00'
---

# Code Snippet be5f71d1

**Language**: Powershell

```powershell
# Install the AZ Module
Install-Module -Name Az -AllowClobber -Scope CurrentUser

# Login to the Azure Account and generate a SAS token
Connect-AzAccount
$context = (Get-AzStorageAccount -ResourceGroupName "myresourcegroup" -Name "mystorageaccount").Context
$token = New-AzStorageContainerSASToken -Name "mycontainer" -Context $context -Permission "rwdl" -ExpiryTime (Get-Date).AddHours(2)
$url = "https://mystorageaccount.blob.core.windows.net/mycontainer" + $token
```
