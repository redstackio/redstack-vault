---
id: 18d7e18c-7bc3-45e5-8abc-8f01be187597
name: 'View the list of domain users:'
type: command
executor: bash
data: 'C:\> wmic useraccount where (domain=''%USERDOMAIN%'') get Name > userlist.txt
  PS C:\> ([adsisearcher]"objectCategory=User").Findall() | ForEach

  {$_.properties.samaccountname} | Sort | Out-File -Encoding ASCII users.txt

  '
output: null
created_at: '2020-07-14T18:21:27.744593+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# View the list of domain users:

```bash
C:\> wmic useraccount where (domain='%USERDOMAIN%') get Name > userlist.txt PS C:\> ([adsisearcher]"objectCategory=User").Findall() | ForEach
{$_.properties.samaccountname} | Sort | Out-File -Encoding ASCII users.txt

```


