---
id: 094db7e9-ef5d-44fc-bbfb-9444e44ea525
name: Add a new schtask persistence using SharPersist
type: command
executor: bash
data: SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n
  "Some Task" -m add
output: null
created_at: '2023-04-06T03:56:16.649819+00:00'
updated_at: '2023-04-10T20:36:23.644724+00:00'
---

# Add a new schtask persistence using SharPersist

```bash
SharPersist -t schtask -c "C:\Windows\System32\cmd.exe" -a "/c calc.exe" -n "Some Task" -m add
```
