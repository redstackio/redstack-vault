---
id: 9071bbdf-0368-4bb9-ba7e-8bc120d4ddc3
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:29.544702+00:00'
updated_at: '2023-04-10T20:37:52.276546+00:00'
---

# Code Snippet 9071bbdf

**Language**: Powershell

```powershell
sc config SSDPSRV start=auto
net start SSDPSRV
net stop upnphost
net start upnphost

sc config upnphost depend=""
```
