---
id: 77405553-c24b-48e5-84e9-1ff4a18795fc
name: Create a Windows PSCredential Object
type: command
executor: powershell
data: '$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force

  $Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument
  "$_DOMAIN\$_USER", $Pass'
output: 'PS C:\Users\Bob > $Pass = ConvertTo-SecureString -String "secretpass" -AsPlainText
  -Force

  PS C:\Users\Bob > $Cred = New-Object -TypeName System.Management.Automation.PSCredential
  -Argument "bank.local\Administrator", $Pass'
created_at: '2020-03-17T05:07:20.698649+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Create a Windows PSCredential Object

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

## Expected Output

```
PS C:\Users\Bob > $Pass = ConvertTo-SecureString -String "secretpass" -AsPlainText -Force
PS C:\Users\Bob > $Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "bank.local\Administrator", $Pass
```


