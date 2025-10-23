---
id: a0f06bb0-4ebb-4a91-a513-5cb6a9a22e7b
name: Create new PSCredential object
type: command
executor: bash
data: '$pass = ConvertTo-SecureString ''supersecurepassword'' -AsPlainText -Force

  $cred = New-Object System.Management.Automation.PSCredential (''DOMAIN\Username'',
  $pass)'
output: null
created_at: '2023-04-06T03:56:31.111678+00:00'
updated_at: '2023-04-10T20:38:05.447927+00:00'
---

# Create new PSCredential object

```bash
$pass = ConvertTo-SecureString 'supersecurepassword' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ('DOMAIN\Username', $pass)
```


