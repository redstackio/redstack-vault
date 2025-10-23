---
id: 6982c6ba-670a-4dd6-ae66-59a466f8fdcb
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:07.771041+00:00'
updated_at: '2023-04-06T03:56:07.771041+00:00'
---

# Code Snippet 6982c6ba

**Language**: Powershell

```powershell
$AttackerSID = Get-DomainUser SvcJoinComputerToDom -Properties objectsid | Select -Expand objectsid
$ACE = Get-DomainObjectACL dc01-ww2.factory.lan | ?{$_.SecurityIdentifier -match $AttackerSID}
$ACE
ConvertFrom-SID $ACE.SecurityIdentifier
```


