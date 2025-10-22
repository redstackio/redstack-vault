---
id: aeff341e-52ef-494e-9513-41f034edc84a
name: Add a new service persistence using SharPersist
type: command
executor: bash
data: SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Service" -m add
output: null
created_at: '2023-04-06T03:56:16.649690+00:00'
updated_at: '2023-04-10T20:36:23.644724+00:00'
---

# Add a new service persistence using SharPersist

```bash
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Service" -m add
```
