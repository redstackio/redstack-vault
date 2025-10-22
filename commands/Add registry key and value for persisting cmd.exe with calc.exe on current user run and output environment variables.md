---
id: 1da375c9-f356-4c6f-9616-bd0404c7f6aa
name: Add registry key and value for persisting cmd.exe with calc.exe on current user
  run and output environment variables
type: command
executor: bash
data: SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun"
  -v "Test Stuff" -m add -o env
output: null
created_at: '2023-04-06T03:56:27.769641+00:00'
updated_at: '2023-04-10T20:37:28.586667+00:00'
---

# Add registry key and value for persisting cmd.exe with calc.exe on current user run and output environment variables

```bash
SharPersist -t reg -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -k "hkcurun" -v "Test Stuff" -m add -o env
```
