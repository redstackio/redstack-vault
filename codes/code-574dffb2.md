---
id: 574dffb2-aced-4703-8788-724ae1b98c86
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:19.854667+00:00'
updated_at: '2023-04-10T20:36:43.232312+00:00'
---

# Code Snippet 574dffb2

**Language**: ps1

```ps1
Get-SQLDatabase -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Verbose | Where-Object {$_.is_encrypted -eq "True"} | ForEach-Object { $_.Decrypt() }
```
