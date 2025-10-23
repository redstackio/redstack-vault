---
id: a3cf6527-661f-46f9-961e-2b3a433719f8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.230031+00:00'
updated_at: '2023-04-06T21:33:38.760126+00:00'
---

# Code Snippet a3cf6527

**Language**: Powershell

```powershell
Get-NetGPO

# Shows active Policy on specified machine
Get-NetGPO -ComputerName <Name of the PC>
Get-NetGPOGroup

#Get users that are part of a Machine's local Admin group
Find-GPOComputerAdmin -ComputerName <ComputerName>
```


