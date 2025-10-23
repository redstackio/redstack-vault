---
id: 6c8c8100-07d0-429e-b2c9-0f73760f37e6
name: Join computer to domain and assign pre-Windows 2000 name
type: command
executor: bash
data: 'netdom.exe join /domain:contoso.com /ou:OU=Desktops,OU=Computers,DC=contoso,DC=com
  /preW2K:CONTOSO\Win10Comp$

  '
output: null
created_at: '2023-04-06T03:56:04.456034+00:00'
updated_at: '2023-04-10T20:26:27.425169+00:00'
---

# Join computer to domain and assign pre-Windows 2000 name

```bash
netdom.exe join /domain:contoso.com /ou:OU=Desktops,OU=Computers,DC=contoso,DC=com /preW2K:CONTOSO\Win10Comp$

```


