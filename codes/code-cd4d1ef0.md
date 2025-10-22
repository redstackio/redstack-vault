---
id: cd4d1ef0-f784-4f97-9ae0-12fc7e987a8f
type: code
language: Powershell
verified: false
created_at: '2023-05-24T22:32:46.952355+00:00'
updated_at: '2023-05-24T22:34:09.711567+00:00'
---

# Code Snippet cd4d1ef0

**Language**: Powershell

```powershell
az login
token=$(az storage container generate-sas --name mycontainer --account-name mystorageaccount --permissions rwdl --expiry 2023-12-31T23:59Z --https-only --output tsv)
$url = "https://mystorageaccount.blob.core.windows.net/mycontainer?$token"
```
