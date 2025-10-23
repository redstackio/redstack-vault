---
id: 174e49f2-fbf8-4a96-ac6d-8ec60fec2776
name: Add new task hourly
type: command
executor: bash
data: SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Task" -m add -o hourly
output: null
created_at: '2023-04-06T03:56:27.837983+00:00'
updated_at: '2023-04-10T20:37:30.438026+00:00'
---

# Add new task hourly

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add -o hourly
```


