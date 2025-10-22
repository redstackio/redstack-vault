---
id: 9dd803e9-7865-470b-901f-6fe4abd16210
name: Enumerate Azure Blobs with Microburst
type: command
executor: powershell
data: Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN> -OutputFile azureblobs.txt
output: 'PS > Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN> -OutputFile azureblobs.txt

  Found Storage Account -  testsecure.blob.core.windows.net

  Found Storage Account -  securetest.blob.core.windows.net

  Found Storage Account -  securedata.blob.core.windows.net

  Found Storage Account -  securefiles.blob.core.windows.net'
created_at: '2023-05-24T22:11:13.024040+00:00'
updated_at: '2023-05-24T22:11:13.198951+00:00'
---

# Enumerate Azure Blobs with Microburst

```powershell
Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN> -OutputFile azureblobs.txt
```

## Expected Output

```
PS > Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN> -OutputFile azureblobs.txt

Found Storage Account -  testsecure.blob.core.windows.net
Found Storage Account -  securetest.blob.core.windows.net
Found Storage Account -  securedata.blob.core.windows.net
Found Storage Account -  securefiles.blob.core.windows.net
```
