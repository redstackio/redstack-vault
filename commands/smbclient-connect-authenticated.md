---
id: ca9c1861-0e35-411d-8e5a-abc37dce88e6
name: smbclient-connect-authenticated
type: command
executor: bash
data: smbclient -U $_USERNAME%$_PASSWORD //$_TARGET_IP/$_SHARE_NAME
output: |-
  Try "help" to get a list of possible commands.
  smb: \> ls
    .                                   D        0  Thu Sep 12 14:30:22 2019
    ..                                 DR        0  Fri Apr 16 02:16:02 2010
    .rhosts                            AH        4  Sun May 20 14:22:32 2012
    .ssh                               DH        0  Mon May 17 21:43:18 2010
    .profile                            H      586  Tue Mar 16 19:12:59 2010
    .sudo_as_admin_successful           H        0  Thu Sep 12 14:30:22 2019
    .distcc                            DH        0  Sat Apr 17 14:11:00 2010
    .bash_history                       H        0  Tue Mar 16 19:01:07 2010

                  7282168 blocks of size 1024. 0 blocks available
created_at: '2019-09-18T01:44:02.126589+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - smb
  - file-access
verified: true
validated: true
---

# smbclient-connect-authenticated

## Command

```bash
smbclient -U $_USERNAME%$_PASSWORD //$_TARGET_IP/$_SHARE_NAME
```

## Description

Connects to an SMB share with authentication for interactive browsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U $_USERNAME%$_PASSWORD | Credentials (user%pass) | Yes |
| //$_TARGET_IP/$_SHARE_NAME | Share path (e.g., //10.10.10.10/C$) | Yes |

## Examples

### Basic Usage

```bash
smbclient -U bob%pass //10.10.10.10/IPC$
```

### NULL Session

```bash
smbclient //10.10.10.10/IPC$
```

## Expected Output

Description: Interactive prompt (smb: \>) for ls, get, etc.

## Related

- [[procedures/Browse-SMB-Share-with-Credentials]]
- [[tools/Samba]]
