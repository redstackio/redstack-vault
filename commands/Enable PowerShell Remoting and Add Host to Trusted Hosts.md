---
id: 67d53df0-17bb-4518-aed8-20c9693635d8
name: Enable PowerShell Remoting and Add Host to Trusted Hosts
type: command
executor: bash
data: 'Enable-PSRemoting -Force

  net start winrm

  Set-Item wsman:\localhost\client\trustedhosts *

  Set-Item WSMan:\localhost\Client\TrustedHosts -Value "10.10.10.10"'
output: null
created_at: '2023-04-06T03:56:31.140924+00:00'
updated_at: '2023-04-10T20:37:59.190248+00:00'
---

# Enable PowerShell Remoting and Add Host to Trusted Hosts

```bash
Enable-PSRemoting -Force
net start winrm

Set-Item wsman:\localhost\client\trustedhosts *
Set-Item WSMan:\localhost\Client\TrustedHosts -Value "10.10.10.10"
```
