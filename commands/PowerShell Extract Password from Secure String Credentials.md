---
id: 4916e4cb-723b-4948-9440-8a70c667d31c
name: PowerShell Extract Password from Secure String Credentials
type: command
executor: ''
data: $creds.getnetworkcredential() | fl *
output: 'PS C:\> $creds.getnetworkcredential() | fl *



  UserName       : BOB-PC/BOB

  Password       : secretpass

  SecurePassword : System.Security.SecureString

  Domain         :'
created_at: '2019-09-30T19:48:33.640595+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerShell Extract Password from Secure String Credentials

```bash
$creds.getnetworkcredential() | fl *
```

## Expected Output

```
PS C:\> $creds.getnetworkcredential() | fl *


UserName       : BOB-PC/BOB
Password       : secretpass
SecurePassword : System.Security.SecureString
Domain         :
```


