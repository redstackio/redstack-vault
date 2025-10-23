---
id: 696e0171-37e6-46ba-9b09-511f3181756e
name: SMB/RPC Enumeration
type: cheatsheet
verified: true
created_at: '2019-09-18T01:44:02.273925+00:00'
updated_at: '2023-06-06T15:16:42.238866+00:00'
---

# SMB/RPC Enumeration

**Status**: ✓ Verified

# Description

Approaches to connecting to and enumerating SMB and RPC services.



## smbclient





**Command** ([[smbclient List SMB Shares]]):

```bash
smbclient -U '$_USERNAME%$_PASSWORD' -L $_TARGET_IP
```







**Command** ([[smbclient List SMB Shares with an Authenticated Session]]):

```bash
smbclient -U $_USERNAME%$_PASSWORD -L $_TARGET_IP
```







**Command** ([[smbclient Connect to an SMB Share (Autenticated)]]):

```bash
smbclient -U $_USERNAME%$_PASSWORD //$_TARGET_IP/$_SHARE_NAME
```







**Command** ([[smbclient Connect to an SMB Share (NTLM)]]):

```bash
smbclient -U $_USERNAME%$_NTLM_HASH:$_NTLM_HASH --pw-nt-hash //$_TARGET_IP/$_SHARE_NAME
```







**Command** ([[smbclient Download All Files Recursively From SMB]]):

```bash
smb: \Victim\> RECURSE ON
smb: \Victim\> PROMPT OFF
smb: \Victim\> mget *
```





## SMBMap







**Command** ([[SMBMap List SMB Shares]]):

```bash
smbmap -u '$_USERNAME' -p '$_PASSWORD' -H $_TARGET_IP
```







**Command** ([[SMBMap List SMB Shares Using an Authenticated Session]]):

```bash
smbmap -u $_USERNAME -p $_PASSWORD -H $_TARGET_IP
```







**Command** ([[SMBMap List an SMB Share's Contents Recursively]]):

```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP
```







**Command** ([[SMBMap Search an SMB Share Recursively by File Name]]):

```bash
smbmap -u $_USERNAME -p $_PASSWORD -R $_SHARE_NAME -H $_TARGET_IP -A $_FILENAME -q
```







**Command** ([[SMBMap Upload a File to an SMB Share]]):

```bash
smbmap -u $_USERNAME -p $_PASSWORD --upload $_FILENAME $_SHARE_NAME/$_FILENAME -H $_TARGET_IP
```





## rpcclient





**Command** ([[rpcclient Connect to an RPC Server with a NULL Session]]):

```bash
rpcclient -U "" -N $_TARGET_IP
```







**Command** ([[rpcclient Authenticate with an RPC Server]]):

```bash
rpcclient -U "$_USERNAME%$_PASSWORD" $_TARGET_IP
```







**Command** ([[List Domain Users on an SMB/RPC Server]]):

```bash
enumdomusers
```







**Command** ([[rpcclient Query an RPC Server for a User's Information]]):

```bash
queryuser $_USER_RID
```







**Command** ([[rpcclient Query an RPC Server's Information]]):

```bash
srvinfo
```







**Command** ([[rpcclient Query an RPC Server for SMB Shares]]):

```bash
netshareenumall
```







**Command** ([[rpcclient Query an RPC Server for Share Information]]):

```bash
netsharegetinfo $_SHARE_NAME
```







**Command** ([[enum4linux Enumerate SMB/RPC Services]]):

```bash
enum4linux $_TARGET_IP
```





## showmount





**Command** ([[showmount List NFS Exports]]):

```bash
showmount -e $_TARGET_IP
```







**Command** ([[Showmount List Mounted NFS Directories]]):

```bash
showmount -d $_TARGET_IP
```






