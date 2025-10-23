---
id: 2101b161-edf7-4f96-9369-8e7a106e3923
name: Enumerate applications with Proxy
type: command
executor: bash
data: Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication
  -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}
output: null
created_at: '2023-04-06T03:56:15.918774+00:00'
updated_at: '2023-04-10T20:19:39.400527+00:00'
---

# Enumerate applications with Proxy

```bash
Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}
```


