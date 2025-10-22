---
id: f31a0ad7-42d5-449e-b3ca-82e71d248726
name: Connect to Azure Account
type: command
executor: bash
data: '$passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force

  $creds = New-Object System.Management.Automation.PSCredential ("test@<TENANT NAME>.onmicrosoft.com",
  $passwd)

  Connect-AzAccount -Credential $creds'
output: null
created_at: '2023-05-23T19:23:37.738596+00:00'
updated_at: '2023-05-23T19:23:39.396554+00:00'
---

# Connect to Azure Account

```bash
$passwd = ConvertTo-SecureString "<PASSWORD>" -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential ("test@<TENANT NAME>.onmicrosoft.com", $passwd)
Connect-AzAccount -Credential $creds
```
