---
id: 2b6e9a4f-985e-4c9f-9bf5-71b0e88a9830
name: Powershell remoting to machine with user credentials
type: command
executor: ''
data: '$pass = ConvertTo-SecureString $PASSWORD -AsPlainText -Force;

  $cred= New-Object System.Management.Automation.PSCredential ($USERNAME, $password
  );

  New-PSSession -computername $SYSTEM -credential $cred'
output: null
created_at: '2023-01-12T19:33:20.917690+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Powershell remoting to machine with user credentials

```bash
$pass = ConvertTo-SecureString $PASSWORD -AsPlainText -Force;
$cred= New-Object System.Management.Automation.PSCredential ($USERNAME, $password );
New-PSSession -computername $SYSTEM -credential $cred
```


