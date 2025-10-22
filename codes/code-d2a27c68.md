---
id: d2a27c68-4e28-4582-a30f-39f436edb044
type: code
language: Powershell
verified: false
created_at: '2023-05-24T22:34:09.705264+00:00'
updated_at: '2023-05-24T22:34:09.722427+00:00'
---

# Code Snippet d2a27c68

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
