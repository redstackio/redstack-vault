---
id: f6ee2f7d-f407-46f4-beb9-b65eb707ad3f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:53.437580+00:00'
updated_at: '2023-04-06T03:55:53.449783+00:00'
---

# Code Snippet f6ee2f7d

**Language**: Powershell

```powershell
# decrypt cookie
$ AspDotNetWrapper.exe --keypath C:\MachineKey.txt --cookie XXXXXXX_XXXXX-XXXXX --decrypt --purpose=owin.cookie --valalgo=hmacsha512 --decalgo=aes

# encrypt cookie (edit Decrypted.txt)
$ AspDotNetWrapper.exe --decryptDataFilePath C:\DecryptedText.txt
```


