---
id: 5edc30b1-7718-4d9c-9bc2-b276f96f9f76
name: Add new task
type: command
executor: bash
data: SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Task" -m add
output: null
created_at: '2023-04-06T03:56:27.837886+00:00'
updated_at: '2023-04-10T20:37:30.438026+00:00'
---

# Add new task

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
```
