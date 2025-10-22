---
id: 5557cfac-b046-48d0-a5fc-8afd438605be
type: code
language: Powershell
verified: false
created_at: '2023-05-24T22:34:09.705389+00:00'
updated_at: '2023-05-24T22:34:09.722427+00:00'
---

# Code Snippet 5557cfac

**Language**: Powershell

```powershell
az login
token=$(az storage container generate-sas --name mycontainer --account-name mystorageaccount --permissions rwdl --expiry 2023-12-31T23:59Z --https-only --output tsv)
$url = "https://mystorageaccount.blob.core.windows.net/mycontainer?$token"
```
