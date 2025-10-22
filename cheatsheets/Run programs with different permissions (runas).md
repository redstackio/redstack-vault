---
id: 43ad7852-08c1-4db7-a6b9-bd51af12c59a
name: Run programs with different permissions (runas)
type: cheatsheet
verified: false
created_at: '2020-07-14T18:23:11.149908+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Run programs with different permissions (runas)

# Description

Allows a user to run specific tools and programs with different permissions than the user's current logon provides.

Applies To: Windows Server 2003, Windows Vista, Windows XP, Windows HPC Server 2008 R2, Windows Server 2008, Windows 7, Windows Server 2003 R2, Windows Server 2000, Windows Server 2012, Windows Server 2003 with SP1, Windows 8

**Command** ([[privileged file copy]]):

```bash
runas /user:hostname\Administrator /savecred "cmd.exe /c type c:\users\administrator\desktop\root.txt > C:\Users\security\AppData\Local\Temp\root.txt"

```

**Command** ([[privileged powershell execution]]):

```powershell
runas /user:hostname\Administrator /savecred "powershell -ExecutionPolicy Bypass -File C:\Users\security\AppData\Local\Temp\boom.ps1"

```

**Command** ([[privileged cmd execution]]):

```bash
runas /user:administrator /savecreds cmd.exe

```
