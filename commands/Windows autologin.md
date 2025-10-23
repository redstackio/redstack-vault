---
id: 6f6e0156-50b1-4cc7-b23b-ba2f727093e7
name: Windows autologin
type: command
executor: bash
data: 'reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"

  reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr
  "DefaultUserName DefaultDomainName DefaultPassword"

  '
output: null
created_at: '2020-07-14T18:14:55.534706+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Windows autologin

```bash
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon" 2>nul | findstr "DefaultUserName DefaultDomainName DefaultPassword"

```


