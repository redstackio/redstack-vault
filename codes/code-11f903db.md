---
id: 11f903db-70f9-4ae5-9ac9-968b5c1e496b
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:31.187186+00:00'
updated_at: '2023-04-10T20:38:06.254062+00:00'
---

# Code Snippet 11f903db

**Language**: ps1

```ps1
$aesKey = (49, 222, 253, 86, 26, 137, 92, 43, 29, 200, 17, 203, 88, 97, 39, 38, 60, 119, 46, 44, 219, 179, 13, 194, 191, 199, 78, 10, 4, 40, 87, 159)
$secureObject = ConvertTo-SecureString -String "76492d11167[SNIP]MwA4AGEAYwA1AGMAZgA=" -Key $aesKey
$decrypted = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureObject)
$decrypted = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($decrypted)

```


