---
id: cc630d96-6f9c-4baa-80d0-59f8ff168390
type: code
language: Powershell
verified: false
created_at: '2023-05-24T22:32:46.952213+00:00'
updated_at: '2023-05-24T22:34:09.711438+00:00'
---

# Code Snippet cc630d96

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


