---
id: ab08ca26-a6bf-4964-8e7b-0220395d5f5d
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:31.140832+00:00'
updated_at: '2023-04-10T20:37:59.144920+00:00'
---

# Code Snippet ab08ca26

**Language**: ps1

```ps1
Enable-PSRemoting -Force
net start winrm

# Add the machine to the trusted hosts
Set-Item wsman:\localhost\client\trustedhosts *
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "10.10.10.10"
```
