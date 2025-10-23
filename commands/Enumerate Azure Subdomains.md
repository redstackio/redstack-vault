---
id: c3a562f5-8d68-4fd8-baed-93c7253a4d71
name: Enumerate Azure Subdomains
type: command
executor: bash
data: 'PS> . C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1

  PS> Invoke-EnumerateAzureSubDomains -Base <TENANT NAME> -Verbose

  '
output: 'PS> . C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1

  PS> Invoke-EnumerateAzureSubDomains -Base <TENANT NAME> -Verbose


  Subdomain Service

  --------- -------

  <TENANT NAME>.mail.protection.outlook.com Email

  <TENANT NAME>.onmicrosoft.com Microsoft Hosted Domain'
created_at: '2023-05-23T16:51:26.151206+00:00'
updated_at: '2023-05-23T16:51:26.181993+00:00'
---

# Enumerate Azure Subdomains

```bash
PS> . C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1
PS> Invoke-EnumerateAzureSubDomains -Base <TENANT NAME> -Verbose

```

## Expected Output

```
PS> . C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureSubDomains.ps1
PS> Invoke-EnumerateAzureSubDomains -Base <TENANT NAME> -Verbose

Subdomain Service
--------- -------
<TENANT NAME>.mail.protection.outlook.com Email
<TENANT NAME>.onmicrosoft.com Microsoft Hosted Domain
```


