---
id: a6d5688b-f594-4ff5-96ed-d152f7da9398
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.419841+00:00'
updated_at: '2023-04-10T20:36:08.326426+00:00'
---

# Code Snippet a6d5688b

**Language**: Powershell

```powershell
Get-ADForest
Get-ADForest -Identity <ForestName>

#Domains of Forest Enumeration
(Get-ADForest).Domains
```


